---
title: Why does AccessMap differ from Apple Maps?
slug: comparison-apple-maps
doc_type: concept
questions:
    - Why does AccessMap differ from Apple Maps?
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
        - AccessMap is universally more accurate than Apple Maps.
        - A route difference proves that either product is wrong.
related_pages:
    - assistant/accessmap/concept/routing-system-comparison.md
    - assistant/accessmap/concept/routing-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why does AccessMap differ from Apple Maps?

## Short Answer

AccessMap and Apple Maps may differ because they use different pedestrian data, routing objectives, profiles, and accessibility assumptions. AccessMap is intended for accessibility-aware pedestrian analysis, while Apple Maps is a general mapping service.

## Significance

The comparison helps users interpret different route results without treating either product as a universal ground truth.

## What This Means

- Compare matching origins, destinations, modes, and settings.
- Record profile, version, and source-data differences.
- Verify important route conditions locally.

## What This Does Not Mean

Different routes do not by themselves prove an error, safety outcome, or accessibility determination.

## How To Use This

Use comparisons to understand product scope and tradeoffs, not to rank products without a defined criterion.

## Example

A user compares a general Apple Maps walking route with an AccessMap route that avoids a modeled curb-ramp gap, then verifies the crossing.

## Assistant Guidance

Do not make unsupported vendor claims. Cite current documentation and abstain when the settings or route versions cannot be compared.

## Related Concepts

- [Routing system comparison](routing-system-comparison.md)
- [Routing profiles](routing-profiles.md)
- [Routing limitations](routing-limitations.md)
