---
uid: 3d939b29-ea39-4f8b-a46d-697b90f2ef15
title: How are crossing links represented across pedestrian data systems?
slug: crossing-links
doc_type: concept
questions:
    - How are crossing links represented across pedestrian data systems?
    - How are crossing links mapped in OpenStreetMap and in OS-CONNECT?
    - Why distinguish crossing links from ordinary sidewalks?
audiences:
    - developer
    - planner
    - jurisdiction
products:
    - OpenSidewalks
    - OS-CONNECT
topics:
    - cross-platform
    - opensidewalks
    - os-connect
    - connectivity
    - editing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A crossing link is an ordinary sidewalk segment in every analysis.
        - There is no way to differentiate between primary blockface-scale sidewalks and small connectors.
related_pages:
    - assistant/accessmap/index.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# How are crossing links represented across pedestrian data systems?

## Short Answer

A crossing link is a connector between a sidewalk centerline and a curb node. It preserves pedestrian network connectivity while allowing the connector to be distinguished from ordinary, blockface-scale sidewalk geometry. The representation depends on the data system and the mapping context.

## Significance

The distinction allows systems to preserve a usable pedestrian connection without treating the connector as ordinary sidewalk geometry in every data operation. Clear representation also helps people interpret data exchanged between OpenStreetMap and OpenSidewalks datasets such as OS-CONNECT.

## What This Means

Keep the connector in the network, and use the representation appropriate to the target data system.

- In OpenStreetMap, the community has shown a clear preference for tagging these connectors with `highway=footway` plus `footway=sidewalk`.
- OpenSidewalks mappers mapping in OpenStreetMap use `highway=footway`, `footway=sidewalk`, and `crossing_link=yes` for these connector segments. The `crossing_link=yes` tag further identifies the connector role.
- In OS-CONNECT, these connectors are represented as bare footways: `highway=footway` with no other identifying tags.
- The geometry remains part of the pedestrian network regardless of representation method and whether the connector is distinguished from ordinary sidewalk geometry.

## What This Does Not Mean

A crossing link is not necessarily represented with the same tags in every system. The OpenStreetMap representation described here should not be applied unchanged to OS-CONNECT, and the presence of a connector tag does not by itself establish a safety condition or a legal accessibility determination.

## How To Use This

Before creating or retagging a connector, identify whether the target is OpenStreetMap, OpenStreetMap with OpenSidewalks mapping conventions, or OpenSidewalks-formatted OS-CONNECT data. Check the current project and schema guidance, preserve connectivity, and document any local mapping assumptions.

## Example

A mapper creates a short way between a sidewalk center line and a curb point. In OpenStreetMap, the mapper tags it with `highway=footway`, `footway=sidewalk`, and `crossing_link=yes`. When the corresponding data is represented in OS-CONNECT, the connector is a bare `highway=footway` without additional identifying tags.

## Assistant Guidance

Distinguish the standard OpenStreetMap tagging approach from the OpenSidewalks-in-OpenStreetMap tagging convention from the OS-CONNECT bare-footway representation. Ask which system and schema version are involved before prescribing tagging processes, and do not infer safety or accessibility outcomes from the representation alone.

## Related Concepts

- [Cross-Platform policies](../index.md)
- [What is the OpenSidewalks data schema?](../../opensidewalks/concept/opensidewalks-schema.md)
- [How can connector segments be distinguished in OpenSidewalks mapping?](../../opensidewalks/concept/connector-segment-tagging.md)
- [What infrastructure types are included in OS-CONNECT?](../../os-connect/concept/included-infrastructure-types.md)
