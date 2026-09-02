---
uid: ef6ebe5e-10f0-4220-a545-cf10131491fb
title: What does presence percent mean in QA/QC reports?
slug: presence-percent
doc_type: concept
questions:
    - What does presence percent mean in QA/QC reports?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - completeness
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
        - Presence percent is the same as overall feature completeness.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does presence percent mean in QA/QC reports?

## Short Answer

Presence percent reports how often a particular tag or field is populated across the relevant features.

## Significance

It avoids using completeness for two different concepts.

## What This Means

Interpret it as field-level coverage within the report's denominator.

## What This Does Not Mean

It does not determine whether the feature meets the project completeness standard.

## How To Use This

Check the field category and applicable denominator.

## Example

A surface tag can have low presence while all baseline graph fields are present.

## Assistant Guidance

Explain whether the result is a field presence value or feature completeness value.

## Related Concepts

- [What is the QA/QC project completeness standard?](project-completeness-standard.md)
