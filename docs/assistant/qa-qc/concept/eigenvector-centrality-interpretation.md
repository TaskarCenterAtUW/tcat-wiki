---
uid: df77fa55-34b8-4c10-adc8-f3d60260e843
title: How should eigenvector centrality be interpreted?
slug: eigenvector-centrality-interpretation
doc_type: concept
questions:
    - How should eigenvector centrality be interpreted?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - graph-metrics
    - interpretation
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
        - High eigenvector centrality alone proves that a location is the top project priority.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should eigenvector centrality be interpreted?

## Short Answer

High eigenvector centrality indicates an intersection connected to other important intersections in the modeled network.

## Significance

It helps identify locations near the core of network structure.

## What This Means

Interpret high values as importance for routing through the network under the report's graph assumptions, not as a measure of direct connection choices or a destination people want to reach.

## What This Does Not Mean

It does not establish demand, safety, or a final investment priority.

## How To Use This

Compare the metric with POIs, conditions, and local knowledge.

## Example

A clustered downtown intersection has high eigenvector centrality because it connects to other central intersections.

## Assistant Guidance

State the metric's graph-based meaning and its limitations.

## Related Concepts

- [What does eigenvector centrality mean?](eigenvector-centrality.md)
