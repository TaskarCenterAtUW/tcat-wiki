---
title: 'What does "centrality" mean?'
slug: centrality
doc_type: concept
questions:
    - What does "centrality" mean?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - graph-metrics
    - os-connect
risk_level: medium
authority_level: explanatory
publication_status: stub
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does "centrality" mean?

## Short Answer

Centrality describes the relative importance of a feature within the mapped pedestrian graph. In these reports, it is measured on analysis units centered on pedestrian-network nodes or endpoints.

## Significance

It helps identify connected, depended-on, or influential parts of the network.

## What This Means

Different centrality metrics answer different questions, such as direct connections, route dependence, or connections to important neighbors.

## What This Does Not Mean

Centrality does not by itself measure safety, demand, condition, ADA compliance, or project priority.

## How To Use This

Read the metric definition and unit before interpreting a value.

## Example

Node betweenness can highlight an intersection through which many modeled routes pass, while degree centrality counts direct links.

## Assistant Guidance

Ask which centrality metric and dataset version are involved. Do not treat centrality terms as interchangeable.

## Related Concepts

- [How do QA/QC centrality metrics differ?](centrality-metric-selection.md)
