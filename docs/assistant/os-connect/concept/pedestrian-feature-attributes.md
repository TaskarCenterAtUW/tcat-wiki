---
uid: 38b7ff04-8d36-486c-9344-48ef4cf6dbe7
title: What attributes are included for sidewalks, crossings, curb ramps, and related pedestrian features?
slug: pedestrian-feature-attributes
doc_type: concept
questions:
    - What attributes are included for sidewalks, crossings, curb ramps, and related pedestrian features?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - editing
    - formats
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The presence of an attribute proves that its value is accurate or complete.
        - One feature type has the same fields and meanings as every other feature type.
related_pages:
    - assistant/os-connect/concept/sidewalk-attributes.md
    - assistant/os-connect/concept/crossing-attributes.md
    - assistant/os-connect/concept/curb-ramp-attributes.md
    - assistant/os-connect/concept/required-vs-recommended-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# What attributes are included for sidewalks, crossings, curb ramps, and related pedestrian features?

## Short Answer

Sidewalks, crossings, curb ramps, and related pedestrian features can carry geometry and feature-specific attributes such as identity, type, surface, width, accessibility information, and connectivity. The exact fields depend on the OS-CONNECT dataset version and its OpenSidewalks schema documentation.

## Significance

Attribute meaning matters for routing, quality review, GIS analysis, and agency decisions. Users need the schema rather than assumptions based only on how a feature appears on the map.

## What This Means

- Identify the feature type and dataset version.
- Consult the current schema for required, recommended, and feature-specific attributes.
- Preserve null or missing values as meaningful data-quality information rather than filling them by assumption.

## What This Does Not Mean

The presence of an attribute does not prove that it is populated, accurate, current, or sufficient for an accessibility determination. Similar-looking features may have different fields and meanings.

## How To Use This

Use the schema and dataset metadata as the source of truth, then inspect representative features before analysis or conversion. Record the version and any filtering or transformation.

## Example

An analyst reviews sidewalk width, surface, crossing, and curb-ramp fields in a released dataset, then records which fields were present and populated before calculating a planning metric.

## Assistant Guidance

Cite the current schema and dataset release. Do not provide an exhaustive field list without a version, and abstain when the feature type or source file is unclear.

## Related Concepts

- [Sidewalk attributes](sidewalk-attributes.md)
- [Crossing attributes](crossing-attributes.md)
- [Curb-ramp attributes](curb-ramp-attributes.md)
- [Required and recommended attributes](required-vs-recommended-attributes.md)
