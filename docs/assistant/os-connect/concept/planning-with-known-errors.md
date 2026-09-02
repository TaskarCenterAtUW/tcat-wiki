---
uid: 22396853-14eb-48a6-be82-3bbe5b097778
title: How should agencies treat OS-CONNECT data in planning workflows when known errors exist?
slug: planning-with-known-errors
doc_type: concept
questions:
    - How should agencies treat OS-CONNECT data in planning workflows when known errors exist?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - planning
    - data-quality
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Known errors make every use of OS-CONNECT data invalid.
        - A planning workaround automatically updates OS-CONNECT source data.
related_pages:
    - assistant/os-connect/concept/qa-qc-report.md
    - assistant/os-connect/concept/correction-validation.md
    - assistant/os-connect/concept/correction-propagation.md
tags:
    - Assistant
---

<!-- @format -->

# How should agencies treat OS-CONNECT data in planning workflows when known errors exist?

## Short Answer

Agencies can use OS-CONNECT in planning when known errors are documented, bounded, and considered in the analysis. They should identify affected areas, validate important findings locally, and avoid presenting the output as complete or error-free.

## Significance

Transparent treatment of known errors lets agencies gain value from an imperfect dataset without hiding limitations. It also creates a record for correction, follow-up, and future release comparison.

## What This Means

- Record the dataset version, known error, affected geography, and likely analytical effect.
- Use field checks or authoritative local sources for high-consequence decisions.
- Report corrections through the applicable workflow and revisit the analysis when the data changes.

## What This Does Not Mean

Known errors do not make every use of the dataset invalid, and a released dataset is not automatically complete. A workaround or local overlay does not update OS-CONNECT or its source data by itself.

## How To Use This

State the limitation next to the affected map, metric, or conclusion. Narrow the analysis if necessary, distinguish observed facts from assumptions, and retain the source and version used.

## Example

A planner notes that a known missing sidewalk affects one neighborhood, flags that area in the analysis, verifies priority sites locally, and reports the correction instead of silently treating the dataset as complete.

## Assistant Guidance

Do not decide whether an analysis is valid without knowing its purpose, geography, and error. Cite the dataset and quality notes, explain uncertainty, and abstain from high-stakes conclusions without local verification.

## Related Concepts

- [OS-CONNECT QA/QC report](qa-qc-report.md)
- [Correction validation](correction-validation.md)
- [Correction propagation](correction-propagation.md)
