---
uid: 9f0b255e-efe7-4ec0-9b9a-1849737b6a32
title: How can centrality reveal a need for network redundancy?
slug: centrality-and-redundancy
doc_type: concept
questions:
    - How can centrality reveal a need for network redundancy?
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
    - connectivity
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-23
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Centrality alone proves that a redundant connection should be built.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can centrality reveal a need for network redundancy?

## Short Answer

A highly depended-on node or edge can suggest that the network has a vulnerable concentration of routes.

## Significance

Alternative connections may reduce reliance on one modeled element.

## What This Means

Use centrality to investigate redundancy alongside conditions, destinations, and local priorities.

## What This Does Not Mean

The metric alone does not select a project or prove that redundancy is feasible.

## How To Use This

Inspect the network and test proposed alternatives with appropriate models.

## Example

A city investigates another crossing near a highly depended-on intersection.

## Assistant Guidance

Describe redundancy as a planning question, not an automated recommendation.

## Related Concepts

- [How can node betweenness support operations?](node-betweenness-operational-use.md)
