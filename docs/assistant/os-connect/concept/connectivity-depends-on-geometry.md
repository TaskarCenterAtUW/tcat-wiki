---
title: Why does OS-CONNECT connectivity depend on geometry?
slug: connectivity-depends-on-geometry
doc_type: concept
questions:
    - Why does OS-CONNECT connectivity depend on geometry?
    - Why are attributes not enough to make a route possible?
audiences:
    - planner
    - jurisdiction
products:
    - OS-CONNECT
    - OpenSidewalks
topics:
    - os-connect
    - opensidewalks
    - connectivity
    - graph-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Correct feature attributes can replace a missing network connector.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/workflow/report-connectivity-data-error.md
tags:
    - Assistant
---

<!-- @format -->

# Why does OS-CONNECT connectivity depend on geometry?

## Short Answer

A route requires connected sidewalk, curb, crossing, and connector geometry. Correct attributes cannot bridge a missing line or node connection.

## Significance

Topology determines whether routing and walkshed analysis can reach a feature.

## What This Means

Inspect both attributes and geometry when diagnosing inaccessible or unreachable areas. QA/QC connectivity and centrality metrics can reveal disconnected, misaligned, or over-simplified network structure even when individual tags look plausible.

## What This Does Not Mean

A nearby feature is not connected merely because its attributes are correct, and an unusual metric is not proof of a real-world mobility pattern without reviewing the geometry and context.

## How To Use This

Report missing connectors through the OS-CONNECT feedback workflow.

## Example

A correctly tagged crossing remains unreachable when no footway connects it to the sidewalk.

## Assistant Guidance

Separate attribute errors from geometry or topology errors.

## Related Concepts

- [How do I report a connectivity error in OS-CONNECT?](../workflow/report-connectivity-data-error.md)
