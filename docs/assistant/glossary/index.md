---
title: Glossary — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-glossary
doc_type: glossary
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
    - glossary
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - Definitions here override product manuals where they differ; manuals win.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/concepts/index.md
    - assistant/glossary/terms.md
---

<!-- @format -->

# Glossary — Assistant Knowledge Base

## Short Answer

This section contains glossary pages defining recurring TCAT terms for assistant-sized answers. The glossary distills key vocabulary from across TCAT products and the broader pedestrian accessibility data domain. For authoritative procedural definitions, product manuals take precedence.

## Significance

Consistent terminology reduces assistant hallucination and prevents conflation of related but distinct concepts (e.g., TDEI vs. OS-CONNECT vs. OpenSidewalks, or workspace vs. OSM database). Agents retrieving glossary pages get grounded, bounded definitions.

## What This Means

- `glossary/index.md` provides a high-level overview of the glossary and its governance.
- `glossary/terms.md` contains the primary A–Z term listing with definitions scoped to assistant-layer usage.
- More detailed conceptual treatment of any term is in [concepts/](../concepts/index.md).

## What This Does Not Mean

- Glossary definitions are not exhaustive for the full transportation domain.
- Where glossary definitions conflict with a product manual, the product manual wins.

## How To Use This

**Agents**: Retrieve glossary pages for short definitional questions ("What is X?"). For deeper conceptual context, follow up with the relevant concept page or product section index. Prefer the narrowest matching page.

**Authors**: Add new terms to `glossary/terms.md` rather than creating per-term files unless the term requires concept-level treatment. Coordinate with product teams before publishing definitions that may conflict with product documentation.

## Example

A user asks: _"What does 'completeness' mean in OS-CONNECT?"_ Retrieve `glossary/terms.md` for the short definition, then retrieve `concepts/completeness.md` for deeper context.

## Assistant Guidance

Glossary pages are suitable for quick definitional answers but should always be supplemented by product-specific context when the question has an operational dimension. Note that definitions here are scoped to the TCAT assistant layer and may not match general GIS or transportation engineering usage.

## Related Concepts

- [Concepts](../concepts/index.md)
- [Dispatch — full file registry](../dispatch.md)
