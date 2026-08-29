---
title: What routing assumptions are used?
slug: routing-assumptions
doc_type: concept
questions:
    - What routing assumptions are used?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
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
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/routing-personalization.md
    - assistant/os-connect/concept/elevation-routing-effects.md
tags:
    - Assistant
---

<!-- @format -->

# What routing assumptions are used?

## Short Answer

Routing assumptions describe which pedestrian features and connections are included, how distance, elevation, barriers, crossings, and attributes affect cost, and how profiles and missing data are handled.

## Significance

Assumptions determine which routes are possible and why different profiles or releases can produce different results.

## What This Means

Record the network source and date, graph construction, origin snapping, profile, cost function, slope and crossing treatment, barriers, restrictions, maximum cost, and missing-data rules.

## What This Does Not Mean

A routing assumption does not prove that a modeled route is accessible, safe, current, or usable for every traveler.

## How To Use This

Read assumptions before interpreting a route or network metric, compare compatible settings, validate important results, and state limitations.

## Example

A route changes after a profile treats a missing curb-ramp value or steep slope differently. The analyst reports the rule rather than calling one result universally correct.

## Assistant Guidance

Name the implementation and settings, cite current documentation, and abstain when the route-processing rules or source release are unknown.

## Related Concepts

- [What is a routable graph?](routable-graph.md)
- [Can routing systems personalize accessibility preferences?](routing-personalization.md)
- [How do elevation constraints affect routing?](elevation-routing-effects.md)
