---
title: How should municipalities interpret completeness scores?
slug: completeness-score-interpretation
doc_type: concept
questions:
    - How should municipalities interpret completeness scores?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - completeness
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A completeness score measures the accuracy of the recorded attributes.
        - A completeness score establishes ADA compliance.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/qa-qc-report.md
    - assistant/os-connect/concept/completeness-vs-ada-compliance.md
tags:
    - Assistant
---

<!-- @format -->

# How should municipalities interpret completeness scores?

## Short Answer

Completeness scores describe whether expected attributes are present on relevant pedestrian features. They do not establish whether those values are accurate or whether the jurisdiction complies with a regulation.

## Significance

Complete metadata supports more consistent routing, accessibility analysis, and comparison.

## What This Means

QA/QC reports can summarize completeness for sidewalks, crossings, and footways and show tag-level presence for fields such as length, surface, incline, width, IDs, and node references. Use low completeness to identify data-collection priorities.

## What This Does Not Mean

Completeness is not correctness, physical condition, lived experience, or legal compliance. A complete attribute can still contain an incorrect value.

## How To Use This

Read completeness alongside spatial review, source information, validation, and current conditions. Do not compare scores without checking definitions and dataset versions.

## Example

A sidewalk dataset with width values on 90% of features has higher width completeness than one with values on 50%, but the score does not prove that the widths are measured correctly.

## Assistant Guidance

State whether the metric concerns attribute presence or another quality dimension. Abstain from ADA conclusions.

## Related Concepts

- [What is an OS-CONNECT QA/QC report?](qa-qc-report.md)
- [How does completeness differ from ADA compliance?](completeness-vs-ada-compliance.md)
