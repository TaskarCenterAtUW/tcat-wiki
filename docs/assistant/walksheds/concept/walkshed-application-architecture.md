---
title: How is the Walksheds tool organized?
slug: walkshed-application-architecture
doc_type: concept
questions:
    - How is the Walksheds tool organized?
    - How does Walksheds use TDEI datasets?
audiences:
    - planner
    - developer
    - jurisdiction
products:
    - Walksheds
    - TDEI
topics:
    - walksheds
    - tdei
    - tdei-ecosystem
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds edits automatically update the source TDEI dataset.
related_pages:
    - walkshed.md
    - os-connect-data-usage.md
    - ../index.md
tags:
    - Assistant
---

<!-- @format -->

# How is the Walksheds tool organized?

## Short Answer

Walksheds is a browser-based analysis tool that loads a TDEI pedestrian network, builds a routing graph, applies preferences and cost functions, and produces walkshed results, scenarios, statistics, and optional edits.

## Significance

The architecture separates source data, router construction, analysis assumptions, and saved outputs.

## What This Means

The tool uses Datasets, Walkshed Preferences, Edits, and Batch tabs. A selected primary and optional extension dataset feed a router. The origin, budget, profile, departure time, and cost function determine the analysis.

## What This Does Not Mean

A local feature edit or saved scenario is not automatically a published source-data change.

## How To Use This

Record dataset versions, extension layers, preferences, cost functions, and scenario names when reproducing results.

## Example

A planner loads an OS-CONNECT dataset, overlays an extension dataset, builds a router, and compares two saved profile scenarios.

## Assistant Guidance

Ask which layer is involved: source dataset, router, preferences, edit, scenario, or batch output.

## Related Concepts

- [What is a walkshed?](walkshed.md)
- [How do I select a walkshed dataset?](../workflow/select-walkshed-dataset.md)
