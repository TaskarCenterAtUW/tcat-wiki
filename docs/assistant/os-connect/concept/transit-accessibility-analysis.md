---
title: Can this data support transit accessibility analysis?
slug: transit-accessibility-analysis
doc_type: concept
questions:
    - Can this data support transit accessibility analysis?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - transit
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/transit-pedestrian-integration.md
    - assistant/os-connect/concept/transit-agency-contribution.md
    - assistant/os-connect/concept/os-connect-tdei-relationship.md
tags:
    - Assistant
---

<!-- @format -->

# Can this data support transit accessibility analysis?

## Short Answer

OS-CONNECT can support transit-accessibility analysis by providing pedestrian-network context around stops, stations, and destinations. It should be combined with current transit feeds, station information, accessibility data, and local or field evidence.

## Significance

Transit access depends on the service, station or stop, and pedestrian path used to reach it. Pedestrian data can expose access gaps outside the transit schedule itself.

## What This Means

Define stops, entrances, service period, pedestrian profiles, network, release, and transfer question. Join sources using documented identifiers and validate important approaches and transfers locally.

## What This Does Not Mean

OS-CONNECT does not measure ridership, on-time performance, service quality, or guarantee an accessible transfer. It does not replace agency data or GTFS Pathways where station-internal semantics are required.

## How To Use This

Use the data for access context, preserve each source and version, and separate modeled pedestrian reachability from transit operations and facility conditions.

## Example

An analyst measures modeled pedestrian access to bus stops, combines it with the agency's current feed, and asks the agency to verify station entrances and transfer conditions.

## Assistant Guidance

Name the pedestrian and transit sources, period, profile, and release. Avoid claims about service or transfer usability without current evidence.

## Related Concepts

- [How could transit and pedestrian systems integrate more deeply?](transit-pedestrian-integration.md)
- [How should transit agencies contribute?](transit-agency-contribution.md)
- [How is OS-CONNECT related to TDEI?](os-connect-tdei-relationship.md)
