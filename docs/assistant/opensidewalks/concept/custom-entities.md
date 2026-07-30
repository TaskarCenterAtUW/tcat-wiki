---
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
    do_not_claim:
        - A Custom Entity is a routable graph element merely because it uses an OpenSidewalks geometry type.
        - A Custom Entity has the semantics of a predefined schema entity without matching that entity's identifying fields.
        - Additional fields have standard schema semantics without an 'ext:' prefix.
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

Custom Entities are user-defined Point, LineString, or Polygon features that extend the OpenSidewalks Schema beyond its predefined Core and Adjacent categories. They allow a dataset to preserve a relevant feature when no predefined entity type fits.

## Significance

Custom Entities support local and specialized data while keeping the feature's geometry, identifier, and nonstandard attributes for downstream consumers.

## What This Means

The schema defines Custom Points, Custom Lines, and Custom Polygons. A Custom Entity has no predefined identifying fields that classify it as a standard Core or Adjacent entity. Each entity needs a unique `_id`. Additional fields that are not defined by the schema must use the `ext:` prefix, and their meaning should be documented for intended consumers.

Custom Entities are not substitutes for Core Entities. If a feature is meant to participate in the traversable graph, determine whether it should be modeled using the applicable Core Entity rather than using a Custom Entity.

## What This Does Not Mean

A Custom Entity does not automatically create network connectivity or acquire the semantics of a standard schema entity. An `ext:` field is not automatically interoperable or meaningful to every consumer, and a Custom Point does not become an on-graph Node merely because it has valid coordinates.

## How To Use This

Confirm that no predefined Core or Adjacent entity fits. Choose Point, LineString, or Polygon geometry, assign a unique `_id`, prefix nonstandard fields with `ext:`, document the source and intended interpretation, and validate the dataset against the applicable schema version.

## Example

A GTFS bus stop can be represented as a Custom Point when the applicable schema version has no predefined entity for that feature. The feature can preserve `ext:stop_id` and `ext:stop_name` alongside its unique `_id` and WGS-84 coordinates. It remains non-routable unless separately represented by appropriate Core Entities.

## Assistant Guidance

Ask which schema version and consumer are involved, what the source feature represents, and whether it needs to be part of the traversable graph. Recommend a predefined entity when one fits. Do not invent `ext:` field semantics or imply that a Custom Entity is routable. Cite the applicable schema documentation and source documentation when available.

## Related Concepts

- [What are Adjacent Entities in OpenSidewalks?](adjacent-entities.md)
- [How do Adjacent and Custom Entities differ?](adjacent-and-custom-entities.md)
- [How do I add Custom Points?](../workflow/add-custom-points-to-osw.md)
