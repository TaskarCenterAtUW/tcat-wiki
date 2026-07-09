#!/usr/bin/env python3
"""akb-generate-dispatch.py - Generate the Assistant Knowledge Base dispatch registry.

Scans an assistant knowledge-base directory (default: docs/assistant/) for
topic subdirectories, each containing an index.md plus concept/ and workflow/
subdirectories of articles, and writes a dispatch.md registry file listing
every article on disk together with its `review_status` frontmatter value.

dispatch.md is a GENERATED build artifact. It must never be hand-edited;
re-run this script (directly, or via utilities/build-site.py) whenever a
page is added, removed, or re-statused under the assistant tree.

Run from any working directory; paths are resolved relative to this file
unless --assistant-dir is given explicitly (used by build-site.py to target
the agent-docs/ copy).
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_ASSISTANT_DIR = REPO_ROOT / "docs" / "assistant"

# Top-level files that live directly in the assistant root and are never
# treated as topic directories or tabled as registry rows.
TOP_LEVEL_PEERS = {"index.md", "dispatch.md", "schema.md", "intents.md"}

# doc_type subdirectories scanned within each topic directory, in emission order.
DOC_TYPE_SECTIONS = [
    ("concept", "Concepts"),
    ("workflow", "Workflows"),
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Static frontmatter for the generated file. `{last_reviewed}` is substituted
# with today's date at generation time; every other field is fixed.
FRONTMATTER_TEMPLATE = """---
title: Assistant Knowledge Base — Dispatch
tags:
    - Assistant
slug: dispatch
doc_type: workflow
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
    - Workspaces
audiences:
    - developer
topics:
    - assistant-layer
    - governance
risk_level: low
authority_level: official
review_status: draft
last_reviewed: {last_reviewed}
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/schema.md
    - assistant/intents.md
---
"""

# Static prose that precedes the generated Registry section. Do not
# interpolate per-topic data here; that belongs in render_registry().
BODY_PREFIX = """
<!-- @format -->

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by utilities/akb-generate-dispatch.py. Re-run the script
     (or utilities/build-site.py) to refresh this file after adding,
     removing, or re-statusing pages under docs/assistant/. -->

# Assistant Knowledge Base — Dispatch

## Short Answer

This file is the registry for all pages in the `docs/assistant/` knowledge base. It is the single source of truth for canonical file paths, authoring status, and section structure. External agents should fetch this file first to enumerate available knowledge-base pages before retrieving individual articles.

Related: [Overview](index.md) · [Schema](schema.md) · [Intents](intents.md)

## Significance

A stable registry decouples retrieval pipelines from the filesystem. Authors use this file to track what has been written, what is still a stub, and what needs review. Integrators can use it to detect new pages without crawling the entire site.

## What This Means

- Every article that physically exists in `docs/assistant/` has a row in this registry; nothing here is aspirational.
- **Status** is one of: `stub` (placeholder exists, body is `TODO`), `draft` (content authored, awaiting review), or `reviewed` (approved by TCAT staff).
- Every page listed here is served as raw Markdown at the same URL with an `.md` extension, regardless of status. See [schema](schema.md) for the human-layer vs. agent-layer distinction.
- Section index files (e.g., `workspaces/index.md`) carry that topic's policy content and per-topic assistant guidance.

## What This Does Not Mean

- This file does not replace the [schema](schema.md), which governs authoring conventions.
- This file does not replace section indexes, which provide richer per-section context.
- A `stub` status does not mean the content is wrong — it means the body has not yet been authored.

## How To Use This

**Agents**: Fetch `dispatch.md`, parse the registry tables, filter by `Status` or topic heading, then retrieve individual pages by constructing their URL as `https://taskarcenteratuw.github.io/tcat-wiki/` + the `Base:` path shown under the relevant heading + the filename in the table.

**Authors**: Write or edit files directly under `docs/assistant/`; do not hand-edit this file. Re-run `utilities/akb-generate-dispatch.py` (or the full `utilities/build-site.py` pipeline) to refresh the registry after adding a page or changing its `review_status`.

**Maintainers**: This file is a generated build artifact. To change its structure, edit `utilities/akb-generate-dispatch.py`.

## Example

An agent looking for Workspaces content: fetches this file, finds the `## Workspaces` heading, selects a relevant row from its `### Concepts` or `### Workflows` table, then fetches that page using the `Base:` prefix plus the filename.

## Assistant Guidance

This page should be fetched fresh rather than cached aggressively; its registry reflects the current authoring state of the knowledge base. If a file listed here returns 404, the generator has not yet been re-run since the file was added.

## Related Concepts

- [Assistant Knowledge Base Index](index.md) — Overview of this retrieval-oriented TCAT knowledge base
- [Assistant Knowledge Base Schema](schema.md) — Authoring contract for Assistant Knowledge Base articles
- [Assistant Knowledge Base Intents](intents.md) — Mapping of retrieval intents to article paths

## Status Legend

| Status     | Meaning                                                  |
| :--------- | :-------------------------------------------------------- |
| `stub`     | Frontmatter and heading scaffold exist; body is `TODO`   |
| `draft`    | Content authored; awaiting TCAT editorial review         |
| `reviewed` | Reviewed and approved by TCAT staff                      |

## Registry

"""


def parse_frontmatter(text):
    """Parse YAML frontmatter into a flat dict of top-level scalar keys.

    Only extracts simple ``key: value`` pairs at zero indentation (not nested
    maps or lists), which is sufficient for reading ``title`` and
    ``review_status``.
    """
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


def topic_title_fallback(dir_name):
    """Return a human-readable title for a topic directory lacking an index.md title."""
    return dir_name.replace("-", " ").title()


def scan_topic(topic_dir: Path):
    """Return a dict describing one topic directory's index title and article rows."""
    index_path = topic_dir / "index.md"
    title = None
    has_index = index_path.exists()
    if has_index:
        title = parse_frontmatter(
            index_path.read_text(encoding="utf-8")).get("title")
    if not title:
        title = topic_title_fallback(topic_dir.name)

    sections = {}
    for doc_type, _label in DOC_TYPE_SECTIONS:
        doc_dir = topic_dir / doc_type
        rows = []
        if doc_dir.is_dir():
            for md_file in sorted(doc_dir.glob("*.md"), key=lambda p: p.name):
                fm = parse_frontmatter(md_file.read_text(encoding="utf-8"))
                status = fm.get("review_status", "stub")
                rows.append((md_file.name, status))
        sections[doc_type] = rows

    return {
        "name": topic_dir.name,
        "title": title,
        "has_index": has_index,
        "sections": sections,
    }


def scan_topics(assistant_dir: Path):
    """Return a list of topic dicts for every subdirectory of assistant_dir, alphabetical."""
    topics = []
    if not assistant_dir.is_dir():
        return topics
    for entry in sorted(assistant_dir.iterdir(), key=lambda p: p.name):
        if entry.is_dir():
            topics.append(scan_topic(entry))
    return topics


def render_topic(topic):
    """Return the Markdown block (H2 + H3 sections) for a single topic dict."""
    lines = [f"## {topic['title']}", ""]
    if topic["has_index"]:
        lines.append(
            f"See [{topic['name']}/index.md]({topic['name']}/index.md) for per-topic "
            "assistant guidance and policies."
        )
        lines.append("")

    for doc_type, label in DOC_TYPE_SECTIONS:
        rows = topic["sections"][doc_type]
        if not rows:
            # Empty subdirectories are omitted entirely rather than emitted
            # with a placeholder note.
            continue
        lines.append(f"### {label}")
        lines.append("")
        lines.append(f"Base: `assistant/{topic['name']}/{doc_type}/`")
        lines.append("")
        lines.append("| File | Status |")
        lines.append("| :--- | :----- |")
        for fname, status in rows:
            lines.append(f"| `{fname}` | {status} |")
        lines.append("")

    return "\n".join(lines).rstrip("\n")


def render_registry(topics):
    """Return the full Markdown for the Registry section body (no heading)."""
    blocks = [render_topic(topic) for topic in topics]
    return "\n\n".join(blocks) + "\n"


def build_dispatch(assistant_dir: Path, today: str | None = None) -> str:
    """Return the complete generated dispatch.md content for assistant_dir."""
    if today is None:
        today = date.today().isoformat()
    topics = scan_topics(assistant_dir)
    frontmatter = FRONTMATTER_TEMPLATE.format(last_reviewed=today)
    return frontmatter + BODY_PREFIX + render_registry(topics)


def write_dispatch(assistant_dir: Path, today: str | None = None) -> Path:
    """Generate dispatch.md content and write it into assistant_dir. Return the path written."""
    content = build_dispatch(assistant_dir, today=today)
    output_path = assistant_dir / "dispatch.md"
    output_path.write_text(content, encoding="utf-8", newline="\n")
    return output_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--assistant-dir",
        type=Path,
        default=DEFAULT_ASSISTANT_DIR,
        help="Path to the assistant knowledge-base directory to scan "
        "(default: docs/assistant/ relative to the repo root).",
    )
    parser.add_argument(
        "--print",
        dest="print_only",
        action="store_true",
        help="Print the generated content to stdout instead of writing dispatch.md.",
    )
    args = parser.parse_args(argv)

    assistant_dir = args.assistant_dir.resolve()
    if not assistant_dir.is_dir():
        print(f"error: assistant directory not found: {assistant_dir}", file=sys.stderr)
        return 1

    if args.print_only:
        print(build_dispatch(assistant_dir), end="")
        return 0

    output_path = write_dispatch(assistant_dir)
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
