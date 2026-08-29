---
title: What is a node versus an edge?
slug: node-vs-edge
doc_type: concept
questions:
    - What is a node versus an edge?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - graph-metrics
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
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/crossing-edge.md
    - assistant/os-connect/concept/centrality-metrics.md
tags:
    - Assistant
---

<!-- @format -->

# What is a node versus an edge?

## Short Answer

A node is a graph point representing a location or connection, while an edge represents a modeled relationship or movement between nodes. In a pedestrian graph, nodes and edges can represent paths, intersections, crossings, or processed connections according to the schema.

## Significance

The distinction supports routing and graph metrics. Errors in nodes, edges, or their relationships can affect connectivity and reachability results.

## What This Means

Read the release-specific graph definitions, inspect endpoints and connections, and distinguish source geometry from the processed graph representation.

## What This Does Not Mean

A crossing edge may connect two sidewalk nodes. A centrality calculation may count nodes or edges differently, so the metric definition matters.

## How To Use This

Nodes and edges are analytical representations, not proof of physical access, safety, or current conditions. A connected graph does not certify an accessible route.

## Example

Use the schema and report definitions for the exact dataset, document versions and assumptions, and validate important relationships locally.

## Assistant Guidance

Name the graph, node or edge type, and metric. Do not infer physical meaning from geometry alone, and abstain when processing rules are unavailable.

## Related Concepts

- [What is a routable graph?](routable-graph.md)
- [What is a crossing edge?](crossing-edge.md)
- [What do OS-CONNECT centrality metrics mean?](centrality-metrics.md)
