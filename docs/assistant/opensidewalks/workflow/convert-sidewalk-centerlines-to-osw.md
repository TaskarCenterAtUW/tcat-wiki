---
uid: 2f476704-7c83-47e7-b994-c0a6e4eaa428
title: How do I convert sidewalk centerlines to OpenSidewalks?
slug: convert-sidewalk-centerlines-to-osw
doc_type: workflow
questions:
    - How do I convert sidewalk centerlines to OpenSidewalks?
    - How do I prepare a sidewalk inventory for TDEI?
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
    - dataset-lineage
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A field mapping example is universal for every source sidewalk dataset.
        - Reprojection and tagging alone prove that the resulting dataset is valid.
related_pages:
    - ../concept/opensidewalks-schema.md
    - ../concept/coordinate-system-and-serialization.md
    - ../concept/tdei-schema-validation.md
    - ../../../opensidewalks/schema/core-edges-in-osw.md
tags:
    - Assistant
---

<!-- @format -->

# How do I convert sidewalk centerlines to OpenSidewalks?

## Short Answer

Reproject source geometry to WGS-84, map source fields to OSW properties, preserve provenance with `ext:` fields, create valid GeoJSON, and validate against the target schema.

## Significance

Conversion makes existing agency or GIS sidewalk inventories available for pedestrian routing and analysis while preserving source context.

## What This Means

Create unique `_id` values, use `highway=footway` and `footway=sidewalk` for sidewalk Edges, convert measurements such as width to meters, normalize surface values, and preserve source identifiers and descriptions with `ext:` fields. Include dataset metadata such as `$schema`, `dataSource`, and `dataTimestamp`.

## What This Does Not Mean

A sample Seattle conversion or a successful geometry transformation does not establish the correct mapping for every source dataset.

## How To Use This

Inspect the source CRS and fields, transform geometry, map fields explicitly, check unique IDs and LineString geometry, then run the matching OSW validator before ingestion.

## Example

A local sidewalk inventory is transformed from a projected CRS to EPSG:4326, its width is converted to meters, and its source ID is preserved as `ext:unit_id`.

## Assistant Guidance

Ask for source schema, CRS, units, OSW version, and target consumer. Do not invent field mappings when source semantics are unclear.

## Related Concepts

- [How are OpenSidewalks datasets represented spatially?](../concept/coordinate-system-and-serialization.md)
- [How does TDEI validate OpenSidewalks data?](../concept/tdei-schema-validation.md)
