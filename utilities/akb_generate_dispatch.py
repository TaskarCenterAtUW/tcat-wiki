#!/usr/bin/env python3
"""akb_generate_dispatch.py - Generate the Assistant Knowledge Base dispatch registry.

Scans an assistant knowledge-base directory (default: docs/assistant/) for
topic subdirectories, each containing an index.md plus concept/ and workflow/
subdirectories of articles, and writes a dispatch.md registry file listing
every article on disk together with its `publication_status` and
`authority_level` frontmatter values.

dispatch.md is a GENERATED build artifact. It must never be hand-edited;
re-run this script (directly, or via utilities/build_site.py) whenever a
page is added, removed, or re-statused under the assistant tree.

Run from any working directory; paths are resolved relative to this file
unless --assistant-dir is given explicitly (used by build_site.py to target
the agent-docs/ copy).
"""

import argparse
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import TypeAlias, TypedDict

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

# Statuses appear in the legend in this order.
STATUS_ORDER = ("stub", "draft", "published", "archived")
AUTHORITY_ORDER = ("provisional", "explanatory", "official")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LAST_REVIEWED_RE = re.compile(r"last_reviewed:\s*\d{4}-\d{2}-\d{2}")

# Static frontmatter for the generated file. `{last_reviewed}` is substituted
# with today's date at generation time; every other field is fixed.
FRONTMATTER_TEMPLATE = """---
title: Assistant Knowledge Base — Dispatch
slug: dispatch
doc_type: workflow
questions:
    - What articles are available in the TCAT Wiki Assistant Knowledge Base?
audiences:
    - developer
products:
    - AccessMap
    - AVIV ScoutRoute
    - Cross-Platform
    - FleXR
    - iOSPointMapper
    - LivAbility
    - OpenSidewalks
    - OS-CONNECT
    - QA-QC Reports
    - Rapid
    - TDEI
    - Walksheds
    - WayKeeper
    - Workspaces
topics:
    - assistant-layer
    - governance
risk_level: low
authority_level: official
publication_status: draft
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
tags:
    - Assistant
---
"""

# Static prose that precedes the generated Registry section. Do not
# interpolate per-topic data here; that belongs in render_registry().
BODY_PREFIX = """
<!-- @format -->

<!-- GENERATED FILE — DO NOT EDIT BY HAND.
     Produced by utilities/akb_generate_dispatch.py. Re-run the script
     (or utilities/build_site.py) to refresh this file after adding,
     removing, or re-statusing pages under docs/assistant/. -->

# Assistant Knowledge Base — Dispatch

## Short Answer

This file is the registry for all pages in the `docs/assistant/` knowledge base. It is the single source of truth for canonical file paths, authoring status, and section structure. External agents should fetch this file first to enumerate available knowledge-base pages before retrieving individual articles.

Related: [Overview](index.md) · [Schema](schema.md) · [Intents](intents.md)

## Significance

A stable registry decouples retrieval pipelines from the filesystem. Authors use this file to track what has been written, what is still a stub, and what needs review. Integrators can use it to detect new pages without crawling the entire site.

## What This Means

- Every article that physically exists in `docs/assistant/` has a row in this registry; nothing here is aspirational.
- **Publication status** is one of: `stub` (placeholder exists, body is `TODO`), `draft` (content authored, awaiting review), `published` (available in the human layer), or `archived` (retained for agents but not published).
- Every page listed here is served as raw Markdown at the same URL with an `.md` extension, regardless of status. See [schema](schema.md) for the human-layer vs. agent-layer distinction.
- Section index files (e.g., `workspaces/index.md`) carry that topic's policy content and per-topic assistant guidance.

## What This Does Not Mean

- This file does not replace the [schema](schema.md), which governs authoring conventions.
- This file does not replace section indexes, which provide richer per-section context.
- A `stub` status does not mean the content is wrong — it means the body has not yet been authored.

## How To Use This

**Agents**: Fetch `dispatch.md`, parse the registry tables, filter by `Status` or topic heading, then retrieve individual pages by constructing their URL as `https://taskarcenteratuw.github.io/tcat-wiki/` + the `Base:` path shown under the relevant heading + the filename in the table.

**Authors**: Write or edit files directly under `docs/assistant/`; do not hand-edit this file. Re-run `utilities/akb_generate_dispatch.py` (or the full `utilities/build_site.py` pipeline) to refresh the registry after adding a page or changing its `publication_status`.

**Maintainers**: This file is a generated build artifact. To change its structure, edit `utilities/akb_generate_dispatch.py`.

## Example

An agent looking for Workspaces content: fetches this file, finds the `## Workspaces` heading, selects a relevant row from its `### Concepts` or `### Workflows` table, then fetches that page using the `Base:` prefix plus the filename.

## Assistant Guidance

This page should be fetched fresh rather than cached aggressively; its registry reflects the current authoring state of the knowledge base. If a file listed here returns 404, the generator has not yet been re-run since the file was added.

## Related Concepts

- [Assistant Knowledge Base Index](index.md) — Overview of this retrieval-oriented TCAT knowledge base
- [Assistant Knowledge Base Schema](schema.md) — Authoring contract for Assistant Knowledge Base articles
- [Assistant Knowledge Base Intents](intents.md) — Mapping of retrieval intents to article paths

## Status Legend

{status_legend}

## Authority Legend

{authority_legend}

## Registry

"""

ArticleRow: TypeAlias = tuple[str, str, str]


class Topic(TypedDict):
    """Scanned metadata and article rows for one assistant topic."""

    name: str
    title: str
    has_index: bool
    sections: dict[str, list[ArticleRow]]


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse YAML frontmatter into a flat dict of top-level scalar keys.

    Only extracts simple ``key: value`` pairs at zero indentation (not nested
    maps or lists), which is sufficient for reading ``title`` and
    ``publication_status`` and ``authority_level``.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    props: dict[str, str] = {}
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


def topic_title_fallback(dir_name: str) -> str:
    """Return a human-readable title for a topic directory lacking an index.md title."""
    return dir_name.replace("-", " ").title()


def scan_topic(topic_dir: Path) -> Topic:
    """Return a dict describing one topic directory's index title and article rows."""
    index_path = topic_dir / "index.md"
    title = None
    has_index = index_path.exists()
    if has_index:
        title = parse_frontmatter(
            index_path.read_text(encoding="utf-8")).get("title")
    if not title:
        title = topic_title_fallback(topic_dir.name)

    sections: dict[str, list[ArticleRow]] = {}
    for doc_type, _label in DOC_TYPE_SECTIONS:
        doc_dir = topic_dir / doc_type
        rows: list[ArticleRow] = []
        if doc_dir.is_dir():
            for md_file in sorted(doc_dir.glob("*.md"), key=lambda p: p.name):
                fm = parse_frontmatter(md_file.read_text(encoding="utf-8"))
                status = fm.get("publication_status") or "stub"
                authority = fm.get("authority_level") or "provisional"
                rows.append((md_file.name, status, authority))
        sections[doc_type] = rows

    return {
        "name": topic_dir.name,
        "title": title,
        "has_index": has_index,
        "sections": sections,
    }


def scan_topics(assistant_dir: Path) -> list[Topic]:
    """Return a list of topic dicts for every subdirectory of assistant_dir, alphabetical."""
    topics: list[Topic] = []
    if not assistant_dir.is_dir():
        return topics
    for entry in sorted(assistant_dir.iterdir(), key=lambda p: p.name):
        if entry.is_dir():
            topics.append(scan_topic(entry))
    return topics


def count_statuses(topics: list[Topic]) -> Counter[str]:
    """Return article counts grouped by publication status across all topic sections."""
    counts: Counter[str] = Counter()
    for topic in topics:
        for doc_type, _label in DOC_TYPE_SECTIONS:
            counts.update(status for _filename, status, _authority
                          in topic["sections"][doc_type])
    return counts


def count_authority_levels(topics: list[Topic]) -> Counter[str]:
    """Return article counts grouped by authority level across all topic sections."""
    counts: Counter[str] = Counter()
    for topic in topics:
        for doc_type, _label in DOC_TYPE_SECTIONS:
            counts.update(authority for _filename, _status, authority
                          in topic["sections"][doc_type])
    return counts


def render_status_legend(counts: Counter[str]) -> str:
    """Return the status legend table, including live article counts."""
    meanings = {
        "stub": "Frontmatter and heading scaffold exist; body is `TODO`",
        "draft": "Content authored; awaiting TCAT editorial review",
        "published": "Available in the human-facing site",
        "archived": "Retained for agents but not published",
    }
    lines = ["| Status | Count | Meaning |", "| :----- | ----: | :------ |"]
    for status in STATUS_ORDER:
        lines.append(f"| `{status}` | {counts[status]} | {meanings[status]} |")
    return "\n".join(lines)


def render_authority_legend(counts: Counter[str]) -> str:
    """Return the authority legend table, including live article counts."""
    meanings = {
        "provisional": "Early or limited-confidence guidance",
        "explanatory": "Established explanation without formal policy authority",
        "official": "Formally endorsed organizational guidance",
    }
    lines = ["| Authority level | Count | Meaning |",
             "| :-------------- | ----: | :------ |"]
    for authority in AUTHORITY_ORDER:
        lines.append(
            f"| `{authority}` | {counts[authority]} | {meanings[authority]} |")
    return "\n".join(lines)


def render_topic(topic: Topic) -> str:
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
        for fname, status, _authority in rows:
            lines.append(f"| `{fname}` | {status} |")
        lines.append("")

    return "\n".join(lines).rstrip("\n")


def render_registry(topics: list[Topic]) -> str:
    """Return the full Markdown for the Registry section body (no heading)."""
    blocks = [render_topic(topic) for topic in topics]
    return "\n\n".join(blocks) + "\n"


def build_dispatch(assistant_dir: Path, today: str | None = None) -> str:
    """Return the complete generated dispatch.md content for assistant_dir."""
    if today is None:
        today = date.today().isoformat()
    topics = scan_topics(assistant_dir)
    frontmatter = FRONTMATTER_TEMPLATE.format(last_reviewed=today)
    body_prefix = BODY_PREFIX.format(
        status_legend=render_status_legend(count_statuses(topics)),
        authority_legend=render_authority_legend(count_authority_levels(topics)))
    return frontmatter + body_prefix + render_registry(topics)


def write_dispatch(assistant_dir: Path, today: str | None = None) -> Path:
    """Generate dispatch.md content and write it into assistant_dir. Return the path written.

    If dispatch.md already exists and the only difference from the freshly
    generated content is the ``last_reviewed`` date, the existing file is
    left untouched (preserving its prior date) instead of being rewritten,
    to avoid noisy no-op diffs when nothing substantive changed.
    """
    output_path = assistant_dir / "dispatch.md"
    content = build_dispatch(assistant_dir, today=today)

    if output_path.exists():
        existing = output_path.read_text(encoding="utf-8")
        if _only_last_reviewed_differs(existing, content):
            return output_path

    output_path.write_text(content, encoding="utf-8", newline="\r\n")
    return output_path


def _only_last_reviewed_differs(old_text: str, new_text: str) -> bool:
    """Return True if old_text and new_text are identical apart from their
    ``last_reviewed: YYYY-MM-DD`` frontmatter line."""
    if old_text == new_text:
        return True
    old_without_date = LAST_REVIEWED_RE.sub(
        "last_reviewed: ", old_text, count=1)
    new_without_date = LAST_REVIEWED_RE.sub(
        "last_reviewed: ", new_text, count=1)
    return old_without_date == new_without_date


def main(argv: list[str] | None = None) -> int:
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
        print(
            f"error: assistant directory not found: {assistant_dir}", file=sys.stderr)
        return 1

    if args.print_only:
        print(build_dispatch(assistant_dir), end="")
        return 0

    output_path = write_dispatch(assistant_dir)
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
