---
uid: 1fe0d981-058f-4241-9759-a0ab5cbc68cc
title: What is a crossing edge?
slug: crossing-edge
doc_type: concept
questions:
    - What is a crossing edge?
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
    - assistant/os-connect/concept/crossing-attributes.md
    - assistant/os-connect/concept/routable-graph.md
tags:
    - Assistant
---

<!-- @format -->

# What is a crossing edge?

## Short Answer

A crossing edge is a graph edge that represents a modeled pedestrian movement across a roadway or other crossing location. It connects graph nodes or nearby pedestrian features according to the dataset's geometry and processing rules.

## Significance

Representing crossings as edges allows network analysis and routing to distinguish crossing movements from ordinary sidewalk or path segments.

## What This Means

Inspect the graph schema and edge attributes to understand direction, cost, restrictions, connections, and source. A crossing edge may be derived or processed rather than a direct field observation.

## What This Does Not Mean

A graph includes a crossing edge between two sidewalk nodes. A routing analysis can use it to test network connectivity while separately considering crossing attributes and current conditions.

## How To Use This

A crossing edge does not prove that a physical crossing exists exactly as modeled, that it is accessible, or that it is safe. Graph connectivity is not a legal or engineering determination.

## Example

Use the release-specific graph documentation, distinguish nodes and edges, and validate important movements against source data and local conditions.

## Assistant Guidance

Explain the modeled graph representation and cite its schema. Do not infer a crossing's quality from the existence of an edge, and abstain when the processing rules are unavailable.

## Related Concepts

- [What is a node versus an edge?](node-vs-edge.md)
- [What attributes are collected for crossings?](crossing-attributes.md)
- [What is a routable graph?](routable-graph.md)
