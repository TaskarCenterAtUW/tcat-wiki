---
uid: 68dbba63-5f2c-4d43-bb91-39114a546e56
title: How do I create a workspace from TDEI?
slug: create-workspace-from-tdei
doc_type: workflow
questions:
    - How do I create a workspace from TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - onboarding
    - project-groups
    - workspace-management
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a workspace from TDEI edits or publishes the source dataset.
        - A newly created workspace is automatically synchronized with TDEI.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-creation-mechanics.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
tags:
    - Assistant
---

<!-- @format -->

# How do I create a workspace from TDEI?

## Short Answer

To create a workspace from TDEI, select the intended dataset and version, provide the required workspace and project-group information, submit the creation request, and wait for initialization. Verify the resulting workspace and source context before editing.

## Significance

The workflow creates a controlled copy and establishes the lineage needed for later review and export.

## What This Means

Confirm environment, permissions, dataset scope, version, workspace title, and project group. Record the resulting workspace ID and source details.

## What This Does Not Mean

Creation does not modify the TDEI source, guarantee freshness, or publish the workspace.

## How To Use This

Follow the current TDEI and Workspaces interface; if a dataset, version, or permission is missing, stop and resolve it before creating the workspace.

## Example

A planner selects a released pedestrian dataset, creates a named workspace in the correct project group, waits for initialization, and checks the dashboard.

## Assistant Guidance

Cite current interface instructions and ask for the environment when the screen sequence differs.

## Related Concepts

 - [What happens when I create a workspace from TDEI?](../concept/workspace-creation-mechanics.md)
 - [Is a workspace a copy or the original dataset?](../concept/workspace-as-dataset-copy.md)
