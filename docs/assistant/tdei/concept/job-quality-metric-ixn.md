---
title: "What does the TDEI IXN quality-metric job do?"
slug: job-quality-metric-ixn
doc_type: concept
questions:
    - What does the TDEI IXN quality-metric job do?
products:
    - TDEI
    - OS-CONNECT
audiences:
    - developer
    - jurisdiction
    - planner
topics:
    - tdei
    - os-connect
    - qa-qc
    - accessibility-metrics
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - An IXN quality score is a legal accessibility determination.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/quality-metric-ixn-calculation.md
    - ../../os-connect/concept/intersection-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI IXN quality-metric job do?

## Short Answer

The IXN job calculates intersection-quality metrics for a TDEI dataset using its dataset ID and, optionally, an intersection-polygon GeoJSON file.

## Significance

The result supports QA/QC review of modeled intersection traversability and network structure.

## What This Means

Provide the TDEI Dataset ID. An optional GeoJSON polygon file can improve performance; if omitted, the system generates Voronoi polygons from the dataset area according to the current documentation. Track the job ID and inspect its result.

## What This Does Not Mean

An IXN result is a modeled indicator, not proof of real-world accessibility, safety, or compliance.

## How To Use This

Record the dataset version, polygon input, job ID, and metric definition when comparing results.

## Example

A jurisdiction submits its dataset ID and intersection polygons, then uses the resulting metric map to investigate low-scoring intersections.

## Assistant Guidance

Ask for dataset ID, polygon input, report version, and intended interpretation.

## Related Concepts

- [What is an OS-CONNECT QA/QC report?](../../os-connect/concept/qa-qc-report.md)
- [How does TDEI job processing work?](job-processing.md)
