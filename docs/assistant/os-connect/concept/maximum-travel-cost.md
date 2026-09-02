---
uid: 54a5848f-4c28-426c-b6d1-1537aa4bf176
title: What is the maximum travel cost?
slug: maximum-travel-cost
doc_type: concept
questions:
    - What is the maximum travel cost?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - walksheds
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
    - assistant/os-connect/concept/max-cost.md
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/maximum-travel-cost.md
tags:
    - Assistant
---

<!-- @format -->

# What is the maximum travel cost?

## Short Answer

Maximum travel cost is the upper limit on accumulated cost used by a network or walkshed analysis. Cost may include distance, elevation, barriers, crossings, or profile-specific penalties according to the implementation.

## Significance

The limit controls how much modeled travel is allowed and therefore affects reachability, route selection, and which destinations appear reachable.

## What This Means

Check the units, cost function, profile, network, origin, and release. The same numeric value may not mean the same thing across profiles or products.

## What This Does Not Mean

Maximum travel cost is not a universal distance, endurance measure, medical threshold, or guarantee of physical accessibility.

## How To Use This

Record the value and definition with each result, compare only compatible analyses, and explain changes as modeled travel-budget effects.

## Example

A lower maximum cost creates a smaller modeled reachability area under the same network and profile; the analyst records the setting rather than treating the change as a physical improvement.

## Assistant Guidance

Name the implementation, units, profile, and release. Cite current documentation and abstain when the cost definition is unknown.

## Related Concepts

- [What is "max_cost"?](../../walksheds/concept/max-cost.md)
- [What is a routable graph?](routable-graph.md)
