---
uid: ee58075d-863b-4684-b394-8b4951dbae4a
title: What do Walksheds map symbols mean?
slug: walkshed-map-symbols
doc_type: concept
questions:
    - What do Walksheds map symbols mean?
    - What does the Walksheds map legend show?
audiences:
    - planner
    - public
products:
    - Walksheds
topics:
    - walksheds
    - interpretation
    - accessibility-metrics
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds map has visual map features that are not documented in the legend.
        - Display of an element as inaccessible is an ADA assessment of that feature.
related_pages:
    - walkshed-scenarios.md
    - walkshed-travel-cost.md
    - ../workflow/compare-walkshed-profiles.md
tags:
    - Assistant
---

<!-- @format -->

# What do Walksheds map symbols mean?

## Short Answer

The Walksheds map legend identifies symbols for movement speed, crossings, stairs, points, and walkshed results. The exact symbols and colors shown depend on the current map and selected settings.

## Significance

The legend connects visual symbols to modeled travel cost and reachability.

## What This Means

The visible legend is organized into these groups:

- **Movement speed due to incline**: high speed for flat areas, medium speed for moderate inclines, low speed for steep areas, and inaccessible segments.
- **Crossings**: unmarked crossings, marked crossings, and inaccessible crossings.
- **Stairs**: accessible and inaccessible stairs.
- **Points**: point features displayed on the map.
- **Walkshed**: cost nodes and the convex hull.

Use the legend to match each map symbol to its label under the selected profile and map settings.

## What This Does Not Mean

A legend label describes how Walksheds is displaying or modeling a map feature for the current analysis; it is not a universal accessibility, safety, or legal rating. The label **Inaccessible** should be interpreted within the category where it appears, such as movement speed, crossings, or stairs.

## How To Use This

Open the map legend after changing the mobility profile, cost settings, dataset, or other map settings. Compare the visible symbol with its label instead of relying on color alone.

## Example

For example, the legend uses a dotted red line for an inaccessible item in the movement-speed and crossing groups, while the stairs group uses a red dashed symbol for inaccessible stairs. The legend also shows colored cost-node points and a nested colored outline for the convex hull.

## Assistant Guidance

Instruct the user to reference the legend on the right side of the Walksheds interface for help interpreting visual aspects of the map. Do not infer a symbol's meaning from color alone or transfer a label from one legend group to another.

## Related Concepts

- [What factors affect Walksheds travel cost?](walkshed-cost-factors.md)
