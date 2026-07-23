---
title: "What attributes are collected for intersections?"
slug: intersection-attributes
doc_type: concept
questions:
    - What attributes are collected for intersections?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - intersections
    - editing
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
        - An IXN score is a legal accessibility determination.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What attributes are collected for intersections?

## Short Answer

OS-CONNECT QA/QC intersection metrics use mapped sidewalk availability, crossings, curb-ramp conditions, connectivity, and crossing distance to estimate modeled intersection traversability.

## Significance

Intersection metrics help identify possible network gaps and data-quality problems at important pedestrian decision points.

## What This Means

The documented IXN score ranges from 0 to 1. A score of 0 indicates no modeled traversable direction, intermediate values indicate some feasible approaches or exits, and 1 indicates all evaluated directions meet the model's criteria.

## What This Does Not Mean

The score represents the modeled dataset and rules. It does not prove that an intersection is safe, accessible to every person, or compliant with ADA requirements.

## How To Use This

Review the score with the map, tags, geometry, and local knowledge. Investigate zero or unexpected scores for missing connections, curb features, or crossings.

## Example

A zero score in a busy intersection may indicate missing curb ramps, a disconnected crossing, or a misclassified feature that needs QA.

## Assistant Guidance

Ask for the report version, score definition, and jurisdiction. Do not convert a modeled score directly into a legal or lived-experience conclusion.

## Related Concepts

- [Why does connectivity depend on geometry?](connectivity-depends-on-geometry.md)
- [What do walkshed metrics represent?](walkshed-metrics.md)
