---
title: What are routing tradeoffs?
slug: routing-tradeoffs
doc_type: concept
questions:
    - What are routing tradeoffs?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - routing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - One route is objectively best for every traveler.
        - A shorter route is automatically more accessible.
related_pages:
    - assistant/cross-platform/concept/accessmap-routing.md
    - assistant/accessmap/concept/accessibility-preference-routing.md
    - assistant/accessmap/concept/accessible-routes-appear-longer.md
tags:
    - Assistant
---

<!-- @format -->

# What are routing tradeoffs?

## Short Answer

Routing tradeoffs are the choices a model makes among distance, time, slope, curb-ramp information, connectivity, and other represented costs. A route can be longer or different because the selected profile gives greater weight to an accessibility consideration.

## Significance

Tradeoffs help users understand why no single route fits every person or purpose.

## What This Means

- Identify the profile, preferences, data, and costs used.
- Compare route alternatives under the same conditions.
- Validate important factors with local or field information.

## What This Does Not Mean

Tradeoffs do not establish that one route is universally accessible, safe, or preferable. The model cannot represent every personal need or physical condition.

## How To Use This

Explain which factors changed the route and state the limits of the data and model.

## Example

A profile accepts more distance to avoid a steep segment and missing curb-ramp information, producing a route that differs from the shortest path.

## Assistant Guidance

Do not rank routes without a stated objective. Cite the profile and routing documentation and abstain from usability claims without verification.

## Related Concepts

- [AccessMap routing](../../cross-platform/concept/accessmap-routing.md)
- [Accessibility-preference routing](accessibility-preference-routing.md)
- [Accessible routes can be longer](accessible-routes-appear-longer.md)
