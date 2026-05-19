---
title: Assistant Knowledge Base
slug: assistant-knowledge-base
doc_type: concept
products:
  - OS-CONNECT
  - AccessMap
  - Walksheds
  - TDEI
  - Workspaces
audiences:
  - planner
  - jurisdiction
  - advocate
  - public
topics:
  - assistant-layer
  - governance
  - RAG
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - This layer replaces official product manuals or legal advice.
related_pages:
  - assistant/policies/public-vs-internal-content.md
  - assistant/policies/assistant-abstention.md
  - rag/README.md
---

# Assistant Knowledge Base

## Short Answer

This section is a governed, retrieval-oriented layer for explaining OS-CONNECT, AccessMap, Walksheds, TDEI, and Workspaces to the public through assistants. It sits beside the existing product documentation: procedures and deep manuals stay where they are; here you find stable answers, boundaries, and assistant-safe phrasing.

## Significance

Public assistants need concise answers, explicit limits on claims, and pointers to authoritative sources. Without a dedicated layer, models over-generalize from fragmented docs or invent compliance interpretations. This corpus aligns language across products and channels while preserving the Zensical site as the human-facing source of truth.

## What This Means

- Each page carries metadata (products, risk, authority, retrieval priority) for filtering and grounding.
- Questions, concepts, workflows, policies, and glossary entries share a common section scaffold so chunks stay comparable for RAG.
- The [RAG export specification](../rag/README.md) describes how these pages map to exported chunks.

## What This Does Not Mean

- Not a replacement for jurisdiction counsel, ADA legal determinations, or engineering sign-off.
- Not a shortcut to skip reading official manuals when making operational changes.
- Not an endorsement of any particular vendor LLM or hosting environment.

## How To Use This

- **Authors and reviewers**: Align wording with product teams; bump `review_status` and `last_reviewed` when content is validated.
- **Assistant operators**: Prefer answers that cite this wiki and abstain per [Assistant abstention](policies/assistant-abstention.md) when context is missing.
- **Data engineers**: Use `scripts/export_rag.py` to produce JSONL from `docs/assistant/`; see [RAG README](../rag/README.md).
- **Question bank (300 stubs + helpline supplement + Workspaces 301–400)**: Browse by product area — [OS-CONNECT questions](questions/os-connect/index.md), [AccessMap questions](questions/accessmap/index.md), [Walksheds questions](questions/walksheds/index.md), [TDEI questions](questions/tdei/index.md), [Workspaces questions](questions/workspaces/index.md), [Support & helpline questions](questions/support/index.md), and [policy-area assistant questions](policies/assistant-policy-questions-index.md). Regenerate the 300 batch from `scripts/data/assistant_questions_300.json` via `python scripts/generate_assistant_questions_300.py`; Workspaces scaffolds from `scripts/data/workspaces_assistant_pages.json` via `python scripts/generate_workspaces_assistant.py`; helpline stubs from `scripts/data/helpline_faq_backlog.json` via `python scripts/build_helpline_backlog.py`.
- **Workspaces assistant layer**: [Concepts](concepts/workspaces/index.md), [Workflows](workflows/workspaces/index.md), [Policies](policies/workspaces/index.md).
- **Helpline / Question Board backlog (May 2026)**: Prioritized external FAQ, staff support questions, [RAG intents](intents/support-intents.md), and [answer patterns](workflows/support-answer-patterns.md) — see [Helpline FAQ backlog](backlog/helpline-faq-backlog.md).

## Example

A resident asks whether OS-CONNECT “proves” ADA compliance. The assistant retrieves [Is completeness ADA compliance?](questions/os-connect/is-completeness-ada-compliance.md), answers briefly from the Short Answer, and explicitly states the boundaries in What This Does Not Mean rather than improvising legal conclusions.

## Assistant Guidance

Lead with the Short Answer. Always mention that product-specific procedures live in the main wiki sections. If the user asks for legal certainty or site-specific engineering, abstain and suggest qualified professionals. Never merge draft policy pages with `authority_level: draft` into answers as if they were official without disclosure.

## Related Concepts

- [Public vs internal content](policies/public-vs-internal-content.md)
- [Assistant abstention](policies/assistant-abstention.md)
- [RAG corpus overview](../rag/README.md)
