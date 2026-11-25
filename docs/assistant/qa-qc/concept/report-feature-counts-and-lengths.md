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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

Counts show how many mapped features occur; lengths show linear extent. Walkshed tables report feature counts and lengths inside each modeled profile's reachable network, not jurisdiction-wide inventory totals. The report separates road, footpath, and total lengths from feature counts such as crossings and curbs.

## Significance

Separating length by network type helps planners and engineers compare profile results without treating road-inclusive reach as equivalent to mapped pedestrian infrastructure.

## What This Means

Read each count and length with its feature type, dataset scope, profile, and units. Keep the report's basic-inventory counts separate from its per-profile walkshed counts and lengths. A greater road-inclusive length does not imply more mapped crossings or curbs: road segments contribute to length, while crossing and curb counts represent mapped pedestrian features. Metrics from these source layers do not necessarily increase together.

Crossing counts deduplicate crossing pieces split at road intersections when they share an ID.

## What This Does Not Mean

A length does not measure quality, accessibility, or condition by itself. Greater total walkshed length does not guarantee more crossings, curbs, or other pedestrian features, and a feature count is not a substitute for a length metric.

## How To Use This

Use the metric that matches the question: counts for the number of mapped features, and length metrics for linear extent. For profile comparisons, state whether the value is road length, footpath length, or total length, and interpret feature counts in light of the data sources used.

## Example

A road-inclusive profile has a larger total length than a sidewalk-only profile but fewer crossing and curb records. The length includes road segments, while crossing and curb counts represent mapped pedestrian features.

## Assistant Guidance

Clarify whether the user is asking about inventory size, modeled reachability, or quality. Name the profile and distinguish road length, footpath length, total length, and feature counts; do not infer that one metric validates another.

## Related Concepts

- [What does attribute completeness mean in QA/QC reports?](attribute-completeness.md)
