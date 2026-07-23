---
title: "How can OSM data be imported into Workspaces?"
slug: import-osm-data-into-workspaces
doc_type: workflow
questions:
    - How can OSM data be imported into Workspaces?
    - How do I bring a selected OSM area into an OSW workspace?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
    - OpenSidewalks
topics:
    - workspaces
    - tdei
    - opensidewalks
    - osm-interoperability
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-12
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Downloading an OSM slice directly creates a finished OpenSidewalks workspace.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can OSM data be imported into Workspaces?

## Short Answer

Use SliceOSM to download a selected area, convert the OSM PBF through a TDEI conversion job, then create a workspace from the resulting OSW file.

## Significance

This provides a controlled path from a selected OSM area to an editable workspace.

## What This Means

Draw or select the area, download the PBF, run OSM-to-OSW conversion, download the result, and create the workspace.

## What This Does Not Mean

Conversion does not guarantee complete or correct pedestrian data.

## How To Use This

Record the area, source date, conversion job, output, and workspace lineage.

## Example

A Covington slice is converted to OSW and loaded into a Workspaces test project.

## Assistant Guidance

Ask for the source area, format, and target project before giving exact steps.

## Related Concepts

- [What sources can create a workspace?](../concept/workspace-source-options.md)
