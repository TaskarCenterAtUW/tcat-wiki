---
uid: 4d60cca7-839b-49e4-a16b-4a15b9fedd03
title: What do OS-CONNECT centrality metrics mean?
slug: centrality-metrics
doc_type: concept
questions:
    - What do OS-CONNECT centrality metrics mean?
    - How should I interpret centrality in an OS-CONNECT QA/QC report?
audiences:
    - planner
    - jurisdiction
    - advocate
products:
    - OS-CONNECT
topics:
    - os-connect
    - qa-qc
    - accessibility-metrics
    - connectivity
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A high centrality value proves high real-world pedestrian use.
        - A low centrality value proves that a location is unimportant to residents.
related_pages:
    - connectivity-depends-on-geometry.md
    - qa-qc-report.md
    - ../../qa-qc/concept/what-is-edge-betweenness.md
tags:
    - Assistant
---

<!-- @format -->

# What do OS-CONNECT centrality metrics mean?

## Short Answer

Centrality metrics describe structural importance in the modeled pedestrian network. They can help identify hubs, bottlenecks, and uneven dependence on network segments.

## Significance

The metrics help data stewards and planners focus review or maintenance questions, but they must be interpreted as properties of the modeled graph.

## What This Means

Degree centrality counts direct connections. Eigenvector centrality reflects connection to other well-connected nodes. Node and edge betweenness measure how often a node or segment lies on shortest paths. Standard deviation of betweenness describes how unevenly network dependence is distributed.

## What This Does Not Mean

Centrality is not a direct measure of observed trips, preference, condition, safety, or public value. Anomalous values can result from missing links, simplified geometry, or topology errors.

## How To Use This

Review maps, histograms, geometry, attributes, and local knowledge together. Use high betweenness to investigate potential critical links and unusual distributions to prioritize QA.

## Example

A sidewalk segment with unusually high edge betweenness is reviewed for missing parallel routes and connectivity errors before being prioritized for maintenance.

## Assistant Guidance

State the metric and graph context. Do not convert centrality into a claim about actual travel without independent evidence.

## Related Concepts

- [Why does connectivity depend on geometry?](connectivity-depends-on-geometry.md)
- [What is an OS-CONNECT QA/QC report?](qa-qc-report.md)
