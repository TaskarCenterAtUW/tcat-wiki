---
uid: 29e2f22b-4a69-417c-a0c5-29680ed3fe8f
title: What does node betweenness centrality mean?
slug: node-betweenness-centrality
doc_type: concept
questions:
    - What does node betweenness centrality mean?
audiences:
    - planner
    - developer
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - graph-metrics
    - intersections
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
        - High node betweenness proves that an intersection is unsafe.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does node betweenness centrality mean?

## Short Answer

Node betweenness indicates how many modeled routes depend on an intersection. It is calculated from graph node and edge data rather than directly from POIs or walksheds.

## Significance

It can reveal network junctions where disruptions may affect many paths.

## What This Means

Higher values indicate greater modeled dependency in the analyzed graph.

## What This Does Not Mean

It does not measure actual trips, safety, or current conditions without supporting evidence.

## How To Use This

Use it with connectivity, POI, and field information.

## Example

A major corridor intersection has high betweenness because many modeled routes pass through it.

## Assistant Guidance

Describe it as graph dependency, not observed travel demand.

## Related Concepts

- [What does centrality mean?](centrality.md)
