---
title: What attributes are collected for curb ramps?
slug: curb-ramp-attributes
doc_type: concept
questions:
    - What attributes are collected for curb ramps?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - curb-ramps
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
    - assistant/os-connect/concept/curb-ramp-identification.md
    - assistant/os-connect/concept/missing-attribute-values.md
tags:
    - Assistant
---

<!-- @format -->

# What attributes are collected for curb ramps?

## Short Answer

Curb-ramp records may include location, geometry, connections, ramp or crossing type, surface, detectable-warning, slope, condition, or other accessibility fields when those values are collected by the schema and release. The exact attributes and definitions are release-specific.

## Significance

Curb-ramp attributes help describe how a ramp relates to crossings and pedestrian paths and can support screening, routing, and quality review.

## What This Means

Check each field's definition, allowed values, source, collection date, and required or recommended status. Preserve missing or unknown values and distinguish observed attributes from inferred ones.

## What This Does Not Mean

A curb-ramp record may identify its connection to a crossing and include a surface or condition value. Those fields can guide review but do not describe every aspect of the ramp's usability.

## How To Use This

The presence or value of an attribute does not certify design compliance, current condition, or accessibility for every traveler. A missing field does not prove that the feature lacks that characteristic.

## Example

Use the schema documentation for the exact release, retain provenance, compare with local records or field observations, and avoid filling unknown values by assumption.

## Assistant Guidance

Name the field and version being discussed. Do not infer meaning from a label alone, and abstain when the schema or source definition is unavailable.

## Related Concepts

- [How are curb ramps identified?](curb-ramp-identification.md)
- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [Why do some features have missing values?](missing-attribute-values.md)
