---
uid: 0f57f435-7da0-42f0-b876-fb32ffc6ff31
title: Why do QA/QC reports show feature counts and lengths?
slug: report-feature-counts-and-lengths
doc_type: concept
questions:
    - Why do QA/QC reports show feature counts and lengths?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - accessibility-metrics
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A feature count alone describes the operational extent of a pedestrian network.
        - A higher total walkshed length guarantees higher crossing or curb counts.
related_pages:
    - assistant/qa-qc/concept/report-data-sources.md
    - assistant/qa-qc/concept/walkshed-profile-comparison.md
    - assistant/qa-qc/concept/report-purpose-and-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why do QA/QC reports show feature counts and lengths?

## Short Answer

Counts show how many mapped features exist; length metrics show linear extent. QA/QC reports can present road length, footpath length, and total length for each walkshed profile, alongside feature counts such as crossings and curbs.

## Significance

Separating length by network type helps planners and engineers compare profile results without treating road-inclusive reach as equivalent to mapped pedestrian infrastructure.

## What This Means

Read each count and length with its feature type, dataset scope, profile, and units. A road-inclusive profile can have greater total length while showing fewer mapped crossings or curbs: road data may contribute segments without carrying the crossing and curb details present in sidewalk or OpenSidewalks data. The report can combine these different source layers, so the metrics do not necessarily increase together.

## What This Does Not Mean

A length does not measure quality, accessibility, or condition by itself. Greater total walkshed length does not guarantee more crossings, curbs, or other pedestrian features, and a feature count is not a substitute for a length metric.

## How To Use This

Use the metric that matches the question: counts for the number of mapped features, and length metrics for linear extent. For profile comparisons, state whether the value is road length, footpath length, or total length, and interpret feature counts in light of the data sources used.

## Example

A road-inclusive profile has a larger total length than a sidewalk-only profile but fewer crossing and curb records. The length includes road segments, while those segments may not carry the same mapped crossing and curb details as the pedestrian-network data.

## Assistant Guidance

Clarify whether the user is asking about inventory size, modeled reachability, or quality. Name the profile and distinguish road length, footpath length, total length, and feature counts; do not infer that one metric validates another.

## Related Concepts

- [What does attribute completeness mean in QA/QC reports?](attribute-completeness.md)
