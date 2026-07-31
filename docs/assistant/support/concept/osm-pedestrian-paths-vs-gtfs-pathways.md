---
title: What is the relationship between pedestrian paths in OpenStreetMap and GTFS Pathways?
slug: osm-pedestrian-paths-vs-gtfs-pathways
doc_type: concept
questions:
    - What is the relationship between pedestrian paths in OpenStreetMap and GTFS Pathways?
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
    - osm-interoperability
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - OSM pedestrian paths and GTFS Pathways are the same dataset or automatically synchronized.
    related_pages:
        - assistant/support/workflow/check-gtfs-feed-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# What is the relationship between pedestrian paths in OpenStreetMap and GTFS Pathways?

## Short Answer

OSM pedestrian paths describe mapped physical ways in a collaborative geographic database. GTFS Pathways describe transit-stop pathways and transfers in a publisher's transit feed.

## Significance

Both can inform walking or transit routing, but their scopes and stewardship differ.

## What This Means

Use OSM or OS-CONNECT for surrounding pedestrian context and GTFS Pathways for station-specific transit semantics. Verify identifiers and versions before joining them.

## What This Does Not Mean

An OSM path does not automatically become a GTFS pathway, and a GTFS pathway does not represent the full street network.

## How To Use This

Check the transit feed and local pedestrian dataset independently.

## Example

A station entrance is connected to a platform in GTFS Pathways while the sidewalk leading to the entrance is represented in pedestrian data.

## Assistant Guidance

Avoid claiming synchronization or completeness without source evidence.

## Related Concepts

- [Check GTFS feed pathways](../workflow/check-gtfs-feed-pathways.md)
