---
uid: 07559100-b9f0-4a58-af67-e55e76e023bc
title: What should agencies do if GTFS Pathways data are missing but pedestrian data exist in OSM or OS-CONNECT?
slug: fallback-when-gtfs-pathways-missing
doc_type: concept
questions:
    - What should agencies do if GTFS Pathways data are missing but pedestrian data exist in OSM or OS-CONNECT?
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
    - gtfs
    - planning
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
        - OSM or OS-CONNECT data automatically replace missing GTFS Pathways data.
        - Surrounding pedestrian data provide all station-internal pathway semantics.
related_pages:
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md
    - assistant/os-connect/concept/gtfs-pathways-generation.md
tags:
    - Assistant
---

<!-- @format -->

# What should agencies do if GTFS Pathways data are missing but pedestrian data exist in OSM or OS-CONNECT?

## Short Answer

When GTFS Pathways data are missing, agencies can use OSM or OS-CONNECT for surrounding pedestrian context while separately confirming station-internal pathways with the transit agency. Do not treat either source as an automatic substitute for a current GTFS Pathways feed.

## Significance

The fallback distinction prevents incomplete station information from being presented as a complete transit pathway network. It also gives agencies a practical way to continue surrounding-access analysis while the feed question is resolved.

## What This Means

- Check the agency's current official feed for `pathways.txt`.
- Use OSM or OS-CONNECT for documented surrounding pedestrian context.
- Identify missing station-internal details and ask the agency about its authoritative source.
- Record sources and limitations in the analysis.

## What This Does Not Mean

Pedestrian data do not automatically contain entrances, platforms, transfers, or other transit-specific semantics. A fallback is not a completed GTFS Pathways dataset or a guarantee of station accessibility.

## How To Use This

Separate surrounding pedestrian analysis from station-internal modeling, and label any assumptions or missing information. Do not publish a derived feed without an explicit, reviewed workflow.

## Example

A planner uses OS-CONNECT to examine the sidewalk leading to a station but flags the missing platform connections and requests station-pathway information from the transit agency.

## Assistant Guidance

Explain the boundary between pedestrian context and GTFS Pathways. Cite the official feed and source datasets, and abstain from inferring station details that are not documented.

## Related Concepts

- [What is GTFS Pathways?](../../accessmap/concept/gtfs-pathways.md)
- [OSM pedestrian paths versus GTFS Pathways](osm-pedestrian-paths-vs-gtfs-pathways.md)
- [Can OS-CONNECT generate GTFS Pathways?](../../os-connect/concept/gtfs-pathways-generation.md)
