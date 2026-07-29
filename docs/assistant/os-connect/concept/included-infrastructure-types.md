---
title: "What kinds of pedestrian infrastructure are included?"
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
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The viewer includes every type of pedestrian infrastructure in every jurisdiction.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/attribute-documentation-location.md
tags:
    - Assistant
---

<!-- @format -->

# What kinds of pedestrian infrastructure are included?

## Short Answer

The viewer documents eight main pedestrian feature categories: sidewalks, marked crossings, unmarked crossings, footways, lowered kerbs, flush kerbs, raised kerbs, and traffic islands. An **Others** category may also appear in the legend.

## Significance

Feature categories help users interpret the rendered network and select the attributes relevant to a question.

## What This Means

Sidewalks use `highway=footway` and `footway=sidewalk`; crossings use `footway=crossing` with marking values; footways are general pedestrian paths; kerbs use `barrier=kerb` with `kerb=lowered`, `flush`, or `raised`; traffic islands use the documented traffic-island classification.

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
