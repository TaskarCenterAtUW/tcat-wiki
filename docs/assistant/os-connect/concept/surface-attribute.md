---
title: 'What does "surface" mean?'
slug: surface-attribute
doc_type: concept
questions:
    - What does "surface" mean?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - editing
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
    - assistant/os-connect/concept/sidewalk-attributes.md
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
    - assistant/os-connect/concept/missing-attribute-values.md
tags:
    - Assistant
---

<!-- @format -->

# What does "surface" mean?

## Short Answer

The `surface` attribute describes the recorded surface material or condition category for a pedestrian feature according to the applicable schema. Its allowed values and meaning depend on the dataset and release.

## Significance

Surface information can help users interpret a feature and can inform routing, accessibility analysis, quality review, or field-prioritization questions.

## What This Means

Check the exact field definition, value domain, source, collection date, and whether the value is observed, inferred, or transformed. Preserve unknown values and validate important conditions locally.

## What This Does Not Mean

`surface` does not by itself describe smoothness, maintenance, safety, accessibility for every traveler, or current condition. A missing surface value does not prove that the feature lacks a surface type.

## How To Use This

Use the schema for the exact release, do not infer values from nearby features, and pair the field with relevant geometry, slope, width, barrier, and local evidence.

## Example

A sidewalk has a recorded surface category but no condition or date information. An analyst uses it as one input and avoids treating it as a current usability judgment.

## Assistant Guidance

Name the schema and value, cite the release, and abstain when the field definition or source is unknown.

## Related Concepts

- [What attributes are collected for sidewalks?](sidewalk-attributes.md)
- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [Why do some features have missing values?](missing-attribute-values.md)
