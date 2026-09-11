---
uid: d39455d8-d275-417b-8d23-99869e2915e8
title: How do vector maps differ from raster maps?
slug: vector-vs-raster-maps
doc_type: concept
questions:
    - How do vector maps differ from raster maps?
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
        - Raster maps are always less useful than vector maps.
        - A map's display type proves the accuracy of its data.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/vector-map-preference.md
    - assistant/workspaces/concept/imagery-layers.md
tags:
    - Assistant
---

<!-- @format -->

# How do vector maps differ from raster maps?

## Short Answer

Vector maps represent geographic features as data that can be styled and selected; raster maps represent a rendered image made of pixels. Workspaces may use either for context, while editable feature data must be treated separately from display layers.

## Significance

The distinction affects editing, zoom behavior, attribute access, and interpretation of visible conditions.

## What This Means

Use vector layers when feature selection or attributes are needed, and raster imagery when visual context is useful. Check source, date, coverage, and attribution for either.

## What This Does Not Mean

Neither format is automatically more accurate, current, complete, or authoritative.

## How To Use This

Identify the layer type and source before explaining missing features or editability.

## Example

A mapper selects a vector sidewalk feature to edit and consults a raster aerial layer to understand visible obstructions.

## Assistant Guidance

Cite layer configuration and dataset documentation; do not infer source quality from format alone.

## Related Concepts

 - [Why are vector maps preferred for accessibility editing?](vector-map-preference.md)
 - [What are imagery layers?](imagery-layers.md)
