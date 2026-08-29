---
title: What confidence measures exist?
slug: confidence-measures
doc_type: concept
questions:
    - What confidence measures exist?
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
    - assistant/os-connect/concept/data-collection-history.md
    - assistant/os-connect/concept/planner-data-validation.md
tags:
    - Assistant
---

<!-- @format -->

# What confidence measures exist?

## Short Answer

Confidence measures summarize how strongly a source, processing method, or model supports a mapped feature or attribute. Their meaning depends on the dataset definition, calculation method, version, and intended use.

## Significance

Confidence can help users prioritize review and distinguish uncertain records from records with stronger supporting evidence. It does not eliminate error or uncertainty.

## What This Means

Check what the measure represents, its scale, source, date, thresholds, and whether it applies to a feature, attribute, or analysis. Compare confidence with coverage, known errors, and local evidence.

## What This Does Not Mean

A feature has a lower confidence value because its source imagery is unclear. The value identifies a review candidate; it does not prove that the feature is wrong or inaccessible.

## How To Use This

A confidence value is not an accuracy guarantee, probability of accessibility, or legal certification. Values from different datasets or releases should not be compared without documented compatibility.

## Example

Report the measure and definition with the dataset version, use thresholds cautiously, sample both high- and low-confidence records, and validate important results locally.

## Assistant Guidance

Name the exact confidence field or method. Do not interpret an undocumented score, and abstain when its scale, provenance, or relationship to the decision is unknown.

## Related Concepts

- [How accurate is the data?](data-accuracy.md)
- [How was OS-CONNECT collected?](data-collection-history.md)
- [How should planners validate the data?](planner-data-validation.md)
