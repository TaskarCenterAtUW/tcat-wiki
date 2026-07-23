---
title: "Why can AVIV ScoutRoute quests be hidden or unavailable?"
slug: quest-visibility-and-local-state
doc_type: concept
questions:
    - Why can AVIV ScoutRoute quests be hidden or unavailable?
    - Why are AVIV ScoutRoute quest icons stacked?
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
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A missing AVIV ScoutRoute quest icon proves that no quest exists.
        - Hiding a quest removes it from the workspace for every contributor.
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

Quest visibility depends on workspace configuration, enabled quest types, map zoom, geographic coverage, and local hidden-quest state. Icons can stack when zoomed out.

## Significance

Visibility problems can be mistaken for missing data, missing permissions, or an empty project.

## What This Means

Zoom in to reveal stacked icons. Quest settings can enable or disable types and control display order. A contributor can hide a quest locally and later restore hidden quests. Workspace availability also depends on project membership, app enablement, and coverage.

## What This Does Not Mean

A hidden or unseen icon does not prove that the underlying feature or task is absent. Local hiding does not remove the quest for other contributors.

## How To Use This

Check the selected workspace and map area, zoom in, review enabled quest types, and restore hidden quests when appropriate.

## Example

A contributor sees only two icons while zoomed out, then zooms in and finds additional quests that had been stacked together.

## Assistant Guidance

Ask for workspace, map area, zoom level, enabled quest types, and whether the contributor previously hid the quest. Do not diagnose missing data from an icon alone.

## Related Concepts

- [What is an app-enabled workspace?](app-enabled-workspaces.md)
- [How do I manage quest visibility?](../workflow/manage-quest-visibility.md)
