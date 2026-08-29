---
title: How do local datasets improve routing quality?
slug: local-datasets-routing-quality
doc_type: concept
questions:
    - How do local datasets improve routing quality?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - data-quality
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
        - A local dataset automatically improves every AccessMap route.
        - Local data are automatically authoritative or error-free.
related_pages:
    - assistant/accessmap/concept/data-sources.md
    - assistant/accessmap/concept/missing-accessibility-data.md
    - assistant/accessmap/concept/route-calculation.md
tags:
    - Assistant
---

<!-- @format -->

# How do local datasets improve routing quality?

## Short Answer

Local datasets can improve routing quality when they add relevant, current, and well-documented pedestrian or accessibility information for the area being routed. The effect depends on how the data are reviewed, integrated, and used by the current system.

## Significance

Local detail can reveal conditions that broader sources miss, but it also introduces source, coverage, and maintenance questions.

## What This Means

- Identify the local publisher, scope, date, schema, and review status.
- Compare local coverage and attributes with the routing dataset.
- Validate important improvements and document the source version.

## What This Does Not Mean

Local does not automatically mean authoritative, complete, or more accurate. Adding data does not guarantee that AccessMap consumes every field or changes every route.

## How To Use This

Use local data with clear provenance and an explicit integration path. Recheck results when the source or product changes.

## Example

A city provides a current curb-ramp inventory, and the routing team documents how it is integrated before comparing route results in that jurisdiction.

## Assistant Guidance

Ask what local source and integration are involved. Cite both datasets, avoid promising an improvement without comparison evidence, and abstain when provenance or support is unclear.

## Related Concepts

- [AccessMap data sources](data-sources.md)
- [Missing accessibility data](missing-accessibility-data.md)
- [How AccessMap calculates routes](route-calculation.md)
