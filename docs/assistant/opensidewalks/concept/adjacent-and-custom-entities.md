---
title: "How are adjacent and custom entities used in OpenSidewalks?"
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
        - Custom fields have standard schema semantics without an ext: prefix.
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

Adjacent entities describe features near the pedestrian network, while Custom Entities and `ext:` fields preserve user-defined information beyond the predefined schema.

## Significance

These mechanisms add useful environmental and regional information without incorrectly turning every nearby feature into a routable graph element.

## What This Means

Adjacent Points, Lines, and Polygons can represent benches, hydrants, walls, fences, planters, and other nearby features. Custom entities use user-defined geometry types, and additional attributes should use the `ext:` prefix. Custom Points can represent non-routable features such as bus stops.

## What This Does Not Mean

Adjacent or custom data does not automatically create network connectivity or acquire the semantics of a standard field.

## How To Use This

Use predefined fields when they fit, preserve source attributes with `ext:`, assign unique `_id` values, and document the source and intended interpretation.

## Example

A GTFS bus stop becomes a Custom Point with a unique `_id`, WGS-84 coordinates, and fields such as `ext:stop_id` and `ext:stop_name`.

## Assistant Guidance

Ask whether the feature needs to be routable and whether a standard entity already exists before recommending a custom extension.

## Related Concepts

- [What entities does the OpenSidewalks Schema define?](network-entities.md)
- [How do I add Custom Points?](../workflow/add-custom-points-to-osw.md)
