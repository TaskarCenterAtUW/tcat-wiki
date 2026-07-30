---
title: What topology rules apply to the OpenSidewalks network?
slug: network-topology
doc_type: concept
questions:
    - What topology rules apply to the OpenSidewalks network?
    - How should OpenSidewalks sidewalks and crossings connect?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OpenSidewalks
    - AccessMap
topics:
    - opensidewalks
    - accessmap
    - connectivity
    - standards
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Crossing line intersections alone create OpenSidewalks network connectivity.
        - A sidewalk can connect directly to a crossing without the documented connecting footway structure.
related_pages:
    - opensidewalks-schema.md
    - connector-segment-tagging.md
    - ../../accessmap/concept/disconnected-sidewalks.md
tags:
    - Assistant
---

<!-- @format -->

# What topology rules apply to the OpenSidewalks network?

## Short Answer

OpenSidewalks network features must connect through explicit shared nodes and endpoints. Crossing, sidewalk, curb, and road relationships are represented as connected geometry rather than inferred from lines that merely cross.

## Significance

Explicit topology enables routing and graph analysis and helps prevent gaps or false connections in the pedestrian network.

## What This Means

Edges should meet end-to-end. A road and a crossing should share a Node where they connect. Crossings do not connect directly to sidewalk centerlines; a plain Footway can connect the crossing to the sidewalk. Curb interfaces and curb ramps are mapped at Edge endpoints.

## What This Does Not Mean

Two line geometries crossing on a map do not necessarily create a network connection. A visually close feature may still be disconnected in the graph.

## How To Use This

Inspect shared nodes, endpoint references, and connecting footways during mapping and validation. Test connectivity in the intended downstream tool.

## Example

A crossing meets the road at a shared middle Node, has curb Nodes at both ends, and uses short footway connectors to reach sidewalk centerlines.

## Assistant Guidance

Ask for the schema version and geometry arrangement before diagnosing a connectivity issue. Distinguish visual proximity from explicit graph topology.

## Related Concepts

- [What entities does the OpenSidewalks Schema define?](network-entities.md)
- [How can connector segments be distinguished?](connector-segment-tagging.md)
