---
uid: 9cfc6245-ea9e-42bb-844c-b5ce7c50a882
title: How are OpenSidewalks datasets represented and referenced spatially?
slug: coordinate-system-and-serialization
doc_type: concept
questions:
    - What coordinate system does OpenSidewalks use?
    - What formats can represent OpenSidewalks data?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - formats
    - vector-data
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
        - OpenSidewalks coordinates can be interpreted in any coordinate reference system without conversion.
        - Removing a GeoJSON crs member makes any source coordinates WGS-84.
related_pages:
    - opensidewalks-schema.md
    - ../workflow/convert-sidewalk-centerlines-to-osw.md
    - ../workflow/add-custom-points-to-osw.md
tags:
    - Assistant
---

<!-- @format -->

# How are OpenSidewalks datasets represented and referenced spatially?

## Short Answer

OpenSidewalks uses WGS-84 longitude and latitude in decimal degrees for GeoJSON data and represents features with vector geometries such as Points, LineStrings, and Polygons.

## Significance

Consistent spatial representation supports exchange between GIS, graph, validation, and routing tools.

## What This Means

OpenSidewalks GeoJSON follows RFC 7946 and does not include a `crs` member. Source datasets in another coordinate system must be reprojected to WGS-84 before conversion. OpenSidewalks data can also be serialized into tabular, graph, and database formats supported by the schema ecosystem.

## What This Does Not Mean

Coordinate order and reference system are not optional details. A file that contains coordinates without correct WGS-84 transformation is not made valid by changing metadata alone.

## How To Use This

Confirm the source CRS, reproject when necessary, and verify that GeoJSON coordinates are `[longitude, latitude]` before validation.

## Example

A Seattle source in EPSG:2926 is transformed to EPSG:4326 before sidewalk LineStrings are written to an OSW GeoJSON dataset.

## Assistant Guidance

Ask for the source CRS, target format, and coordinate order before diagnosing spatial misalignment.

## Related Concepts

- [What metadata describes an OpenSidewalks dataset?](dataset-metadata-and-provenance.md)
- [How do I convert sidewalk centerlines?](../workflow/convert-sidewalk-centerlines-to-osw.md)
