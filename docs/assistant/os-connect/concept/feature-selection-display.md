---
title: "What does this selected feature represent?"
slug: feature-selection-display
doc_type: concept
questions:
    - What does this selected feature represent?
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
        - A feature is absent because its details do not appear at a low zoom level.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does this selected feature represent?

## Short Answer

The Data Viewer displays a feature popup when users hover over or tap a mapped feature at zoom level 16 or higher.

## Significance

Detailed selection helps users inspect the attributes behind a line or point instead of relying only on its color or shape.

## What This Means

The popup may show `highway`, `footway`, `kerb`, `barrier`, `incline`, `width`, `length`, `foot`, `surface`, and `tactile_paving`. Only attributes present on that feature are shown.

## What This Does Not Mean

Popup behavior and attribute presence do not establish that the feature is current, complete, or physically accessible.

## How To Use This

Enable Data, zoom to level 16 or higher, and hover or tap the feature. Record the dataset and feature context when reporting an issue.

## Example

A user zooms to level 16, taps a sidewalk, and reads its width, surface, and incline values.

## Assistant Guidance

Ask for the zoom level and active data layer before diagnosing a missing popup.

## Related Concepts

- [What are the different map layers?](map-layers.md)
- [Where are attribute definitions documented?](attribute-documentation-location.md)
