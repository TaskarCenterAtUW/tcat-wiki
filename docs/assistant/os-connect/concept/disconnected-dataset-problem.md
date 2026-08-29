---
title: Why are disconnected pedestrian datasets a problem?
slug: disconnected-dataset-problem
doc_type: concept
questions:
    - Why are disconnected pedestrian datasets a problem?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - data-quality
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
    - assistant/os-connect/concept/disconnected-sidewalk-identification.md
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/connectivity-depends-on-geometry.md
tags:
    - Assistant
---

<!-- @format -->

# Why are disconnected pedestrian datasets a problem?

## Short Answer

Disconnected pedestrian datasets make it harder to see, analyze, and route through the network. Gaps between features can hide access barriers, reduce modeled reachability, and make results difficult to compare across jurisdictions or products.

## Significance

Pedestrian access often depends on a sequence of sidewalks, crossings, ramps, and entrances. Missing relationships in separate datasets can make an apparently available path unusable in analysis.

## What This Means

Check geometry, connectivity, crossings, feature relationships, coverage, and release versions. Use a connected graph or network analysis only with documented processing rules and appropriate validation.

## What This Does Not Mean

Dataset disconnection does not prove that the physical network is disconnected, and a connected dataset does not prove that a route is accessible or current.

## How To Use This

Use identified gaps to prioritize data review and local verification. Preserve source data and document whether a gap reflects missing mapping, a processing issue, a boundary, or a real condition.

## Example

A sidewalk appears to end at a roadway because the crossing is absent from the dataset. The analyst reports the missing connection instead of concluding that the physical route does not exist.

## Assistant Guidance

Distinguish data-network gaps from real-world barriers. Cite the release and method, avoid compliance claims, and abstain when the geometry or processing context is unknown.

## Related Concepts

- [How are disconnected sidewalks identified?](disconnected-sidewalk-identification.md)
- [What is a routable graph?](routable-graph.md)
- [Why does OS-CONNECT connectivity depend on geometry?](connectivity-depends-on-geometry.md)
