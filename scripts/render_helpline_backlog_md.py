#!/usr/bin/env python3
"""Render docs/assistant/backlog/helpline-faq-backlog.md from helpline_faq_backlog.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "scripts/data/helpline_faq_backlog.json").read_text(encoding="utf-8"))
priority = set(DATA["priority_faq"])

def link(r: dict) -> str:
    path = r.get("existing_path", "").replace("assistant/", "")
    mark = " ⭐" if r["q"] in priority else ""
    return f"- [{r['q']}](../{path}){mark}" if path else f"- {r['q']}{mark}"

lines = [
    "---",
    "title: Helpline & Question Board FAQ backlog",
    "slug: helpline-faq-backlog",
    "doc_type: workflow",
    "products:",
    "  - OS-CONNECT",
    "  - AccessMap",
    "  - Walksheds",
    "  - TDEI",
    "audiences:",
    "  - planner",
    "  - jurisdiction",
    "  - public",
    "topics:",
    "  - helpline",
    "  - backlog",
    "risk_level: low",
    "authority_level: draft",
    "review_status: draft",
    'last_reviewed: "2026-05-18"',
    "retrieval_priority: high",
    "assistant_behavior:",
    "  allow_inference: false",
    "  requires_citation: true",
    "  abstain_if_missing_context: true",
    "  do_not_claim:",
    "    - This backlog replaces product manuals or operational runbooks.",
    "related_pages:",
    "  - assistant/intents/support-intents.md",
    "  - assistant/workflows/support-answer-patterns.md",
    "  - assistant/index.md",
    "---",
    "",
    "# Helpline & Question Board FAQ backlog",
    "",
    "## Short Answer",
    "",
    "This page tracks practical FAQ and support questions from the Question Board and helpline, maps them to assistant pages, and links to RAG **intents** and **answer patterns** for staff retrieval.",
    "",
    "## Significance",
    "",
    "Partners ask workflow questions—downloads, corrections, ArcGIS, GTFS Pathways, OSM tagging, Mappy Hours—that differ from abstract product FAQs. This backlog aligns human authoring with RAG grounding.",
    "",
    "## Top 10 priority FAQ (author first)",
    "",
]
for i, q in enumerate(DATA["priority_faq"], 1):
    match = next((r for r in DATA["faq_questions"] if r["q"] == q), None)
    if match and match.get("existing_path"):
        path = match["existing_path"].replace("assistant/", "")
        lines.append(f"{i}. [{q}](../{path})")
    else:
        lines.append(f"{i}. {q}")

by_pri: dict[str, list] = {}
for r in DATA["faq_questions"]:
    by_pri.setdefault(r["priority"], []).append(r)

lines.extend([
    "",
    "## Coverage summary",
    "",
    f"- **Total helpline FAQ entries:** {len(DATA['faq_questions'])}",
    f"- **External-user questions:** {len(by_pri.get('external', []))}",
    f"- **Staff / support operations:** {len(by_pri.get('support', []))}",
    f"- **RAG intents:** {len(DATA['intents'])} → [Support intents](../intents/support-intents.md)",
    f"- **Answer patterns:** {len(DATA['patterns'])} → [Support answer patterns](../workflows/support-answer-patterns.md)",
    "",
    "Machine-readable source: `scripts/data/helpline_faq_backlog.json`. Regenerate stubs: `python scripts/build_helpline_backlog.py`.",
    "",
    "## New question areas (May 2026 helpline)",
    "",
    "Compared to the original 300-question batch, this backlog adds emphasis on:",
    "",
    "- **Ecosystem clarity** (TDEI vs OS-CONNECT vs OpenSidewalks vs OSM vs AccessMap vs Walksheds vs GTFS)",
    "- **Downloads & OSW format** (files, edges/nodes, OSW vs OSM export)",
    "- **Issue reporting lifecycle** (viewer reports, review, releases, bulk corrections)",
    "- **GTFS Pathways** (vs OS-CONNECT, pathways.txt, missing pathways)",
    "- **OSM sidewalk street-name tagging** (for trip-planning vendors)",
    "- **Community mapping & Mappy Hours** (Tasking Manager, training, referrals)",
    "- **Support operations** (contacts, tone, uncertainty, cross-team ownership)",
    "",
    "Cross-product pages live under [Support & helpline questions](../questions/support/index.md).",
    "",
    "## External FAQ (all)",
    "",
])
for r in sorted(by_pri.get("external", []), key=lambda x: x["q"]):
    lines.append(link(r))

lines.extend(["", "## Staff / support operations", ""])
for r in sorted(by_pri.get("support", []), key=lambda x: x["q"]):
    lines.append(link(r))

lines.extend([
    "",
    "## Assistant Guidance",
    "",
    "Author the top 10 and the issue-reporting cluster first. Use [support answer patterns](../workflows/support-answer-patterns.md) when drafting replies. Route ambiguous queries via [support intents](../intents/support-intents.md). Do not ingest TODO stubs into production RAG without review filters.",
    "",
    "## Related Concepts",
    "",
    "- [Support intents](../intents/support-intents.md)",
    "- [Support answer patterns](../workflows/support-answer-patterns.md)",
    "- [Assistant Knowledge Base](../index.md)",
    "",
])

out = ROOT / "docs/assistant/backlog/helpline-faq-backlog.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {out}")
