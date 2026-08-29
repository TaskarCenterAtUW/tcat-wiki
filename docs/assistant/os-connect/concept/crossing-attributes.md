---
title: What attributes are collected for crossings?
slug: crossing-attributes
doc_type: concept
questions:
    - What attributes are collected for crossings?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - crossings
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
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
    - assistant/os-connect/concept/curb-ramp-attributes.md
    - assistant/os-connect/concept/intersection-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# What attributes are collected for crossings?

## Short Answer

Crossing records may include fields describing location, geometry, crossing type, connections, control or signal information, surface or access conditions, and relationships to nearby pedestrian features. The exact fields and allowed values depend on the OpenSidewalks schema and dataset release.

## Significance

Crossing attributes help users and network processes distinguish a pedestrian movement across a roadway from the sidewalks or paths that approach it.

## What This Means

Read the field definitions and release metadata together. Check whether a value is observed, inferred, required, optional, or missing, and preserve unknown values instead of filling them by assumption.

## What This Does Not Mean

A crossing has geometry connecting two sidewalk approaches and a field describing its crossing type. An analyst can use that information to screen connectivity, but still needs local evidence for current accessibility.

## How To Use This

The presence of a crossing record does not prove that the crossing is safe, accessible, signalized, or usable for every traveler. A list of fields is not a complete inventory of all crossing conditions.

## Example

Use the exact schema documentation for the release, record the source and version, and validate important crossings with imagery, local records, or field observations.

## Assistant Guidance

Name the attribute and its definition rather than inferring meaning from a field name. Abstain when the release, schema, or value domain is not known.

## Related Concepts

- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [What attributes are collected for curb ramps?](curb-ramp-attributes.md)
- [What attributes are collected for intersections?](intersection-attributes.md)
