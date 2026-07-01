---
title: Policies — Assistant Knowledge Base
tags:
    - Assistant
slug: cross-platform-index
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
last_reviewed: 2026-07-01
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
    - assistant/workspaces/index.md
---

<!-- @format -->

# Policies — Assistant Knowledge Base

## Short Answer

This section contains cross-product policy pages that govern what assistants may and may not claim when answering questions about TCAT tools and data. Policies cover ADA compliance limits, data freshness caveats, abstention rules, public vs. internal content boundaries, and AI output validation requirements.

## Significance

Without explicit policy pages, assistants may over-claim — stating that OS-CONNECT data constitutes an ADA inventory, or that Walksheds results guarantee barrier-free access. Policy pages encode hard guardrails that reduce legal and reputational risk for TCAT and its partners.

## What This Means

- **Concepts** (`concept/`) address ideas that cut across at least two TCAT products — such as the connected pedestrian graph, accessibility islands, data completeness, and ADA compliance boundaries. Workspaces-specific concepts (sandbox governance, dataset lineage, imagery layers) are in `workspaces/concept/`.
- **Workflows** (`workflow/`) describe task sequences, actor roles, and tool involvement for common cross-product tasks — such as reviewing community feedback, updating jurisdiction data, using AccessMap for public engagement, and using OS-CONNECT for ADA transition planning. Workspaces-specific workflows are in `workspaces/workflow/`. Staff communication patterns are in `workflow/support-answer-patterns.md`.

## What This Does Not Mean

- Policy pages do not replace legal counsel, engineering sign-off, or official ADA determinations from qualified authorities.
- These policies are scoped to AI assistant behavior; they do not govern human staff communications (see [workflow/support-answer-patterns.md](workflow/support-answer-patterns.md) for staff guidance).

## How To Use This

**Agents**: Before answering any question touching ADA compliance, legal authority, data accuracy, or internal information, retrieve the relevant policy page. Treat policy pages as hard constraints: if a `do_not_claim` item matches what you would otherwise say, abstain or reframe. For definitional questions ("what is X?"), retrieve the matching page from `concept/`; supplement with product-specific pages when the question has an operational context — for example, accessibility islands → `concept/accessibility-islands.md`, then `walksheds/what-are-accessibility-islands-in-walkshed-analysis.md`. For "how do I do X?" questions spanning multiple tools, match to the closest page in `workflow/` — for example, ADA planning → `workflow/use-os-connect-for-ada-transition-planning.md`; public engagement → `workflow/use-accessmap-for-public-engagement.md`; SRTS → `workflow/use-walksheds-for-safe-routes-to-school.md`.

**Authors**: Policy pages have `authority_level: official` and require TCAT editorial review. Draft pages should be marked `review_status: draft` until approved. Use `risk_level: high` for pages touching legal or safety content.

## Example

An agent is about to answer: _"Is this data ADA-compliant?"_ It retrieves `policies/ada-safety-legal-boundaries.md`, finds `do_not_claim: ["OS-CONNECT data constitutes an official ADA compliance inventory"]`, and reformulates the answer to explain what the data does and does not represent.

## Assistant Guidance

Retrieve policy pages proactively for any question involving compliance, data authority, AI-generated content, or internal information. Do not rely solely on per-page `assistant_behavior` fields; cross-check with the relevant policy page for the authoritative constraint. Concept pages provide definitional grounding; always supplement them with product-specific pages when a user's question has an operational context. Workflow pages often involve external stakeholder coordination; when presenting a workflow, note which steps require human judgment or external approval, and which are tool-assisted.

## Related Concepts

- [Workspaces policies](../workspaces/index.md)
- [Dispatch — full file registry](../dispatch.md)

## Planned Pages

**Concepts**

| File                                                                | Scope                                                     |
| :------------------------------------------------------------------ | :-------------------------------------------------------- |
| `concept/ada-safety-legal-boundaries.md`                            | What assistants may/may not say about ADA compliance      |
| `concept/assistant-abstention.md`                                   | When and how to abstain from answering                    |
| `concept/data-freshness.md`                                         | How to communicate data currency limitations              |
| `concept/how-should-ai-outputs-be-validated.md`                     | Requirements for human review of AI-generated content     |
| `concept/public-vs-internal-content.md`                             | What is appropriate for public vs. internal RAG pipelines |
| `concept/what-are-the-risks-of-automated-accessibility-analysis.md` | Risk framing for AI-assisted analysis                     |

**Workflows**

| File                                                     | Workflow                                                                  |
| :------------------------------------------------------- | :------------------------------------------------------------------------ |
| `workflow/review-community-feedback.md`                  | How to review and act on community-submitted data corrections             |
| `workflow/support-answer-patterns.md`                    | Communication patterns for staff responding to external partner questions |
| `workflow/update-jurisdiction-data.md`                   | How jurisdictions submit and track data updates                           |
| `workflow/use-accessmap-for-public-engagement.md`        | Using AccessMap in community meetings and public-facing planning          |
| `workflow/use-os-connect-for-ada-transition-planning.md` | Integrating OS-CONNECT data into ADA transition plan workflows            |
| `workflow/use-walksheds-for-safe-routes-to-school.md`    | Using Walksheds for SRTS analysis and grant applications                  |
