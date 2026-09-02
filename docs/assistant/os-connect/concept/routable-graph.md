---
uid: c9b0897b-7cbf-4960-9d82-3718a746de3c
title: What is a routable graph?
slug: routable-graph
doc_type: concept
questions:
    - What is a routable graph?
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
    - assistant/os-connect/concept/node-vs-edge.md
    - assistant/os-connect/concept/crossing-edge.md
    - assistant/os-connect/concept/routing-assumptions.md
tags:
    - Assistant
---

<!-- @format -->

# What is a routable graph?

## Short Answer

A routable graph is a network representation of pedestrian features, nodes, edges, connections, and costs that a routing process can use to calculate paths or reachability.

## Significance

It translates mapped geometry and attributes into a structure that can account for connections, crossings, barriers, profiles, and travel costs.

## What This Means

Check how the graph is built, how features are snapped and connected, what costs and restrictions apply, how missing data are handled, and which release is used.

## What This Does Not Mean

A graph can connect two sidewalk nodes through a crossing edge and assign a cost to that movement under a selected profile.

## How To Use This

A routable graph does not prove that a path exists physically as modeled, is safe or accessible, or is current. Graph connectivity is not legal or engineering certification.

## Example

Use graph results for bounded analysis, document assumptions and versions, inspect unexpected connections, and validate consequential findings locally.

## Assistant Guidance

Name the graph, source, profile, and cost rules. Do not infer physical conditions from graph structure alone and abstain when processing rules are unknown.

## Related Concepts

- [What is a node versus an edge?](node-vs-edge.md)
- [What is a crossing edge?](crossing-edge.md)
- [What routing assumptions are used?](routing-assumptions.md)
