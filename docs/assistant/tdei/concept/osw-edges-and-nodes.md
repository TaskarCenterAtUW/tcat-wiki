---
title: What are edges and nodes in the OSW download?
slug: osw-edges-and-nodes
doc_type: concept
questions:
    - What are edges and nodes in the OSW download?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - export
    - graph-metrics
    - opensidewalks
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every OSW edge is a sidewalk and every node is a curb ramp or crossing.
        - Graph structure alone proves accessibility or physical condition.
related_pages:
    - assistant/tdei/concept/osw-download-contents.md
    - assistant/opensidewalks/concept/network-entities.md
    - assistant/os-connect/concept/node-vs-edge.md
tags:
    - Assistant
---

<!-- @format -->

# What are edges and nodes in the OSW download?

## Short Answer

In an OSW download, nodes represent points in the pedestrian network and edges represent connections or traversable segments between points. Their exact fields and representation depend on the OSW schema and the dataset version.

## Significance

Understanding nodes and edges helps users interpret network geometry, connectivity, and routing analysis. It prevents a graph representation from being mistaken for a simple list of independent map features.

## What This Means

- Use nodes to understand endpoints, intersections, or other network points.
- Use edges to understand connected segments and their attributes.
- Check the schema and version for the authoritative field definitions and identifiers.

## What This Does Not Mean

An edge is not automatically a sidewalk, and a node is not automatically a curb ramp or crossing. Graph structure alone does not establish accessibility, condition, or legal status.

## How To Use This

Read the download with its schema and metadata, inspect identifiers and relationships, and preserve the version when converting or analyzing the data.

## Example

A GIS analyst follows an edge between two nodes, then checks the feature attributes to determine whether it represents a sidewalk segment, crossing, or another network relationship.

## Assistant Guidance

Cite the applicable OSW schema and release. Do not infer field meanings from geometry alone, and ask for the dataset version when the user's file differs from the documented structure.

## Related Concepts

- [OSW download contents](osw-download-contents.md)
- [OpenSidewalks network entities](../../opensidewalks/concept/network-entities.md)
- [Nodes versus edges in OS-CONNECT](../../os-connect/concept/node-vs-edge.md)
