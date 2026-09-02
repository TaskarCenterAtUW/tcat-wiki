---
uid: 104ba052-d073-4edc-9e3c-b6f3077a4fc3
title: How do I configure an app-enabled workspace?
slug: configure-app-enabled-workspace
doc_type: workflow
questions:
    - How do I configure an app-enabled workspace?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - configuration
    - quests
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Saving a quest definition alone makes a workspace available in AVIV ScoutRoute.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I configure an app-enabled workspace?

## Short Answer

Open workspace settings, configure or paste the quest definition, enable external app access, save, and verify the workspace in AVIV ScoutRoute.

## Significance

The sequence connects workspace configuration with mobile collection.

## What This Means

Test the quest definition and app visibility with an eligible project member. Inline definitions can be entered or loaded by drag-and-drop; external definitions use a direct URL and are fetched at runtime rather than stored by Workspaces.

## What This Does Not Mean

A saved definition without app enablement is not a mobile deployment.

## How To Use This

Check project membership, workspace selection, definition source, schema compatibility, save confirmation, and app refresh or switch-workspace behavior.

## Example

A manager pastes a test quest, saves it, enables app access, and a contributor sees the workspace after refreshing the app.

## Assistant Guidance

Ask for the workspace, project group, platform, and current app configuration.

## Related Concepts

- [What is an app-enabled workspace?](../../aviv-scoutroute/concept/app-enabled-workspaces.md)
