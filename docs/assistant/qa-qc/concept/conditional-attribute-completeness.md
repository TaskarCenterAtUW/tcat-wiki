---
uid: e0820a0e-84c0-4e38-99b6-bab0c16e2fa3
title: Why can conditional attribute completeness be low?
slug: conditional-attribute-completeness
doc_type: concept
questions:
    - Why can conditional attribute completeness be low?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - data-quality
    - completeness
    - interpretation
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
        - A low conditional-field percentage always indicates poor data collection.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Why can conditional attribute completeness be low?

## Short Answer

Some attributes apply only when another tag has a particular value. Their completeness should be interpreted over the applicable subset.

## Significance

A raw percentage can mislead when the field is irrelevant to most features.

## What This Means

Check the field's conditions and denominator before judging the result. Conditional or additional fields should not automatically be treated as failures of the project completeness standard.

## What This Does Not Mean

A low overall percentage does not necessarily mean applicable features are missing values.

## How To Use This

Use the schema and report methodology to identify conditional fields.

## Example

Tactile-paving color may apply only where tactile paving exists.

## Assistant Guidance

Ask whether the report calculates conditional completeness and do not infer failure from raw percentages.

## Related Concepts

- [What does attribute completeness mean in QA/QC reports?](attribute-completeness.md)
