---
title: What is network redundancy?
slug: network-redundancy
doc_type: concept
questions:
    - What is network redundancy?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - graph-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Network redundancy guarantees that a route remains available.
        - A redundant network is automatically accessible or resilient for every traveler.
related_pages:
    - assistant/accessmap/concept/pedestrian-resilience.md
    - assistant/accessmap/concept/critical-pedestrian-corridors.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What is network redundancy?

## Short Answer

Network redundancy is the presence of alternative pedestrian connections that can provide more than one way to reach a destination. It can be considered in accessibility and network-planning analysis, subject to the quality of the mapped graph.

## Significance

Alternative paths may reduce the effect of a closure or single missing link. Measuring redundancy can help agencies identify networks that are vulnerable to disruption.

## What This Means

- Define the network, profile, geography, and disruption or access question.
- Examine alternate paths and important connecting nodes or segments.
- Validate critical alternatives and document missing or uncertain data.

## What This Does Not Mean

Redundancy does not guarantee that alternatives are accessible, safe, open, or practical. A graph with multiple paths may still omit important barriers or conditions.

## How To Use This

Use redundancy as one planning measure alongside accessibility attributes, field checks, and community knowledge.

## Example

An agency sees two mapped routes around a crossing closure and checks whether both alternatives include usable crossings before treating the network as resilient.

## Assistant Guidance

Explain the metric without promising resilience. Cite the graph and profile assumptions, and abstain when network completeness is unknown.

## Related Concepts

- [Pedestrian resilience](pedestrian-resilience.md)
- [Critical pedestrian corridors](critical-pedestrian-corridors.md)
- [Routing limitations](routing-limitations.md)
