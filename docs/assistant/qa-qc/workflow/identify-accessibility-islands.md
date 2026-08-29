---
title: How do I use QA/QC Reports to identify accessibility islands?
slug: identify-accessibility-islands
doc_type: workflow
questions:
    - How do I use QA/QC Reports to identify accessibility islands?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - review
    - os-connect
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/qa-qc/concept/accessibility-island.md
    - assistant/qa-qc/concept/connected-pedestrian-graph.md
    - assistant/qa-qc/concept/completeness-vs-accessibility-gaps.md
tags:
    - Assistant
---

<!-- @format -->

# How do I use QA/QC Reports to identify accessibility islands?

## Short Answer

Use the QA/QC report's connectivity or accessibility outputs to identify candidate islands, then inspect the map, graph, profile, threshold, and data coverage before interpreting the result.

## Significance

Islands can focus review on modeled components that do not connect to the broader network under the selected assumptions.

## What This Means

1. Confirm the report, dataset release, geography, profile, and travel threshold.
2. Locate the component or area flagged as an island.
3. Inspect nearby paths, crossings, barriers, endpoints, and missing attributes.
4. Compare with imagery, local records, field observations, or community reports.
5. Record whether the result is a data gap, modeled restriction, or physical condition requiring action.

## What This Does Not Mean

The workflow does not certify accessibility, prove a real-world isolation condition, or automatically identify the responsible agency.

## How To Use This

Keep the report output and validation evidence together, prioritize high-consequence locations, and state uncertainty in any public or planning use.

## Example

A QA/QC map shows a small component near a school. Reviewers find that a crossing edge is absent from the release and submit a specific correction rather than labeling the neighborhood inaccessible.

## Assistant Guidance

Name the report section, profile, threshold, and release. Do not generalize from an island without local review, and abstain when the report's graph assumptions are unavailable.

## Related Concepts

- [What is an accessibility island?](../concept/accessibility-island.md)
- [What does "connected pedestrian graph" mean?](../concept/connected-pedestrian-graph.md)
- [Why can a city have high completeness but still accessibility gaps?](../concept/completeness-vs-accessibility-gaps.md)
