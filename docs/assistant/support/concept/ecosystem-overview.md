---
uid: 6a494c93-24a2-4b28-93a3-3a4d00f271e3
title: What is the difference between TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex?
slug: ecosystem-overview
doc_type: concept
questions:
    - What is the difference between TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - tdei-ecosystem
    - overview
    - os-connect
    - accessmap
    - walksheds
    - tdei
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
        - TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex are interchangeable products or datasets.
        - A dataset or tool in this ecosystem automatically updates every other one.
related_pages:
    - assistant/support/concept/tdei-os-connect-osm-differences.md
    - assistant/cross-platform/concept/os-connect-vs-gtfs-pathways.md
    - assistant/tdei/concept/file-formats.md
    - assistant/accessmap/concept/accessmap.md
    - assistant/walksheds/concept/walkshed.md
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between TDEI, OS-CONNECT, OpenSidewalks, OpenStreetMap, AccessMap, Walksheds, GTFS, GTFS Pathways, and GTFS-Flex?

## Short Answer

These names refer to different layers of a transportation-accessibility ecosystem: TDEI manages data and releases, OS-CONNECT provides pedestrian-network data and viewing, OpenSidewalks defines pedestrian-network data structures, OpenStreetMap is a collaborative geographic database, AccessMap performs accessibility-aware routing, Walksheds analyzes reachable areas, and GTFS, GTFS Pathways, and GTFS-Flex describe transit data or services.

## Significance

Clear boundaries help agencies choose the right source, tool, or format and avoid assuming that related systems share identical data or responsibilities.

## What This Means

- Match the question to the relevant layer: storage and release, schema, map data, routing, reachability, or transit service.
- Check the current dataset, version, publisher, and intended use.
- Treat conversions and integrations as explicit workflows rather than automatic synchronization.

## What This Does Not Mean

- The products and formats are not interchangeable.
- Similar names or geometry do not prove shared ownership, synchronization, or authority.
- A tool's output does not automatically establish legal, safety, or accessibility compliance.

## How To Use This

Start with the user's outcome, then explain only the relevant products and boundaries. Cite each source or release separately when comparing them.

## Example

An agency needs station-internal pathways and surrounding sidewalk access. Staff distinguish GTFS Pathways from OS-CONNECT, then identify which release and routing or GIS workflow is needed for each.

## Assistant Guidance

Use the narrowest supported comparison, avoid claiming current integrations without evidence, and abstain when the product, dataset, or version is unclear.

## Related Concepts

- [TDEI, OS-CONNECT, and OSM differences](tdei-os-connect-osm-differences.md)
- [OS-CONNECT versus GTFS Pathways](../../cross-platform/concept/os-connect-vs-gtfs-pathways.md)
- [TDEI file formats](../../tdei/concept/file-formats.md)
