---
uid: 557c7f7d-8153-4cda-8ad1-1511aad3c7a9
title: Why can AVIV ScoutRoute quests be hidden or unavailable?
slug: quest-visibility-and-local-state
doc_type: concept
questions:
    - Why can AVIV ScoutRoute quests be hidden or unavailable?
    - Why are AVIV ScoutRoute quest icons stacked?
    - Can clustering hide AVIV ScoutRoute quest icons?
    - Can completed answers or recency hide an AVIV ScoutRoute quest?
audiences:
    - advocate
    - public
    - planner
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - workspaces
    - data-freshness
    - data-collection
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - app-enabled-workspaces.md
    - ../workflow/manage-quest-visibility.md
    - ../../../aviv-scoutroute/user-manual/map-interface.md
tags:
    - Assistant
---

<!-- @format -->

# Why can AVIV ScoutRoute quests be hidden or unavailable?

## Short Answer

Quest visibility depends on workspace configuration, enabled quest types, map zoom, geographic coverage, local hidden-quest state, answer completion, and the element's edited timestamp compared with `recency_period`. Nearby quests can also be clustered into one map icon, making individual quests appear hidden.

## Significance

Visibility problems can be mistaken for missing data, missing permissions, or an empty project.

## What This Means

Zoom in to separate clustered icons. The **Manage Quests** screen lets contributors show or hide individual items or quest types using the **Enabled** checkboxes. A hidden individual quest can be restored from **Undo Edits** by selecting its **You hid it** entry and choosing **Undo**. Workspace availability also depends on project membership, app enablement, and coverage.

For a configured quest, the visibility conditions are:

- **Answer completion:** at least one applicable question is unanswered.
- **Recency:** `(now - element.timestampEdited) >= recencyPeriodInDays`.

With `recency_period: 0` set in a quest definition, the recency condition is satisfied immediately, making a completed quest eligible for resurvey even when every applicable question has an answer. This removes the waiting period; workspace configuration, enabled quest types, coverage, local hiding, and map visibility still affect whether it appears.

If all applicable questions are answered and the recency period has not elapsed, the quest is hidden as completed. If the recency period has elapsed, the quest can become visible again with its prior answers available for revalidation.

Questions skipped because they do not apply based on earlier answers do not block completion. When a quest becomes visible again because of recency, previously submitted answers remain stored and can be prefilled for revalidation. The app does not use `ext:gig_complete` or `ext:gig_last_updated` tags for completion or recency.

## What This Does Not Mean

A hidden or unseen icon does not prove that the underlying feature or task is absent. Local hiding does not remove the quest for other contributors. Recency does not delete or invalidate the answers already stored on the element.

## How To Use This

Check the selected workspace and map area, zoom in to separate clustered icons, review enabled quest types in **Manage Quests**, and use **Undo Edits** to restore an individually hidden quest. If the quest remains unavailable, check whether all applicable questions are complete and whether the recency period has elapsed.

## Example

A contributor sees one icon while several nearby quests are clustered. After zooming in, the quests separate. A completed quest remains hidden until its configured recency period elapses, when it reappears with its prior answers for revalidation.

With `recency_period: 0`, a completed quest is immediately eligible for resurvey; existing answers remain stored for review.

## Assistant Guidance

Ask for workspace, map area, zoom level, enabled quest types, answer completion, `recency_period`, element `timestampEdited`, and whether the contributor previously hid the quest. Explain that a zero-day recency period removes the waiting period but does not bypass other visibility conditions or delete answers. Distinguish clustering from quest availability, and do not diagnose missing data from an icon alone or treat completion or recency as answer deletion.

## Related Concepts

- [What is an app-enabled workspace?](app-enabled-workspaces.md)
- [How do I manage quest visibility?](../workflow/manage-quest-visibility.md)
