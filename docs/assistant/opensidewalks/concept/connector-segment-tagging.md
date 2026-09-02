---
uid: 34d58e62-1933-4601-8ea6-4390a5e693df
title: How can connector segments be distinguished in OpenSidewalks mapping?
slug: connector-segment-tagging
doc_type: concept
questions:
    - How can connector segments be distinguished from sidewalks?
    - How do I identify crossing links in OSW data?
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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The crossing_link tag is the universal or final OpenSidewalks tagging rule.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/cross-platform/concept/crossing-links.md
tags:
    - Assistant
---

<!-- @format -->

# How can connector segments be distinguished in OpenSidewalks mapping?

## Short Answer

Connector segments can be tagged to distinguish a short connection between a sidewalk centerline and a curb or crossing from ordinary sidewalk ways. The use of `crossing_link` as an OpenStreetMap convention is provisional and must be checked against current guidance.

## Significance

Explicit classification lets a network retain the geometry while allowing routing and safety analyses to interpret it differently. It can also prevent connectors from inflating sidewalk-specific counts.

## What This Means

Preserve a usable pedestrian network connection and record its connector role with the supported tags. The current Tasking Manager guide describes a connector as being tagged with `highway=footway` plus `footway=sidewalk`, with optional `crossing_link=yes`. Downstream tools can then include the way in connectivity while classifying it separately.

## What This Does Not Mean

A connector tag does not remove the geometry from the network or guarantee that every consumer interprets it correctly. It is not a substitute for current schema documentation.

## How To Use This

Review current OpenSidewalks and project tagging rules before applying `crossing_link=yes` tags.

## Example

A short way from a curb ramp to a sidewalk is retained for routing but tagged as a crossing link so it is not counted as a standard sidewalk segment.

## Assistant Guidance

Do not present the discussed tag as settled or widely used. Ask for the current schema version and target consumer before giving exact tagging instructions.

## Related Concepts

- [How are crossing links represented across pedestrian data systems?](../../cross-platform/concept/crossing-links.md)
