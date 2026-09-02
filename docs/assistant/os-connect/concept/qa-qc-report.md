---
uid: 9b05cee8-585e-401e-a8fe-c37b92c2ee26
title: What is the QA/QC report?
slug: qa-qc-report
doc_type: concept
questions:
    - What is the QA/QC report?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - qa-qc
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
        - An OS-CONNECT QA/QC report certifies ADA compliance or real-world accessibility.
        - A single metric fully describes pedestrian network quality.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/completeness-score-interpretation.md
    - assistant/os-connect/concept/walkshed-metrics.md
    - assistant/os-connect/concept/centrality-metrics.md
tags:
    - Assistant
---

<!-- @format -->

# What is the QA/QC report?

## Short Answer

An OS-CONNECT QA/QC report is a standardized analysis of pedestrian-network data for a jurisdiction. It examines completeness, modeled reachability, connectivity, and other indicators of data quality and usefulness.

## Significance

Reports help planners, transportation professionals, jurisdictions, and community members understand whether data is suitable for accessibility, safety, reachability, and infrastructure-planning questions.

## What This Means

Reports can include tag completion, walkshed accessibility, amenity density, intersection traversability, centrality, routing comparisons, maps, histograms, and summary tables. Each section answers a different data or network question.

## What This Does Not Mean

The report evaluates the dataset and its assumptions. It does not replace field validation, professional judgment, legal analysis, or lived experience.

## How To Use This

Read the dataset metadata, report scope, metric definitions, profile assumptions, maps, and caveats together. Use anomalous results to prioritize investigation.

## Example

A planner uses a low-completeness map and a zero-traversability intersection score to identify locations for data review, not to declare a jurisdiction noncompliant.

## Assistant Guidance

Name the metric, dataset version, and report subsection in every answer. Abstain from legal conclusions.

## Related Concepts

- [How should completeness scores be interpreted?](completeness-score-interpretation.md)
- [What do walkshed metrics represent?](walkshed-metrics.md)
- [What do centrality metrics mean?](centrality-metrics.md)
