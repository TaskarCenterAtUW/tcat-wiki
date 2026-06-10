---
title: Assistant Intents
tags:
    - Assistant
slug: assistant-intents
doc_type: workflow
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
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: low
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/support/index.md
---

<!-- @format -->

# Assistant Intents

## Short Answer

This section catalogs named retrieval intents — patterns of user queries that map to specific knowledge-base pages. Intents help retrieval pipelines route ambiguous questions to the most relevant pages without requiring exact keyword matches.

## Significance

Named intents provide a structured vocabulary for retrieval system configuration. They are particularly useful for helpline and support contexts where users may phrase similar questions in many different ways.

## What This Means

- `intents/support-intents.md` maps common helpline and Question Board queries to their canonical knowledge-base pages.

## What This Does Not Mean

- Not a substitute for the [dispatch](../dispatch.md) as the authoritative file registry.
- Not product documentation; intents are operational metadata for retrieval systems.

## How To Use This

**Integrators**: Load intent mappings from `intents/support-intents.md` into your retrieval pipeline's query routing layer. When a user query matches an intent pattern, retrieve the mapped page directly.

**Authors**: Add intent entries to `support-intents.md` when helpline experience reveals new query patterns not captured by existing page titles.

## Example

A retrieval system receives: _"How long until my correction shows up?"_ It matches the `correction-timeline` intent and retrieves `os-connect/how-long-do-corrections-take-to-appear-in-a-public-release.md`.

## Assistant Guidance

Intents are metadata for retrieval pipelines, not content for end users. Do not surface intent categories directly in responses; use them only for internal routing.

## Related Concepts

- [Support Q&A](../support/index.md)
- [Dispatch — full file registry](../dispatch.md)
