---
uid: 4d328378-d4be-418a-a4c0-22eff37413bf
title: What attributes are collected for sidewalks?
slug: sidewalk-attributes
doc_type: concept
questions:
    - What attributes are collected for sidewalks?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - sidewalks
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
    - assistant/os-connect/concept/required-vs-recommended-attributes.md
    - assistant/os-connect/concept/sidewalk-street-name-association.md
tags:
    - Assistant
---

<!-- @format -->

# What attributes are collected for sidewalks?

## Short Answer

Sidewalk records may include geometry, width, surface, slope, access, street-name relationships, barriers, and other fields defined by the schema and release. The exact attributes and value definitions are release-specific.

## Significance

Attributes add context to sidewalk geometry and can support routing, quality review, planning, and data exchange.

## What This Means

Check the schema, feature type, source, date, required or recommended status, and missing-value convention. Preserve unknown values and distinguish observed, inferred, and transformed fields.

## What This Does Not Mean

An attribute does not certify a sidewalk, prove accessibility, or guarantee current conditions. A missing value does not prove the characteristic is absent.

## How To Use This

Use the exact release documentation, retain provenance, validate important features locally, and avoid filling fields by assumption.

## Example

A sidewalk has separate geometry and a width value, but its surface condition is unknown. An analyst uses the known fields for screening and identifies the unknown for review.

## Assistant Guidance

Name the field, schema, source, and version. Do not infer meaning from labels alone and abstain when definitions are unavailable.

## Related Concepts

- [Pedestrian feature attributes](pedestrian-feature-attributes.md)
- [Required versus recommended attributes](required-vs-recommended-attributes.md)
- [Sidewalk street-name association](sidewalk-street-name-association.md)
