---
uid: 6d618115-a9d1-4ce0-9c72-ac4751cd4dc8
title: "How does attribute presence differ from feature completeness?"
slug: attribute-presence-vs-feature-completeness
doc_type: concept
questions:
    - How does attribute presence differ from feature completeness?
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
    - interpretation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-23
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Attribute presence percentage measures how many real-world features have that attribute.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How does attribute presence differ from feature completeness?

## Short Answer

Attribute presence measures whether a field is populated on features in the dataset. Feature completeness measures whether a feature meets the project's required standard.

## Significance

The two percentages answer different questions.

## What This Means

A field can be present on every dataset feature without proving that every real-world feature has been mapped.

## What This Does Not Mean

Presence is not a count of real-world infrastructure and is not ADA compliance.

## How To Use This

Read the denominator and project standard before interpreting a percentage.

## Example

A tactile-paving field is present on all mapped curb nodes, even though not all real-world curbs are in the dataset.

## Assistant Guidance

Distinguish dataset coverage from real-world prevalence.

## Related Concepts

- [What does presence percent mean in QA/QC reports?](presence-percent.md)
