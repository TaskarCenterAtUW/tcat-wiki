---
title: How do Adjacent and Custom Entities differ in OpenSidewalks?
slug: adjacent-vs-custom-entities
doc_type: concept
questions:
    - How do Adjacent and Custom Entities differ in OpenSidewalks?
    - Should I use an Adjacent Entity or a Custom Entity?
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
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every adjacent entity is a traversable part of an OpenSidewalks-formatted dataset's graph.
        - Custom entities are routable graph elements merely because they use OpenSidewalks geometry types.
        - Additional fields have valid standard schema semantics without an 'ext:' prefix.
related_pages:
    - adjacent-entities.md
    - custom-entities.md
    - network-entities.md
    - dataset-metadata-and-provenance.md
    - ../workflow/add-custom-points-to-osw.md
tags:
    - Assistant
---

<!-- @format -->

# How do Adjacent and Custom Entities differ in OpenSidewalks?

## Short Answer

Adjacent Entities are predefined non-network features that describe the environment around a pedestrian network. Custom Entities are user-defined Point, LineString, or Polygon features for data that does not fit a predefined Core or Adjacent entity. Additional fields that are not defined by the schema use the `ext:` prefix.

## Significance

The distinction helps data producers preserve the difference between features with established OpenSidewalks schema semantics and out-of-schema data support.

## What This Means

Use an Adjacent Entity when the feature matches a predefined OpenSidewalks type, such as an adjacent Point, Line, or Polygon. Use a Custom Entity when the feature is relevant to the dataset but does not match a predefined Core or Adjacent type. Both are spatial features rather than graph primitives. Each entity needs a unique `_id`, and fields not defined by the schema must use the `ext:` prefix.

## What This Does Not Mean

Neither category automatically creates network connectivity or becomes part of a traversable graph. A geometry type alone does not determine the complete entity meaning, and an `ext:` field is not automatically a standardized OpenSidewalks field.

## How To Use This

First decide whether the feature belongs in the Core network. If it does not, check whether a predefined Adjacent Entity fits. Use a Custom Entity only when no predefined type fits. Assign a unique `_id`, use the geometry model that matches the source feature, preserve nonstandard source attributes with `ext:`, and document the source and intended interpretation. Check the applicable schema version and validate the resulting dataset.

## Example

A bench uses a predefined Adjacent Point type. A GTFS bus stop, if it does not match a predefined type in the applicable schema version, can be represented as a Custom Point with a unique `_id`, WGS-84 coordinates in GeoJSON order, and fields such as `ext:stop_id` and `ext:stop_name`. Neither feature creates an Edge or connects to the pedestrian graph.

## Assistant Guidance

Ask which schema version and consumer are involved. Then ask whether the feature needs to be a routable graph element and whether a predefined Core or Adjacent entity already exists. Recommend a Custom Entity only when the feature does not match a predefined type. Do not infer routability or standardized meaning from geometry or an `ext:`-prefixed field alone. Cite the applicable schema documentation.

## Related Concepts

- [What entities does the OpenSidewalks Schema define?](network-entities.md)
- [What are Adjacent Entities in OpenSidewalks?](adjacent-entities.md)
- [What are Custom Entities in OpenSidewalks?](custom-entities.md)
- [How do I add Custom Points?](../workflow/add-custom-points-to-osw.md)
