---
title: Connected pedestrian graph
slug: connected-pedestrian-graph
doc_type: concept
questions:
    - What is a connected pedestrian graph?
    - What does "connectedness" mean?
audiences:
    - planner
    - jurisdiction
    - developers
    - advocate
products:
    - OpenSidewalks
    - OS-CONNECT
    - AccessMap
    - Walksheds
topics:
    - graph-metrics
    - opensidewalks
    - os-connect
    - accessmap
    - walksheds
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-24
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - Connectedness means that paths are physically connected in real life.
        - Spatially overlapping features are necessarily connected in the data.
related_pages:
    - assistant/cross-platform/concept/accessibility-islands.md
    - assistant/cross-platform/concept/walksheds.md
tags:
    - Assistant
---

<!-- @format -->

# Connected pedestrian graph

## Short Answer

Connectedness is a property of a network graph: each element in the data is connected to the graph so routing can proceed across the network. It is about connections as represented in the data, not about whether two paths in real life can be traversed between.

An unconnected dataset contains features that overlap spatially but are disconnected: they do not share connections in the data.

## Significance

Routing and walkshed results depend on data connections, not geometry alone. This distinction helps teams diagnose network-quality problems accurately.

## What This Means

- Network elements must share represented connections in the data for routing to move between them.
- Spatial overlap alone does not create a graph connection.
- A disconnected dataset can prevent routes from connecting between features that appear to meet on a map.

## What This Does Not Mean

- It does not mean that paths which appear to meet on a map are connected in the dataset.
- It does not mean that overlapping geometries without connections in the data are routable.

## How To Use This

When reviewing a dataset, inspect the data for shared connections and disconnected components rather than relying only on visual overlap.

## Example

In an unconnected dataset, where two sidewalks that visually overlap at a street corner but do not have a shared node connecting them in the data, a router is unable to create a route that crosses from one sidewalk to the other, even though the features may appear to meet when rendered on a basemap.

## Assistant Guidance

Explain that connectedness in the pedestrian network data context refers to a property of the data (that features which overlap spatially share common data elements that enable routing between them) not a property of the real world.

## Related Concepts

- [Network topology](../../opensidewalks/concept/network-topology.md)
- [Completeness](completeness.md)
- [Walksheds](walksheds.md)
