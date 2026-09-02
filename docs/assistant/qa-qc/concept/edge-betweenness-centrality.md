---
uid: ebf0cec2-a43f-4618-9d34-04b933aea3f5
title: What does edge betweenness centrality mean?
slug: edge-betweenness-centrality
doc_type: concept
questions:
    - What does edge betweenness centrality mean?
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
    - connectivity
    - sidewalks
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
        - High edge betweenness proves that a sidewalk segment is unsafe.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does edge betweenness centrality mean?

## Short Answer

Edge betweenness indicates how many modeled routes depend on a network segment. It is calculated at the edge level from the graph data.

## Significance

It can identify links whose disruption may affect many modeled paths.

## What This Means

Higher values indicate greater graph dependency under the report's assumptions.

## What This Does Not Mean

It does not measure actual demand, condition, or safety by itself.

## How To Use This

Compare it with POIs, connectivity, data quality, and field evidence.

## Example

A segment on a major corridor has high edge betweenness because many routes use it.

## Assistant Guidance

Describe the metric as modeled dependency, not observed travel volume.

## Related Concepts

- [What does node betweenness centrality mean?](node-betweenness-centrality.md)
