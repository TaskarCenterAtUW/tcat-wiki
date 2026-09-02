---
uid: 007890b5-c089-482e-a2bb-6b8e06992e3f
title: What network assumptions are used?
slug: network-assumptions
doc_type: concept
questions:
    - What network assumptions are used?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - graph-metrics
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
    - assistant/walksheds/concept/walkshed-calculation.md
    - assistant/walksheds/concept/barrier-incorporation.md
    - assistant/walksheds/concept/disconnected-network-handling.md
tags:
    - Assistant
---

<!-- @format -->

# What network assumptions are used?

## Short Answer

Walkshed network assumptions describe which pedestrian features, connections, crossings, barriers, costs, access restrictions, elevation effects, and snapping rules the analysis uses. Exact assumptions depend on the product, dataset, profile, and release.

## Significance

Assumptions determine which routes are possible and how travel cost is accumulated. They explain why a walkshed is a model of reachability rather than a direct survey of conditions.

## What This Means

Record the network source and date, graph construction, profile, crossing and barrier treatment, elevation, maximum cost, destination filters, and handling of missing or disconnected data.

## What This Does Not Mean

A network assumption does not prove that a feature exists, is accessible, or is usable now. Results from different assumptions should not be compared as if they were identical.

## How To Use This

Read the assumptions before interpreting a result, test sensitivity to important settings, validate high-consequence findings locally, and state limitations in reports.

## Example

A path is excluded because the selected profile treats a modeled barrier as impassable. The analyst reports the rule and checks whether the barrier is current and correctly represented.

## Assistant Guidance

Name the implementation and settings, avoid filling undocumented rules by intuition, and abstain when the network construction or profile behavior is unknown.

## Related Concepts

- [How are walksheds calculated?](walkshed-calculation.md)
- [How are barriers incorporated?](barrier-incorporation.md)
- [How are disconnected networks handled?](disconnected-network-handling.md)
