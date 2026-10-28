---
uid: 7d259a83-dc6a-4470-8042-e7adfbfaed3f
title: Why does AccessMap choose longer routes?
slug: longer-route-selection
doc_type: concept
questions:
    - Why does AccessMap choose longer routes?
    - Why might AccessMap choose a longer route?
audiences:
    - public
    - advocate
products:
    - AccessMap
topics:
    - accessmap
    - routing
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/cross-platform/concept/accessmap-routing.md
    - assistant/accessmap/concept/mobility-profiles.md
tags:
    - Assistant
---

<!-- @format -->

# Why does AccessMap choose longer routes?

## Short Answer

AccessMap can return a longer route than a shortest-distance route because the selected mobility profile and preferences affect route selection. A longer route may reflect modeled tradeoffs such as avoiding steep inclines, but route length alone does not establish that the result is correct.

## Significance

A route that differs from another router may reflect different network data or preferences, but the difference alone does not establish that the result is intended or rule out a data or routing problem.

## What This Means

The selected profile and preferences can change which route AccessMap returns. Compare routes using the same region, origin, destination, and profile settings, then review the route summary and Trip Information details, including distance, estimated time, and steepest inclines.

## What This Does Not Mean

- Not proof that a shorter path is illegal or impassable for everyone.
- Not proof that the route is correct or free of data and routing problems merely because a different router returns another path.

## How To Use This

Check the region, origin, destination, active profile, and preferences before comparing routes. If the route or mapped information still appears inaccurate, use AccessMap's feature or direction-step feedback rather than assuming every difference is intended.

## Example

Two routes use the same origin and destination, but AccessMap's selected profile avoids a steep segment, producing a longer path. This may reflect the profile's routing tradeoff; compare the settings and route details before deciding whether the result needs to be reported.

## Assistant Guidance

Explain that profile and preference settings can change the route and that distance alone does not determine whether a route suits a user. Do not assume a different or longer route is necessarily expected or correct; ask for comparable route inputs, cite current route-planning and profile guidance, and suggest feedback for suspected data or routing problems.

## Related Concepts

- [AccessMap routing (concept)](route-calculation.md)
- [How do mobility profiles work?](mobility-profiles.md)
- [AccessMap route planning manual](../../../accessmap/user-manual/route-planning.md)
