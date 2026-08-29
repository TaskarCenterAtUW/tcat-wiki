---
title: What happens when accessibility data is missing?
slug: missing-accessibility-data
doc_type: concept
questions:
    - What happens when accessibility data is missing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - completeness
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Missing accessibility data proves that a feature is inaccessible.
        - AccessMap fills every missing accessibility value automatically.
related_pages:
    - assistant/accessmap/concept/routing-limitations.md
    - assistant/accessmap/concept/accessibility-assumptions.md
    - assistant/accessmap/concept/local-datasets-routing-quality.md
tags:
    - Assistant
---

<!-- @format -->

# What happens when accessibility data is missing?

## Short Answer

When accessibility data are missing, AccessMap's behavior depends on the attribute, selected profile, and current routing implementation. It may use other network information, increase uncertainty, change route selection, or prevent a route from being identified. Missing data are not the same as a confirmed inaccessible condition.

## Significance

Missing attributes can affect people who depend on accessibility-aware routing and can hide gaps in the underlying data. They are a reason to interpret results cautiously and improve coverage.

## What This Means

- Identify which feature, attribute, profile, and dataset version are involved.
- Treat route results as uncertain where important accessibility information is missing; do not assume that every missing field is handled in the same way.
- Verify priority locations and report data gaps through the current feedback process.

## What This Does Not Mean

Missing information does not prove that a curb ramp, accessible surface, or connection is absent. A route result does not guarantee accessibility or compensate for unrecorded conditions.

## How To Use This

State the missing information and its likely effect, then recommend local verification or a data report. Do not silently infer favorable or unfavorable values.

## Example

A route avoids a crossing with no mapped curb-ramp information. The user treats the result as uncertain and checks the crossing rather than concluding that no ramp exists.

## Assistant Guidance

Distinguish missing data from physical absence. Cite the dataset and profile guidance, ask for location and version, and abstain from definitive accessibility claims.

## Related Concepts

- [Routing limitations](routing-limitations.md)
- [Accessibility assumptions](accessibility-assumptions.md)
- [Local datasets and routing quality](local-datasets-routing-quality.md)
