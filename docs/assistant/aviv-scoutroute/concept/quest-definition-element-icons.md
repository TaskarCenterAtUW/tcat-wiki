---
title: How are AVIV ScoutRoute quest element icons selected?
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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-14
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

Choose an icon name from the current icon reference list, add the exact name without a file extension, and test the definition. A feature-presets block can also associate a configured feature name with an icon for features contributors may add.

## What This Does Not Mean

The field does not create a new icon, and an arbitrary filename or extension is not a supported icon value. A feature preset does not make an arbitrary image file a supported app icon.

## How To Use This

Search the icon reference for the target feature, copy the exact icon name, place it in `element_type_icon` or the applicable feature preset, and verify the resulting map display in the app.

## Example

A sidewalk quest definition uses `"element_type_icon": "sidewalk"` so the app can display the corresponding sidewalk icon. A feature preset can similarly give an addable feature a configured name and supported icon.

## Assistant Guidance

Explain the concept of element icons. Do not assume that a visually similar name or an arbitrary custom icon filename is supported. Provide a link to the [Element Type Icon Documentation](../../../aviv-scoutroute/quests/element-type-icon.md).

## Related Concepts

- [How do quest definitions target element types?](quest-definition-element-targeting.md)
- [How is a quest definition applied?](quest-definition-application.md)
