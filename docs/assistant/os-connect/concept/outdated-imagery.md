---
title: "What happens when imagery is outdated?"
slug: outdated-imagery
doc_type: concept
questions:
    - What happens when imagery is outdated?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - imagery
    - data-freshness
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Imagery misalignment proves that the OS-CONNECT feature geometry is wrong.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/map-layers.md
    - assistant/os-connect/workflow/report-data-error.md
tags:
    - Assistant
---

<!-- @format -->

# What happens when imagery is outdated?

## Short Answer

The viewer documents a known imagery shift that can make mapped edges appear misaligned with the Imagery basemap.

## Significance

Users may mistake a basemap offset for an error in OS-CONNECT data.

## What This Means

Compare the Raster basemap, imagery alignment, dataset version, and feature geometry before reporting a mapping error.

## What This Does Not Mean

Imagery misalignment is not by itself proof of a source-data error, and an aligned image is not proof that the feature is current.

## How To Use This

Use Raster for clearer feature inspection and Imagery for comparison. Report an issue when the mapped geometry remains wrong after accounting for the known shift.

## Example

A sidewalk appears offset from aerial imagery but aligns with the Raster map and neighboring network geometry.

## Assistant Guidance

Ask which basemap is active and whether the issue is reproducible across sources.

## Related Concepts

- [What are the different map layers?](map-layers.md)
- [How do I report an error?](../workflow/report-data-error.md)
