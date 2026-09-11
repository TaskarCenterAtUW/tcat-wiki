---
uid: 19b860bf-74a1-4b1e-8d99-c4e8bd164799
title: QA/QC — Assistant Knowledge Base
slug: qa-qc-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the QA/QC knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
    - TDEI
topics:
    - qa-qc
    - tdei-ecosystem
    - accessibility-data
    - os-connect
    - tdei
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - A QA/QC report proves ADA compliance.
        - A quality metric is an absolute field condition rating.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
tags:
    - Assistant
---

<!-- @format -->

# QA/QC — Assistant Knowledge Base

## Short Answer

This section explains QA/QC reports for pedestrian-network data, including report structure, metrics, provenance, limitations, and interpretation. Reports help users identify patterns and review priorities; they do not replace local validation or legal assessment.

## Significance

QA/QC results influence where teams spend review and maintenance effort. Clear interpretation prevents relative metrics or coverage findings from being presented as regulatory conclusions.

## What This Means

 - Identify the report, dataset, release, geography, and analysis set.
 - Read metric definitions and limitations before interpreting a value.
 - Use results to prioritize investigation and quality work.

## What This Does Not Mean

QA/QC does not certify ADA compliance, prove that a feature is safe or unsafe, or establish that a dataset is complete everywhere. A report describes the analyzed data and method.

## How To Use This

Record the report context, inspect the contributing data, and corroborate important findings with current local or field evidence. Ask for the metric and comparison set when a user supplies only a score.

## Example

A jurisdiction sees an outlying network metric, checks the report's definition and provenance, and schedules a local review instead of treating the number as a final compliance finding.

## Assistant Guidance

Cite the report and metric documentation. Abstain when the release, comparison set, method, or intended legal use is unknown.

## Related Concepts

 - [What does a z-score mean?](concept/z-score.md)
 - [What are QA/QC report limitations?](concept/qa-qc-limitations.md)
 - [What is report provenance?](concept/report-provenance.md)
