---
uid: e2be6bc3-de31-4d51-b9ab-862dfdcc2cb8
title: What happens when I create a workspace from a TDEI dataset?
slug: workspace-creation-mechanics
doc_type: concept
questions:
    - What happens when I create a workspace from a TDEI dataset?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - sandbox-governance
    - dataset-lineage
    - publication-workflow
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a workspace keeps it synchronized with the TDEI source.
        - Workspace creation publishes the copied dataset.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/workflow/create-workspace-from-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# What happens when I create a workspace from a TDEI dataset?

## Short Answer

Creating a workspace from a TDEI dataset selects a source and version, creates a separate workspace copy, and initializes it for editing. The exact processing and status messages depend on the creation method and current environment.

## Significance

Understanding the copy step clarifies why later source releases do not automatically appear in the workspace and why lineage must be recorded.

## What This Means

Confirm the source dataset, version, scope, workspace title, project group, and creation result before editing.

## What This Does Not Mean

Creation does not mean that the source was changed, the workspace is public, or all source metadata and later updates are synchronized.

## How To Use This

Use the current creation workflow and retain the resulting workspace identifier and source details.

## Example

A user chooses a TDEI dataset, creates a workspace, waits for initialization, and verifies the selected workspace before inviting contributors.

## Assistant Guidance

Cite the creation workflow and abstain when the source version or environment is unknown.

## Related Concepts

 - [How do I create a workspace from TDEI?](../workflow/create-workspace-from-tdei.md)
 - [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
