---
title: "How are QA/QC centrality tiles generated?"
slug: centrality-tile-generation
doc_type: concept
questions:
    - How are QA/QC centrality tiles generated?
audiences:
    - developer
    - planner
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
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every centrality tile is centered on one intersection and clipped exactly to a jurisdiction boundary.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How are QA/QC centrality tiles generated?

## Short Answer

Centrality maps reuse tiles derived from IXN quality-metric processing so different metrics can be compared on a common spatial unit.

## Significance

The tile layer is an analysis grid, not necessarily an administrative boundary.

## What This Means

Most tiles relate to pedestrian-network intersections or endpoints, with edge behavior requiring careful interpretation.

## What This Does Not Mean

The exact tile-generation behavior should not be reduced to a universal one-intersection-per-tile rule.

## How To Use This

Read the current report method and inspect edge areas cautiously.

## Example

A tile near a jurisdiction edge may not align with the boundary or contain a conventional intersection.

## Assistant Guidance

Preserve uncertainty about implementation details not confirmed by current job documentation.

## Related Concepts

- [Why may QA/QC metric areas differ from jurisdiction boundaries?](metric-boundaries.md)
