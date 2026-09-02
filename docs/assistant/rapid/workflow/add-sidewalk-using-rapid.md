---
uid: 92f3af12-0ecd-4ea0-8bba-b941b5384fc4
title: How do I add a sidewalk using Rapid?
slug: add-sidewalk-using-rapid
doc_type: workflow
questions:
    - How do I add a sidewalk using Rapid?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Rapid
topics:
    - rapid
    - editing-tools
    - collaborative-editing
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/rapid/concept/rapid.md
    - assistant/os-connect/concept/separated-sidewalk-mapping.md
    - assistant/os-connect/concept/recommended-sidewalk-tagging-pattern.md
tags:
    - Assistant
---

<!-- @format -->

# How do I add a sidewalk using Rapid?

## Short Answer

To add a sidewalk using Rapid, select the correct location and imagery, draw the pedestrian geometry based on evidence, apply supported tags or presets, review connections and attributes, and save the edit through the current OpenStreetMap workflow.

## Significance

Sidewalk geometry and tagging affect how other users and systems interpret the pedestrian network. Careful editing reduces false connections and unsupported accessibility claims.

## What This Means

1. Confirm the area, imagery date, and editing permissions.
2. Trace the sidewalk's physical geometry; keep it separate from roadway geometry when appropriate.
3. Apply current supported tags and presets.
4. Check crossings, connections, attributes, and nearby edits.
5. Review the changeset and submit only edits supported by evidence.

## What This Does Not Mean

An edit in Rapid does not automatically update OS-CONNECT, TDEI, AccessMap, or another downstream dataset. Imagery does not prove every accessibility attribute.

## How To Use This

Use current Rapid and OpenStreetMap guidance, document uncertainty, avoid mapping from assumptions, and seek review for complex or inaccessible-to-observe locations.

## Example

A mapper traces a separate sidewalk from current imagery, checks that it connects to mapped crossings, and leaves unknown accessibility fields unfilled until verified.

## Assistant Guidance

Do not prescribe a preset or tag without checking the current editor and project guidance. Cite the source, distinguish OSM edits from downstream releases, and abstain when imagery or geometry is ambiguous.

## Related Concepts

- [What is Rapid?](../concept/rapid.md)
- [What should mappers do when a sidewalk is separated from the road geometry?](../../os-connect/concept/separated-sidewalk-mapping.md)
- [Which sidewalk-to-street-name tagging pattern is currently recommended?](../../os-connect/concept/recommended-sidewalk-tagging-pattern.md)
