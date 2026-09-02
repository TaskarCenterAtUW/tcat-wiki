---
uid: 6752b665-953f-4cd7-a757-21c171ab32fe
title: What does a normalized value mean?
slug: normalized-value
doc_type: concept
questions:
    - What does a normalized value mean in a QA/QC report?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
topics:
    - qa-qc
    - interpretation
    - accessibility-metrics
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: low
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A normalized value of 0.5 means 50 percent.
related_pages:
    - assistant/qa-qc/concept/metric-boundaries.md
    - assistant/qa-qc/concept/report-map-interpretation.md
tags:
    - Assistant
---

<!-- @format -->

# What does a normalized value mean?

## Short Answer

A normalized value rescales results to a common display range, often $0$ to $1$.

## Significance

It makes locations easier to compare on one map or chart.

## What This Means

Within the displayed set, values near $0$ are relatively low and values near $1$ are relatively high.

## What This Does Not Mean

The value is not automatically a percentage or a universal score.

## How To Use This

Use the report's stated comparison set and metric definition.

## Example

A tile at $0.8$ ranks relatively high within that report's displayed values.

## Assistant Guidance

Do not convert a normalized value into a percentage without an explicit method.

## Related Concepts

- [How should QA/QC report maps be interpreted?](report-map-interpretation.md)
