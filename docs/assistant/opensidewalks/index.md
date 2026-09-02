---
uid: 1df8e7aa-2bc6-4360-bb30-c1c69cc0e260
title: OpenSidewalks — Assistant Knowledge Base
slug: opensidewalks-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the OpenSidewalks knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - tdei-ecosystem
    - accessibility-data
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - OpenSidewalks is only a sidewalk layer.
        - OpenStreetMap compatibility means every OpenSidewalks dataset has identical semantics to OSM.
        - Schema validation proves that a dataset is current everywhere.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
tags:
    - Assistant
---

<!-- @format -->

# OpenSidewalks — Assistant Knowledge Base

## Short Answer

OpenSidewalks is a TCAT-led initiative and accessibility-forward pedestrian network data standard. It describes connected pedestrian infrastructure and related features in a form that can support routing, analysis, and planning.

## Significance

The explicit network model helps downstream tools reason about pedestrian connectivity, barriers, crossings, sidewalks, and related infrastructure rather than treating features as an unconnected collection.

## What This Means

OpenSidewalks is designed to be largely compatible with OpenStreetMap, but data can also come from other sources. TDEI supports validation, ingestion, management, and downstream use of OpenSidewalks-compliant data. Mapping and validation activities may be coordinated through the OSM US Tasking Manager.

## What This Does Not Mean

OpenSidewalks is not a guarantee that every pedestrian feature is mapped, accessible, current, or interpreted identically by every consumer. A validated dataset still has a source, timestamp, version, and coverage boundary.

## How To Use This

Identify the schema version, source, region, timestamp, and intended consumer before interpreting or transforming a dataset. For OSM-based mapping, follow current OpenSidewalks and local OSM guidance.

## Example

A project maps sidewalks, crossings, and curb features in the OSM US Tasking Manager, validates the connections and tags, and uses TDEI tooling to validate the resulting dataset.

## Assistant Guidance

Ask for the schema version, data source, geometry type, region, and downstream use. Cite the relevant schema or mapping guide, and do not infer accessibility from a tag without context.

## Related Concepts

- [What is the OpenSidewalks data schema?](concept/opensidewalks-schema.md)
- [What are the OpenSidewalks network entities?](concept/network-entities.md)
- [How does TDEI validate OpenSidewalks data?](concept/tdei-schema-validation.md)
