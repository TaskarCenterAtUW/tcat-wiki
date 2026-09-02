---
uid: ca15dde9-af31-45f6-9044-21d22c621ffe
title: Can AccessMap integrate with GTFS?
slug: gtfs-integration
doc_type: concept
questions:
    - Can AccessMap integrate with GTFS?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - gtfs
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
        - AccessMap automatically consumes every GTFS feed or file.
        - GTFS data alone provide complete pedestrian accessibility information.
related_pages:
    - assistant/accessmap/concept/transit-pedestrian-routing-integration.md
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# Can AccessMap integrate with GTFS?

## Short Answer

AccessMap may use transit-related data with pedestrian routing when the current integration supports the relevant GTFS feed, stops, or pathway information. Confirm the exact feed, version, and supported files before assuming a connection.

## Significance

Transit stops and pedestrian access are related but different data layers. Clear integration boundaries prevent a schedule feed from being treated as a complete accessible pedestrian network.

## What This Means

- Identify the agency feed, version, stops, and intended analysis.
- Check whether the current workflow supports the relevant GTFS files.
- Combine transit information with pedestrian-network and accessibility data.
- Validate important station or stop connections.

## What This Does Not Mean

GTFS integration does not guarantee accessible transfers, current schedules, station-internal pathways, or route usability. A GTFS feed is not automatically synchronized with OS-CONNECT or OpenStreetMap.

## How To Use This

Use the current feed documentation and AccessMap integration guidance, and distinguish GTFS, GTFS Pathways, and pedestrian-network sources.

## Example

A planner uses a current transit feed to locate stops, then analyzes the pedestrian paths to those stops separately under an accessibility profile.

## Assistant Guidance

Do not claim support for a file or feed without version-specific evidence. Cite the agency feed and product documentation, and abstain when the integration behavior is unclear.

## Related Concepts

- [Transit accessibility and pedestrian routing](transit-pedestrian-routing-integration.md)
- [GTFS Pathways](gtfs-pathways.md)
- [OSM pedestrian paths versus GTFS Pathways](../../support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md)
