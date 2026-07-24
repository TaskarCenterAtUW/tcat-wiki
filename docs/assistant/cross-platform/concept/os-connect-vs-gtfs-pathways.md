---
title: How is OS-CONNECT different from GTFS-Pathways?
slug: os-connect-vs-gtfs-pathways
doc_type: concept
questions:
    - How is OS-CONNECT different from GTFS-Pathways?
    - Should I use OS-CONNECT or GTFS-Pathways for transit access data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
    - developer
products:
    - OS-CONNECT
    - AccessMap
topics:
    - cross-platform
    - os-connect
    - gtfs
    - accessmap
    - accessibility-data
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-24
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - OS-CONNECT and GTFS-Pathways describe the same geographic scope.
        - OS-CONNECT automatically includes a transit agency's station-internal pathways.
        - GTFS-Pathways is a complete connected pedestrian network for Washington State.
related_pages:
    - assistant/cross-platform/index.md
    - assistant/os-connect/index.md
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/support/workflow/choose-dataset-for-transit-stations.md
tags:
    - Assistant
---

<!-- @format -->

# How is OS-CONNECT different from GTFS-Pathways?

## Short Answer

OS-CONNECT is Washington's connected pedestrian network dataset. GTFS-Pathways is an expansion of the General Transit Feed Specification (GTFS) for describing pathways and transfers inside a transit station or stop.

Use OS-CONNECT for pedestrian-network context outside the station and use a transit agency's GTFS-Pathways data for station-internal connections when the published feed provides those records. A trip-planning analysis may need both datasets because they describe different parts of the journey.

## Significance

The distinction affects dataset selection, routing, and the interpretation of accessibility information. Treating one source as a replacement for the other can omit either the surrounding pedestrian network or the station's internal layout.

## What This Means

- OS-CONNECT represents a connected pedestrian network in Washington State, including sidewalks, crossings, curb ramps, and related pedestrian infrastructure.
- GTFS-Pathways represents connections among transit-facility nodes, such as entrances, platforms, elevators, stairs, escalators, and walkways, through GTFS records such as `pathways.txt`, `levels.txt`, and related `stops.txt` records.
- OS-CONNECT and GTFS-Pathways can be combined at a station entrance, but the connection between datasets must be checked rather than assumed.
- Actual coverage depends on the published dataset or feed version. Inspect the records and documentation before relying on a feature or accessibility value.

## What This Does Not Mean

- OS-CONNECT is not automatically the authoritative source for a transit agency's station-internal pathways.
- GTFS-Pathways is not a complete connected pedestrian network for Washington State or the streets around a station.
- A matching map location does not prove that the two datasets share a routable connection.
- An accessibility attribute in either source does not guarantee that current physical conditions are accessible or unchanged.

## How To Use This

- **Planners and jurisdictions:** Define the geographic boundary of the analysis first. Use GTFS-Pathways for station-internal movement and OS-CONNECT for the surrounding pedestrian approach, then document the feed and dataset versions.
- **Trip-planning integrators and developers:** Inspect the agency feed for `pathways.txt`, `levels.txt`, and the related `stops.txt` hierarchy. Check station entrances and nearby pedestrian features before joining the two networks.
- **Advocates and public users:** Ask which source supports a specific accessibility claim and whether the source is current. For a current physical condition, verify with the transit agency or another qualified source.

## Example

A regional planner evaluates an accessible route from a sidewalk to a station platform. The planner uses OS-CONNECT to examine the sidewalk and crossing leading to the station entrance, then checks the transit agency's GTFS-Pathways records for the entrance, elevator, and platform connections. If either source lacks the needed records, the planner reports the gap instead of assuming that the route is continuous.

## Assistant Guidance

Explain the difference in geographic scope. Verify the current OS-CONNECT release and transit feed contents before answering any specific questions about coverage or accessibility. If the user does not identify a dataset version, station, or jurisdiction when that context affects the answer, ask for it or state the limitation. Do not present either dataset as a legal compliance determination or a guarantee of current physical accessibility.

## Related Concepts

- [Cross-Platform knowledge base](../index.md)
- [OS-CONNECT knowledge base](../../os-connect/index.md)
- [What is GTFS-Pathways?](../../accessmap/concept/gtfs-pathways.md)
- [Which dataset should I use if I need transit-station pathway data?](../../support/workflow/choose-dataset-for-transit-stations.md)
