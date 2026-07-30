---
title: How are adjacent and custom entities used in OpenSidewalks?
slug: adjacent-and-custom-entities
doc_type: concept
questions:
    - What are adjacent entities in OpenSidewalks?
    - How do custom entities extend the OpenSidewalks Schema?
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
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every adjacent entity is a traversable part of the OpenSidewalks graph.
        - Custom entities are routable graph elements merely because they use OpenSidewalks geometry types.
        - Additional fields have standard schema semantics without an ext: prefix.
related_pages:
    - network-entities.md
    - dataset-metadata-and-provenance.md
    - ../workflow/add-custom-points-to-osw.md
tags:
    - Assistant
---

<!-- @format -->

# How are adjacent and custom entities used in OpenSidewalks?

## Short Answer

Adjacent Entities describe features near the pedestrian network. Custom Entities are user-defined Point, LineString, or Polygon features that extend the schema beyond the predefined Core and Adjacent categories. Additional fields that are not defined by the schema use the `ext:` prefix.

## Significance

These mechanisms add useful environmental and regional information without incorrectly turning every nearby feature into a routable graph element.

## What This Means

Adjacent Entities have three geometry models: Points, Lines, and Polygons. They describe features that are relevant to the pedestrian network but are not represented as graph elements. Examples include benches or hydrants as Points, walls or fences as Lines, and planters as Polygons. Their relationship to other dataset features is spatial.

Custom Entities also have three geometry models: Custom Points, Custom Lines, and Custom Polygons. They are user-defined features for data that does not fit a predefined Core or Adjacent entity. Each entity needs a unique `_id`, and fields not defined by the schema must use the `ext:` prefix. Custom Points can represent non-routable features such as bus stops.

## What This Does Not Mean

Adjacent or custom data does not automatically create network connectivity or become part of the traversable graph. A geometry type alone does not determine the complete entity meaning, and an `ext:` field is not automatically a standardized OpenSidewalks field.

## How To Use This

First decide whether the feature belongs in the Core network, describes an adjacent feature, or requires a Custom Entity. Use a predefined entity and field when one fits. Otherwise, assign a unique `_id`, use the geometry model that matches the source feature, preserve nonstandard source attributes with `ext:`, and document the source and intended interpretation. Check the applicable schema version and validate the resulting dataset.

## Example

A GTFS bus stop becomes a Custom Point with a unique `_id`, WGS-84 coordinates in GeoJSON order, and fields such as `ext:stop_id` and `ext:stop_name`. It remains a nearby, non-routable feature; it does not create an Edge or connect the pedestrian graph.

## Assistant Guidance

Ask which schema version and consumer are involved. Then ask whether the feature needs to be a routable graph element, whether a predefined Core or Adjacent entity already exists, and which source attributes must be preserved. Do not infer routability or standardized meaning from geometry or an `ext:` field alone. Cite the applicable schema documentation.

## Related Concepts

- [What entities does the OpenSidewalks Schema define?](network-entities.md)
- [How do I add Custom Points?](../workflow/add-custom-points-to-osw.md)
