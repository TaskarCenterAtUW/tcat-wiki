---
uid: eee83492-a21e-4dd3-b964-e617211ac70a
title: Why are z-scores used?
slug: z-score-usage
doc_type: concept
questions:
    - Why are z-scores used?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - graph-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A high z-score proves that a location is unsafe or deficient.
        - Z-scores from different reports are directly comparable.
related_pages:
    - assistant/os-connect/index.md
    - assistant/qa-qc/concept/z-score.md
    - assistant/qa-qc/concept/metric-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# Why are z-scores used?

## Short Answer

Z-scores show how far a value is above or below the average for the report's comparison set. They make relative outliers easier to identify, but their meaning depends on the metric, dataset, and analysis set.

## Significance

Relative scores help reviewers focus on locations that differ from the rest of the analyzed network. They support triage without turning a statistical comparison into a direct safety or compliance judgment.

## What This Means

 - Positive values are above the comparison-set average; negative values are below it.
 - Interpret the score with the underlying metric and comparison population.
 - Use the report's definitions and scope before comparing locations.

## What This Does Not Mean

A z-score is not an absolute condition rating, a legal finding, a field verification, or a guarantee that a high or low value means the same thing in another report.

## How To Use This

Name the report, release, metric, and comparison set. Use a high relative score to prioritize review, then inspect the underlying features and local evidence.

## Example

A tile has a high z-score for a network metric because it stands out from the other tiles in that report. An analyst inspects contributing features before deciding whether action is warranted.

## Assistant Guidance

Do not compare z-scores across different analysis sets without a documented common basis. Cite the report's metric definition and abstain when its population or release is unknown.

## Related Concepts

 - [OS-CONNECT — Assistant Knowledge Base](../index.md)
 - [What does a z-score mean?](../../qa-qc/concept/z-score.md)
 - [What are QA/QC metric boundaries?](../../qa-qc/concept/metric-boundaries.md)
