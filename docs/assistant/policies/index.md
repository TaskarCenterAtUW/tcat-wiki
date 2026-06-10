---
title: Policies — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-policies
doc_type: policy
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
risk_level: medium
authority_level: official
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - These policies replace jurisdiction-specific legal counsel.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/policies/index.md
---

<!-- @format -->

# Policies — Assistant Knowledge Base

## Short Answer

This section contains cross-product policy pages that govern what assistants may and may not claim when answering questions about TCAT tools and data. Policies cover ADA compliance limits, data freshness caveats, abstention rules, public vs. internal content boundaries, and AI output validation requirements.

## Significance

Without explicit policy pages, assistants may over-claim — stating that OS-CONNECT data constitutes an ADA inventory, or that Walksheds results guarantee barrier-free access. Policy pages encode hard guardrails that reduce legal and reputational risk for TCAT and its partners.

## What This Means

- Pages in `policies/` are authoritative behavioral constraints for all assistants consuming this knowledge base.
- Every page in `docs/assistant/` references relevant policy pages in its `related_pages` frontmatter.
- Product-specific policies (e.g., Workspaces abstention boundaries, export caveats) are in [workspaces/policies/](../workspaces/policies/index.md).

## What This Does Not Mean

- Policy pages do not replace legal counsel, engineering sign-off, or official ADA determinations from qualified authorities.
- These policies are scoped to AI assistant behavior; they do not govern human staff communications (see [workflows/support-answer-patterns.md](../workflows/support-answer-patterns.md) for staff guidance).

## How To Use This

**Agents**: Before answering any question touching ADA compliance, legal authority, data accuracy, or internal information, retrieve the relevant policy page. Treat policy pages as hard constraints: if a `do_not_claim` item matches what you would otherwise say, abstain or reframe.

**Authors**: Policy pages have `authority_level: official` and require TCAT editorial review. Draft pages should be marked `review_status: draft` until approved. Use `risk_level: high` for pages touching legal or safety content.

## Example

An agent is about to answer: _"Is this data ADA-compliant?"_ It retrieves `policies/ada-safety-legal-boundaries.md`, finds `do_not_claim: ["OS-CONNECT data constitutes an official ADA compliance inventory"]`, and reformulates the answer to explain what the data does and does not represent.

## Assistant Guidance

Retrieve policy pages proactively for any question involving compliance, data authority, AI-generated content, or internal information. Do not rely solely on per-page `assistant_behavior` fields; cross-check with the relevant policy page for the authoritative constraint.

## Related Concepts

- [Workspaces policies](../workspaces/policies/index.md)
- [Concepts — ADA compliance boundaries](../concepts/index.md)
- [Dispatch — full file registry](../dispatch.md)

## Planned Pages

| File | Scope |
|------|-------|
| `policies/ada-safety-legal-boundaries.md` | What assistants may/may not say about ADA compliance |
| `policies/assistant-abstention.md` | When and how to abstain from answering |
| `policies/assistant-policy-questions-index.md` | Index of all policy-related questions |
| `policies/data-freshness.md` | How to communicate data currency limitations |
| `policies/how-should-ai-outputs-be-validated.md` | Requirements for human review of AI-generated content |
| `policies/public-vs-internal-content.md` | What is appropriate for public vs. internal RAG pipelines |
| `policies/what-are-the-risks-of-automated-accessibility-analysis.md` | Risk framing for AI-assisted analysis |
