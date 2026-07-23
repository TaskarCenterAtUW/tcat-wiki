---
title: "How do I add Custom Points to an OpenSidewalks dataset?"
slug: add-custom-points-to-osw
doc_type: workflow
questions:
    - How do I add Custom Points to OpenSidewalks?
    - How can I convert GTFS stops to OpenSidewalks?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
    - TDEI
topics:
    - opensidewalks
    - tdei
    - formats
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
        - An OpenSidewalks Custom Point is a routable network Edge.
        - A source point dataset can omit unique IDs or coordinate validation.
related_pages:
    - ../concept/adjacent-and-custom-entities.md
    - ../concept/coordinate-system-and-serialization.md
    - ../../../opensidewalks/schema/custom-points-in-osw.md
tags:
    - Assistant
---

<!-- @format -->

# How do I add Custom Points to an OpenSidewalks dataset?

## Short Answer

Create GeoJSON Point features with unique `_id` values, WGS-84 coordinates, and `ext:`-prefixed source attributes for nonstandard fields, then validate the dataset.

## Significance

Custom Points allow useful non-routable features such as bus stops, entrances, kiosks, and accessibility facilities to travel with a pedestrian dataset.

## What This Means

Place longitude before latitude, preserve source identifiers and descriptions in `ext:` properties, add dataset metadata, and confirm that IDs are unique across the complete dataset. GTFS `stop_lon` and `stop_lat` already use the expected WGS-84 coordinate order when valid.

## What This Does Not Mean

A Custom Point does not create a sidewalk, crossing, or connected route. Source coordinates and IDs still require quality checks.

## How To Use This

Remove records with missing coordinates, verify coordinate reference systems, map source fields explicitly, construct a FeatureCollection, and run the matching validator.

## Example

A GTFS stop becomes `bus_stop_1001` with `ext:stop_id`, `ext:stop_name`, and a Point geometry of `[longitude, latitude]`.

## Assistant Guidance

Ask whether the point should be routable and what source format is being converted. Do not treat Custom Points as substitutes for network entities.

## Related Concepts

- [How are adjacent and custom entities used?](../concept/adjacent-and-custom-entities.md)
- [What entities does the OpenSidewalks Schema define?](../concept/network-entities.md)
