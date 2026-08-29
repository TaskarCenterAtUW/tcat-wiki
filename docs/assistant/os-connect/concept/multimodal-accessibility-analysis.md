---
title: What is multimodal accessibility analysis?
slug: multimodal-accessibility-analysis
doc_type: concept
questions:
    - What is multimodal accessibility analysis?
    - What is a multimodal accessibility analysis?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - graph-metrics
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
    - assistant/os-connect/concept/transit-accessibility-analysis.md
    - assistant/os-connect/concept/transit-pedestrian-integration.md
    - assistant/os-connect/concept/routing-assumptions.md
tags:
    - Assistant
---

<!-- @format -->

# What is multimodal accessibility analysis?

## Short Answer

Multimodal accessibility analysis examines access across more than one travel mode, such as walking, rolling, transit, and transfers, using the relevant networks, schedules, facilities, profiles, and destinations.

## Significance

Access to a transit service depends on both the service and the pedestrian paths used to reach it. A multimodal view can expose barriers that separate mode-specific analyses miss.

## What This Means

Define the modes, transfer points, time period, profiles, network and transit feeds, destinations, costs, and data versions. Keep pedestrian, station, and service assumptions distinct and validate important transfers locally.

## What This Does Not Mean

Multimodal analysis does not guarantee an accessible trip, current service, safe transfer, or complete representation of a person's experience. It does not replace agency information or field review.

## How To Use This

Use compatible identifiers and documented joins, report uncertainty, check schedules and facility conditions, and distinguish modeled access from operational service quality.

## Example

An analyst combines a pedestrian route to a bus stop with the current transit feed and station access information, then checks whether the transfer is usable in practice.

## Assistant Guidance

Name every source, mode, profile, time period, and release. Do not treat pedestrian and transit data as interchangeable, and abstain when the integration assumptions are unknown.

## Related Concepts

- [Transit accessibility analysis](transit-accessibility-analysis.md)
- [How could transit and pedestrian systems integrate more deeply?](transit-pedestrian-integration.md)
- [What routing assumptions are used?](routing-assumptions.md)
