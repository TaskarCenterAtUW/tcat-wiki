---
uid: 7673d5e9-a8da-4d70-b425-2f87263a592c
title: What are tile layers?
slug: tile-layers
doc_type: concept
questions:
    - What are tile layers?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - imagery
    - basemaps
    - configuration
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A tile layer is the editable workspace dataset.
        - Every tile layer is current, complete, or available at every zoom.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/imagery-layers.md
    - assistant/workspaces/concept/basemap-loading.md
tags:
    - Assistant
---

<!-- @format -->

# What are tile layers?

## Short Answer

A tile layer is a map display layer delivered as tiles for efficient viewing. In Workspaces, tile layers may provide basemap or imagery context and are distinct from the editable feature data.

## Significance

Tile layers make large geographic sources practical to display, but their source, zoom range, date, and access affect what users see.

## What This Means

Check the layer definition, source, attribution, zoom behavior, and loading status when interpreting a map.

## What This Does Not Mean

A tile layer does not certify a feature, expose every underlying attribute, or become editable merely because it appears on the map.

## How To Use This

Use tile layers as visual context and consult the underlying dataset or source record for analysis.

## Example

A mapper notices a street in a tile layer and opens the editable feature data before changing an attribute.

## Assistant Guidance

Distinguish tile display from source data. Ask for the layer configuration when a user reports missing or stale map content.

## Related Concepts

 - [What are imagery layers?](imagery-layers.md)
 - [How are basemaps loaded?](basemap-loading.md)
