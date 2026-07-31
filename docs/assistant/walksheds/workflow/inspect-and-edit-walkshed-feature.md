---
title: How do I inspect and edit a Walksheds feature?
slug: inspect-and-edit-walkshed-feature
doc_type: workflow
questions:
    - How do I inspect and edit a Walksheds feature?
    - How do I test a hypothetical infrastructure improvement?
audiences:
    - planner
    - developer
    - jurisdiction
products:
    - Walksheds
topics:
    - walksheds
    - editing
    - accessibility-metrics
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A Walksheds feature edit automatically changes the source TDEI dataset.
related_pages:
    - ../concept/walkshed-edit-limitations.md
    - ../concept/walkshed-edit-history.md
    - ../../../walksheds/user-manual/edits.md
tags:
    - Assistant
---

<!-- @format -->

# How do I inspect and edit a Walksheds feature?

## Short Answer

Select a feature, inspect its attributes, choose **Edit Feature**, save the change, and review the recalculated walkshed. Use the Edits tab to inspect or remove local edits.

## Significance

Feature edits can test data corrections or hypothetical infrastructure changes within an analysis.

## What This Means

A selected feature can become a new origin or destination, or its attributes can be edited. Saving recalculates the walkshed. The Edits tab lists modified attributes and can restore original values.

## What This Does Not Mean

A local edit is not automatically a published change to the TDEI source dataset.

## How To Use This

Label edits as correction tests or hypothetical scenarios, record the original and changed values, and remove them when they no longer apply.

## Example

A planner marks a crossing as ramped to estimate the effect of a possible improvement, then removes the edit after comparing results.

## Assistant Guidance

Ask whether the edit is intended as source correction or hypothetical modeling. Do not claim that the source dataset changed.

## Related Concepts

- [How do I model an infrastructure change?](model-infrastructure-change.md)
- [What are Walksheds scenarios?](../concept/walkshed-scenarios.md)
