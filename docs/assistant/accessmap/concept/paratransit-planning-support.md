---
title: Can AccessMap support paratransit planning?
slug: paratransit-planning-support
doc_type: concept
questions:
    - Can AccessMap support paratransit planning?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - transit
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
        - AccessMap plans or determines paratransit eligibility by itself.
        - A pedestrian route result replaces paratransit operations or policy.
related_pages:
    - assistant/accessmap/concept/transit-pedestrian-routing-integration.md
    - assistant/accessmap/concept/accessibility-needs.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Can AccessMap support paratransit planning?

## Short Answer

AccessMap may support paratransit planning by providing pedestrian-access context around origins, destinations, stops, or transfer locations. It does not by itself determine eligibility, schedule vehicles, or replace transit-agency operations and policy.

## Significance

The walking connection to a pickup, drop-off, or transfer point can affect an accessible trip. Modeling that connection can inform questions for paratransit planners.

## What This Means

- Identify the service area, access points, profiles, and current pedestrian data.
- Analyze connections as a supplement to paratransit service and rider information.
- Validate important locations with the transit agency and affected riders.

## What This Does Not Mean

Pedestrian routing is not paratransit eligibility, demand, scheduling, dispatch, or service reliability. A modeled route does not guarantee that a rider can complete the trip.

## How To Use This

Use AccessMap to frame access questions, then combine results with agency records, rider input, and operational review.

## Example

A transit agency reviews pedestrian access between a neighborhood and a paratransit pickup point, then combines that information with its service design and rider feedback.

## Assistant Guidance

Do not make eligibility or service promises. Cite route and transit documentation, ask for agency and service context, and abstain from operational conclusions without current agency data.

## Related Concepts

- [Transit accessibility integration](transit-pedestrian-routing-integration.md)
- [Accessibility needs](accessibility-needs.md)
- [Routing limitations](routing-limitations.md)
