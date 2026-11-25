---
uid: 68dbba63-5f2c-4d43-bb91-39114a546e56
title: How do I create a workspace from TDEI?
slug: create-workspace-from-tdei
doc_type: workflow
questions:
    - How do I create a workspace from TDEI?
    - How do I create a Workspace from a dataset in TDEI?
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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-creation-mechanics.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - workspaces/user-manual/create.md
    - workspaces/user-manual/dashboard.md
tags:
    - Assistant
---

<!-- @format -->

# How do I create a workspace from TDEI?

## Short Answer

In Workspaces, choose **Create Workspace** and **Create From TDEI**, enter a workspace title, select a project group and dataset, review the dataset details and map preview, then select **Create Workspace**. Wait for setup to finish and verify the source information on the Dashboard before editing.

## Significance

The workflow creates a controlled copy and establishes the lineage needed for later review and export.

## What This Means

1. Open **Create Workspace** and select **Create From TDEI**.
2. Enter a **Workspace Title** and select the intended **Project Group**.
3. Select the TDEI dataset and review its available details and map preview.
4. Select **Create Workspace** and wait while Workspaces initializes the copy.
5. On the Dashboard, verify the workspace, its source TDEI dataset ID, and the available version information before editing.

You can also select **Open in Workspaces** from a TDEI Portal dataset's action menu. Confirm that the dataset and project group are the intended ones before continuing.

## What This Does Not Mean

Creation makes a separate workspace copy; it does not modify the TDEI source, guarantee that the source is the newest available release, or publish the workspace.

## How To Use This

Use the current interface and confirm the dataset ID, project group, and setup status. If the intended dataset is unavailable or the workspace remains in setup, resolve that issue before editing.

## Example

A planner opens **Create Workspace → Create From TDEI**, selects a dataset and project group, reviews the map preview, creates the workspace, waits for setup to finish, and checks its source ID on the Dashboard.

## Assistant Guidance

Cite current interface instructions and ask for the environment when the screen sequence differs.

## Related Concepts

- [What happens when I create a workspace from TDEI?](../concept/workspace-creation-mechanics.md)
- [Is a workspace a copy or the original dataset?](../concept/workspace-as-dataset-copy.md)
