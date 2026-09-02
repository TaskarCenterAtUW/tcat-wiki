---
uid: af7c583d-5c7d-4b29-9849-a78661e61f1d
title: Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?
slug: choose-dataset-for-arcgis
doc_type: workflow
questions:
    - Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - dataset-lineage
    - arcgis
    - planning
    - os-connect
    - accessmap
    - walksheds
    - tdei
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
        - The newest dataset is automatically the right dataset for every ArcGIS project.
        - Successful import proves that the data are complete or authoritative.
related_pages:
    - assistant/support/workflow/choose-dataset-for-planning.md
    - assistant/os-connect/concept/gis-software-compatibility.md
    - assistant/tdei/concept/file-formats.md
tags:
    - Assistant
---

<!-- @format -->

# Which dataset and format should an agency use for pedestrian walkway data in ArcGIS?

## Short Answer

Choose a released pedestrian-network dataset whose geographic boundary, features, attributes, format, and release information match the ArcGIS task. This may be an OS-CONNECT or OpenSidewalks-compatible TDEI release; verify the current release and available download format before importing it.

## Significance

Dataset selection affects whether an agency can represent the pedestrian features and attributes needed for planning. Choosing by product name alone can produce a file with the wrong scope or format.

## What This Means

- Define the planning question and geographic extent.
- Check the release, project group, feature coverage, attributes, and available format.
- Test the import on a small sample and record the dataset version used.

## What This Does Not Mean

- The newest available file is not automatically the best dataset for every ArcGIS project.
- Successful import does not prove that data are complete, current, or authoritative.

## How To Use This

Document the area, required features, and analysis before choosing a release. Compare those requirements with the release metadata, test the import, and retain the dataset identifier or version for reproducibility.

## Example

An agency needs sidewalk and crossing geometry for a citywide planning map. Staff select a released pedestrian-network dataset covering the city, test its available format in ArcGIS, and record the release details before analysis.

## Assistant Guidance

Ask for the geography, purpose, required features, and ArcGIS workflow. Cite the release documentation, do not invent dataset identifiers, and abstain when the current release, scope, or authority is unclear.

## Related Concepts

- [Choose a dataset for planning](choose-dataset-for-planning.md)
- [Can OS-CONNECT work with GIS software?](../../os-connect/concept/gis-software-compatibility.md)
- [TDEI file formats](../../tdei/concept/file-formats.md)
