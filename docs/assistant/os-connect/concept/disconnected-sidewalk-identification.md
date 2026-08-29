---
title: How are disconnected sidewalks identified?
slug: disconnected-sidewalk-identification
doc_type: concept
questions:
    - How are disconnected sidewalks identified?
    - Why are some sidewalks disconnected?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - connectivity
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
    - assistant/os-connect/concept/disconnected-dataset-problem.md
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/common-errors.md
tags:
    - Assistant
---

<!-- @format -->

# How are disconnected sidewalks identified?

## Short Answer

Disconnected sidewalks can be identified by inspecting endpoint geometry, graph connections, crossing relationships, and network-analysis results. The exact detection rule depends on the dataset and processing workflow.

## Significance

Identifying possible disconnections helps prioritize review and can reveal missing paths, crossings, ramps, or geometry relationships that affect modeled access.

## What This Means

Check endpoints, nearby features, crossing edges, barriers, access restrictions, and source coverage. Compare the apparent gap with imagery, local records, or field observations before classifying it.

## What This Does Not Mean

A sidewalk endpoint is near a roadway but has no crossing edge. Review shows either a missing mapped crossing or a real access gap; the result is documented as unresolved until verified.

## How To Use This

A disconnected graph segment does not prove that the physical sidewalk is disconnected, and a connected segment does not prove that it is usable or accessible.

## Example

Use release-specific graph definitions, record the location and version, inspect complex intersections, and submit specific geometry or attribute corrections through the current channel.

## Assistant Guidance

Explain whether the result is a geometric, graph, or physical-condition finding. Cite the method and evidence, and abstain when the processing rule or source data are unavailable.

## Related Concepts

- [Why are disconnected pedestrian datasets a problem?](disconnected-dataset-problem.md)
- [What is a routable graph?](routable-graph.md)
- [What kinds of errors are most common?](common-errors.md)
