---
uid: 3d2b9770-ef79-4e85-91f8-1468def552d1
title: How are slopes incorporated into routing?
slug: slope-routing
doc_type: concept
questions:
    - How are slopes incorporated into routing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - slope
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
    do_not_claim:
        - A modeled slope value proves that a route is usable for every traveler.
        - AccessMap's slope treatment replaces field measurement or engineering review.
related_pages:
    - assistant/accessmap/concept/steep-slopes-effect.md
    - assistant/accessmap/concept/avoid-steep-slopes.md
    - assistant/accessmap/concept/route-calculation.md
tags:
    - Assistant
---

<!-- @format -->

# How are slopes incorporated into routing?

## Short Answer

AccessMap can incorporate mapped or modeled slope information into route calculation and profile preferences. Steep segments may receive a higher cost or be avoided when the selected profile calls for that behavior.

## Significance

Slope can materially change route choice for people who use mobility devices or have limited endurance. Explaining its treatment makes route differences more understandable.

## What This Means

- Identify the profile and slope preference used.
- Check whether slope data are available and current for the area.
- Compare the modeled result with local conditions when the trip matters.

## What This Does Not Mean

Slope treatment is not a complete accessibility assessment. A route with a lower modeled slope can still have barriers, and a missing slope value does not prove that the segment is flat.

## How To Use This

State that slope is one route factor among several. Cite current AccessMap guidance and avoid presenting a route result as a field or engineering measurement.

## Example

A user selects a profile that avoids steep slopes, and AccessMap chooses a longer route with a lower modeled slope. The user verifies the route before relying on it.

## Assistant Guidance

Explain the profile-dependent model, cite the relevant documentation, and abstain when the slope source, threshold, or product version is unknown.

## Related Concepts

- [How steep slopes affect route selection](steep-slopes-effect.md)
- [Avoid steep slopes](avoid-steep-slopes.md)
- [How AccessMap calculates routes](route-calculation.md)
