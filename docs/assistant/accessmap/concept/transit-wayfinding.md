---
title: Can AccessMap support transit wayfinding?
slug: transit-wayfinding
doc_type: concept
questions:
    - Can AccessMap support transit wayfinding?
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
        - AccessMap replaces transit-agency wayfinding or station information.
        - An accessible route guarantees that all transit transfer conditions are usable.
related_pages:
    - assistant/accessmap/concept/transit-pedestrian-routing-integration.md
    - assistant/accessmap/concept/inaccessible-transit-stations.md
    - assistant/accessmap/concept/gtfs-integration.md
tags:
    - Assistant
---

<!-- @format -->

# Can AccessMap support transit wayfinding?

## Short Answer

AccessMap can support the pedestrian portion of transit wayfinding by showing accessibility-aware routes to or from transit locations. Station-internal details and transit-service information may require GTFS Pathways or agency-provided data.

## Significance

People need both a usable pedestrian approach and clear transit information to make a transfer. Separating those layers helps agencies identify missing data and avoid misleading directions.

## What This Means

- Identify the transit stop or station and the pedestrian approach.
- Select a relevant accessibility profile and review the source data.
- Combine route results with current agency wayfinding and station information.

## What This Does Not Mean

AccessMap does not replace an agency's authoritative schedule, station map, or wayfinding system. A route does not guarantee elevators, platforms, transfers, or temporary conditions are usable.

## How To Use This

Use AccessMap for the pedestrian connection, and verify transit-specific information with the responsible agency or feed.

## Example

A rider plans a route to an accessible station entrance, then checks the agency's current service and elevator information before traveling.

## Assistant Guidance

Distinguish pedestrian routing from transit and station data. Cite each source, ask for the station and profile, and abstain when current operational information is missing.

## Related Concepts

- [Transit accessibility and pedestrian routing](transit-pedestrian-routing-integration.md)
- [Inaccessible transit stations](inaccessible-transit-stations.md)
- [GTFS integration](gtfs-integration.md)
