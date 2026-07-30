---
title: What are Adjacent Entities in OpenSidewalks?
slug: adjacent-entities
doc_type: concept
questions:
    - What are Adjacent Entities in OpenSidewalks?
    - What are OpenSidewalks Adjacent Points, Lines, and Polygons?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - vector-data
    - interoperability
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any Adjacent Entity is a traversable part of the OpenSidewalks graph.
        - Adjacent Entities are required for a valid OpenSidewalks dataset.
        - A geometry type alone determines an Adjacent Entity's complete meaning.
related_pages:
    - custom-entities.md
    - adjacent-and-custom-entities.md
    - network-entities.md
tags:
    - Assistant
---

<!-- @format -->

# What are Adjacent Entities in OpenSidewalks?

## Short Answer

Adjacent Entities are predefined Point, Line, and Polygon features that describe the environment around an OpenSidewalks pedestrian network. They are relevant to the pedestrian experience but are not elements of the network graph.

## Significance

Adjacent Entities let a dataset preserve useful environmental context, such as nearby vegetation, barriers, or seating, without confusing that context with traversable network geometry.

## What This Means

Adjacent Entities have three geometry models: Points, Lines, and Polygons. Examples include a bench or hydrant as an adjacent Point, a wall or fence as an adjacent Line, and a building as an adjacent Polygon. Their relationship to Core Entities is spatial rather than defined by network endpoint metadata.

Adjacent Entities are optional; they are not required to produce a valid OpenSidewalks dataset. Schema-defined Adjacent Entities use the fields and semantics of the applicable schema version, including a unique `_id` for each entity.

## What This Does Not Mean

An Adjacent Entity is not a Node, Edge, Zone, or other traversable graph element. A feature's physical proximity to a path does not create network connectivity, and omitting Adjacent Entities does not by itself make a dataset invalid.

## How To Use This

Use a predefined Adjacent Entity when a nearby feature matches the applicable schema type. Assign its required identifying fields and a unique `_id`, preserve any additional not-in-schema attributes with the `ext:` prefix, and validate against the relevant schema version.

## Example

A bench beside a sidewalk is represented as an adjacent Point. A routing tool may use the bench as environmental context, but the bench does not become a Node or connect to the sidewalk's endpoint Nodes.

## Assistant Guidance

Ask which schema version and consumer are involved. Confirm that the feature matches a predefined Adjacent Entity and is not intended to be a traversable Core Entity. Do not infer graph connectivity from proximity or geometry alone. Cite the applicable schema documentation.

## Related Concepts

- [What are Custom Entities in OpenSidewalks?](custom-entities.md)
- [How do Adjacent and Custom Entities differ?](adjacent-vs-custom-entities.md)
- [What entities does the OpenSidewalks Schema define?](network-entities.md)
