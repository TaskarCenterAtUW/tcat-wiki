---
title: How does transit accessibility integrate with pedestrian routing?
slug: transit-pedestrian-routing-integration
doc_type: concept
questions:
    - How does transit accessibility integrate with pedestrian routing?
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
    do_not_claim:
        - Transit data automatically provide complete pedestrian accessibility information.
        - A connected transit and pedestrian route guarantees an accessible transfer.
related_pages:
    - assistant/accessmap/concept/gtfs-integration.md
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/accessmap/concept/inaccessible-transit-stations.md
tags:
    - Assistant
---

<!-- @format -->

# How does transit accessibility integrate with pedestrian routing?

## Short Answer

Transit accessibility integrates pedestrian routing with transit stops, stations, and service information so users can consider the walk to, from, or between transit locations. The pedestrian and transit layers remain distinct and must be interpreted together.

## Significance

An accessible transit trip depends on both service information and the physical connections used to reach it. Integration exposes gaps that either layer alone can miss.

## What This Means

- Identify the transit feed, pedestrian dataset, station or stop, and profile.
- Join or compare the layers using documented identifiers and geometry.
- Verify transfers, entrances, elevators, crossings, and current service conditions.

## What This Does Not Mean

Integration does not make either source complete or current, and a connected model does not guarantee a usable transfer. GTFS Pathways and general pedestrian data are not interchangeable.

## How To Use This

Document the source versions and assumptions, then pair modeled results with agency information and local verification.

## Example

A rider's trip combines a GTFS stop with an AccessMap pedestrian route to the station entrance, while station-internal pathways are checked through the agency's current information.

## Assistant Guidance

Keep transit and pedestrian claims separate, cite each source, and abstain when identifiers, versions, or current operational conditions are missing.

## Related Concepts

- [GTFS integration](gtfs-integration.md)
- [GTFS Pathways](gtfs-pathways.md)
- [Inaccessible transit stations](inaccessible-transit-stations.md)
