---
title: "Can I use this in ArcGIS or QGIS?"
slug: gis-software-compatibility
doc_type: concept
questions:
    - Can I use this in ArcGIS or QGIS?
    - Can OS-CONNECT data be used in ArcGIS?
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
    do_not_claim:
        - Opening OS-CONNECT data in GIS software proves that the data are complete.
        - Every OS-CONNECT file has identical import behavior in every GIS application.
related_pages:
    - assistant/os-connect/workflow/import-into-arcgis.md
    - assistant/support/workflow/choose-dataset-for-arcgis.md
    - assistant/os-connect/concept/gis-software-compatibility.md
tags:
    - Assistant
---

<!-- @format -->

# Can I use this in ArcGIS or QGIS?

## Short Answer

OS-CONNECT data can be used with GIS software when the downloaded format, schema, coordinate reference information, and intended workflow are compatible. Confirm the current release and import requirements for ArcGIS or QGIS rather than assuming every download behaves identically.

## Significance

GIS compatibility lets agencies inspect, map, and analyze pedestrian data using existing tools. It does not remove the need to understand the dataset's scope, attributes, version, and limitations.

## What This Means

- Obtain the intended OS-CONNECT or OpenSidewalks-compatible release.
- Check the available format and coordinate reference information.
- Import a sample, inspect geometry and attributes, and document the source version.

## What This Does Not Mean

- GIS compatibility does not prove that a dataset is complete, current, or authoritative.
- Opening a file in ArcGIS or QGIS does not make unsupported transformations reliable.

## How To Use This

Identify the GIS application, file format, desired layers, and analysis. Follow the current import workflow and retain release metadata for reproducibility.

## Example

An analyst imports a released pedestrian dataset into ArcGIS, checks that sidewalks and crossings appear as expected, and records the release and coordinate information before analysis.

## Assistant Guidance

Ask which product release and GIS application are involved. Cite current format and import guidance, do not promise compatibility for an unspecified file, and abstain when version or format details are missing.

## Related Concepts

- [Import OS-CONNECT or OSW GeoJSON into ArcGIS](../workflow/import-into-arcgis.md)
- [Choose a dataset and format for ArcGIS](../../support/workflow/choose-dataset-for-arcgis.md)
- [TDEI file formats](../../tdei/concept/file-formats.md)
