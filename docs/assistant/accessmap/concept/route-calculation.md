---
title: How does AccessMap calculate accessible routes?
slug: route-calculation
doc_type: concept
questions:
    - How does AccessMap calculate accessible routes?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - routing
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
        - AccessMap's estimated time is a guaranteed travel time.
        - AccessMap route calculations prove that every mapped segment is usable now.
related_pages:
    - mobility-profiles.md
    - profile-responsive-map.md
    - ../../../accessmap/user-manual/route-planning.md
tags:
    - Assistant
---

<!-- @format -->

# How does AccessMap calculate accessible routes?

## Short Answer

AccessMap calculates a pedestrian route from selected waypoints using the selected mobility profile and available network data. The result includes a map route and summary information such as distance, estimated time, elevation, and steepest grades.

## Significance

The calculation makes route comparisons more useful for people whose travel is affected by slope, barriers, surface, streets, or other mapped conditions.

## What This Means

Users set an origin and destination, choose a profile or Custom preferences, and review the route. The Trip Information panel can show experienced elevation gain, total distance, estimated time, and steepest uphill and downhill inclines. Changing preferences can produce a different route.

## What This Does Not Mean

A calculation is not an accessibility audit, a guarantee of current conditions, or a promise that the estimated time will match a particular traveler.

## How To Use This

Review the map, legend, route summary, and Trip Information panel before travel. Compare settings when the first result does not fit the user's needs.

## Example

A user lowers the maximum uphill steepness, recalculates the route, and compares the new distance and elevation profile with the earlier result.

## Assistant Guidance

Ask for the region, endpoints, profile, and relevant preferences when diagnosing a route. Cite the user manual for current interface behavior.

## Related Concepts

- [How do mobility profiles work?](mobility-profiles.md)
- [How does AccessMap respond to mobility profiles?](profile-responsive-map.md)
