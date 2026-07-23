---
title: "How are AVIV ScoutRoute quest element icons selected?"
slug: quest-definition-element-icons
doc_type: concept
questions:
    - How are AVIV ScoutRoute quest element icons selected?
    - What does element_type_icon do in a quest definition?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any arbitrary string in element_type_icon displays a matching custom icon in the app.
related_pages:
    - quest-definition-element-targeting.md
    - ../workflow/update-quest-definition-in-workspace.md
    - ../../../aviv-scoutroute/quests/element-type-icon.md
tags:
    - Assistant
---

<!-- @format -->

# How are AVIV ScoutRoute quest element icons selected?

## Short Answer

The `element_type_icon` value in a Long Form Quest Definition tells AVIV ScoutRoute which available icon to use for the targeted element type.

## Significance

A suitable icon helps contributors recognize the feature represented by a quest on the map.

## What This Means

Choose an icon name from the current icon reference, add the exact name without a file extension, and test the definition. If the value is missing or unsupported, the app falls back to a default icon according to the current guide.

## What This Does Not Mean

The field does not create a new icon, and an arbitrary filename or extension is not a supported icon value.

## How To Use This

Search the icon reference for the target feature, copy the exact icon name, place it in `element_type_icon`, and verify the resulting map display.

## Example

A sidewalk quest definition uses `"element_type_icon": "sidewalk"` so the app can display the corresponding sidewalk icon.

## Assistant Guidance

Ask for the active definition and app version when an icon does not appear as expected. Do not assume that a visually similar name is supported.

## Related Concepts

- [How do quest definitions target element types?](quest-definition-element-targeting.md)
- [How is a quest definition applied?](quest-definition-application.md)
