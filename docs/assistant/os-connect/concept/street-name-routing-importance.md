---
title: Why do street names matter for walking directions?
slug: street-name-routing-importance
doc_type: concept
questions:
    - Why do street names matter for walking directions?
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
    - routing
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
        - A street name alone guarantees clear or correct walking directions.
        - A named pedestrian path is necessarily connected or accessible.
related_pages:
    - assistant/os-connect/concept/sidewalk-street-name-association.md
    - assistant/os-connect/concept/street-name-tags-for-routing.md
    - assistant/os-connect/concept/missing-street-names-for-vendors.md
tags:
    - Assistant
---

<!-- @format -->

# Why do street names matter for walking directions?

## Short Answer

Street names help people and trip-planning systems describe walking segments and turns in terms users recognize. For separated sidewalks, a documented relationship to the adjacent street can make instructions more understandable without changing the pedestrian geometry.

## Significance

Clear instructions support navigation and make pedestrian-network data more useful to vendors, agencies, and the public.

## What This Means

- Preserve the pedestrian path and its relevant name or street relationship.
- Use the current tagging and consumer guidance.
- Test instructions on representative routes and note missing or uncertain names.

## What This Does Not Mean

Street names do not replace connectivity, accessibility attributes, or field verification. A consumer may ignore or interpret a tag differently.

## How To Use This

Review the source tags, nearby geometry, and data version, then document how the intended consumer uses them. Report ambiguous relationships rather than guessing.

## Example

A routing vendor uses a separated sidewalk's documented relationship to a parallel street to produce a recognizable instruction while continuing to route on the pedestrian path.

## Assistant Guidance

Explain the user benefit without promising a vendor-specific result. Cite the tagging guidance and ask which data version and consumer are involved.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)
- [Street-name tags for routing](street-name-tags-for-routing.md)
- [Missing street names for vendors](missing-street-names-for-vendors.md)
