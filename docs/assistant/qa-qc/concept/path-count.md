---
title: 'What does "path count" mean in QA/QC reports?'
slug: path-count
doc_type: concept
questions:
    - What does path count mean in QA/QC reports?
    - What does "path count" mean?
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
    - os-connect
    - walksheds
    - accessibility-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does "path count" mean in QA/QC reports?

## Short Answer

Path count is the number of deduplicated mapped features reachable within merged POI-origin walksheds for a profile.

## Significance

It summarizes reachable network elements rather than the total inventory.

## What This Means

Counts can include sidewalks, crossings, curbs, and related features within the modeled walksheds.

## What This Does Not Mean

An overlapping feature is not counted once for every POI, and the value is not a citywide count of every feature.

## How To Use This

Read the count with its profile, POI set, budget, and dataset version.

## Example

A sidewalk reached from two nearby POIs contributes once after overlapping walksheds are merged.

## Assistant Guidance

Distinguish path count from total feature count and ask which profile and origins were used.

## Related Concepts

- [What are the limits of POI-origin walkshed analysis?](../../walksheds/concept/poi-origin-analysis-limits.md)
