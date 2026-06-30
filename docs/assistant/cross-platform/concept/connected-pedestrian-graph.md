---
title: Connected pedestrian graph
tags:
    - Assistant
slug: connected-pedestrian-graph
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
audiences:
    - planner
    - jurisdiction
    - advocate
topics:
    - network-topology
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - The graph matches every informal desire line or off-street private path.
related_pages:
    - assistant/concepts/accessibility-islands.md
    - assistant/concepts/walksheds.md
---

<!-- @format -->

# Connected pedestrian graph

## Short Answer

The connected pedestrian graph is the set of walkable edges and nodes — sidewalks, crossings, ramps, and transitions — that routing and walkshed engines use as a network. Connectivity is a property of that graph under specific rules and data, not of aerial imagery alone.

## Significance

Many public questions about "missing routes" or "wrong walksheds" are graph questions. Explaining the graph shifts conversations from app bugs alone to data stewardship and design standards.

## What This Means

Edges carry attributes (slope, surface, crossing type, etc.) that affect whether they are traversable for a profile or cost model. The same geometry can be connected for one profile and effectively disconnected for another.

## What This Does Not Mean

- Not equivalent to every socially used walking path.
- Not a promise that the fastest car road connection is mirrored for pedestrians.

## How To Use This

When scoping improvements, trace graph components and critical connectors. When communicating with the public, distinguish "not routable in the app" from "physically impossible to walk."

## Example

A campus path exists on the ground but is not in OS-CONNECT; the routing graph may omit it until mapped and validated through the jurisdiction's pipeline.

## Assistant Guidance

If users report a missing connection, acknowledge graph dependence and point to feedback or data contribution pathways in the relevant product docs without promising timelines.

## Related Concepts

- [Accessibility islands](accessibility-islands.md)
- [Walksheds](walksheds.md)
