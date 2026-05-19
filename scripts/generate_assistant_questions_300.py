#!/usr/bin/env python3
"""
Generate 300 assistant question scaffolds from scripts/data/assistant_questions_300.json
and refresh per-folder index.md files under docs/assistant/questions/* and docs/assistant/policies/.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts" / "data" / "assistant_questions_300.json"
DOCS = ROOT / "docs"
ASSISTANT = DOCS / "assistant"

# Markdown appended to auto-generated folder indexes (legacy curated stubs).
ADDITIONAL_INDEX_LINKS: dict[str, list[tuple[str, str]]] = {
    "os-connect": [
        ("Is completeness the same as ADA compliance?", "is-completeness-ada-compliance.md"),
        ("Why are some sidewalks disconnected?", "why-are-sidewalks-disconnected.md"),
    ],
    "accessmap": [
        ("Why does AccessMap choose longer routes?", "why-does-accessmap-choose-longer-routes.md"),
        ("How do mobility profiles work?", "how-do-mobility-profiles-work.md"),
    ],
    "walksheds": [
        ("What is a walkshed?", "what-is-a-walkshed.md"),
        ("How can walksheds support Safe Routes to School?", "how-can-walksheds-support-srts.md"),
    ],
    "tdei": [
        ("Where do I download OS-CONNECT data?", "where-do-i-download-os-connect-data.md"),
        ("How do I use the TDEI portal?", "how-do-i-use-the-tdei-portal.md"),
    ],
}

HIGH_RISK_PAT = re.compile(
    r"(?i)\b("
    r"ada|compliance|compliant|legal|liable|liability|lawyer|"
    r"safety|injur|crash|accura|reliab|version|fresh|outdated|"
    r"guarantee|proof|title\s*ii|litigat|"
    r"ai\b|automated\s+analysis|ai-generated|"
    r"licens|warrant|certif"
    r")\b"
)

PRODUCT_FOR_FOLDER = {
    "os-connect": ["OS-CONNECT"],
    "accessmap": ["AccessMap"],
    "walksheds": ["Walksheds"],
    "tdei": ["TDEI"],
    "policies": ["OS-CONNECT", "AccessMap", "Walksheds", "TDEI"],
}


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    # Keep full slug; longest helpline titles are ~110 chars (under typical path limits).
    return s


def risk_level_for(question: str, topics: list) -> str:
    if HIGH_RISK_PAT.search(question):
        return "high"
    t = " ".join(topics).lower()
    if any(k in t for k in ("ada", "legal", "safety", "risk", "ai")):
        return "high"
    return "medium"


def retrieval_priority_for(qid: int, topics: list) -> str:
    if qid in {45, 46, 47, 198, 199, 201, 202}:
        return "medium"
    return "high"


def build_page(title: str, slug: str, folder: str, topics: list, risk: str, rp: str) -> str:
    products = PRODUCT_FOR_FOLDER[folder]
    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"slug: {slug}",
        "doc_type: question",
        "products:",
    ]
    for p in products:
        lines.append(f"  - {p}")
    lines.extend(
        [
            "audiences:",
            "  - planner",
            "  - jurisdiction",
            "  - advocate",
            "  - public",
            "topics:",
        ]
    )
    for t in topics:
        lines.append(f"  - {t}")
    lines.extend(
        [
            f"risk_level: {risk}",
            "authority_level: explanatory",
            "review_status: draft",
            'last_reviewed: ""',
            f"retrieval_priority: {rp}",
            "assistant_behavior:",
            "  allow_inference: false",
            "  requires_citation: true",
            "  abstain_if_missing_context: true",
            "  do_not_claim: []",
            "related_pages: []",
            "---",
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
    return "\n".join(lines)


def write_indexes(by_folder: dict[str, list[tuple[int, str, str]]]) -> None:
    """by_folder: folder -> list of (id, slug, title) for question pages only."""
    for folder, items in sorted(by_folder.items()):
        if folder == "policies":
            base = ASSISTANT / "policies"
            index_name = "assistant-policy-questions-index.md"
            heading = "Policy-area assistant questions (index)"
        else:
            base = ASSISTANT / "questions" / folder
            index_name = "index.md"
            heading = f"{folder.replace('-', ' ').title()} — assistant questions"

        rel_base = base.relative_to(ASSISTANT).as_posix()
        md_files = sorted(items, key=lambda x: x[0])
        lines = [
            "---",
            f"title: {json.dumps(heading, ensure_ascii=False)}",
            "---",
            "",
            f"# {heading}",
            "",
            "This index lists RAG-oriented question stubs (`doc_type: question`). "
            "Open a page to draft vetted answers; do not treat `TODO` placeholders as authoritative.",
            "",
            "## Questions by ID",
            "",
        ]
        for qid, slug, title in md_files:
            path = f"{slug}.md"
            lines.append(f"{qid}. [{title}]({path})")
        extra = ADDITIONAL_INDEX_LINKS.get(folder)
        if extra:
            lines.extend(
                [
                    "",
                    "## Additional curated pages (pre-batch)",
                    "",
                    "These pages predate the numbered stub set and may contain fuller draft or reviewed answers.",
                    "",
                ]
            )
            for etitle, efile in extra:
                lines.append(f"- [{etitle}]({efile})")
        lines.append("")
        (base / index_name).write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = json.loads(DATA.read_text(encoding="utf-8"))
    if len(rows) != 300:
        print(f"Expected 300 rows, got {len(rows)}", file=sys.stderr)
        return 1

    used_slugs: set[str] = set()
    by_folder: dict[str, list[tuple[int, str, str]]] = {}

    for row in rows:
        qid = row["id"]
        folder = row["folder"]
        title = row["q"]
        topics = row["topics"]
        base_slug = slugify(title)
        slug = base_slug
        if slug in used_slugs:
            slug = f"{base_slug}-{qid}"
        while slug in used_slugs:
            slug = f"{slug}-dup"
        used_slugs.add(slug)

        if folder == "policies":
            out_dir = ASSISTANT / "policies"
        else:
            out_dir = ASSISTANT / "questions" / folder

        out_dir.mkdir(parents=True, exist_ok=True)
        risk = risk_level_for(title, topics)
        rp = retrieval_priority_for(qid, topics)
        body = build_page(title, slug, folder, topics, risk, rp)
        out_path = out_dir / f"{slug}.md"
        out_path.write_text(body, encoding="utf-8")
        by_folder.setdefault(folder, []).append((qid, slug, title))

    write_indexes(by_folder)
    print(f"Wrote {len(rows)} question pages + folder indexes.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
