---
uid: def5bb9e-356c-4676-9b3a-2ad468262d32
title: How are inaccessible transit stations represented?
slug: inaccessible-transit-stations
doc_type: concept
questions:
    - How are inaccessible transit stations represented?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - transit
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
        - A station shown as inaccessible has no possible accessible path.
        - A station not flagged as inaccessible is guaranteed to be accessible.
related_pages:
    - assistant/accessmap/concept/transit-wayfinding.md
    - assistant/accessmap/concept/transit-pedestrian-routing-integration.md
    - assistant/accessmap/concept/gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# How are inaccessible transit stations represented?

## Short Answer

AccessMap may represent a transit station as difficult or unavailable for a selected accessibility profile when the pedestrian network, station connection, or relevant attributes do not support a route. The result is data- and profile-dependent.

## Significance

Station access affects whether a transit trip can be completed, but a map representation may not include all entrances, elevators, platforms, or temporary conditions.

## What This Means

- Identify the station, entrance, profile, dataset, and transit feed.
- Check the pedestrian route and station-specific pathway information separately.
- Verify current elevator, closure, and access information with the agency.

## What This Does Not Mean

An inaccessible result does not prove that no accessible route exists, and an available result does not guarantee that the station is currently usable. It is not an ADA determination.

## How To Use This

Use the result to identify verification needs and explain which layer caused the limitation. Cite the pedestrian and agency sources.

## Example

A route cannot reach a station entrance under a selected profile, so the user checks another entrance and the agency's current elevator status before traveling.

## Assistant Guidance

Do not provide definitive station-access claims from the map alone. Ask for the station, profile, version, and current conditions, and direct urgent riders to official agency information.

## Related Concepts

- [Transit wayfinding](transit-wayfinding.md)
- [Transit accessibility integration](transit-pedestrian-routing-integration.md)
- [GTFS Pathways](gtfs-pathways.md)
