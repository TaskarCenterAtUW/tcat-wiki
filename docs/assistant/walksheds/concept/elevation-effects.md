---
uid: 8f2fb961-4a5e-4087-a770-4f92a9560a2d
title: How does elevation affect walksheds?
slug: elevation-effects
doc_type: concept
questions:
    - How does elevation affect walksheds?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - elevation
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
    - assistant/walksheds/concept/elevation-routing-effects.md
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/walkshed-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# How does elevation affect walksheds?

## Short Answer

Elevation can affect walksheds by changing segment cost, limiting permitted slopes, or making routes less preferred or unreachable under a selected profile. The effect depends on the elevation source, resolution, network geometry, and routing implementation.

## Significance

A slope can consume more of a travel budget and change the shape of the reachable area, especially for profiles with elevation or mobility constraints.

## What This Means

Check the elevation source, units, profile, slope treatment, maximum cost, and segment geometry. Compare profiles and validate important results locally.

## What This Does Not Mean

A wheelchair-oriented walkshed is smaller uphill than a general pedestrian walkshed under the same travel limit because the modeled elevation cost differs.

## How To Use This

Elevation modeling does not prove that a slope is physically inaccessible or safe. A threshold is not a medical or universal accessibility standard.

## Example

Document elevation and profile assumptions, compare scenarios carefully, retain versions, and state uncertainty in maps and decisions.

## Assistant Guidance

Name the elevation source and calculation rule. Do not infer a person's capability from a modeled slope, and abstain when provenance or profile behavior is unknown.

## Related Concepts

- [How do elevation constraints affect routing?](../../os-connect/concept/elevation-routing-effects.md)
- [What network assumptions are used?](network-assumptions.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
