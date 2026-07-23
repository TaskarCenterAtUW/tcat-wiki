---
title: "How do I search for a jurisdiction?"
slug: search-for-jurisdiction
doc_type: workflow
questions:
    - How do I search for a jurisdiction?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - public-vs-private-data
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
        - Searching for a jurisdiction proves that its dataset is complete or current.
related_pages:
    - ../concept/viewer-overview.md
    - ../concept/data-freshness.md
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I search for a jurisdiction?

## Short Answer

Use **Search For Dataset** in the top-right corner of the OS-CONNECT Data Viewer to find a dataset by name or partial name.

## Significance

Searching helps users navigate quickly to a jurisdiction's dataset boundary and inspect its available pedestrian data.

## What This Means

Enter a case-insensitive partial or complete dataset name, select **Search**, and let the viewer zoom to the matching result. Dataset names commonly use suffixes such as `City`, `UGA`, `UI`, `County`, or `CDP`.

## What This Does Not Mean

A search result does not establish that the jurisdiction has complete coverage or the latest data.

## How To Use This

After finding a dataset, inspect its boundary popup, upload date, version, TDEI ID, and QA/QC report.

## Example

A user searches for `gold`, selects the matching dataset, and the map fits the `WSP_Goldendale_City` boundary.

## Assistant Guidance

Ask for the exact dataset name and viewer behavior. Do not infer a missing result means no data exists without checking naming and coverage.

## Related Concepts

- [What am I looking at in the viewer?](../concept/viewer-overview.md)
- [How do I report an error?](report-data-error.md)
