---
title: How are Walksheds batch outputs handled?
slug: walkshed-batch-output
doc_type: concept
questions:
    - How are Walksheds batch outputs handled?
    - Are Walksheds batch results saved as scenarios?
    - How should I name Walksheds batch inputs for scenario comparison?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - export
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds always provides one combined download for every batch result.
related_pages:
    - walkshed-batch-input.md
    - walkshed-scenarios.md
    - ../workflow/compare-walkshed-profiles.md
    - ../workflow/run-batch-walksheds.md
tags:
    - Assistant
---

<!-- @format -->

# How are Walksheds batch outputs handled?

## Short Answer

Each walkshed calculated from a batch input is saved as a scenario. Use the optional `name` field in the CSV input to identify the location and mobility profile represented by each result.

## Significance

Output handling affects large-area analysis and reproducibility.

## What This Means

When preparing a batch, include a descriptive value in the optional `name` field for each input row. Include both the location and the mobility profile, such as `Location - pedestrian` and `Location - wheelchair`. To compare profiles from the same origin, use matching location names and distinct profile labels while changing the profile settings in the corresponding rows.

After the batch finishes, the results appear in the **Scenarios** tab with their names. Descriptive names make it easier to identify what each scenario models before selecting, comparing, or overlaying the results.

## What This Does Not Mean

The scenario name alone does not document every input setting; retain the CSV and record the profile and other relevant parameters used for each row.

## How To Use This

Before uploading, choose names that distinguish location and mobility profile. After processing, review the scenario names against the input CSV and retain the input alongside any exported or visualized results.

## Example

A batch contains two rows for the same location. The first uses pedestrian profile settings and the name `Location - pedestrian`; the second uses powered-wheelchair profile settings and the name `Location - wheelchair`. Both results are saved as scenarios, and the names identify the profile represented by each scenario in the **Scenarios** tab.

## Assistant Guidance

Explain that batch results are saved as scenarios and that the optional `name` field controls how each result is identified in the **Scenarios** tab.

## Related Concepts

- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
