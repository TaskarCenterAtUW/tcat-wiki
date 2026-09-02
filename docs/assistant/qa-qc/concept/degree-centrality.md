---
uid: 76ce1628-3c14-498b-aa1b-e52a895c9bc8
title: What does degree centrality mean in pedestrian-network reports?
slug: degree-centrality
doc_type: concept
questions:
    - What does degree centrality mean in pedestrian-network reports?
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
        - Degree centrality alone identifies the most important project location.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does degree centrality mean in pedestrian-network reports?

## Short Answer

Degree centrality indicates how many walkable links meet at an intersection.

## Significance

It describes local connection choices in the mapped graph.

## What This Means

Higher values indicate more directly connected links under the report's graph model.

## What This Does Not Mean

It does not measure safety, demand, or condition by itself.

## How To Use This

Compare it with other metrics and local knowledge.

## Example

An intersection with many connected links has higher degree centrality than a simple endpoint.

## Assistant Guidance

Do not convert degree centrality directly into a funding priority.

## Related Concepts

- [What does centrality mean?](centrality.md)
