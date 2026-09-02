---
uid: 841c5a81-ce33-4954-8b83-c1cf4da5056d
title: How does construction affect routing?
slug: construction-routing-effect
doc_type: concept
questions:
    - How does construction affect routing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - construction
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
        - AccessMap always reflects current construction conditions.
        - A route unaffected in the model is guaranteed to be open.
related_pages:
    - assistant/accessmap/concept/temporary-barriers.md
    - assistant/accessmap/concept/update-cadence.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# How does construction affect routing?

## Short Answer

Construction can change an AccessMap route when a mapped closure, barrier, or unavailable segment is represented in the current data. If the construction is missing or outdated, the model may not reflect the field condition.

## Significance

Temporary changes can make a route result stale and can affect people who depend on a precise accessible path.

## What This Means

- Check the route date, source dataset, and temporary-condition information.
- Compare alternate routes when a closure affects the trip.
- Verify current conditions and report missing or outdated barriers.

## What This Does Not Mean

No map result guarantees that construction conditions are current. A construction label does not describe every detour, surface, or access condition.

## How To Use This

Treat construction as time-sensitive, cite the data date, and use official local notices or field verification for current travel decisions.

## Example

A sidewalk closure is present in local information but absent from the route dataset. The user checks the official notice and chooses a verified alternate path.

## Assistant Guidance

Do not provide current detour instructions without current evidence. Ask for location and date, cite the source, and abstain from safety claims.

## Related Concepts

- [Temporary barriers](temporary-barriers.md)
- [AccessMap update cadence](update-cadence.md)
- [Routing limitations](routing-limitations.md)
