---
title: How are basemaps loaded?
slug: basemap-loading
doc_type: concept
questions:
    - How are basemaps loaded?
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
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/raster-and-vector-basemaps.md
    - assistant/workspaces/concept/tile-layers.md
    - assistant/workspaces/concept/imagery-layers.md
tags:
    - Assistant
---

<!-- @format -->

# How are basemaps loaded?

## Short Answer

Workspaces loads a basemap through the current map configuration and tile or map service used by the application. The exact source, style, availability, and loading behavior can vary by environment and workspace configuration.

## Significance

Basemaps provide geographic context for editing but are separate from the editable workspace data and imagery layers.

## What This Means

Check the workspace environment, map settings, network access, and layer configuration. Distinguish the basemap from editable features and reference imagery when interpreting the map.

## What This Does Not Mean

Basemap loading does not guarantee that the map is current, that an underlying feature is authoritative, or that a missing visual element is absent from the workspace data.

## How To Use This

Use the current workspace settings and layer documentation, check network or service errors, and verify the active layer before making an edit.

## Example

An editor sees a basemap tile fail to load and confirms the workspace data and imagery layers separately before concluding that a sidewalk is missing.

## Assistant Guidance

Do not name a provider or loading sequence without current evidence. Ask for the environment and layer, cite configuration guidance, and abstain when live behavior cannot be verified.

## Related Concepts

- [Raster and vector basemaps](raster-and-vector-basemaps.md)
- [What are tile layers?](tile-layers.md)
- [What are imagery layers?](imagery-layers.md)
