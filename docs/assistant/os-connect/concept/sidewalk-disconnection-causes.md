---
uid: 15b469c9-2470-40fa-aa5c-fbeb441f07d9
title: Why are sidewalks disconnected on the map?
slug: sidewalk-disconnection-causes
doc_type: concept
questions:
    - What happens when sidewalks are disconnected?
    - Why are sidewalks disconnected on the map?
audiences:
    - public
    - advocate
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
topics:
    - os-connect
    - graph-metrics
    - data-quality
    - accessmap
    - walksheds
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A specific local gap is definitely a data error without verification.
related_pages:
    - assistant/cross-platform/concept/accessibility-islands.md
    - assistant/cross-platform/concept/connected-pedestrian-graph.md
tags:
    - Assistant
---

<!-- @format -->

# Why are sidewalks disconnected on the map?

## Short Answer

Disconnection usually means the routing or visualization graph lacks a valid link between segments — often a missing crossing, an unmapped connector, a tagging mismatch, or a rule that forbids traversing a segment for the active profile.

## Significance

An apparent disconnection can affect route results, walkshed boundaries, and how people interpret the map. Explaining the difference between map display and network connectivity helps users distinguish a data or modeling issue from a condition that needs local verification and constructive feedback.

## What This Means

Basemap tiles can look continuous while the pedestrian network data underneath is not. A graph may be disconnected because of a missing crossing link, an unmapped connector, a tagging mismatch, or a rule that prevents the active routing profile from traversing a segment. Depending on the data workflow, fixes may flow through mapping, imports, and validation pipelines.

## What This Does Not Mean

- A disconnected map does not prove that walking is impossible on the ground; the physical connection may exist but not be represented in the data.
- A specific local gap is not definitely a data error without checking the location, dataset, and active routing or visualization profile.
- The gap is not necessarily one team's oversight; private property, construction, or modeling choices can affect how a connection is represented.

## How To Use This

Use this explanation when a route or visualization appears to stop unexpectedly. For a specific location, identify the dataset and product involved, inspect the apparent gap, and use the product-specific feedback or correction workflow in AccessMap, Walksheds, or OS-CONNECT documentation when available.

## Example

A footpath crosses a large parking lot without modeled walkway edges; routing may not connect across the lot until paths are mapped consistently.

## Assistant Guidance

Explain the common causes: a missing crossing link, an unmapped connector or path, a tagging mismatch, or a profile restriction. Cite this article when using its explanation, and abstain from diagnosing a user's exact pin without location, dataset, and profile context. Do not state that the physical route is impossible, that the gap is definitely a data error, or that one team is necessarily responsible.

## Related Concepts

- [Accessibility islands](../../cross-platform/concept/accessibility-islands.md)
- [Connected pedestrian graph](../../cross-platform/concept/connected-pedestrian-graph.md)
