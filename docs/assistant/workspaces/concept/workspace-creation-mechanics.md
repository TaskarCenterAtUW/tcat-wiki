---
uid: e2be6bc3-de31-4d51-b9ab-862dfdcc2cb8
title: What happens when I create a workspace from a TDEI dataset?
slug: workspace-creation-mechanics
doc_type: concept
questions:
    - What happens when I create a workspace from a TDEI dataset?
    - What does it mean to check out a TDEI dataset into a Workspace?
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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

In Workspaces, creating a workspace from TDEI selects a dataset and creates a separate copy for editing. Calling this a “check out” describes the copy-and-edit step; the documented workflow is not a lock or an automatic check-in to the source.

## Significance

Understanding the copy step clarifies why later source releases do not automatically appear in the workspace and why lineage must be recorded.

## What This Means

Confirm the source dataset and available version information, workspace title, project group, and creation result before editing. Record the source dataset ID and version shown for the workspace so its lineage is clear.

## What This Does Not Mean

Creation does not change the source dataset, make the workspace public, or create a live link that automatically synchronizes later source updates.

## How To Use This

Use the current creation workflow and retain the resulting workspace identifier and source details.

## Example

A user selects a TDEI dataset, creates a workspace copy in the appropriate project group, waits for initialization, and verifies the source ID and version before editing.

## Assistant Guidance

Cite the creation workflow and abstain when the source version or environment is unknown.

## Related Concepts

- [How do I create a workspace from TDEI?](../workflow/create-workspace-from-tdei.md)
- [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
