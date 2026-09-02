---
uid: f8e12f00-6b83-4cb2-bacc-35f019d8a973
title: How can trip planners use sidewalk street-name tags to produce better walking instructions?
slug: street-name-tags-for-routing
doc_type: concept
questions:
    - How can trip planners use sidewalk street-name tags to produce better walking instructions?
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
        - Street-name tags guarantee identical walking instructions in every trip planner.
        - A street name proves that a pedestrian path is connected or accessible.
related_pages:
    - assistant/os-connect/concept/sidewalk-street-name-association.md
    - assistant/os-connect/concept/recommended-sidewalk-tagging-pattern.md
    - assistant/os-connect/concept/street-name-routing-importance.md
tags:
    - Assistant
---

<!-- @format -->

# How can trip planners use sidewalk street-name tags to produce better walking instructions?

## Short Answer

Trip planners can use supported sidewalk street-name tags to associate a separated pedestrian path with the road or street it follows and produce more understandable walking instructions. OS-CONNECT does not define a dedicated street-name tag; consumer behavior depends on the source convention, planner data processing, and current tagging support.

## Significance

Clear names help users follow walking directions and help vendors interpret pedestrian paths that are not drawn on the road centerline. Consistent tagging also makes it easier to compare data across mapping workflows.

## What This Means

- Preserve the mapped pedestrian geometry and its relevant name or street relationship.
- Follow the current supported tagging pattern when processing OSM or OS-CONNECT data, recognizing that `street:name` is increasingly used in OSM and that consumers may support tags differently.
- Test instructions in the intended consumer and retain the source version.

## What This Does Not Mean

Street-name tags do not replace connectivity, access attributes, or route validation. A consumer may ignore a tag or interpret it differently, so the tag cannot guarantee a particular instruction.

## How To Use This

Vendors should document how they map the tags into route instructions, test representative separated sidewalks, and report ambiguous or missing data with the source and version.

## Example

A trip planner receives a separated sidewalk with an association to a parallel street. It uses the relationship to name the walking segment while still routing on the pedestrian geometry.

## Assistant Guidance

Do not promise a specific vendor's behavior. Cite the current tagging guidance, ask which consumer and data version are involved, and abstain when the relationship or processing rule is unknown.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)
- [Recommended sidewalk tagging pattern](recommended-sidewalk-tagging-pattern.md)
- [Why street names matter for walking directions](street-name-routing-importance.md)
