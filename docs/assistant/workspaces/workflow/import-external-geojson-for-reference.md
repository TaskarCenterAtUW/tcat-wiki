---
uid: 8ef7fda7-b7bc-46ce-96c6-c2fe01eb0cc9
title: How can I load external GeoJSON for reference in Workspaces?
slug: import-external-geojson-for-reference
doc_type: workflow
questions:
    - How can I load external GeoJSON for reference in Workspaces?
    - Can I bring additional data or reference layers into a Workspace to help with editing?
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
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/workspace-and-tdei-boundary.md
tags:
    - Assistant
---

<!-- @format -->

# How can I load external GeoJSON for reference in Workspaces?

## Short Answer

Yes. In Rapid within Workspaces, load supported GeoJSON through **Custom Map Data** as a local file or supported URL to view it as a reference layer. Workspace imagery or basemaps are configured separately and provide visual context rather than imported feature data.

## Significance

This lets editors compare external data with the workspace before deciding whether an official edit is appropriate.

## What This Means

The overlay helps compare external information with the editable workspace. Its presence does not add those features to the workspace dataset; an editor must make and review any intended changes separately.

## What This Does Not Mean

A reference overlay is not automatically incorporated into the workspace, and the documented workflow does not establish support for arbitrary formats or automatic merging.

## How To Use This

Record the reference source, confirm that it is displayed as an overlay, and avoid treating it as authoritative workspace data. Use the workspace's separate imagery settings for basemap configuration.

## Example

A city sidewalk GeoJSON is loaded over an OS-CONNECT workspace to inspect differences.

## Assistant Guidance

Distinguish viewing an overlay from importing validated features into the dataset.

## Related Concepts

- [What is the boundary between Workspaces and TDEI?](../concept/workspace-and-tdei-boundary.md)
