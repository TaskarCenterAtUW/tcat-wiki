---
title: How is AccessMap different from Walksheds?
slug: accessmap-vs-walksheds
doc_type: concept
questions:
    - How is AccessMap different from Walksheds?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - accessmap
    - walksheds
    - os-connect
    - tdei
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/accessmap/concept/accessmap.md
    - assistant/walksheds/concept/walkshed.md
    - assistant/cross-platform/concept/accessmap-routing.md
tags:
    - Assistant
---

<!-- @format -->

# How is AccessMap different from Walksheds?

## Short Answer

AccessMap is primarily route-focused: it helps calculate or compare pedestrian routes under selected accessibility preferences. Walksheds are primarily reachable-area-focused: they show which locations can be reached within a selected travel cost or profile. Both depend on datasets, profiles, network assumptions, and current product behavior.

## Significance

The distinction helps users choose a tool based on whether they need a path between places or an area of potential reachability around a starting point or destination.

## What This Means

For AccessMap, identify endpoints, profile, preferences, route cost, and route summary. For Walksheds, identify the origin, travel limit, profile, network, and reachable-area definition. Record source and product versions for either analysis.

## What This Does Not Mean

Neither output guarantees accessibility, current conditions, or suitability for every traveler. Similar datasets or profile names do not make the tools interchangeable.

## How To Use This

Use the narrowest tool for the decision, compare assumptions when combining outputs, validate important findings locally, and explain modeled results as evidence rather than certainty.

## Example

An agency uses AccessMap to compare approaches to a transit station and Walksheds to screen destinations reachable from several stops. It documents the different profiles and travel limits before comparing results.

## Assistant Guidance

Do not claim that one tool replaces the other or that their outputs are directly comparable without checking methods. Cite current product documentation and abstain when the dataset or configuration is unknown.

## Related Concepts

- [What is AccessMap?](../../accessmap/concept/accessmap.md)
- [What is a walkshed?](../../walksheds/concept/walkshed.md)
- [How does AccessMap calculate accessible routes?](../../accessmap/concept/route-calculation.md)
