---
title: What does the TDEI Filter Dataset By BBox job do?
slug: job-filter-dataset-by-bbox
doc_type: concept
questions:
    - What does the TDEI Filter Dataset By BBox job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - vector-data
    - editing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Bounding-box filtering preserves every relationship or context outside the selected extent.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/filter-dataset-by-bbox.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Filter Dataset By BBox job do?

## Short Answer

The Filter Dataset By BBox job extracts a subgraph or dataset area within a specified bounding box.

## Significance

Spatial filtering creates a smaller working area for analysis, conversion, or inspection.

## What This Means

Provide the required dataset and bounding-box inputs, submit the job, and inspect the output and job status.

## What This Does Not Mean

A bounding-box result is not automatically equivalent to the source dataset and may omit context beyond the selected extent.

## How To Use This

Record the source dataset, bounding box, coordinate system, output, and version.

## Example

A developer extracts one city block from a larger pedestrian network for a test workflow.

## Assistant Guidance

Ask for the bbox coordinate order, CRS, and intended downstream use.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
