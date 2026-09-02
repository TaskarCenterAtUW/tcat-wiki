---
uid: 622342dd-bb05-4814-95e5-75286b469b66
title: Why does AccessMap differ from HERE routing?
slug: here-routing-comparison
doc_type: concept
questions:
    - Why does AccessMap differ from HERE routing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - comparison
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
        - AccessMap is universally more accurate than HERE routing.
        - A difference between AccessMap and HERE proves one route is wrong.
related_pages:
    - assistant/accessmap/concept/routing-system-comparison.md
    - assistant/accessmap/concept/routing-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why does AccessMap differ from HERE routing?

## Short Answer

AccessMap and HERE may produce different walking routes because they use different data, routing objectives, profiles, and treatment of accessibility information. A comparison should identify those differences rather than assume one product is a universal reference.

## Significance

Comparative testing helps agencies understand whether a product fits an accessibility-aware use case and where results need verification.

## What This Means

- Use the same origin, destination, mode, and conditions where possible.
- Record profiles, data versions, and route assumptions.
- Compare results with field observations for important locations.

## What This Does Not Mean

Route differences do not by themselves establish accuracy, safety, or accessibility. Neither product's route replaces local verification.

## How To Use This

Document the comparison method and interpret results within each product's scope.

## Example

An analyst compares a general route from HERE with an AccessMap route using a slope-sensitive profile and explains the difference through the settings and data.

## Assistant Guidance

Do not make unsupported vendor comparisons. Cite current product documentation and abstain when profiles, versions, or source data are unknown.

## Related Concepts

- [Routing system comparison](routing-system-comparison.md)
- [Routing profiles](routing-profiles.md)
- [Routing limitations](routing-limitations.md)
