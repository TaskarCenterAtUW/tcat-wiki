---
title: "What is OpenSidewalks?"
slug: opensidewalks
doc_type: concept
questions:
    - What is OpenSidewalks?
    - What is the OpenSidewalks initiative?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - overview
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
        - OpenSidewalks is limited to sidewalk centerlines.
        - OpenSidewalks data is necessarily derived from OpenStreetMap.
related_pages:
    - ../index.md
    - opensidewalks-schema.md
    - network-entities.md
tags:
    - Assistant
---

<!-- @format -->

# What is OpenSidewalks?

## Short Answer

OpenSidewalks is a TCAT-led initiative and accessibility-forward standard for describing pedestrian networks and related infrastructure.

## Significance

The initiative supports consistent data collection and connected pedestrian routing, analysis, planning, and advocacy.

## What This Means

OpenSidewalks is designed to be largely compatible with OpenStreetMap, but datasets can also be created from agency data, imagery, or other sources. Its schema represents network and adjacent features with explicit geometry and metadata.

## What This Does Not Mean

OpenSidewalks is not only a sidewalk layer, and compatibility with OpenStreetMap does not mean the two systems have identical semantics.

## How To Use This

Identify the schema version, source, region, and intended consumer before using an OpenSidewalks dataset.

## Example

A city converts sidewalk inventory data into OpenSidewalks features so a downstream routing system can analyze connected pedestrian paths.

## Assistant Guidance

Ask whether the user means the initiative, the schema, an OSM mapping project, or a TDEI dataset.

## Related Concepts

- [What is the OpenSidewalks data schema?](opensidewalks-schema.md)
- [What are the OpenSidewalks network entities?](network-entities.md)
