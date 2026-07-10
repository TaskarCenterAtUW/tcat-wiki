#!/usr/bin/env python3
"""build-site.py - Two-layer build orchestrator for the TCAT Wiki.

Produces two parallel copies of docs/ used to build/serve the site:

  - human-docs/  Filtered copy. Removes docs/assistant/support/ entirely and
                 any docs/assistant/**/*.md whose review_status frontmatter is
                 not "reviewed". Zensical builds the HTML site from this copy.
  - agent-docs/  Full copy (all review statuses, including support/). The
                 assistant dispatch registry is regenerated into this copy,
                 and each Markdown file has agent-irrelevant syntax (images,
                 the `@format` pragma, and <img-comparison-slider> blocks)
                 stripped. After `zensical build`, every file in this copy is
                 overlaid onto site/ at the same relative path, so each HTML
                 page also has a parallel raw-Markdown copy at the same URL
                 with an `.md` extension.

Both copies, plus the generated zensical.build.toml (a copy of zensical.toml
with docs_dir pointed at human-docs/), are build artifacts: gitignored, and
never mutate docs/ or the committed zensical.toml.

CLI usage (run from any working directory; paths resolve relative to this
file's repo):

    python utilities/build-site.py            # prep only (copy/filter/strip/config)
    python utilities/build-site.py --build     # prep, then `zensical build -c`, then overlay
    python utilities/build-site.py --serve     # prep, then `zensical serve` (blocking)

Exits non-zero, with a list of offending pages, if a reviewed human-docs page
links to an assistant page that was filtered out of the human layer (a stub,
a draft, or anything under assistant/support/) — this is treated as an
authoring error, per the project's human/agent layer split (see
docs/assistant/schema.md).
"""

import argparse
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path

import tomlkit

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.resolve()

DOCS_DIR = REPO_ROOT / "docs"
HUMAN_DOCS_DIR = REPO_ROOT / "human-docs"
AGENT_DOCS_DIR = REPO_ROOT / "agent-docs"
SITE_DIR = REPO_ROOT / "site"
SOURCE_CONFIG_PATH = REPO_ROOT / "zensical.toml"
BUILD_CONFIG_PATH = REPO_ROOT / "zensical.build.toml"

ASSISTANT_SUBDIR = "assistant"
SUPPORT_SUBDIR = "support"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Markdown link targets that should never be treated as internal file paths.
_EXTERNAL_LINK_PREFIXES = ("http://", "https://", "mailto:", "//")

# Agent-strip regexes. Kept small and independently testable.
_IMAGE_LINE_RE = re.compile(r"(?m)^[ \t]*!\[[^\]]*\]\([^)]*\)[ \t]*\n?")
_IMAGE_INLINE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_FORMAT_PRAGMA_RE = re.compile(r"(?m)^<!--\s*@format\s*-->[ \t]*\n?")
_SLIDER_BLOCK_RE = re.compile(
    r"(?s)<img-comparison-slider[^>]*>.*?</img-comparison-slider>\n?")
_EXCESS_BLANK_LINES_RE = re.compile(r"\n{3,}")


class HumanDocsValidationError(Exception):
    """Raised when a reviewed human-docs page links to an unbuilt assistant page.

    ``errors`` is a list of (offending_page, link_target) tuples, both given
    as paths relative to the human-docs root, suitable for direct printing.
    """

    def __init__(self, errors):
        self.errors = errors
        super().__init__(
            f"{len(errors)} human-docs page(s) link to unbuilt assistant page(s)"
        )


def _import_dispatch_generator():
    """Import utilities/akb-generate-dispatch.py despite its hyphenated filename."""
    module_path = SCRIPT_DIR / "akb-generate-dispatch.py"
    spec = importlib.util.spec_from_file_location(
        "akb_generate_dispatch", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load module spec from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_frontmatter(text):
    """Parse simple top-level ``key: value`` YAML frontmatter into a dict."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    props = {}
    for line in match.group(1).split("\n"):
        if not line or line[0] in " \t#-":
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] in "'\"" and value[-1] == value[0]:
            value = value[1:-1]
        if value:
            props[key] = value
    return props


# =============================================================================
# Step 1: clean + copy
# =============================================================================

def clean_generated(human_dir=HUMAN_DOCS_DIR, agent_dir=AGENT_DOCS_DIR,
                    build_config=BUILD_CONFIG_PATH):
    """Remove previously generated human-docs/, agent-docs/, and zensical.build.toml."""
    for path in (human_dir, agent_dir):
        if path.exists():
            shutil.rmtree(path)
    if build_config.exists():
        build_config.unlink()


def copy_layers(docs_dir=DOCS_DIR, human_dir=HUMAN_DOCS_DIR, agent_dir=AGENT_DOCS_DIR):
    """Copy docs_dir into human_dir and agent_dir. Never mutates docs_dir."""
    shutil.copytree(docs_dir, human_dir)
    shutil.copytree(docs_dir, agent_dir)


# =============================================================================
# Step 2: filter human-docs
# =============================================================================

def delete_non_reviewed_assistant_pages(human_dir):
    """Remove assistant/support/ and any non-reviewed assistant page from human_dir.

    Returns a dict with keys:
      - "removed": sorted list of removed file paths, relative to human_dir
      - "non_reviewed_index_topics": sorted list of topic dir names (relative
        to assistant/) whose index.md was removed for being non-reviewed
        (these topics will have no human-facing landing page)
    """
    assistant_dir = human_dir / ASSISTANT_SUBDIR
    removed = []
    non_reviewed_index_topics = []

    support_dir = assistant_dir / SUPPORT_SUBDIR
    if support_dir.is_dir():
        for md_file in support_dir.rglob("*.md"):
            removed.append(md_file.relative_to(human_dir).as_posix())
        shutil.rmtree(support_dir)

    if assistant_dir.is_dir():
        for md_file in sorted(assistant_dir.rglob("*.md")):
            if not md_file.exists():
                continue  # already removed as part of support/ above
            frontmatter = parse_frontmatter(
                md_file.read_text(encoding="utf-8"))
            if frontmatter.get("review_status") != "reviewed":
                if md_file.name == "index.md":
                    topic = md_file.parent.relative_to(assistant_dir)
                    if str(topic) != ".":
                        non_reviewed_index_topics.append(topic.as_posix())
                removed.append(md_file.relative_to(human_dir).as_posix())
                md_file.unlink()

    return {
        "removed": sorted(removed),
        "non_reviewed_index_topics": sorted(non_reviewed_index_topics),
    }


def _iter_markdown_link_targets(text):
    """Yield raw link target strings from Markdown inline links `[text](target)`."""
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        yield match.group(1).strip()


def find_broken_assistant_links(human_dir):
    """Return a list of (offending_page, link_target) for links into a missing assistant page.

    Only internal links whose resolved target falls under human_dir/assistant/
    are checked (that is the only subtree this filter step removes files
    from); links elsewhere are assumed valid (validated separately by
    utilities/check-links.ps1 against the source docs/ tree).
    """
    assistant_dir = (human_dir / ASSISTANT_SUBDIR).resolve()
    errors = []
    for md_file in sorted(human_dir.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        for target in _iter_markdown_link_targets(text):
            if not target or target.startswith("#"):
                continue
            if target.startswith(_EXTERNAL_LINK_PREFIXES):
                continue
            path_part = target.split("#", 1)[0].strip()
            if not path_part:
                continue
            try:
                resolved = (md_file.parent / path_part).resolve()
            except OSError:
                continue
            try:
                resolved.relative_to(assistant_dir)
            except ValueError:
                continue  # not a link into the assistant tree
            if not resolved.exists():
                errors.append(
                    (md_file.relative_to(human_dir).as_posix(), target))
    return errors


def filter_human_docs(human_dir=HUMAN_DOCS_DIR):
    """Filter human_dir in place; raise HumanDocsValidationError on broken links.

    Returns the same info dict as delete_non_reviewed_assistant_pages() on
    success.
    """
    info = delete_non_reviewed_assistant_pages(human_dir)
    if info["non_reviewed_index_topics"]:
        print(
            "warning: the following assistant topics have a non-reviewed "
            "index.md and will have no human-facing landing page: "
            + ", ".join(info["non_reviewed_index_topics"]),
            file=sys.stderr,
        )
    errors = find_broken_assistant_links(human_dir)
    if errors:
        raise HumanDocsValidationError(errors)
    return info


# =============================================================================
# Step 3: generate dispatch (agent-docs only)
# =============================================================================

def generate_dispatch(agent_dir=AGENT_DOCS_DIR):
    """Regenerate assistant/dispatch.md inside agent_dir."""
    module = _import_dispatch_generator()
    return module.write_dispatch(agent_dir / ASSISTANT_SUBDIR)


# =============================================================================
# Step 4: strip agent-docs
# =============================================================================

def strip_markdown_text(text):
    """Return text with images, the @format pragma, and slider blocks removed."""
    text = _SLIDER_BLOCK_RE.sub("", text)
    text = _IMAGE_LINE_RE.sub("", text)
    text = _IMAGE_INLINE_RE.sub("", text)
    text = _FORMAT_PRAGMA_RE.sub("", text)
    text = _EXCESS_BLANK_LINES_RE.sub("\n\n", text)
    return text


def strip_agent_docs(agent_dir=AGENT_DOCS_DIR):
    """Apply strip_markdown_text() to every Markdown file under agent_dir, in place."""
    for md_file in agent_dir.rglob("*.md"):
        original = md_file.read_text(encoding="utf-8")
        stripped = strip_markdown_text(original)
        if stripped != original:
            md_file.write_text(stripped, encoding="utf-8", newline="\n")


# =============================================================================
# Step 5: generate zensical.build.toml
# =============================================================================

def write_build_config(source_config=SOURCE_CONFIG_PATH,
                       build_config=BUILD_CONFIG_PATH,
                       docs_dir_name="human-docs"):
    """Write build_config as a copy of source_config with docs_dir overridden."""
    text = source_config.read_text(encoding="utf-8")
    doc = tomlkit.parse(text)
    doc["project"]["docs_dir"] = docs_dir_name
    build_config.write_text(tomlkit.dumps(doc), encoding="utf-8", newline="\n")
    return build_config


# =============================================================================
# Step 6: build + overlay
# =============================================================================

def overlay_agent_layer(agent_dir=AGENT_DOCS_DIR, site_dir=SITE_DIR):
    """Copy every agent_dir/**/*.md onto site_dir/** at the same relative path."""
    copied = []
    for md_file in agent_dir.rglob("*.md"):
        rel = md_file.relative_to(agent_dir)
        dest = site_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, dest)
        copied.append(rel.as_posix())
    return sorted(copied)


def run_zensical_build(build_config=BUILD_CONFIG_PATH):
    subprocess.run(
        [sys.executable, "-m", "zensical", "build",
         "-f", str(build_config), "-c"],
        cwd=REPO_ROOT, check=True,
    )


def run_zensical_serve(build_config=BUILD_CONFIG_PATH):
    subprocess.run(
        [sys.executable, "-m", "zensical", "serve", "-f", str(build_config)],
        cwd=REPO_ROOT, check=True,
    )


# =============================================================================
# Orchestration
# =============================================================================

def prepare(docs_dir=DOCS_DIR, human_dir=HUMAN_DOCS_DIR, agent_dir=AGENT_DOCS_DIR,
            source_config=SOURCE_CONFIG_PATH, build_config=BUILD_CONFIG_PATH):
    """Run the full prep pipeline: clean, copy, filter, dispatch, strip, config.

    Raises HumanDocsValidationError if a reviewed human page links to an
    unbuilt assistant page.
    """
    clean_generated(human_dir, agent_dir, build_config)
    copy_layers(docs_dir, human_dir, agent_dir)
    filter_human_docs(human_dir)
    generate_dispatch(agent_dir)
    strip_agent_docs(agent_dir)
    write_build_config(source_config, build_config)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--build", action="store_true",
        help="After prep, run `zensical build -c` and overlay agent-docs onto site/.",
    )
    parser.add_argument(
        "--serve", action="store_true",
        help="After prep, run `zensical serve` (blocking; re-run this script to refresh).",
    )
    args = parser.parse_args(argv)

    if args.build and args.serve:
        print("error: --build and --serve are mutually exclusive", file=sys.stderr)
        return 1

    try:
        prepare()

        if args.build:
            run_zensical_build()
            overlay_agent_layer()
            print(f"Build complete: {SITE_DIR}")
        elif args.serve:
            run_zensical_serve()
        else:
            print(
                f"Prep complete: {HUMAN_DOCS_DIR}, {AGENT_DOCS_DIR}, {BUILD_CONFIG_PATH}")
    except KeyboardInterrupt:
        print("\nOperation canceled.", file=sys.stderr)
        return 130
    except HumanDocsValidationError as exc:
        print(
            "error: reviewed human-docs page(s) link to an unbuilt assistant "
            "page (stub, draft, or support/). Fix the source link or change "
            "the target page's review_status:",
            file=sys.stderr,
        )
        for offending_page, link_target in exc.errors:
            print(f"  {offending_page} -> {link_target}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
