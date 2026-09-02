---
uid: 79f77bc9-75ed-4b0d-8d0f-7b862a0ede07
title: What is edge betweenness?
slug: edge-betweenness
doc_type: concept
questions:
    - What is edge betweenness?
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
last_reviewed: 2026-08-20
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Edge betweenness measures the number of observed trips using a segment.
        - High edge betweenness proves that a segment is unsafe or inaccessible.
        - High edge betweenness alone establishes a maintenance or investment priority.
related_pages:
    - assistant/qa-qc/concept/node-betweenness-centrality.md
    - assistant/qa-qc/concept/edge-betweenness-centrality.md
tags:
    - Assistant
---

<!-- @format -->

# What is edge betweenness?

## Short Answer

Edge betweenness indicates how often a modeled route uses a particular network edge, such as a sidewalk or path segment. A higher value means that more modeled routes pass through that segment.

## Significance

It can identify segments that connect parts of the network and may affect many modeled routes if they are disconnected or unavailable.

## What This Means

The value represents modeled route dependence on an edge in the analyzed graph. It is calculated from graph structure and the report's routing assumptions.

## What This Does Not Mean

It does not directly measure observed trips, pedestrian volume, accessibility, safety, physical condition, or maintenance priority. A high value does not prove that a segment is unsafe or that people currently use it frequently.

## How To Use This

Use edge betweenness to identify segments for further review. Compare it with node betweenness, connectivity, data-quality indicators, points of interest, and field evidence. Interpret the result within the geographic area, network data, and routing assumptions used by the report.

## Example

If many modeled routes between destinations pass through one sidewalk segment, that segment has a higher edge-betweenness value than a segment used by fewer routes. The result indicates modeled dependence on the segment; it does not establish the number of observed trips.

## Assistant Guidance

Explain edge betweenness as a graph metric for modeled route dependence. State that higher values indicate that more modeled routes pass through the edge. Do not describe the value as a count of actual trips unless independent trip data supports that claim. Mention the report's assumptions and limitations when interpreting the metric.

## Related Concepts

- [What does node betweenness centrality mean?](node-betweenness-centrality.md)
- [What does edge betweenness centrality mean?](edge-betweenness-centrality.md)
