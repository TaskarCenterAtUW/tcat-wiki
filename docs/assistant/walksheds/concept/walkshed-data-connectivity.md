---
title: Why does network connectivity matter in Walksheds?
slug: walkshed-data-connectivity
doc_type: concept
questions:
    - Why does network connectivity matter in Walksheds?
    - Why can changing an attribute fail to expand a walkshed?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
    - OS-CONNECT
topics:
    - walksheds
    - os-connect
    - connectivity
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Correcting an attribute fixes a missing network connection.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Why does network connectivity matter in Walksheds?

## Short Answer

Walksheds require connected geometry from an origin to a destination. Attribute changes cannot compensate for a missing connector or disconnected sidewalk.

## Significance

Connectivity determines whether a route can be calculated at all.

## What This Means

Inspect sidewalks, curb connectors, crossings, and other links before interpreting a scenario.

## What This Does Not Mean

A feature that appears nearby is not necessarily reachable in the graph.

## How To Use This

Report missing geometry through the source-data feedback process and rerun the analysis after correction.

## Example

A crossing with curb-ramp attributes remains unreachable because no line connects it to the sidewalk.

## Assistant Guidance

Distinguish attribute limitations from topology or geometry errors.

## Related Concepts

- [What can feature edits do in Walksheds?](walkshed-feature-edits.md)
