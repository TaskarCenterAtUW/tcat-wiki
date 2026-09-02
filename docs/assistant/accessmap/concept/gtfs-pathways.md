---
uid: adab452f-b9b6-4817-b49c-10e7e9ba2baf
title: What is GTFS Pathways?
slug: gtfs-pathways
doc_type: concept
questions:
    - What is GTFS Pathways?
audiences:
    - planner
    - developer
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - gtfs
    - accessibility-data
    - transit
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - GTFS Pathways is a complete sidewalk inventory outside transit facilities.
        - A GTFS feed contains station pathways unless its published files and records show them.
        - Wheelchair accessibility information in GTFS guarantees current physical accessibility.
related_pages:
    - assistant/accessmap/index.md
    - assistant/support/concept/os-connect-vs-gtfs-pathways.md
    - assistant/support/workflow/check-gtfs-feed-pathways.md
    - assistant/support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# What is GTFS Pathways?

## Short Answer

GTFS Pathways is the GTFS component for describing pathways and transfers inside a transit station or stop. It represents entrances, stairs, escalators, elevators, platforms, and other station nodes as a connected network.

It gives transit agencies and trip-planning systems structured information about how riders move through a station, including accessibility details that a general outdoor-focused pedestrian network does not provide by itself.

## Significance

Station layout and accessibility information helps riders determine whether a transfer is feasible before beginning a trip. It also helps trip-planning systems model station interiors instead of treating a station as a single point.

## What This Means

- It describes the internal structure of a transit facility and the connections between its spaces.
- It can include information about movement, transfers, levels, and physical accessibility.
- Coverage and detail depend on what the transit agency publishes in its feed and supporting documentation.

## What This Does Not Mean

- GTFS Pathways is not a statewide sidewalk inventory or a substitute for connected pedestrian data outside the transit facility.
- A populated accessibility field is data about the publisher's reported condition; it is not an independent accessibility certification or guarantee that conditions remain current.
- A GTFS feed contains station pathways only when its published files and records provide them; do not infer this from a station map or stop listing.

## How To Use This

- **Transit agencies:** Publish accurate station, connection, and accessibility information where known.
- **Trip-planning integrators:** Use the pathway network to model station movement and transfers.
- **Planners and advocates:** Combine GTFS Pathways with pedestrian-network data to understand access beyond the station.

## Example

A transit agency models a station with an elevator entrance, an interior elevator node, and bidirectional walkway pathways to a platform. A trip planner uses those records for the station transfer and uses pedestrian data for the surrounding streets.

## Assistant Guidance

Cite this page and the official GTFS reference when explaining the concept. Verify current agency publication status and feed contents rather than inferring them from a station map. Distinguish GTFS Pathways from OS-CONNECT and OSM. If the question concerns legal compliance or a current physical condition, recommend agency or qualified professional verification.

## Related Concepts

- [AccessMap knowledge base](../index.md)
- [How is OS-CONNECT different from GTFS Pathways?](../../cross-platform/concept/os-connect-vs-gtfs-pathways.md)
- [How can I tell whether a GTFS feed includes pathways?](../../support/workflow/check-gtfs-feed-pathways.md)
- [What is the relationship between pedestrian paths in OSM and GTFS Pathways?](../../support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md)
