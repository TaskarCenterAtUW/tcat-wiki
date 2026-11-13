---
uid: 30e8fc9c-9807-4698-903b-82ff2c572882
title: What are Custom Entities in OpenSidewalks?
slug: custom-entities
doc_type: concept
questions:
    - What are Custom Entities in OpenSidewalks?
    - How do Custom Entities extend the OpenSidewalks Schema?
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
    - formats
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - adjacent-entities.md
    - adjacent-and-custom-entities.md
    - ../workflow/add-custom-points-to-osw.md
tags:
    - Assistant
---

<!-- @format -->

# What are Custom Entities in OpenSidewalks?

## Short Answer

Custom Entities are user-defined schema types for features that do not fit predefined entity types. In OpenSidewalks 0.3, Custom Nodes, Edges, and Zones extend the traversable Core Entity models, while Custom Points, Lines, and Polygons extend the non-network Adjacent Entity models.

## Significance

Custom Entities support local and specialized data while keeping the feature's geometry, identifier, and nonstandard attributes for downstream consumers.

## What This Means

Custom Nodes are Points with a unique `_id`. Custom Edges are directional LineStrings with a unique `_id` and endpoint references `_u_id` and `_v_id`. Custom Zones are Polygons with a unique `_id` and `_w_id`, a list of Node references. These three custom types are graph entities. Custom Points, Lines, and Polygons each need a unique `_id` but are not graph entities. Additional fields not defined by the schema must use the `ext:` prefix, and their meaning should be documented for intended consumers.

Use a predefined Core Entity when its semantics fit the feature. When no predefined Core type fits but the feature belongs in the traversable graph, use the matching Custom Node, Edge, or Zone and provide its required topology.

## What This Does Not Mean

A Custom Point, Line, or Polygon does not create network connectivity. A Custom Node, Edge, or Zone uses the relevant graph structure but does not acquire the semantics of a predefined entity type. An `ext:` field is not automatically interoperable or meaningful to every consumer, and a Custom Point does not become an on-graph Node merely because it has valid coordinates.

## How To Use This

Confirm that no predefined Core or Adjacent entity fits, then choose the custom model that matches the feature: Node, Edge, or Zone when it belongs in the traversable graph; Point, Line, or Polygon when it is spatial context only. Supply the model's required identifier and topology fields, prefix nonstandard fields with `ext:`, document their meaning, and validate against the applicable schema version.

## Example

A GTFS bus stop can be represented as a Custom Point when the applicable schema version has no predefined entity for that feature. The feature can preserve `ext:stop_id` and `ext:stop_name` alongside its unique `_id` and WGS-84 coordinates. It remains non-routable unless separately represented by appropriate Core Entities.

## Assistant Guidance

Ask which schema version and consumer are involved, what the source feature represents, and whether it needs to be part of the traversable graph. Recommend a predefined entity when one fits. Do not invent `ext:` field semantics or imply that a Custom Entity is routable. Cite the applicable schema documentation and source documentation when available.

## Related Concepts

- [What are Adjacent Entities in OpenSidewalks?](adjacent-entities.md)
- [How do Adjacent and Custom Entities differ?](adjacent-vs-custom-entities.md)
- [How do I add Custom Points?](../workflow/add-custom-points-to-osw.md)
