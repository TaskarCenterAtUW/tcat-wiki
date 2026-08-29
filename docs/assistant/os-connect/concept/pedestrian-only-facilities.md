---
title: How are pedestrian-only facilities handled?
slug: pedestrian-only-facilities
doc_type: concept
questions:
    - How are pedestrian-only facilities handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - accessibility-data
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
    - assistant/os-connect/concept/included-infrastructure-types.md
    - assistant/os-connect/concept/excluded-infrastructure-types.md
    - assistant/os-connect/concept/private-facilities.md
tags:
    - Assistant
---

<!-- @format -->

# How are pedestrian-only facilities handled?

## Short Answer

Pedestrian-only facilities are handled according to the dataset's feature definitions, geometry, access rules, source coverage, and release. They may include paths, plazas, trails, walkways, or other features not intended for motor vehicles when those features are in scope.

## Significance

Pedestrian-only features can be important links in a connected network and may provide access that roadway-centered data misses.

## What This Means

Check the feature type, public or restricted access, geometry, connections, surface, slope, source date, and schema. Validate whether the feature is open and usable for the intended trip.

## What This Does Not Mean

Pedestrian-only does not mean universally accessible, public, safe, current, or connected. A missing feature does not prove that it does not exist.

## How To Use This

Include relevant facilities in analysis only when their access and representation are understood. Label uncertain or private features and report specific coverage or connection issues.

## Example

A pedestrian plaza connects two sidewalks in the dataset, but current access is restricted during an event. The analyst checks local information before using it in a time-sensitive route or walkshed.

## Assistant Guidance

Ask for the facility type, access conditions, release, and intended use. Do not infer accessibility from the pedestrian-only label and abstain when scope or access rules are unknown.

## Related Concepts

- [What kinds of pedestrian infrastructure are included?](included-infrastructure-types.md)
- [What kinds of pedestrian infrastructure are not included?](excluded-infrastructure-types.md)
- [How are private facilities handled?](private-facilities.md)
