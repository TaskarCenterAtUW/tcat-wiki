---
title: Can OS-CONNECT generate GTFS Pathways data?
slug: gtfs-pathways-generation
doc_type: concept
questions:
    - Can OS-CONNECT generate GTFS Pathways data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - gtfs
    - export
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
        - OS-CONNECT automatically generates an agency's GTFS Pathways feed.
        - OS-CONNECT and GTFS Pathways are interchangeable datasets.
related_pages:
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/cross-platform/concept/os-connect-vs-gtfs-pathways.md
    - assistant/support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# Can OS-CONNECT generate GTFS Pathways data?

## Short Answer

OS-CONNECT and GTFS Pathways describe different kinds of network data. OS-CONNECT does not automatically generate an agency's GTFS Pathways feed; producing station-pathway data requires an appropriate transit-data workflow and agency review.

## Significance

The distinction prevents a pedestrian inventory from being treated as a transit feed. Station entrances, platforms, and internal transfers need transit-specific semantics and publisher responsibility.

## What This Means

- Use OS-CONNECT for its released pedestrian-network data and documented attributes.
- Use GTFS Pathways for station or stop pathway information when an agency publishes it.
- Treat any conversion or derivative workflow as requiring explicit current documentation.

## What This Does Not Mean

- OS-CONNECT is not automatically a GTFS Pathways generator.
- Similar geometry does not make two datasets interchangeable or synchronized.

## How To Use This

Identify whether the goal is surrounding pedestrian access or station-internal pathway data. Consult the current agency and TDEI workflow before proposing a conversion.

## Example

A planner has sidewalk data near a station but needs `pathways.txt`. The planner treats the sidewalk data as context and asks the transit-data steward about a separate GTFS Pathways workflow.

## Assistant Guidance

Do not promise automatic generation or feed publication. Cite the relevant format documentation and abstain when a current conversion workflow is not documented.

## Related Concepts

- [What is GTFS Pathways?](../../accessmap/concept/gtfs-pathways.md)
- [OS-CONNECT versus GTFS Pathways](../../cross-platform/concept/os-connect-vs-gtfs-pathways.md)
- [OSM pedestrian paths versus GTFS Pathways](../../support/concept/osm-pedestrian-paths-vs-gtfs-pathways.md)
