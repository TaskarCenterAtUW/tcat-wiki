---
uid: a4ad0bc0-677f-4e0e-ad70-b6b898cc22d8
title: How can quest definitions request photographs?
slug: quest-definition-picture-questions
doc_type: concept
questions:
    - How can quest definitions request photographs?
    - How does a contributor take a photo for an AVIV ScoutRoute quest?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - field-data-collection
    - documentation
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Quest photos are private to the project team without checking the current workflow.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/workspaces/concept/public-availability-of-quest-photos.md
    - aviv-scoutroute/user-manual/quest-types.md
tags:
    - Assistant
---

<!-- @format -->

# How can quest definitions request photographs?

## Short Answer

A quest definition can include a photo question to document new, changed, or otherwise relevant infrastructure.

## Significance

Photos can capture conditions that existing imagery cannot show, especially after construction.

## What This Means

When a quest requests a photo, the Android form presents a **Please take a photo of the location** control. The contributor opens the camera, captures and confirms an image, and returns to the quest; the form can show an upload confirmation. A previously attached image may offer options to retake or remove it. Exact labels and behavior are version-sensitive.

## What This Does Not Mean

A photo request does not replace geometry, attribute, or privacy review.

## How To Use This

Explain what the image should document and how it will be handled. Ask contributors to capture only necessary, permitted images, and check current privacy and publication rules before deployment.

## Example

A curb-ramp quest asks the contributor for a location photo. The contributor selects the ramp answer, captures and confirms an image, checks the upload confirmation, and submits the quest responses.

## Assistant Guidance

Confirm current privacy, licensing, and publication rules before recommending photo questions. Do not infer access or retention from the fact that an image upload succeeded.

## Related Concepts

- [Who can access photos collected through quests?](../../workspaces/concept/public-availability-of-quest-photos.md)
- [AVIV ScoutRoute Quest Types user manual](../../../aviv-scoutroute/user-manual/quest-types.md)
