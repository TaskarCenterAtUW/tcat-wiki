---
uid: bec67c43-7e58-40ef-a719-bcc2f6615978
title: What does eigenvector centrality say about network importance?
slug: eigenvector-centrality-network-importance
doc_type: concept
questions:
    - What does eigenvector centrality say about network importance?
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
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Eigenvector centrality identifies the places people most want to reach.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does eigenvector centrality say about network importance?

## Short Answer

High eigenvector centrality indicates an intersection important for connecting to other important intersections, or routing through the network.

## Significance

It differs from identifying destinations or places people want to reach.

## What This Means

A location can be central to network connectivity without being a prominent local destination.

## What This Does Not Mean

The metric does not by itself establish demand, safety, or priority.

## How To Use This

Compare it with POIs, local knowledge, and other centrality metrics.

## Example

A less prominent intersection scores highly because it connects several important network areas.

## Assistant Guidance

Describe it as through-network importance, not destination importance.

## Related Concepts

- [How should eigenvector centrality be interpreted?](eigenvector-centrality-interpretation.md)
