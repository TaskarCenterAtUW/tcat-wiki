---
uid: 27f771b1-961f-4d26-8d1c-65b8e61ed33f
title: What coordinate system is used?
slug: coordinate-system
doc_type: concept
questions:
    - What coordinate system is used?
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
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
    - assistant/tdei/concept/file-formats.md
tags:
    - Assistant
---

<!-- @format -->

# What coordinate system is used?

## Short Answer

The coordinate system for an OS-CONNECT dataset depends on the specific release and format. Check the dataset metadata or export documentation rather than assuming that every download uses the same coordinate reference system.

## Significance

Correct coordinate interpretation is necessary for display, spatial joins, measurements, and conversion between GIS formats. A mismatch can make valid features appear displaced or produce incorrect distances and areas.

## What This Means

Inspect the file's declared coordinate reference system, axis order, units, and transformation requirements. Preserve that metadata when importing or exporting the data and confirm the result against known locations.

## What This Does Not Mean

The map's visual position does not prove that a file has the correct coordinate system. Coordinate-system information does not establish data accuracy or accessibility.

## How To Use This

Use the metadata supplied with the exact release and format. In GIS software, define or transform the source explicitly only after confirming its declared system, and document any transformation applied.

## Example

An analyst imports a pedestrian dataset into a local GIS project, checks the file metadata before overlaying parcels, and verifies that several known intersections align after any documented transformation.

## Assistant Guidance

Do not name a universal CRS without a source for the release being discussed. Ask for the format and dataset version, cite its metadata, and abstain when the coordinate reference is not documented.

## Related Concepts

- [Can I use this in ArcGIS or QGIS?](gis-software-compatibility.md)
- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [What file formats are available in TDEI?](../../tdei/concept/file-formats.md)
