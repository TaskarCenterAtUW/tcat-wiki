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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/report-provenance.md
    - assistant/qa-qc/concept/point-of-interest-sources.md
    - assistant/qa-qc/concept/report-question-sections.md
tags:
    - Assistant
---

<!-- @format -->

# What source information appears in a QA/QC report?

## Short Answer

The report's summary and provenance tables identify its dataset and jurisdiction, dataset and pipeline versions, analysis area, collection date, mapped-feature inventory, imagery reference, and points-of-interest (POI) sources. The fields provided vary by report.

## Significance

These details establish which data was measured and help readers compare reports responsibly.

## What This Means

Read the report's inventory and provenance tables before interpreting its maps or metrics. The dataset summary lists the dataset name, version, pipeline version, area, collection date, and counts of accessibility islands, POIs, and disconnected POIs. The elements table lists counts of sidewalks, crossings, curbs, and POIs. The provenance table identifies imagery vintage, report-generation time, registry-ingest time, report-code version, and POI sources or extract dates when provided.

## What This Does Not Mean

A collection date, imagery reference year, registry-ingest timestamp, and report-generation timestamp describe different events and are not interchangeable. A listed POI source does not establish that the inventory is complete or that its snapshot date is known.

## How To Use This

Record the dataset name and version, pipeline version, geography, collection date, and any source dates or report-code identifiers shown. If a field is marked “Not provided” or omitted, report it as unavailable instead of inferring it from another date or report.

## Example

A report lists its available dataset, pipeline, collection, imagery, ingest, and generation metadata. When the POI extract date is absent, record it as not provided rather than substituting another timestamp.

## Assistant Guidance

Ask for the exact report metadata when a result is disputed or compared. Keep the report's source dates and version identifiers distinct, and do not claim a missing POI snapshot date or other unreported metadata.

## Related Concepts

- [What does a TDEI derived dataset ID show?](../../tdei/concept/derived-dataset-lineage.md)
- [What is QA/QC report provenance?](report-provenance.md)
