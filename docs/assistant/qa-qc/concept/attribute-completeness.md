---
uid: b4f6542d-8213-45af-9c68-667e93204aa2
title: What does attribute completeness mean in QA/QC reports?
slug: attribute-completeness
doc_type: concept
questions:
    - What does attribute completeness mean in QA/QC reports?
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
        - A 100 percent attribute-completeness value proves attribute accuracy.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does attribute completeness mean in QA/QC reports?

## Short Answer

Attribute completeness is the share of applicable features with a given tag or attribute populated. Project-required fields, baseline graph fields, and additional accessibility fields may have different meanings.

## Significance

It shows where mapped data has missing values that may limit analysis.

## What This Means

Review project-required, baseline graph, additional accessibility, and conditional fields separately.

## What This Does Not Mean

Completeness measures presence in the dataset, not real-world prevalence, correctness, currency, field accuracy, ADA compliance, or whether every additional accessibility field is populated.

## How To Use This

Compare important attributes with the intended metric and collection scope.

## Example

A required identifier can be complete even when optional surface details are incomplete.

## Assistant Guidance

Do not equate completeness with quality or compliance.

## Related Concepts

- [What are conditional completeness values?](conditional-attribute-completeness.md)
