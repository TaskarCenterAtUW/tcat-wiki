---
uid: b96f1524-81e2-49ad-aebe-96f65d155d87
title: What is an app-enabled workspace?
slug: app-enabled-workspaces
doc_type: concept
questions:
    - What is an app-enabled workspace?
    - Why does a workspace need app enablement for AVIV ScoutRoute?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
    - Workspaces
topics:
    - aviv-scoutroute
    - workspaces
    - configuration
    - quests
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every workspace is automatically visible in AVIV ScoutRoute.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/workflow/join-a-project-and-find-quests.md
tags:
    - Assistant
---

<!-- @format -->

# What is an app-enabled workspace?

## Short Answer

An app-enabled workspace is configured to appear in AVIV ScoutRoute for eligible project members. It provides the workspace and its quests as a mobile survey destination.

## Significance

Workspace configuration determines whether contributors can see a project in the app. A dataset can exist in Workspaces without being available for mobile quests.

## What This Means

Project administrators must configure the workspace for app access and provide appropriate quests, either directly or through the supported definition URL. App access must be enabled after workspace creation. Users must also belong to the associated project group. After login, eligible users select an available workspace from the app. This supports targeted feature contributions rather than unrestricted editing of the entire dataset.

## What This Does Not Mean

App enablement does not make a workspace public or guarantee that every user can access it. Membership, coverage, and quest configuration still matter.

## How To Use This

When troubleshooting visibility, check app enablement, project membership, workspace coverage, and quest definitions. Confirm the current product settings because the interface may change.

## Example

A project group contains two workspaces, but only one is app-enabled. A member using AVIV ScoutRoute sees only the configured workspace.

## Assistant Guidance

Treat “app-enabled” as a configuration state, not a guarantee of access. Ask for the project group and workspace before diagnosing missing quests.

## Related Concepts

- [How do I join a project and find quests in AVIV ScoutRoute?](../workflow/join-a-project-and-find-quests.md)
