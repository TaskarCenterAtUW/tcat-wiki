---
title: What is the relationship between OS-CONNECT and local GIS?
slug: os-connect-local-gis-relationship
doc_type: concept
questions:
    - What is the relationship between OS-CONNECT and local GIS?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - gis
    - stewardship
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/gis-software-compatibility.md
    - assistant/os-connect/concept/local-data-validation.md
    - assistant/os-connect/concept/data-ownership.md
tags:
    - Assistant
---

<!-- @format -->

# What is the relationship between OS-CONNECT and local GIS?

## Short Answer

OS-CONNECT can provide a shared pedestrian-data source or release that agencies view, download, transform, and combine with local GIS layers. Local GIS remains the agency's environment for its own records, analysis, validation, and operational decisions.

## Significance

Combining shared and local data can add context while preserving local authority and source lineage.

## What This Means

Check format, coordinate reference system, schema, release, licensing, identifiers, and transformation requirements. Keep OS-CONNECT and local layers labeled separately and document joins and conflicts.

## What This Does Not Mean

Importing OS-CONNECT into GIS does not make it authoritative for every local feature, update local records automatically, or guarantee that geometry and attributes remain unchanged after conversion.

## How To Use This

Use the exact release and metadata, validate imports against known locations, preserve attribution, and use local authoritative data for current high-consequence decisions.

## Example

An agency overlays an OSW download with its curb-ramp inventory, checks the coordinate system and field meanings, and documents where the sources disagree.

## Assistant Guidance

Ask which GIS software, format, release, and intended use are involved. Cite conversion and metadata guidance, and abstain when compatibility or source authority is unknown.

## Related Concepts

- [Can I use this in ArcGIS or QGIS?](gis-software-compatibility.md)
- [How should agencies validate the data locally?](local-data-validation.md)
- [Who owns OS-CONNECT data?](data-ownership.md)
