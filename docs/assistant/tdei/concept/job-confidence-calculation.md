---
title: What does the TDEI Confidence Calculation job do?
slug: job-confidence-calculation
doc_type: concept
questions:
    - What does the TDEI Confidence Calculation job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - data-quality
    - accessibility-metrics
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
        - A confidence score is a probability of physical accessibility.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/confidence-calculation.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Confidence Calculation job do?

## Short Answer

The Confidence Calculation job computes confidence values for a dataset according to the current TDEI processing configuration.

## Significance

Confidence indicators can help users prioritize review and understand uncertainty in processed data.

## What This Means

Submit the required dataset input, track the job, and interpret its result using the job's definition and dataset context.

## What This Does Not Mean

A confidence value is not a guarantee of correctness, safety, accessibility, or legal compliance.

## How To Use This

Record the calculation version, input dataset, output, and interpretation rules.

## Example

A steward uses confidence values to identify features for additional review before publication.

## Assistant Guidance

Ask what the score measures and avoid translating it into a real-world guarantee.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
