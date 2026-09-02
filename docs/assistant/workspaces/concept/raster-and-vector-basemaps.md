---
uid: 440a81d4-ad61-4e04-932e-befaec565511
title: What is the difference between raster and vector basemaps?
slug: raster-and-vector-basemaps
doc_type: concept
questions:
    - What is the difference between raster and vector basemaps?
audiences:
    - developer
    - planner
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - basemaps
    - vector-data
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Raster and vector basemaps provide identical interaction and precision.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between raster and vector basemaps?

## Short Answer

Raster basemaps are rendered images; vector basemaps deliver feature data that the client renders using style rules.

## Significance

The representation affects efficiency, styling, interaction, and visible precision.

## What This Means

Raster layers can work well as visual backgrounds, while vector layers support more client-side flexibility.

## What This Does Not Mean

A basemap is not necessarily the editable dataset being surveyed.

## How To Use This

Choose a supported layer according to the app, provider, and intended use.

## Example

A static raster tile layer provides imagery behind editable sidewalk data.

## Assistant Guidance

Ask whether the user means a background layer or the editable pedestrian network.

## Related Concepts

- [How is custom imagery configured in a workspace?](custom-imagery-configuration.md)
