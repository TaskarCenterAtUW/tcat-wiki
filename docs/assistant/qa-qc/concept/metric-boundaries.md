---
uid: 80590023-aa2e-4493-8c2f-26d33f8523dc
title: Why may QA/QC metric areas differ from jurisdiction boundaries?
slug: metric-boundaries
doc_type: concept
questions:
    - Why may QA/QC metric areas differ from jurisdiction boundaries?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - graph-metrics
    - intersections
    - interpretation
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
        - QA/QC metric tiles are administrative boundaries.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Why may QA/QC metric areas differ from jurisdiction boundaries?

## Short Answer

Metric tiles are derived from IXN processing and reused across connectivity metrics; they may not align exactly with jurisdiction boundaries.

## Significance

This reflects the metric's network unit and edge behavior. Shared tiles support comparison across connectivity metrics.

## What This Means

Read the report method and legend before interpreting tile coverage.

## What This Does Not Mean

A tile crossing or stopping short of a boundary is not automatically an error.

## How To Use This

Compare metrics using the shared tile set and inspect edge areas cautiously.

## Example

An intersection-centered tile extends across a city boundary while the analyzed intersection remains the metric's focus.

## Assistant Guidance

Do not describe every tile as one intersection polygon without current method documentation.

## Related Concepts

- [What are QA/QC task-grid overlays?](task-grid-overlays.md)
