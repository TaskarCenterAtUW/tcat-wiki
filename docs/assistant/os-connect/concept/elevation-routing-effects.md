---
title: How do elevation constraints affect routing?
slug: elevation-routing-effects
doc_type: concept
questions:
    - How do elevation constraints affect routing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - elevation
    - routing
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
    - assistant/os-connect/concept/routing-assumptions.md
    - assistant/os-connect/concept/walkshed-metrics.md
    - assistant/os-connect/concept/field-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How do elevation constraints affect routing?

## Short Answer

Elevation constraints can affect modeled routing by increasing travel cost, limiting a profile's permitted slope, or making some paths less preferred or unreachable. The effect depends on the elevation source, network geometry, profile, and routing implementation.

## Significance

Slope can materially affect travel for people using wheelchairs, mobility devices, or who have other mobility considerations. Elevation data also contain measurement and resolution uncertainty.

## What This Means

Check the elevation source, units, profile settings, segment geometry, and treatment of uphill and downhill travel. Compare modeled results with route summaries and local conditions when important.

## What This Does Not Mean

An elevation constraint does not establish that a path is physically inaccessible or safe. A route that satisfies a modeled threshold does not guarantee usability for a particular traveler.

## How To Use This

Document the profile and threshold, compare alternatives, retain the dataset and elevation versions, and validate high-consequence routes locally.

## Example

A wheelchair-oriented analysis avoids a steep segment and selects a longer route. The result is explained as a modeled preference based on the selected threshold, not as a universal accessibility judgment.

## Assistant Guidance

Name the routing implementation and assumptions. Do not infer a traveler's ability from a slope value, and abstain when elevation provenance or profile behavior is unknown.

## Related Concepts

- [What routing assumptions are used?](routing-assumptions.md)
- [What do walkshed metrics represent?](walkshed-metrics.md)
- [How should field validation be incorporated?](field-validation.md)
