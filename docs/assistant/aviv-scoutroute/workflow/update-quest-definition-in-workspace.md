---
title: "How do I update a quest definition in a workspace?"
slug: update-quest-definition-in-workspace
doc_type: workflow
questions:
    - How do I update a quest definition in a workspace?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
    - Workspaces
topics:
    - aviv-scoutroute
    - workspaces
    - quests
    - configuration
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
        - Editing a quest definition changes an app without saving and refreshing the workspace configuration.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest-definition-application.md
tags:
    - Assistant
---

<!-- @format -->

# How do I update a quest definition in a workspace?

## Short Answer

Edit or replace the quest definition in workspace settings, save it, enable app access, and refresh or switch the workspace in AVIV ScoutRoute before testing.

## Significance

This supports rapid iteration while keeping configuration explicit.

## What This Means

Test a small change, answer the resulting quest, and inspect the change in Workspaces review. Long Form Quest Definitions are JSON configurations; the related schema, element query, and icon settings must be compatible with the active workspace.

## What This Does Not Mean

A changed creator file is not automatically deployed to every workspace.

## How To Use This

Record the definition source, workspace, app state, platform, app version, and test result. Refresh or switch the workspace before concluding that a change is active.

## Example

A new streetlight question appears after the workspace definition is saved and the app workspace is reopened.

## Assistant Guidance

Ask which source and workspace configuration are active.

## Related Concepts

- [How is a quest definition applied?](../concept/quest-definition-application.md)
