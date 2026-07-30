---
title: What data powers AccessMap?
slug: data-sources
doc_type: concept
questions:
    - What data powers AccessMap?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - dataset-lineage
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
        - AccessMap has complete pedestrian network data everywhere.
        - A feature missing from AccessMap is absent from the real world.
related_pages:
    - ../index.md
    - ../../os-connect/index.md
    - ../../opensidewalks/index.md
tags:
    - Assistant
---

<!-- @format -->

# What data powers AccessMap?

## Short Answer

AccessMap is powered by OpenSidewalks and OpenStreetMap data. It uses available pedestrian network information for paths, crossings, curb ramps, barriers, elevation, and related features.

## Significance

The source data determines which pedestrian features and accessibility attributes AccessMap can use when displaying and calculating routes.

## What This Means

Coverage depends on available pedestrian network data. AccessMap is available in regions across Washington State and beyond, but coverage outside Washington varies by region and local data availability.

## What This Does Not Mean

Data coverage is not proof that every real-world feature is mapped or current. An absent attribute or feature should not be interpreted as proof that the condition does not exist.

## How To Use This

When interpreting a route, identify the region and consider whether the relevant pedestrian data is available. Report observed inaccuracies or missing features through AccessMap feedback.

## Example

A user sees that a curb ramp is not represented in a route area and submits feedback rather than assuming that no curb ramp exists.

## Assistant Guidance

Distinguish mapped information from real-world conditions. Cite the source documentation and abstain when a question requires data freshness or regional coverage not provided by the available context.

## Related Concepts

- [How can I submit feedback about an AccessMap feature?](feature-feedback.md)
- [OpenSidewalks knowledge base](../../opensidewalks/index.md)
