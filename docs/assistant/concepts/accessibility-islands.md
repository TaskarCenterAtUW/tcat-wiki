---
title: Accessibility islands
tags:
    - Assistant
slug: accessibility-islands
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - network-topology
    - pedestrian-graph
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - A specific neighborhood is an island without checking current local graph connectivity.
related_pages:
    - assistant/concepts/connected-pedestrian-graph.md
    - assistant/questions/os-connect/why-are-sidewalks-disconnected.md
---

<!-- @format -->

# Accessibility islands

## Short Answer

An accessibility island is a subgraph of the pedestrian network that is internally reachable under given rules but disconnected from other parts—so a person following those rules cannot travel between islands without leaving the modeled walk network or violating a constraint.

## Significance

Islands explain counterintuitive routing gaps, walkshed boundaries, and completeness narratives. Naming the pattern reduces blame directed at individual apps when the underlying data topology is the driver.

## What This Means

Connectivity depends on modeled geometry, attributes, and the cost or access rules in use (for example, curb ramps, surface types, or custom costs). Fixing an island often requires data edits, imports, or infrastructure changes—not only app settings.

## What This Does Not Mean

- Not every disconnected appearance on a basemap implies an island in the routed graph; basemap tiles can differ from routing data.
- Not a moral judgment about a community’s commitment to access.

## How To Use This

Planners can prioritize bridge links between islands. Advocates can pair island maps with engagement narratives. Assistants should describe islands qualitatively unless a cited report names a geography.

## Example

Two dense corridors each have full local sidewalk coverage but lack a tagged crossing connection between them. Routing may treat them as separate islands until a valid crossing link exists in the dataset.

## Assistant Guidance

Use neutral, technical language. If asked "why can’t I get there," explain islanding as one common cause and suggest reporting data issues through the appropriate product channel. Do not guess at a specific user’s location without data.

## Related Concepts

- [Connected pedestrian graph](connected-pedestrian-graph.md)
- [Why are sidewalks disconnected?](../questions/os-connect/why-are-sidewalks-disconnected.md)
