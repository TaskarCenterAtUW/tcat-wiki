---
title: Which sidewalk-to-street-name tagging pattern is currently recommended?
slug: recommended-sidewalk-tagging-pattern
doc_type: concept
questions:
    - Which sidewalk-to-street-name tagging pattern is currently recommended?
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
        - One sidewalk-to-street tag is permanently correct for every dataset and consumer.
        - A street-name tag creates a physical pedestrian connection.
related_pages:
    - assistant/os-connect/concept/sidewalk-street-name-association.md
    - assistant/os-connect/concept/street-name-vs-is-sidepath-of-name.md
    - assistant/os-connect/concept/street-name-tags-for-routing.md
tags:
    - Assistant
---

<!-- @format -->

# Which sidewalk-to-street-name tagging pattern is currently recommended?

## Short Answer

OS-CONNECT does not define a dedicated sidewalk-to-street-name tag. In OpenStreetMap, use the current project or community guidance; `street:name` is increasingly used for the associated street, while `is_sidepath:of:name` remains in use. Keep the sidewalk as its own pedestrian geometry and verify the convention for the intended schema or consumer before editing.

## Significance

Consistent tagging helps routing and data consumers interpret a sidewalk that follows a road without incorrectly merging the two features.

## What This Means

- Map the sidewalk separately when its physical geometry is separate.
- In OSM, check whether the current project guidance calls for `street:name` or another supported convention; do not assume that OS-CONNECT supplies a dedicated tag.
- Check the result in the intended consumer and retain the source version.

## What This Does Not Mean

The pattern does not guarantee a physical connection, accessibility, or identical behavior across consumers. Do not choose a tag solely because it makes a map label appear convenient.

## How To Use This

Consult the current OpenStreetMap, OpenSidewalks, or project guidance and document the convention used. Ask for review when adjacent roads or path relationships are ambiguous, or when the intended consumer's tag support is unknown.

## Example

An editor maps a sidewalk parallel to a road and applies the project's current association pattern, then checks that routing uses the pedestrian path rather than treating it as roadway geometry.

## Assistant Guidance

Cite the current tagging reference and avoid inventing tags. Ask which schema and consumer are involved, and abstain when the latest recommendation cannot be verified.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)
- [Street name versus sidepath name](street-name-vs-is-sidepath-of-name.md)
- [Street-name tags for routing](street-name-tags-for-routing.md)
