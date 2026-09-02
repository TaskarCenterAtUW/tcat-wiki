---
uid: adeefd4e-94b5-4a1a-b82d-9e66e8b957ca
title: How do I import OS-CONNECT / OSW GeoJSON into ArcGIS?
slug: import-into-arcgis
doc_type: workflow
questions:
    - How do I import OS-CONNECT / OSW GeoJSON into ArcGIS?
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
    - arcgis
    - data-collection
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
        - Successful ArcGIS import proves that the dataset is complete or authoritative.
        - Every OSW or OS-CONNECT file imports identically in every ArcGIS version.
related_pages:
    - assistant/support/workflow/choose-dataset-for-arcgis.md
    - assistant/os-connect/concept/gis-software-compatibility.md
    - assistant/tdei/concept/osw-download-contents.md
tags:
    - Assistant
---

<!-- @format -->

# How do I import OS-CONNECT / OSW GeoJSON into ArcGIS?

## Short Answer

Download the intended OS-CONNECT or OSW GeoJSON release, then add it to an ArcGIS project as a GeoJSON or converted feature layer. Verify the geometry, attributes, coordinate reference information, and dataset version after import.

## Significance

Import validation matters because a file can open successfully while still having the wrong scope, fields, coordinate reference, or release for the planning question.

## What This Means

- Confirm the dataset, release, geographic scope, and format before importing.
- Add the GeoJSON to ArcGIS using the current ArcGIS workflow for GeoJSON or converted feature data.
- Inspect representative sidewalks, crossings, curb ramps, attributes, and coordinate information.
- Record the source release and any transformations applied.

## What This Does Not Mean

Opening a file in ArcGIS does not prove that it is complete, current, authoritative, or suitable for legal or engineering decisions. Exact ArcGIS behavior can vary by version and file structure.

## How To Use This

Use a small sample first, compare the imported layer with the source, and preserve the original file and metadata. Ask for current product-specific instructions when an import fails or fields do not appear as expected.

## Example

An analyst downloads an OS-CONNECT GeoJSON release, adds it to ArcGIS, checks a sample of sidewalk and crossing features, and records the release and coordinate information before mapping a larger area.

## Assistant Guidance

Ask which ArcGIS version, file format, dataset release, and desired output are involved. Cite current format documentation, do not promise that every file imports identically, and abstain when the source version is unknown.

## Related Concepts

- [Choose a dataset and format for ArcGIS](../../support/workflow/choose-dataset-for-arcgis.md)
- [Can OS-CONNECT work with GIS software?](../concept/gis-software-compatibility.md)
- [What files are included in an OSW download?](../../tdei/concept/osw-download-contents.md)
