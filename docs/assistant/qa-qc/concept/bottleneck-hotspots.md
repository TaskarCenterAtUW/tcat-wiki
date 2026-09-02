---
uid: 2932c97d-2f41-488f-9054-1e864aeb1f97
title: What are QA/QC bottleneck hotspots?
slug: bottleneck-hotspots
doc_type: concept
questions:
    - What are QA/QC bottleneck hotspots?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - bottlenecks
    - prioritization
    - connectivity
    - accessibility-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A QA/QC bottleneck hotspot is automatically a recommended project.
related_pages:
    - assistant/qa-qc/concept/poi-density-and-prioritization.md
tags:
    - Assistant
---

<!-- @format -->

# What are QA/QC bottleneck hotspots?

## Short Answer

Bottleneck hotspots are locations where poor traversability intersects with important network or destination connections.

## Significance

They identify places where improvements may have broad network effects.

## What This Means

A hotspot combines modeled route dependence with modeled traversal difficulty. A report may derive it by converting traversability to a barrier score, standardizing both signals, and combining them for within-report comparison.

## What This Does Not Mean

It is not a confirmed field problem, final design, safety determination, or funding decision.

## How To Use This

Review the underlying centrality and traversability values, POIs, connectivity, data quality, and local priorities.

## Example

A hospital connection with limited pedestrian links appears as a hotspot for further study.

## Assistant Guidance

Explain which inputs produced the hotspot and preserve uncertainty.

## Related Concepts

- [How can POI density inform QA/QC priorities?](poi-density-and-prioritization.md)
