---
title: "How is custom imagery configured in a workspace?"
slug: custom-imagery-configuration
doc_type: concept
questions:
    - How is custom imagery configured in a workspace?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - imagery
    - configuration
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
        - Custom imagery configuration imports imagery files into the workspace.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How is custom imagery configured in a workspace?

## Short Answer

Custom imagery settings define background layers that can appear in AVIV ScoutRoute. The configuration describes tile sources rather than importing the imagery itself.

## Significance

Background layers help contributors orient themselves while editing or surveying.

## What This Means

The workspace stores imagery-layer configuration, including supported URLs and layer details.

## What This Does Not Mean

The setting does not necessarily support every provider, access restriction, or vector layer.

## How To Use This

Follow the current imagery schema and test the layer in the target app and environment.

## Example

A workspace adds a public raster tile source that contributors can select as a background.

## Assistant Guidance

Ask for the schema version, provider permissions, and target app before giving configuration advice.

## Related Concepts

- [What are raster and vector basemaps?](raster-and-vector-basemaps.md)
