---
title: How should QA/QC metric coverage be interpreted?
slug: metric-coverage-and-interpretation
doc_type: concept
questions:
    - How should QA/QC metric coverage be interpreted?
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
    - interpretation
    - data-quality
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
        - A report average fully describes the distribution of pedestrian-network conditions.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should QA/QC metric coverage be interpreted?

## Short Answer

Interpret distributions, low-connectivity areas, missing data, and known gaps alongside report averages.

## Significance

Averages can hide concentrated problems or uneven network dependency.

## What This Means

Review maps, distributions, metric definitions, and dataset coverage together.

## What This Does Not Mean

A high average does not prove that every corridor performs well.

## How To Use This

Compare patterns with field knowledge and the report's source context.

## Example

A citywide average masks a low-connectivity corridor that appears clearly on the metric map.

## Assistant Guidance

Ask which distribution and geography the user is interpreting.

## Related Concepts

- [What is the purpose of a QA/QC report?](report-purpose-and-limitations.md)
