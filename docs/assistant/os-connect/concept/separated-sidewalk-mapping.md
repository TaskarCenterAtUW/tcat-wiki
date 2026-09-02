---
uid: da501179-baf0-4c40-a8be-6d50687de676
title: What should mappers do when a sidewalk is separated from the road geometry?
slug: separated-sidewalk-mapping
doc_type: concept
questions:
    - What should mappers do when a sidewalk is separated from the road geometry?
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
        - A separated sidewalk should be merged into the road geometry.
        - Geometric separation proves that a sidewalk is disconnected or inaccessible.
related_pages:
    - assistant/os-connect/concept/sidewalk-street-name-association.md
    - assistant/os-connect/concept/recommended-sidewalk-tagging-pattern.md
    - assistant/os-connect/concept/connectivity-depends-on-geometry.md
tags:
    - Assistant
---

<!-- @format -->

# What should mappers do when a sidewalk is separated from the road geometry?

## Short Answer

Map a sidewalk as its own pedestrian feature when its physical geometry is separated from the road. Connect it to the pedestrian network where a real crossing or connector exists, and use the current street-association guidance without merging the sidewalk into the vehicle road.

## Significance

Separate geometry is common in pedestrian mapping and can preserve the actual path people use. Consistent modeling helps routing, accessibility analysis, and later review.

## What This Means

- Trace the pedestrian path according to the physical evidence.
- Add valid connections at crossings, entrances, and other connectors.
- Apply the current sidewalk-to-street-name convention where appropriate.
- Validate the result in the intended data consumer.

## What This Does Not Mean

Geometric separation does not by itself mean the sidewalk is disconnected. A street-name association does not create a physical connection, and a map does not prove accessibility or legal status.

## How To Use This

Use imagery, local knowledge, and field verification for ambiguous or high-consequence locations. Preserve the separate geometry and document assumptions rather than forcing connectivity.

## Example

An OSM mapper sees a sidewalk set back from the roadway, traces it separately, maps the crosswalk connector, and records the adjacent street relationship for downstream users.

## Assistant Guidance

Do not tell a mapper to merge features merely because they are nearby. Cite current mapping guidance, ask for the location and intended schema, and abstain when the physical connection is unclear.

## Related Concepts

- [Sidewalk street-name association](sidewalk-street-name-association.md)
- [Recommended sidewalk tagging pattern](recommended-sidewalk-tagging-pattern.md)
- [Connectivity depends on geometry](connectivity-depends-on-geometry.md)
