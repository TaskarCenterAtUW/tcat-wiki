---
uid: f03df76b-2445-4429-b3ca-79a67850adac
title: What kinds of errors are most common?
slug: common-errors
doc_type: concept
questions:
    - What kinds of errors are most common?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
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
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/data-accuracy.md
    - assistant/os-connect/concept/disconnected-sidewalk-identification.md
    - assistant/os-connect/concept/missing-attribute-values.md
tags:
    - Assistant
---

<!-- @format -->

# What kinds of errors are most common?

## Short Answer

Common errors can include missing or outdated features, disconnected or misaligned geometry, incorrect feature types, incomplete accessibility attributes, duplicate records, incorrect relationships, and source or version confusion. The pattern varies by dataset and location.

## Significance

Knowing likely error types helps reviewers sample data efficiently and helps reporters provide evidence that can be investigated.

## What This Means

Check geometry, connectivity, feature classification, attributes, dates, provenance, coverage, and relationships. Compare representative records with imagery, local records, field observations, or other documented sources.

## What This Does Not Mean

An apparent error is not necessarily an error without knowing the source, schema, release, and intended representation. A common error list is not a substitute for a dataset-specific quality assessment.

## How To Use This

Record the exact location or identifier, observed problem, expected value, source version, evidence, and likely effect. Submit the issue through the current documented channel and retain the report for follow-up.

## Example

A sidewalk appears to stop at an intersection, but review shows that a crossing feature is missing rather than the sidewalk itself. The report identifies the missing relationship and the release examined.

## Assistant Guidance

Name the observed error and evidence rather than claiming a general accuracy rate. Cite the dataset and validation guidance, and abstain when the source or representation cannot be identified.

## Related Concepts

- [How accurate is the data?](data-accuracy.md)
- [How are disconnected sidewalks identified?](disconnected-sidewalk-identification.md)
- [Why do some features have missing values?](missing-attribute-values.md)
