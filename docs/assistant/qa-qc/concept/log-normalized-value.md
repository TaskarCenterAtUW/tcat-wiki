---
title: What does a log-normalized value mean?
slug: log-normalized-value
doc_type: concept
questions:
    - What does a log-normalized value mean in a QA/QC report?
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
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A log-normalized value of 0.5 means half the original network importance.
related_pages:
    - assistant/qa-qc/concept/normalized-value.md
    - assistant/qa-qc/concept/metric-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# What does a log-normalized value mean?

## Short Answer

A log-normalized value applies a logarithmic transformation before rescaling results to a display range such as $0$ to $1$.

## Significance

It keeps patterns visible when a few locations have much larger values than most others.

## What This Means

The displayed value supports relative visual comparison after the transformation.

## What This Does Not Mean

It is not a percentage and does not preserve a direct original-unit interpretation.

## How To Use This

Compare values within the same report and read the metric's method.

## Example

A map can show high-centrality outliers without allowing them to flatten all other colors.

## Assistant Guidance

Explain the transformation before comparing log-normalized results with raw values.

## Related Concepts

- [What does a normalized value mean?](normalized-value.md)
