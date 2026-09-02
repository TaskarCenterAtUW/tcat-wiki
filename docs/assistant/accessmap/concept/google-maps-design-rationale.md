---
uid: bb4dabc2-8f6b-4491-8360-923c0d614e1f
title: Why does AccessMap differ from Google Maps?
slug: google-maps-design-rationale
doc_type: concept
questions:
    - Why does AccessMap differ from Google Maps?
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
        - AccessMap and Google Maps have the same routing purpose and assumptions.
        - AccessMap is universally more accurate than Google Maps.
related_pages:
    - assistant/accessmap/concept/google-maps-comparison.md
    - assistant/accessmap/concept/routing-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why does AccessMap differ from Google Maps?

## Short Answer

AccessMap differs from Google Maps because it focuses on accessibility-aware pedestrian routing rather than only general-purpose route selection. Differences can result from data sources, profiles, routing objectives, and treatment of accessibility attributes.

## Significance

Understanding the design difference helps users interpret route discrepancies and choose the tool that fits the question.

## What This Means

- Compare equivalent origins, destinations, modes, and time context.
- Record AccessMap preferences, product versions, and source data.
- Verify important route conditions locally.

## What This Does Not Mean

The design distinction does not prove that either route is correct, safe, or accessible in the field. AccessMap is not a replacement for every Google Maps capability.

## How To Use This

Use the comparison to explain scope and tradeoffs, not to make unsupported vendor rankings.

## Example

A user compares a Google Maps walking route with an AccessMap route that avoids modeled slopes, then checks the route conditions before traveling.

## Assistant Guidance

Answer with documented product behavior, cite the comparison, and abstain when route settings or versions are unknown.

## Related Concepts

- [AccessMap versus Google Maps](google-maps-comparison.md)
- [Routing profiles](routing-profiles.md)
- [Routing limitations](routing-limitations.md)
