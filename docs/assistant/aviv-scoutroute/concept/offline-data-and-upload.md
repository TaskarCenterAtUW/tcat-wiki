---
uid: 9e865fd0-fe83-4ee2-be27-e8d0a179b590
title: How does AVIV ScoutRoute handle downloaded data and uploads?
slug: offline-data-and-upload
doc_type: concept
questions:
    - How does AVIV ScoutRoute handle downloaded data and uploads?
    - Can I download AVIV ScoutRoute data before a field survey?
audiences:
    - advocate
    - public
    - planner
    - developer
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - data-freshness
    - field-data-collection
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - ../workflow/manage-quest-visibility.md
    - quest-contributions.md
    - ../../../aviv-scoutroute/user-manual/app-settings.md
tags:
    - Assistant
---

<!-- @format -->

# How does AVIV ScoutRoute handle downloaded data and uploads?

## Short Answer

AVIV ScoutRoute can download data for the visible map area. The current user manual describes this as preparation for limited connectivity and warns that it does not guarantee every app operation will work offline. It describes submitted quest answers as saved to the workspace through changesets, but does not specify an automatic-versus-manual upload setting.

## Significance

Preloading data can help contributors prepare for areas with limited connectivity, but downloading map data and submitting quest answers are separate operations with different offline requirements.

## What This Means

Move the map to the survey area and select the downward-arrow control to download data for the visible area. The user manual says submitted quest answers are saved to the workspace through a changeset. It does not specify an automatic-versus-manual upload preference; confirm behavior for the app version and connectivity in use rather than assuming submissions remain queued locally.

## What This Does Not Mean

Downloaded data is not a guarantee of current information or complete offline functionality. The manual does not document a separate setting to defer answer uploads, so do not describe submitted answers as remaining locally queued for later manual upload.

## How To Use This

Download the relevant area before a survey when appropriate. Because downloaded map data does not guarantee offline submission, verify connectivity and follow project procedures when confirming that a contribution was saved to the workspace.

## Example

A contributor uses Wi-Fi to download the visible survey area before walking a route. The contributor understands that this may help with limited connectivity but does not guarantee all app operations will work offline.

## Assistant Guidance

Ask for the platform, app version, connectivity, and downloaded area. Do not claim that the current documentation provides a separate upload setting or promise that a downloaded area supports offline submission.

## Related Concepts

- [What do quest contributions change?](quest-contributions.md)
- [What is a quest?](quest.md)
- [AVIV ScoutRoute User Manual: Map Interface](../../../aviv-scoutroute/user-manual/map-interface.md)
- [AVIV ScoutRoute User Manual: Completing Quests](../../../aviv-scoutroute/user-manual/completing-quests.md)
