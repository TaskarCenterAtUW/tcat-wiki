---
uid: d99c51e4-adc0-44dc-9068-a7729475a2ed
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
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/report-purpose-and-limitations.md
    - assistant/qa-qc/concept/report-data-sources.md
tags:
    - Assistant
---

<!-- @format -->

# What is QA/QC report provenance?

## Short Answer

Provenance identifies the dataset and source context, the processing versions, and the distinct dates associated with a QA/QC report.

## Significance

It lets readers distinguish data changes from report presentation changes.

## What This Means

Read each provenance field separately: dataset name and version, collection date, imagery reference year, registry-ingest timestamp, report-generation timestamp, QA/QC pipeline version, report-code release tag or commit, and POI sources or snapshot date. Record only fields the report provides; label an absent value “Not provided” rather than filling the gap from another date.

## What This Does Not Mean

A newer report-generation date does not necessarily mean newer source data or imagery. The dataset collection date, imagery vintage, registry-ingest time, and POI snapshot date are also different from one another.

## How To Use This

Record the dataset and pipeline versions and each relevant source or processing date when comparing or citing results. Note explicitly when the report does not provide an imagery date, POI snapshot date, or other needed provenance field.

## Example

A planner compares dataset and pipeline versions, an imagery reference, a registry-ingest timestamp, and a report-generation timestamp. The POI extraction date is not listed, so the planner records it as “Not provided” instead of substituting the report-generation date.

## Assistant Guidance

Ask which dataset, pipeline, imagery, ingest, report-generation, or POI date the user means before comparing reports. Do not infer a missing date from the report's other timestamps.

## Related Concepts

- [What source information appears in a QA/QC report?](report-data-sources.md)
