---
title: "Which projection supports regional walkshed length calculations?"
slug: projection-for-walkshed-lengths
doc_type: concept
questions:
    - Which projection supports regional walkshed length calculations?
    - Why might QA/QC distance results change after a projection change?
audiences:
    - developer
    - planner
products:
    - QA-QC Reports
topics:
    - qa-qc
    - walksheds
    - gis
    - data-quality
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
        - EPSG:26910 is the correct projection for every geographic region.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Which projection supports regional walkshed length calculations?

## Short Answer

For Pacific Northwest calculations, EPSG:26910 (UTM zone 10N) was found to produce walkshed lengths closer to manual GIS measurements than Web Mercator, EPSG:3857.

## Significance

A projection choice can materially change reported distances. Regional calculations should use a coordinate system appropriate to the area being measured.

## What This Means

Compare calculated lengths with independent GIS measurements after changing the projection. Treat the result as a data-processing decision, not a display setting.

## What This Does Not Mean

EPSG:26910 is not automatically appropriate outside its geographic area. A closer result in one region does not validate every pipeline output.

## How To Use This

Document the projection used for each report and verify representative measurements. Recheck affected reports after changing projection logic.

## Example

A reported walkshed length changes from about 144 meters to 96 meters after switching from EPSG:3857 to EPSG:26910; manual measurement supports the latter result.

## Assistant Guidance

Ask for the region, projection, and metric before explaining a discrepancy. Do not generalize a regional projection choice without GIS verification.

## Related Concepts

- [What is a walkshed?](../../walksheds/concept/walkshed.md)
