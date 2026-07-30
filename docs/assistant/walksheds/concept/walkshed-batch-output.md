---
title: How are Walksheds batch outputs handled?
slug: walkshed-batch-output
doc_type: concept
questions:
    - How are Walksheds batch outputs handled?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - export
    - limitations
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-26
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds always provides one combined download for every batch result.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How are Walksheds batch outputs handled?

## Short Answer

Batch results may be available as individual outputs or summaries, depending on the current interface.

## Significance

Output handling affects large-area analysis and reproducibility.

## What This Means

Record which locations and profiles produced each result.

## What This Does Not Mean

A batch run necessarily creates a single downloadable archive of all GeoJSON outputs.

## How To Use This

Plan for individual downloads or use an approved script when available.

## Example

A city-wide batch produces many per-location walkshed files that must be collected separately.

## Assistant Guidance

Verify current export capabilities before promising bulk download.

## Related Concepts

- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
