---
uid: 95ad30a0-0069-40c8-a452-23a4c03b3fcf
title: What happens when sidewalks are disconnected?
slug: disconnected-sidewalks
doc_type: concept
questions:
    - What happens when sidewalks are disconnected?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - connectivity
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A disconnected sidewalk on the map proves that walking is impossible.
        - A disconnected map segment is definitely a data error without verification.
related_pages:
    - assistant/os-connect/concept/sidewalk-disconnection-causes.md
    - assistant/accessmap/concept/routing-limitations.md
    - assistant/accessmap/concept/missing-accessibility-data.md
tags:
    - Assistant
---

<!-- @format -->

# What happens when sidewalks are disconnected?

## Short Answer

When sidewalks are disconnected in AccessMap, the modeled graph lacks a usable link for the selected profile. Possible causes include missing crossings, unmapped connectors, geometry or tagging mismatches, restrictions, or missing data.

## Significance

Disconnection can prevent a route from reaching a destination or make a route appear longer. It also identifies a location for data and field review.

## What This Means

- Check the location, dataset, profile, and route settings.
- Compare the map with imagery, local knowledge, or field conditions.
- Report a suspected data problem with precise evidence.

## What This Does Not Mean

The map does not prove that the physical sidewalk is disconnected or that one team caused the gap. A route failure is not an accessibility or safety determination.

## How To Use This

Explain the modeled cause and distinguish it from physical conditions. Verify important gaps locally and cite the relevant data version.

## Example

A footpath reaches a parking-lot edge but has no mapped connector, so AccessMap cannot route across it. A mapper verifies the connection and submits a correction.

## Assistant Guidance

Ask for the location, profile, and dataset version. Cite the OS-CONNECT and AccessMap guidance, do not diagnose a pin without context, and abstain from claiming that walking is impossible.

## Related Concepts

- [Sidewalk disconnection causes](../../os-connect/concept/sidewalk-disconnection-causes.md)
- [Routing limitations](routing-limitations.md)
- [Missing accessibility data](missing-accessibility-data.md)
