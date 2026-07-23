---
title: "How can connector segments be distinguished in OpenSidewalks mapping?"
slug: connector-segment-tagging
doc_type: concept
questions:
    - How can connector segments be distinguished from sidewalks?
    - What is the purpose of crossing-link tags?
audiences:
    - developer
    - planner
products:
    - OpenSidewalks
    - AccessMap
topics:
    - opensidewalks
    - accessmap
    - crossings
    - connectivity
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The crossing_link tag is the universal or final OpenSidewalks tagging rule.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can connector segments be distinguished in OpenSidewalks mapping?

## Short Answer

Connector segments can be tagged to distinguish a short connection between a sidewalk center line and a curb or crossing point from ordinary sidewalk ways. The discussed `crossing_link` convention is provisional and must be checked against current guidance.

## Significance

Explicit classification lets a network retain the geometry while allowing routing and safety analyses to interpret it differently. It can also prevent connectors from inflating sidewalk-specific counts.

## What This Means

Preserve a usable pedestrian connection and record its connector role with the supported tags. The current Tasking Manager guide describes a connector as `highway=footway` plus `footway=sidewalk`, with optional `crossing_link=yes`. Downstream tools can then include the way in connectivity while classifying it separately.

## What This Does Not Mean

A connector tag does not remove the geometry from the network or guarantee that every consumer interprets it correctly. It is not a substitute for current schema documentation.

## How To Use This

Review current OpenSidewalks and project tagging rules before applying `crossing_link` or related tags. Test the result in the intended downstream tools.

## Example

A short way from a curb ramp to a sidewalk is retained for routing but tagged as a crossing link so it is not counted as a standard sidewalk segment.

## Assistant Guidance

Do not present the discussed tag as settled or universal. Ask for the current schema version and target consumer before giving exact tagging instructions.

## Related Concepts

- [What are crossing links in pedestrian data?](../../accessmap/concept/crossing-links.md)
