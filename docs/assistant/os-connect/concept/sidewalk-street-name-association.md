---
uid: d0f7f947-33ef-420c-9cc3-fc09156dcf9a
title: "How should separately mapped sidewalks be associated with street names in OSM?"
slug: sidewalk-street-name-association
doc_type: concept
questions:
    - How should separately mapped sidewalks be associated with street names in OSM?
    - How should separately mapped sidewalks be associated with street names in OpenStreetMap?
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
    - collaborative-editing
    - editing
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
        - A sidewalk should be merged into road geometry solely to provide a street name.
        - A street-name relationship proves that a sidewalk is physically connected or accessible.
related_pages:
    - assistant/os-connect/concept/recommended-sidewalk-tagging-pattern.md
    - assistant/os-connect/concept/street-name-vs-is-sidepath-of-name.md
    - assistant/os-connect/concept/street-name-tags-for-routing.md
tags:
    - Assistant
---

<!-- @format -->

# How should separately mapped sidewalks be associated with street names in OSM?

## Short Answer

Separately mapped sidewalks should remain their own pedestrian geometry. In OpenStreetMap, the association with an adjacent street may use the current supported convention, including the growing use of `street:name`; OS-CONNECT does not define a dedicated street-name tag. Verify the convention for the project, schema, and downstream consumer.

## Significance

Street-name association helps people and trip-planning systems describe where a pedestrian path runs. Inconsistent tagging can reduce the quality of walking instructions or obscure the relationship between a sidewalk and its road.

## What This Means

- Keep a physically separate sidewalk as its own pedestrian feature.
- Apply the current documented OSM relationship or name pattern consistently; do not represent it as an OS-CONNECT-specific tag.
- Distinguish a sidewalk's own name from a tag identifying the road it follows.

## What This Does Not Mean

- A sidewalk should not be merged into road geometry solely to make its street name available.
- One tag cannot guarantee identical behavior in every consumer.
- A name relationship does not prove physical connectivity or accessibility.

## How To Use This

Map the physical geometry first, then apply the current recommended relationship pattern and validate it in the intended consumer. Record the convention used when working with older data or complex sites.

## Example

An OSM mapper traces a sidewalk several meters from a parallel roadway. The mapper keeps it as a separate path, applies the documented street association, and checks the result in a routing consumer.

## Assistant Guidance

Refer to the current recommended tagging article rather than inventing tags. Ask whether the user needs OSM editing, OpenSidewalks conversion, or trip-planning behavior, and abstain when the road relationship is ambiguous.

## Related Concepts

- [Recommended sidewalk tagging pattern](recommended-sidewalk-tagging-pattern.md)
- [Street name versus sidepath name](street-name-vs-is-sidepath-of-name.md)
- [Street-name tags for routing](street-name-tags-for-routing.md)
