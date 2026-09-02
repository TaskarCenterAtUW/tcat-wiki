---
uid: ecc403bc-f209-4462-81bf-6ff233e26e39
title: What does the TDEI Quality Metric Tag job do?
slug: job-quality-metric-tag
doc_type: concept
questions:
    - What does the TDEI Quality Metric Tag job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - data-quality
    - qa-qc
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
        - Tag-quality metrics measure the accuracy of every tag value.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/quality-metric-tag.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Quality Metric Tag job do?

## Short Answer

The Quality Metric Tag job calculates tag-related quality metrics for a dataset.

## Significance

Tag metrics can identify missing or unevenly populated attributes that affect downstream analysis.

## What This Means

Submit the required dataset inputs, track the job, and interpret the output using its metric definition and dataset version.

## What This Does Not Mean

Tag presence or a derived quality metric does not prove that values are accurate, current, or legally sufficient.

## How To Use This

Use results to prioritize data review and compare like-for-like dataset versions.

## Example

A steward identifies low width-tag completeness and plans targeted data collection.

## Assistant Guidance

Distinguish tag presence from tag correctness and compliance.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
