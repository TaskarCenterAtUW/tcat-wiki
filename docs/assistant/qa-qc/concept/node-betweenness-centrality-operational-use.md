---
title: What does node betweenness centrality reveal operationally?
slug: node-betweenness-centrality-operational-use
doc_type: concept
questions:
    - What does node centrality reveal operationally?
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
last_reviewed: 2026-08-14
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Node betweenness centrality proves the real-world condition of an intersection or segment.
        - A high node betweenness centrality value by itself determines a maintenance or investment priority.
        - Node betweenness centrality measures observed trips or travel demand.
related_pages:
    - assistant/qa-qc/concept/node-betweenness-centrality.md
    - assistant/qa-qc/concept/edge-betweenness-centrality.md
tags:
    - Assistant
---

<!-- @format -->

# What does node betweenness centrality reveal operationally?

## Short Answer

Node betweenness centrality indicates how many modeled routes pass through an intersection or other network node. A higher value means that more modeled routes depend on that node; a lower value means fewer modeled routes depend on it.

## Significance

This metric can help planners identify intersections where maintenance or a network disruption could affect many modeled routes. It can also help advocates identify highly relied-on locations where network updates or improvements may deserve attention.

## What This Means

Node betweenness centrality is calculated from the pedestrian network graph using graph-analysis libraries such as NetworkX and rustworkx. It describes modeled route dependence at a node; it is not calculated from points of interest or walksheds.

## What This Does Not Mean

The metric does not prove the real-world condition of an intersection or segment. A high value does not by itself prove that a location is unsafe, that people make the modeled trips, or that it should receive maintenance or investment priority.

## How To Use This

Planners can review locations with the highest values as candidates for maintenance investigation, then confirm conditions and alternatives with field evidence and local knowledge. Advocates can use high values to support requests for planners to review or update the pedestrian network. Compare the metric with other QA/QC measures rather than using it as a standalone decision rule.

## Example

If many modeled routes pass through one intersection, that intersection has a higher node betweenness centrality value than a similar intersection used by fewer modeled routes. A problem at the higher-value node could affect more modeled routes, but field review is needed to determine the actual condition and response.

## Assistant Guidance

Use the full term **node betweenness centrality** when answering. Explain higher values as greater modeled route dependence and lower values as less modeled route dependence. State that the metric comes from the network graph, not from POIs or walksheds, and avoid presenting it as observed travel demand or proof of physical condition. Cite the relevant QA/QC Report when answering from this page.

## Related Concepts

- [What does node betweenness centrality mean?](node-betweenness-centrality.md)
- [What does edge betweenness centrality mean?](edge-betweenness-centrality.md)
