---
title: What is QA/QC report provenance?
slug: report-provenance
doc_type: concept
questions:
    - What is QA/QC report provenance?
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
    - releases
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
        - A report generation date is the same as the source data ingest date.
related_pages:
    - assistant/qa-qc/concept/report-purpose-and-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What is QA/QC report provenance?

## Short Answer

Provenance identifies the dataset, pipeline, source context, and dates used to produce a report.

## Significance

It lets readers distinguish data changes from report presentation changes.

## What This Means

Read dataset version, pipeline version, imagery or collection date, report generation date, registry or ingest date, and source metadata together.

## What This Does Not Mean

A newer report-generation date does not necessarily mean newer source data or imagery.

## How To Use This

Record provenance when comparing or citing results, and note any source date that the report does not provide.

## Example

A report is regenerated after a layout change while its registry ingest date remains unchanged.

## Assistant Guidance

Ask which date or version the user means before comparing reports.

## Related Concepts

- [What source information appears in a QA/QC report?](report-data-sources.md)
