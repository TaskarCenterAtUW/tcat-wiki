---
uid: c32dabcf-84ae-4926-8d01-fe2906b4b51b
title: What kinds of pedestrian infrastructure are included?
slug: included-infrastructure-types
doc_type: concept
questions:
    - What kinds of pedestrian infrastructure are included?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - formats
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/attribute-documentation-location.md
tags:
    - Assistant
---

<!-- @format -->

# What kinds of pedestrian infrastructure are included?

## Short Answer

The viewer manual documents nine displayed categories: sidewalks, marked crossings, unmarked crossings, footways, lowered kerbs, flush kerbs, raised kerbs, traffic islands, and **Others**. Its tag descriptions identify sidewalks, crossings, footways, curbs, and traffic islands using `highway`, `footway`, `crossing:markings`, `barrier`, and `kerb` values.

## Significance

Feature categories help users interpret the rendered network and select the attributes relevant to a question.

## What This Means

Sidewalks use `highway=footway` and `footway=sidewalk`; crossings use `footway=crossing` with `crossing:markings=yes` or `no`; general footways use `highway=footway` without a footway subclass; kerbs use `barrier=kerb` with `kerb=lowered`, `flush`, or `raised`; traffic islands use `highway=footway` and `footway=traffic_island`.

## What This Does Not Mean

The categories do not prove that every feature is mapped, correctly tagged, or accessible to every traveler.

## How To Use This

Use the feature type with the selected feature's attributes, geometry, dataset version, and QA/QC context.

## Example

A marked crossing appears separately from an unmarked crossing so users can inspect its tags and mapped connectivity.

## Assistant Guidance

Ask which viewer category and schema version are involved. Do not infer a missing category means the physical feature is absent.

## Related Concepts

- [What do the colors mean?](map-color-legend.md)
- [Where are attribute definitions documented?](attribute-documentation-location.md)
