---
uid: 44e7cf77-c4f6-4911-97bb-8cd20f26c76c
title: What limitations can affect QA/QC reports for small datasets?
slug: small-dataset-limitations
doc_type: concept
questions:
    - What limitations can affect QA/QC reports for small datasets?
    - Why might a small dataset lack detailed routing analysis or points of interest?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - data-quality
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every OS-CONNECT dataset supports every QA/QC metric.
        - A missing routing or points-of-interest result proves that the dataset is invalid.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What limitations can affect QA/QC reports for small datasets?

## Short Answer

Very small datasets may not contain many points of interest or enough network structure for full routing and QA/QC metrics. These cases require interpreting the report in light of the dataset's size and coverage.

## Significance

A metric that cannot be produced is different from a metric that reports a poor result. Distinguishing the two prevents over-interpreting limited coverage.

## What This Means

Check the dataset's geographic extent, feature counts, POI inventory, and available report sections before comparing it with larger datasets. A small or incomplete POI inventory can limit destination-based walkshed interpretation.

## What This Does Not Mean

Missing routing or points-of-interest results do not by themselves prove that the dataset is invalid or that the data pipeline failed. Confirm the specific report and dataset conditions.

## How To Use This

Record which metrics are available and which are absent. Ask for the dataset scope and current QA/QC processing details before drawing conclusions.

## Example

A small town dataset contains only a few pedestrian features and points of interest. Its report may provide limited network analysis and should not be compared directly with metrics in a statewide report.

## Assistant Guidance

Ask which metric or report section is missing. Do not infer a data-quality failure from an unavailable analysis without current processing evidence.

## Related Concepts

- [What does completeness mean?](completeness.md)
