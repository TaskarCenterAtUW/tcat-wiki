---
title: What is the boundary between Workspaces and TDEI?
slug: workspace-and-tdei-boundary
doc_type: concept
questions:
    - What is the boundary between Workspaces and TDEI?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - editing
    - dataset-lineage
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
        - TDEI and Workspaces perform the same dataset operations.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is the boundary between Workspaces and TDEI?

## Short Answer

TDEI manages whole datasets, metadata, jobs, and releases; Workspaces supports feature-level editing and review of a selected copy.

## Significance

The distinction helps users choose the right tool for inventory management or GIS editing.

## What This Means

Use TDEI for dataset-wide processing and Workspaces for element-wise changes.

## What This Does Not Mean

Opening a workspace automatically updates or publishes the TDEI dataset.

## How To Use This

Identify whether the task concerns the whole dataset or individual features.

## Example

TDEI adds inferred inclines across a dataset, while Workspaces edits one sidewalk's geometry.

## Assistant Guidance

Ask whether the user needs dataset-level or feature-level work.

## Related Concepts

- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
