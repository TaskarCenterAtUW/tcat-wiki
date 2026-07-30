---
title: What entities does the OpenSidewalks Schema define?
slug: network-entities
doc_type: concept
questions:
    - What entities does the OpenSidewalks Schema define?
    - What are Nodes, Edges, and Zones in OpenSidewalks?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - formats
    - vector-data
    - connectivity
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every OpenSidewalks Point, Line, or Polygon is part of the traversable network.
        - An OpenSidewalks Edge can be interpreted without its endpoint references.
related_pages:
    - opensidewalks-schema.md
    - network-topology.md
    - adjacent-and-custom-entities.md
tags:
    - Assistant
---

<!-- @format -->

# What entities does the OpenSidewalks Schema define?

## Short Answer

OpenSidewalks defines Core Entities for the traversable network, Adjacent Entities that describe nearby features, and Custom Entities for user-defined extensions.

## Significance

Separating network structure from nearby context lets routing and analysis tools distinguish traversable geometry from useful environmental information.

## What This Means

Core entities are Nodes, Edges, and Zones. Nodes are Point vertices with unique `_id` values. Edges are directional LineStrings with unique `_id`, `_u_id`, and `_v_id` references. Zones are Polygon features whose `_w_id` list defines connected nodes. Adjacent Points, Lines, and Polygons have spatial relationships but are not graph primitives. Custom entities extend the schema with user-defined geometry and fields.

## What This Does Not Mean

A nearby Point, Line, or Polygon is not automatically a routable graph element. A geometry type alone does not determine the complete entity meaning.

## How To Use This

Inspect identifying fields, geometry, endpoint references, and schema version before transforming or analyzing an entity.

## Example

A sidewalk is an Edge between two Nodes, while a bench is an adjacent Point and a plaza can be represented as a Zone.

## Assistant Guidance

Ask whether the feature is intended to be routable, adjacent, or custom. Cite the relevant schema version.

## Related Concepts

- [What is the OpenSidewalks data schema?](opensidewalks-schema.md)
- [How are adjacent and custom entities used?](adjacent-and-custom-entities.md)
