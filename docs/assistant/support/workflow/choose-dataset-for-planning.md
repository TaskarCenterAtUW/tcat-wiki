---
uid: 601d1ddd-d691-4920-be36-72edff5cf8d7
title: Which dataset should I use if I need pedestrian walkway data for planning?
slug: choose-dataset-for-planning
doc_type: workflow
questions:
    - Which dataset should I use if I need pedestrian walkway data for planning?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - dataset-lineage
    - planning
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - One dataset is appropriate for every planning purpose or jurisdiction.
    related_pages:
        - assistant/support/workflow/choose-dataset-for-arcgis.md
tags:
    - Assistant
---

<!-- @format -->

# Which dataset should I use if I need pedestrian walkway data for planning?

## Short Answer

Choose the latest appropriate released dataset whose boundary, features, attributes, and quality information match the planning question. For pedestrian-network planning, this may be OS-CONNECT or an OpenSidewalks-compatible TDEI release.

## Significance

Dataset selection affects whether results can be interpreted and reproduced.

## What This Means

Check geographic scope, release date, source, version, completeness, QA/QC information, and intended use before analysis.

## What This Does Not Mean

A current release is not necessarily complete, authoritative for every feature, or suitable for legal decisions.

## How To Use This

Document the selection and validate priority locations locally.

## Example

A planner chooses a city release rather than a statewide extract because the study concerns one jurisdiction and its local stewardship context.

## Assistant Guidance

If the question does not identify a jurisdiction or use, ask for that context.

## Related Concepts

- [Choose a dataset for ArcGIS](choose-dataset-for-arcgis.md)
