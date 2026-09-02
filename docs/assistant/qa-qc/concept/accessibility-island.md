---
uid: 48d0ded2-e1d3-4caa-ad78-40041fd7e4d9
title: What is an accessibility island?
slug: accessibility-island
doc_type: concept
questions:
    - What is an accessibility island?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - accessibility-data
    - os-connect
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
    - assistant/qa-qc/workflow/identify-accessibility-islands.md
    - assistant/qa-qc/concept/connected-pedestrian-graph.md
    - assistant/qa-qc/concept/completeness-vs-accessibility-gaps.md
tags:
    - Assistant
---

<!-- @format -->

# What is an accessibility island?

## Short Answer

An accessibility island is a mapped area or network component that appears separated from other accessible or connected components under the selected dataset, profile, and analysis rules.

## Significance

Islands can reveal possible connectivity or data gaps that limit modeled reachability and warrant review.

## What This Means

Interpret the island using the report's graph, profile, threshold, coverage, and data-version assumptions. Inspect nearby crossings, barriers, endpoints, and missing attributes.

## What This Does Not Mean

An accessibility island is not proof that a real neighborhood is inaccessible, nor does its absence prove equitable access or compliance. It may reflect missing data or a modeling rule.

## How To Use This

Use islands as screening indicators, validate important locations locally, and compare results with field evidence and community knowledge before prioritizing action.

## Example

A report identifies a small connected component separated by a missing crossing edge. Reviewers inspect the intersection to determine whether the issue is mapped connectivity or a physical barrier.

## Assistant Guidance

Name the dataset, profile, metric, and report scope. Avoid treating an island as a judgment about residents or places, and abstain when the analysis assumptions are missing.

## Related Concepts

- [How do I use QA/QC Reports to identify accessibility islands?](../workflow/identify-accessibility-islands.md)
- [What does "connected pedestrian graph" mean?](connected-pedestrian-graph.md)
- [Why can a city have high completeness but still accessibility gaps?](completeness-vs-accessibility-gaps.md)
