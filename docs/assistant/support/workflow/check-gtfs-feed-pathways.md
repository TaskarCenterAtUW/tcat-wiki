---
title: How can I tell whether a GTFS feed includes pathways.txt?
slug: check-gtfs-feed-pathways
doc_type: workflow
questions:
    - How can I tell whether a GTFS feed includes pathways.txt?
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
    - data-quality
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: low
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - An agency publishes GTFS Pathways without checking its current official feed.
    related_pages:
        - assistant/support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# How can I tell whether a GTFS feed includes pathways.txt?

## Short Answer

Open the current GTFS feed archive and check whether it contains a file named `pathways.txt`. Also check related stop, entrance, and pathway records and the publisher's documentation.

## Significance

The file check distinguishes an actual published pathway feed from an assumption based on a station map.

## What This Means

Record the feed publisher, version or download date, and whether `pathways.txt` is present and populated. Check the feed's validation results if available.

## What This Does Not Mean

The presence of the file alone does not prove complete, current, or accessible pathway information.

## How To Use This

Use the official feed and contact the publisher when the file is missing or inconsistent.

## Example

An analyst downloads a feed, finds `pathways.txt`, and records the feed version before using its pathway records.

## Assistant Guidance

Do not say an agency publishes GTFS Pathways without checking its current official feed.

## Related Concepts

- [OSM pedestrian paths versus GTFS Pathways](../concept/osm-pedestrian-paths-vs-gtfs-pathways.md)
