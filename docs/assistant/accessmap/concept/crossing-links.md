---
title: What are crossing links in pedestrian data?
slug: crossing-links
doc_type: concept
questions:
    - What are crossing links in pedestrian data?
    - Why distinguish connector segments from sidewalks?
audiences:
    - developer
    - planner
products:
    - AccessMap
    - OpenSidewalks
topics:
    - accessmap
    - opensidewalks
    - crossings
    - connectivity
    - safety
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
        - A crossing link is an ordinary sidewalk segment in every analysis.
related_pages:
    - assistant/accessmap/index.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# What are crossing links in pedestrian data?

## Short Answer

A crossing link is a connector between a sidewalk center line and a curb or crossing point. It can preserve pedestrian connectivity while being distinguished from ordinary sidewalk geometry.

## Significance

The distinction supports routing and separate analyses of crossing access, visibility, or exposure to roadway traffic. Removing the geometry would lose a useful pedestrian connection.

## What This Means

Keep the connector in the network when pedestrians use it, but use the applicable tagging to identify its role. Downstream analyses can then include or classify it appropriately.

AccessMap may combine curb-ramp conditions into a crossing-level travel decision, while OS-CONNECT can expose the individual curb ramps for inspection.

## What This Does Not Mean

A crossing link should not automatically be interpreted as a full sidewalk or treated identically in every metric. Current tagging guidance controls the exact representation.

## How To Use This

Check the current OpenSidewalks and mapping guidance before creating or retagging connector segments. Preserve connectivity and document any local mapping assumptions.

## Example

A short way connects a sidewalk center line to a curb ramp. It remains routable but is identified as a connector rather than counted as ordinary sidewalk length.

## Assistant Guidance

Use this as provisional terminology. Do not prescribe a tag or infer safety properties without the current schema and project guidance.

## Related Concepts

- [What is the OpenSidewalks data schema?](../../opensidewalks/concept/opensidewalks-schema.md)
