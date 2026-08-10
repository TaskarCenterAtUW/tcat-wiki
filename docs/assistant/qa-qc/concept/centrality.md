---
title: What is centrality?
slug: centrality
doc_type: concept
questions:
    - What is centrality?
    - What does centrality mean?
    - What does higher centrality mean?
    - What does a lower centrality value mean?
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
publication_status: draft
last_reviewed: 2026-08-10
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Centrality directly measures safety, demand, or physical condition.
        - A high centrality value by itself proves that a location should be a project priority.
        - All centrality metrics measure the same kind of importance.
        - A centrality value is a direct observation of real-world travel or conditions.
        - An intersection-centered tile is the same as a parcel, service area, or exact field-survey boundary.
related_pages:
    - assistant/qa-qc/concept/centrality-metric-selection.md
    - assistant/qa-qc/concept/intersection-tile.md
    - assistant/qa-qc/concept/degree-centrality.md
    - assistant/qa-qc/concept/node-betweenness-centrality.md
    - assistant/qa-qc/concept/eigenvector-centrality.md
tags:
    - Assistant
---

<!-- @format -->

# What is centrality?

## Short Answer

Centrality describes the relative importance or significance of a feature type within a network or dataset. For example, it can describe how well-connected an intersection is.

In these reports, centrality is measured by tile. The tiles are centered on intersections or other pedestrian-network nodes.

## Significance

Centrality helps describe which mapped features are more connected, depended on, or influential than others. Using tiles provides a consistent geographic unit for displaying and comparing these values.

## What This Means

The meaning of a centrality value depends on the feature type, metric, and analysis unit. For an intersection-centered tile, a centrality metric may describe how well-connected the intersection is, how many modeled routes depend on it, or how it connects to other important intersections.

## What This Does Not Mean

Centrality does not by itself measure safety, demand, condition, ADA compliance, or project priority.

## How To Use This

Read the metric definition and confirm that the values are reported by intersection-centered tile before interpreting or comparing them.

## Example

If one intersection-centered tile has a higher degree-centrality value than another, the mapped graph represents more direct connections at that intersection. Node betweenness can instead highlight an intersection through which many modeled routes pass.

## Assistant Guidance

Ask which centrality metric and QA/QC Report are involved. Do not treat centrality terms as interchangeable.

## Related Concepts

- [How do QA/QC centrality metrics differ?](centrality-metric-selection.md)
