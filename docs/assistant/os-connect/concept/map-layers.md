---
uid: 092fb787-d775-47de-8c42-4feed6a809e0
title: What are the different map layers?
slug: map-layers
doc_type: concept
questions:
    - What are the different map layers?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - public-vs-private-data
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Turning off a viewer layer changes the underlying dataset.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/viewer-overview.md
tags:
    - Assistant
---

<!-- @format -->

# What are the different map layers?

## Short Answer

The viewer has independent **Data** and **Boundaries** layers, plus an exclusive Raster/Imagery basemap toggle.

## Significance

Independent layers let users focus on network features, jurisdiction coverage, or both without changing source data.

## What This Means

Use **Data** to show or hide sidewalks, crossings, footways, curbs, and traffic islands. Use **Boundaries** to show or hide dataset polygons. Use **Raster** for map contrast or **Imagery** to compare mapped features with visible infrastructure.

## What This Does Not Mean

Layer visibility is only a display choice; it does not edit, filter, or update the dataset.

## How To Use This

Turn off Data to inspect coverage boundaries, or turn off Boundaries to reduce clutter while inspecting features.

## Example

A planner hides Data to see which jurisdictions have boundaries, then re-enables it to inspect a sidewalk network.

## Assistant Guidance

Ask which layer and basemap are active before diagnosing a missing feature.

## Related Concepts

- [What am I looking at in the viewer?](viewer-overview.md)
