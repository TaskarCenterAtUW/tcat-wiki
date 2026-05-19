---
title: Assistant abstention and escalation
slug: assistant-abstention
doc_type: policy
products:
  - OS-CONNECT
  - AccessMap
  - Walksheds
  - TDEI
audiences:
  - planner
  - jurisdiction
  - advocate
  - public
topics:
  - governance
  - assistant-behavior
risk_level: high
authority_level: draft
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - Draft policy text is enforceable organizational policy until formally adopted.
related_pages:
  - assistant/policies/public-vs-internal-content.md
  - assistant/policies/ada-safety-legal-boundaries.md
---

# Assistant abstention and escalation

## Short Answer

Public assistants should abstain—clearly stating uncertainty and limits—when context is missing, stakes are legal or medical, or retrieved content is draft. Escalate to human-reviewed channels rather than guessing.

## Significance

Abstention is a safety and trust control for RAG systems. Without it, models confabulate precision that datasets do not support.

## What This Means

Triggers include unknown jurisdiction, unspecified dataset version, compliance proof requests, individualized medical routing advice, and missing citations for high `risk_level` topics.

## What This Does Not Mean

- Not rude refusal; abstention includes helpful next steps (which doc to read, which professional to consult).
- Not permission to ignore easy factual questions that are well documented.

## How To Use This

Encode triggers from `assistant_behavior` and `risk_level` in retrieval filters and post-generation checks.

## Example

User: “Does OS-CONNECT prove our ADA plan is complete?” Assistant: “No—completeness is a data concept, not legal compliance. For ADA questions, consult qualified counsel,” with links to relevant wiki pages.

## Assistant Guidance

When `abstain_if_missing_context` is true in frontmatter, mirror that behavior in consumer systems. Surface `do_not_claim` bullets as hard negatives.

## Related Concepts

- [Public vs internal content](public-vs-internal-content.md)
- [ADA safety and legal boundaries](ada-safety-legal-boundaries.md)
