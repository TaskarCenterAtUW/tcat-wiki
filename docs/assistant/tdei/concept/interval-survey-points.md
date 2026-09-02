---
uid: 4195411a-cf4f-4713-b93e-ff79201e1139
title: How should interval survey points be represented?
slug: interval-survey-points
doc_type: concept
questions:
    - How should interval survey points be represented?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - data-collection
    - vector-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Snapping interval survey points to a sidewalk automatically makes them useful for routing.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should interval survey points be represented?

## Short Answer

Interval measurements can remain as a separate point dataset, be snapped for visualization, or be used to split lines when routing needs segment-level attributes.

## Significance

The intended use determines whether splitting the source lines adds value or unnecessary noise.

## What This Means

Keep points separate for inventory or maintenance when appropriate; derive segmented lines only for a routing need.

## What This Does Not Mean

A point on a sidewalk is not automatically a routable network segment.

## How To Use This

Document whether points are source observations, overlays, or inputs to a derived network.

## Example

A maintenance point is snapped to the nearest sidewalk for display but remains separate from the routing graph.

## Assistant Guidance

Ask whether the user needs inventory, visualization, maintenance, or routing.

## Related Concepts

- [Why can one area have multiple TDEI datasets?](dataset-purpose-and-representation.md)
