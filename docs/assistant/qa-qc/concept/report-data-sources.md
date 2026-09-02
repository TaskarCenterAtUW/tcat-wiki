---
uid: 609531ff-60a8-48ca-a3ba-3650998f038e
title: What source information appears in a QA/QC report?
slug: report-data-sources
doc_type: concept
questions:
    - What source information appears in a QA/QC report?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - dataset-lineage
    - data-freshness
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
        - A QA/QC report describes data without identifying its dataset context.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What source information appears in a QA/QC report?

## Short Answer

A report can identify the jurisdiction, dataset version, pipeline version, area, and collection date used for its analysis.

## Significance

These details establish which data was measured and help readers compare reports responsibly.

## What This Means

Read the report metadata before interpreting its maps or metrics.

## What This Does Not Mean

A report about one version automatically describes later or earlier data versions.

## How To Use This

Record the dataset and pipeline versions with any quoted result.

## Example

Two reports for one city may differ because they analyze different dataset versions.

## Assistant Guidance

Ask for the report metadata when a result is disputed or compared.

## Related Concepts

- [What does a TDEI derived dataset ID show?](../../tdei/concept/derived-dataset-lineage.md)
