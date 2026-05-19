#!/usr/bin/env python3
"""
Generate Workspaces assistant KB scaffolds (questions 301–400, concepts, workflows, policies).

Usage (from repository root):
    python scripts/generate_workspaces_assistant.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts" / "data" / "workspaces_assistant_pages.json"
ASSISTANT = ROOT / "docs" / "assistant"


def build_frontmatter(
    *,
    title: str,
    slug: str,
    doc_type: str,
    topics: list[str],
    risk_level: str,
) -> str:
    lines = [
        "---",
        f'title: "{title}"',
        f"slug: {slug}",
        f"doc_type: {doc_type}",
        "products:",
        "  - Workspaces",
        "audiences:",
        "  - planner",
        "  - jurisdiction",
        "  - advocate",
        "  - public",
        "topics:",
    ]
    for topic in topics:
        lines.append(f"  - {topic}")
    lines.extend(
        [
            f"risk_level: {risk_level}",
            "authority_level: draft",
            "review_status: draft",
            "last_reviewed:",
            "retrieval_priority: medium",
            "assistant_behavior:",
            "  allow_inference: false",
            "  requires_citation: true",
            "  abstain_if_missing_context: true",
            "  do_not_claim: []",
            "related_pages: []",
            "---",
        ]
    )
    return "\n".join(lines)


def build_body(title: str) -> str:
    return "\n".join(
        [
            "",
            f"# {title}",
            "",
            "## Short Answer",
            "",
            "TODO",
            "",
            "## Significance",
            "",
            "TODO",
            "",
            "## What This Means",
            "",
            "TODO",
            "",
            "## What This Does Not Mean",
            "",
            "TODO",
            "",
            "## How To Use This",
            "",
            "TODO",
            "",
            "## Example",
            "",
            "TODO",
            "",
            "## Assistant Guidance",
            "",
            "TODO",
            "",
            "## Related Concepts",
            "",
            "TODO",
            "",
        ]
    )


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_index(
    path: Path,
    heading: str,
    description: str,
    items: list[tuple[str, str, int | None]],
) -> None:
    lines = [
        "---",
        f'title: "{heading}"',
        "---",
        "",
        f"# {heading}",
        "",
        description,
        "",
    ]
    for entry in items:
        if len(entry) == 3:
            slug, title, qid = entry
            lines.append(f"{qid}. [{title}]({slug}.md)")
        else:
            slug, title = entry
            lines.append(f"- [{title}]({slug}.md)")
    lines.append("")
    write_page(path, "\n".join(lines))


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    questions = payload["questions"]
    if len(questions) != 100:
        print(f"Expected 100 questions, got {len(questions)}", file=sys.stderr)
        return 1

    q_dir = ASSISTANT / "questions" / "workspaces"
    c_dir = ASSISTANT / "concepts" / "workspaces"
    w_dir = ASSISTANT / "workflows" / "workspaces"
    p_dir = ASSISTANT / "policies" / "workspaces"

    index_questions: list[tuple[str, str, int]] = []

    for row in questions:
        slug = row["slug"]
        title = row["title"]
        fm = build_frontmatter(
            title=title,
            slug=slug,
            doc_type="question",
            topics=row["topics"],
            risk_level=row["risk_level"],
        )
        write_page(q_dir / f"{slug}.md", fm + "\n" + build_body(title))
        index_questions.append((slug, title, row["id"]))

    index_concepts: list[tuple[str, str]] = []
    for row in payload["concepts"]:
        slug, title = row["slug"], row["title"]
        fm = build_frontmatter(
            title=title,
            slug=slug,
            doc_type="concept",
            topics=row["topics"],
            risk_level=row["risk_level"],
        )
        write_page(c_dir / f"{slug}.md", fm + "\n" + build_body(title))
        index_concepts.append((slug, title))

    index_workflows: list[tuple[str, str]] = []
    for row in payload["workflows"]:
        slug, title = row["slug"], row["title"]
        fm = build_frontmatter(
            title=title,
            slug=slug,
            doc_type="workflow",
            topics=row["topics"],
            risk_level=row["risk_level"],
        )
        write_page(w_dir / f"{slug}.md", fm + "\n" + build_body(title))
        index_workflows.append((slug, title))

    index_policies: list[tuple[str, str]] = []
    for row in payload["policies"]:
        slug, title = row["slug"], row["title"]
        fm = build_frontmatter(
            title=title,
            slug=slug,
            doc_type="policy",
            topics=row["topics"],
            risk_level=row["risk_level"],
        )
        write_page(p_dir / f"{slug}.md", fm + "\n" + build_body(title))
        index_policies.append((slug, title))

    write_index(
        q_dir / "index.md",
        "Workspaces — assistant questions",
        "RAG-oriented question stubs (`doc_type: question`) for Workspaces (IDs 301–400). "
        "Open a page to draft vetted answers; do not treat `TODO` placeholders as authoritative.",
        index_questions,
    )
    write_index(
        c_dir / "index.md",
        "Workspaces — concepts",
        "Core concepts for collaborative editing, sandboxing, and publication in Workspaces.",
        index_concepts,
    )
    write_index(
        w_dir / "index.md",
        "Workspaces — workflows",
        "Step-oriented workflows for creating, editing, reviewing, and exporting workspace data.",
        index_workflows,
    )
    write_index(
        p_dir / "index.md",
        "Workspaces — policies",
        "Governance and safety boundaries for public assistant answers about Workspaces.",
        index_policies,
    )

    print(
        f"Wrote {len(questions)} questions, {len(payload['concepts'])} concepts, "
        f"{len(payload['workflows'])} workflows, {len(payload['policies'])} policies, "
        "and 4 index pages.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
