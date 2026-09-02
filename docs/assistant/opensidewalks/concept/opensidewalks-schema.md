---
uid: 85c9e786-df58-40a6-af7c-8e5e680061a9
title: What is the OpenSidewalks data schema?
slug: opensidewalks-schema
doc_type: concept
questions:
    - What is the OpenSidewalks data schema?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - formats
    - accessibility-data
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
        - OpenSidewalks data is an unconnected collection of map features.
        - A schema version label alone proves that a dataset is valid for every consumer.
related_pages:
    - ../index.md
    - network-entities.md
    - network-topology.md
    - dataset-metadata-and-provenance.md
tags:
    - Assistant
---

<!-- @format -->

# What is the OpenSidewalks data schema?

## Short Answer

The OpenSidewalks Schema is an explicit network schema for describing pedestrian paths, crossings, some streets, barriers, and related features as connected, graph-analyzable data.

## Significance

The graph model allows routing and analysis tools to construct network relationships from metadata rather than relying only on spatial inference.

## What This Means

Core entities include Nodes, Edges, and Zones. Adjacent and Custom Entities describe relevant features that are not necessarily part of the traversable graph. Edges reference endpoint Nodes with `_u_id` and `_v_id`; Zones reference Nodes with `_w_id`. Data is intended to be largely compatible with OpenStreetMap but may come from other sources.

## What This Does Not Mean

Schema compatibility does not guarantee complete coverage, current conditions, or identical interpretation by every tool. Always check the dataset's `$schema` and the target consumer.

## How To Use This

Before using a dataset, identify its schema version, entity types, topology, metadata, coordinate system, and validation status. Use the maintained schema documentation for exact field requirements.

## Example

A sidewalk Edge references two endpoint Nodes, while a nearby bench is represented as an adjacent Point rather than as a traversable network Edge.

## Assistant Guidance

Do not infer a field's meaning across schema versions. Ask which entity, geometry, and consumer are involved, and cite the versioned schema.

## Related Concepts

- [What are the OpenSidewalks network entities?](network-entities.md)
- [What topology rules apply?](network-topology.md)
