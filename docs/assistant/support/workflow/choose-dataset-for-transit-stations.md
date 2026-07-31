---
title: Which dataset should I use if I need transit-station pathway data?
slug: choose-dataset-for-transit-stations
doc_type: workflow
questions:
    - Which dataset should I use if I need transit-station pathway data?
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
    - dataset-lineage
    - gtfs
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
        - The existence of pedestrian data proves that transit-station pathways are published.
    related_pages:
        - assistant/support/workflow/check-gtfs-feed-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# Which dataset should I use if I need transit-station pathway data?

## Short Answer

Use the transit agency's GTFS-Pathways feed for station-internal pathway data. Use OS-CONNECT or another pedestrian dataset for the surrounding walking network.

## Significance

The two sources represent different parts of a station-access journey.

## What This Means

Verify whether the feed contains `pathways.txt`, related stop records, entrances, and the feed version. Check pedestrian coverage separately.

## What This Does Not Mean

OS-CONNECT does not automatically provide the agency's authoritative station pathway records.

## How To Use This

Choose sources by the boundary of the analysis and document each version.

## Example

A station study joins GTFS pathway records with nearby pedestrian edges and validates the connection at the entrance.

## Assistant Guidance

Do not infer pathway publication from the existence of pedestrian data.

## Related Concepts

- [Check GTFS feed pathways](check-gtfs-feed-pathways.md)
