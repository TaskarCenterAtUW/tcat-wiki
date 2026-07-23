---
title: "How do QA/QC centrality metrics differ?"
slug: centrality-metric-selection
doc_type: concept
questions:
    - How do QA/QC centrality metrics differ?
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
    - interpretation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-23
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - All centrality metrics measure the same kind of importance.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do QA/QC centrality metrics differ?

## Short Answer

Degree centrality counts direct connections; node and edge betweenness describe modeled route dependence; eigenvector centrality reflects connections to important neighbors.

## Significance

Choosing the metric affects the question being answered.

## What This Means

Use the measured unit and definition to select a metric.

## What This Does Not Mean

A high value in one metric is not interchangeable with a high value in another.

## How To Use This

Read the metric definition before interpreting a map or ranking.

## Example

Degree highlights many choices at a node, while edge betweenness highlights a relied-on segment.

## Assistant Guidance

Ask whether the user means a node, edge, direct connection, or network-neighbor metric.

## Related Concepts

- [What does centrality mean?](centrality.md)
