---
title: Concepts — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-concepts
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
    - accessibility-data
    - vector-data
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/glossary/index.md
---

<!-- @format -->

# Concepts — Assistant Knowledge Base

## Short Answer

This section contains cross-product conceptual pages that explain foundational ideas relevant to multiple TCAT tools. Each page defines a concept, explains its significance, and describes how it applies across products such as OS-CONNECT, AccessMap, and Walksheds.

## Significance

Cross-product concepts — such as the connected pedestrian graph, accessibility islands, data completeness, and ADA compliance boundaries — appear in questions across all TCAT products. Having dedicated concept pages prevents redundant explanations and ensures consistent, grounded answers.

## What This Means

- Pages in `concepts/` address ideas that cut across at least two TCAT products or that are prerequisite knowledge for understanding product-specific questions.
- Workspaces-specific concepts (sandbox governance, dataset lineage, imagery layers, etc.) are in [workspaces/](../workspaces/index.md), colocated with the Workspaces question pages.
- Term definitions for the glossary are in [glossary/](../glossary/index.md).

## What This Does Not Mean

- Concept pages are not procedure guides; for procedural content, see [workflows/](../workflows/index.md) or the relevant product section.
- Definitions here are scoped to assistant-layer usage; product manuals take precedence for authoritative technical definitions.

## How To Use This

**Agents**: For questions about what a term means, check [glossary/](../glossary/index.md) first, then retrieve the matching concept page for deeper context. Concept pages carry `retrieval_priority: medium` and supplement rather than replace product-specific pages.

**Authors**: Six concepts are planned. Start with `completeness.md` and `connected-pedestrian-graph.md`, which are referenced across many OS-CONNECT and Walksheds questions.

## Example

A planner asks: _"What is an accessibility island?"_ Retrieve `concepts/accessibility-islands.md` for the foundational definition, then retrieve `walksheds/what-are-accessibility-islands-in-walkshed-analysis.md` for the Walksheds-specific application.

## Assistant Guidance

Concept pages provide definitional grounding; always supplement them with product-specific pages when a user's question has an operational context. For ADA-adjacent concepts, check `risk_level` and follow the guidance in `policies/ada-safety-legal-boundaries.md`.

## Related Concepts

- [Glossary](../glossary/index.md)
- [Policies](../policies/index.md)
- [Workspaces concepts](../workspaces/index.md)
- [Dispatch — full file registry](../dispatch.md)

## Planned Pages

| File | Concept |
|------|---------|
| `concepts/accessibility-islands.md` | Isolated accessible zones disconnected from the broader network |
| `concepts/accessmap-routing.md` | How AccessMap applies mobility-profile-aware routing |
| `concepts/ada-compliance-boundaries.md` | What assistants may and may not say about ADA compliance |
| `concepts/completeness.md` | What network completeness scores mean and their limits |
| `concepts/connected-pedestrian-graph.md` | The routable pedestrian network model underlying TCAT tools |
| `concepts/walksheds.md` | The walkshed concept: network-based reachability analysis |
