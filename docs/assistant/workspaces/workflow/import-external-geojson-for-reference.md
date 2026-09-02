---
uid: 8ef7fda7-b7bc-46ce-96c6-c2fe01eb0cc9
title: How can I load external GeoJSON for reference in Workspaces?
slug: import-external-geojson-for-reference
doc_type: workflow
questions:
    - How can I load external GeoJSON for reference in Workspaces?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - Rapid
topics:
    - workspaces
    - rapid
    - formats
    - gis
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Loading external GeoJSON as custom map data automatically adds it to the official workspace dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can I load external GeoJSON for reference in Workspaces?

## Short Answer

Download the external GeoJSON, open the workspace in Rapid, and load it through Custom Map Data as a local file or supported URL.

## Significance

This lets editors compare external data with the workspace before deciding whether an official edit is appropriate.

## What This Means

The layer appears as reference data and may expose its source attributes.

## What This Does Not Mean

A reference overlay is not automatically incorporated into the workspace.

## How To Use This

Document the source and avoid saving unintended changes.

## Example

A city sidewalk GeoJSON is loaded over an OS-CONNECT workspace to inspect differences.

## Assistant Guidance

Distinguish viewing an overlay from importing validated features into the dataset.

## Related Concepts

- [What is the boundary between Workspaces and TDEI?](../concept/workspace-and-tdei-boundary.md)
