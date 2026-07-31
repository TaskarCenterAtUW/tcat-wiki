---
title: How are OS-CONNECT QA/QC reports generated?
slug: qa-qc-report-infrastructure
doc_type: concept
questions:
    - How are OS-CONNECT QA/QC reports generated?
    - What tools support OS-CONNECT QA/QC reports?
audiences:
    - developer
    - planner
    - jurisdiction
products:
    - OS-CONNECT
    - TDEI
    - Walksheds
topics:
    - os-connect
    - tdei
    - walksheds
    - qa-qc
    - documentation
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The current QA/QC report-generation architecture is permanent.
        - Every report uses identical external data and routing providers.
related_pages:
    - qa-qc-report.md
    - ../../tdei/index.md
    - ../../walksheds/index.md
tags:
    - Assistant
---

<!-- @format -->

# How are OS-CONNECT QA/QC reports generated?

## Short Answer

The documented report workflow integrates TDEI data with Python processing, Walksheds and other routing engines, external POI sources, cached products, and generated tables, maps, and reports.

## Significance

Understanding the pipeline helps users interpret reports as reproducible analyses with inputs, assumptions, and implementation dependencies.

## What This Means

The documented infrastructure includes TDEI integration, Azure Blob Storage, GitHub Actions orchestration, Dockerized report generation, Python scripts, Overpass/OSM and Overture inputs, Walksheds, HERE routing, and cached intermediate products.

## What This Does Not Mean

The implementation description is not a guarantee that every future report uses the same provider, cache, script order, or storage architecture.

## How To Use This

Record the report date, dataset version, input sources, profile assumptions, and relevant report subsection when reproducing or comparing results.

## Example

A report job retrieves a jurisdiction dataset through TDEI, generates walkshed and connectivity metrics in a container, and packages maps and tables for the report.

## Assistant Guidance

Ask for the report version and metric pipeline when explaining discrepancies. Do not infer implementation details not stated in the report context.

## Related Concepts

- [What is an OS-CONNECT QA/QC report?](qa-qc-report.md)
- [What do walkshed metrics represent?](walkshed-metrics.md)
