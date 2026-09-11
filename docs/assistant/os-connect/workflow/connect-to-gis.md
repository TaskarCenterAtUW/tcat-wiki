---
uid: afb34589-73d9-43b8-9ba6-a9450856969f
title: How do I connect this to GIS software?
slug: connect-to-gis
doc_type: workflow
questions:
    - How do I connect this to GIS software?
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
last_reviewed: 2026-09-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Connecting OS-CONNECT to GIS automatically refreshes the data.
        - Every GIS application supports every OS-CONNECT download format and field.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/workflow/import-into-arcgis.md
    - assistant/os-connect/concept/gis-software-compatibility.md
tags:
    - Assistant
---

<!-- @format -->

# How do I connect this to GIS software?

## Short Answer

To use OS-CONNECT data in GIS, identify the jurisdiction and release, download the documented format, add it to the GIS application, and verify the coordinate system, fields, scope, and attribution. Exact steps depend on the GIS software and current download instructions.

## Significance

GIS integration lets analysts combine pedestrian-network data with local layers and tools. Verification is necessary because import settings can affect geometry, attributes, and apparent coverage.

## What This Means

 - Select and record the dataset release and geographic scope.
 - Download a format supported by the target GIS application.
 - Add the data and verify projection, geometry, attributes, and attribution.
 - Preserve source and release information with derived analysis.

## What This Does Not Mean

Adding a download to GIS does not create a live connection, guarantee current data, or make the imported layer authoritative. A successful import does not prove that the dataset is complete or correctly interpreted.

## How To Use This

Ask which GIS application, format, release, and intended analysis are involved. Preserve the original source before transforming data.

## Example

A planner downloads a selected OS-CONNECT release, loads it into ArcGIS, checks the coordinate system and fields, and records the release in project metadata.

## Assistant Guidance

Use current OS-CONNECT download and GIS compatibility guidance. If format, projection, or release is unknown, do not guess; ask for context or abstain.

## Related Concepts

 - [OS-CONNECT — Assistant Knowledge Base](../index.md)
 - [How do I import OS-CONNECT data into ArcGIS?](import-into-arcgis.md)
 - [What GIS software is compatible?](../concept/gis-software-compatibility.md)
