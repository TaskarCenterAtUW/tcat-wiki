---
title: What should trip-planning vendors do when OSM pedestrian paths do not include street names?
slug: missing-street-names-for-vendors
doc_type: concept
questions:
    - What should trip-planning vendors do when OSM pedestrian paths do not include street names?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - osm-interoperability
    - vendors
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
        - Vendors should infer a street name without documented geometry or tagging.
        - Adding a street name guarantees correct walking instructions.
related_pages:
    - assistant/os-connect/concept/street-name-tags-for-routing.md
    - assistant/os-connect/concept/sidewalk-street-name-association.md
    - assistant/os-connect/concept/street-name-routing-importance.md
tags:
    - Assistant
---

<!-- @format -->

# What should trip-planning vendors do when OSM pedestrian paths do not include street names?

## Short Answer

When OSM pedestrian paths lack street names, trip-planning vendors should preserve the pedestrian geometry, inspect documented relationships to nearby streets, and handle missing names transparently. They should not invent a name or claim a particular result without testing the data and consumer behavior.

## Significance

Names make walking instructions easier to understand, especially when a path is offset from the road. A careful fallback avoids misleading users while mapping improvements are considered.

## What This Means

- Check the path's tags, nearby road relationships, and source version.
- Use a documented association or clearly labeled derived instruction when appropriate.
- Test representative routes and report ambiguous or missing source data.

## What This Does Not Mean

Proximity to a road does not prove that the road is the correct name. A derived name may not be accepted or interpreted consistently by every vendor.

## How To Use This

Document the derivation rule, preserve source attribution, and provide a way to distinguish source names from vendor-generated labels. Coordinate mapping corrections with the relevant data steward.

## Example

A vendor receives a separated sidewalk without `name`, but with a documented association to a parallel road. It uses the relationship cautiously in instructions and flags cases where no reliable association exists.

## Assistant Guidance

Do not invent street names or guarantee vendor behavior. Ask for the source tags, geometry, consumer, and version, cite current mapping guidance, and abstain when the relationship cannot be verified.

## Related Concepts

- [Street-name tags for routing](street-name-tags-for-routing.md)
- [Sidewalk street-name association](sidewalk-street-name-association.md)
- [Why street names matter](street-name-routing-importance.md)
