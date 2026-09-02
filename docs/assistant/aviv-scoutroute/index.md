---
uid: d8895c9a-7a18-4506-a8b0-b4d014aacaaf
title: AVIV ScoutRoute — Assistant Knowledge Base
slug: aviv-scoutroute-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the AVIV ScoutRoute knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - tdei-ecosystem
    - field-data-collection
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - AVIV ScoutRoute provides quests everywhere without project configuration.
        - A submitted quest answer is automatically a final published dataset edit.
        - Android and iOS have materially different AVIV ScoutRoute functionality.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
tags:
    - Assistant
---

<!-- @format -->

# AVIV ScoutRoute — Assistant Knowledge Base

## Short Answer

AVIV ScoutRoute is a mobile field-data collection app. It uses project-group membership, configured workspaces, and feature-specific quests to collect pedestrian and accessibility observations.

## Significance

The app connects on-the-ground observations to project datasets. Accurate answers require contributors to inspect the physical feature and report uncertainty rather than guess.

## What This Means

Users register or sign in through TDEI, join the relevant project group, select an app-enabled workspace, inspect quest features, answer questions, and submit contributions. iOS and Android provide nearly identical functionality; installation and permission steps differ.

## What This Does Not Mean

AVIV ScoutRoute is not a global task list, an unrestricted editor, or a guarantee that a submitted answer is immediately published. Availability depends on project, workspace, coverage, and quest configuration.

## How To Use This

Use the current project instructions and product documentation for installation and workspace access. Use direct observation for physical features and verify the active workspace and quest definition when troubleshooting.

## Example

A volunteer registers through a project referral link, opens the app-enabled workspace, answers a sidewalk quest after observing the location, and submits the contribution for the project's review workflow.

## Assistant Guidance

Ask for platform, app version, project group, workspace, and quest definition when diagnosing behavior. Treat installation URLs and UI labels as version-sensitive. Do not promise publication or correction without evidence.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](concept/quest.md)
- [What is an app-enabled workspace?](concept/app-enabled-workspaces.md)
- [How do I join a project and find quests?](workflow/join-a-project-and-find-quests.md)
