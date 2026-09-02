---
uid: 57acb4d0-6cad-4afe-b348-2fe0c3b2ea09
title: What accessibility needs does AccessMap support?
slug: accessibility-needs
doc_type: concept
questions:
    - What accessibility needs does AccessMap support?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
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
    do_not_claim:
        - AccessMap represents every person's accessibility needs completely.
        - A supported accessibility need guarantees that every route is usable.
related_pages:
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/accessibility-assumptions.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What accessibility needs does AccessMap support?

## Short Answer

AccessMap supports route planning around selected accessibility considerations, including mobility profiles and preferences related to slopes, curb ramps, and other mapped pedestrian conditions. Support depends on the available data and the current product implementation.

## Significance

Making accessibility considerations visible can help people and agencies compare route tradeoffs. It also makes the limits of modeled accessibility easier to discuss.

## What This Means

- Choose the profile or preferences closest to the traveler's needs.
- Review which mapped attributes affect the route.
- Verify important conditions in the field and account for missing data.

## What This Does Not Mean

AccessMap does not represent every disability, individual need, or physical condition. A profile is not a medical assessment, ADA determination, or guarantee of access.

## How To Use This

State the profile and relevant preferences, then describe the route as a model based on available data. Use current documentation for supported profiles and settings.

## Example

A traveler selects a wheelchair-oriented profile and avoids a route with a modeled steep slope, then checks current construction and surface conditions before traveling.

## Assistant Guidance

Do not infer a user's needs or promise usability. Cite the current profile and limitation documentation, and abstain when the relevant setting or data version is unclear.

## Related Concepts

- [Mobility profiles](mobility-profiles.md)
- [Accessibility assumptions](accessibility-assumptions.md)
- [Routing limitations](routing-limitations.md)
