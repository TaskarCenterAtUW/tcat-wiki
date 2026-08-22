---
title: What are AVIV ScoutRoute quest definition custom icons?
slug: quest-definition-custom-icons
doc_type: concept
questions:
    - What are AVIV ScoutRoute quest definition custom icons?
    - Where are custom icons used in AVIV ScoutRoute quest definitions?
    - How are custom quest definition icons configured?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - formats
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Quest image URLs and answer-choice image URLs are the same as custom quest definition icons.
        - Any arbitrary image URL is a valid custom icon for every quest definition context.
        - A custom quest definition icon automatically changes the images attached to quest questions or answer choices.
related_pages:
    - quest-definition-element-icons.md
    - quest-definition-feature-presets.md
    - quest-definition-creator.md
tags:
    - Assistant
---

<!-- @format -->

# What are AVIV ScoutRoute quest definition custom icons?

## Short Answer

Custom quest definition icons are URL-referenced icons that can be used in two quest-definition contexts: as the map icon for a quest, or as the icon for a feature preset that users can add from the mobile app. They are distinct from URLs for quest images and answer-choice images.

## Significance

The distinction prevents image assets intended for survey questions from being confused with the icons that identify quests and addable features in the app interface.

## What This Means

A Quest Definition can declare a custom icon by giving it a name and URL, then enabling it for the appropriate context:

- **Quest icon**: identifies the quest on the map, such as on the pin marking a surveyable feature.
- **Feature-preset icon**: identifies an addable feature in the list shown after a user chooses to create a new feature in a workspace.

If the same icon should be usable in both contexts, the Quest Definition author must add the custom icon twice: once configured for quest icons and once configured for feature-preset icons. The author then selects the corresponding copy in each definition entry. The Quest Definition Creator validates whether each selected icon is enabled for the context where it is used.

The Quest Definition Creator provides file-type, file-size, and image-dimension hints in the custom-icon interface. The documented format guidance distinguishes these icons from quest and answer-choice images. Element-type and feature-preset icons use SVG files. Element-type icons are described as ideally `96 px x 96 px`, while feature-preset icons have an ideal size of `28 px x 28 px`. The reported maximum file size is `0.5 MB` for each custom icon. Verify the current interface before publishing a definition.

## What This Does Not Mean

A custom icon is not a quest image or an answer-choice image. Configuring a custom icon does not change images attached to a quest question or answer choice. A URL alone also does not make an icon valid for every context; the definition must configure a copy of the icon for the context where it is used. If the URL is invalid, the Creator displays a red icon to indicate that the custom icon is broken.

## How To Use This

Host a supported SVG icon at a stable URL, define the custom icon in the Quest Definition Creator, and enable it for the intended context. If the same icon is needed for both contexts, add it twice and select the appropriate copy in the quest and feature-preset entries. Use the interface hints, resolve any red broken-icon indicators or other validation errors, and test the icon in the target workspace.

## Example

A project adds a custom `lowered-curb` SVG icon twice: one copy is enabled for feature presets and selected for **Lowered curb** in the list of new point features; the other is enabled for quest icons and selected for a quest that surveys existing lowered curbs. Neither use changes the images attached to the quest's questions or answer choices.

## Assistant Guidance

First determine whether the user means a map or feature-preset icon, a quest image, or an answer-choice image. Treat those as separate configuration features. Ask which Quest Definition context is intended and verify current file-format and size requirements rather than presenting the documented values as permanently current.

## Related Concepts

- [How are AVIV ScoutRoute quest element icons selected?](quest-definition-element-icons.md)
- [What are AVIV ScoutRoute quest feature presets?](quest-definition-feature-presets.md)
- [What is the AVIV ScoutRoute Quest Definition Creator?](quest-definition-creator.md)
