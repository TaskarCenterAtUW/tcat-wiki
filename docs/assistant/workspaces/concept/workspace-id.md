---
uid: 6ec02d37-b8ef-4919-aa7b-b3e33e2b37ef
title: What is the workspace ID used for?
slug: workspace-id
doc_type: concept
questions:
    - What is the workspace ID used for?
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
        - A workspace ID identifies a dataset version independently of its environment.
        - Knowing a workspace ID grants access to the workspace.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-dashboard.md
    - assistant/workspaces/workflow/export-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# What is the workspace ID used for?

## Short Answer

The workspace ID identifies a workspace within its Workspaces environment and is used to open the workspace or target workspace-specific API requests. It is not a permission or a dataset-version identifier by itself.

## Significance

Correct identification prevents edits or exports against the wrong workspace.

## What This Means

Extract the ID from the current workspace URL or dashboard, retain the environment with it, and verify the title before using it in a request.

## What This Does Not Mean

An ID alone does not grant access, identify the source release, or prove that the workspace is current.

## How To Use This

Ask for the complete workspace URL or environment when troubleshooting an ID.

## Example

A developer extracts `1074` from a stage workspace URL and uses it with the stage API and matching authorization context.

## Assistant Guidance

Cite the current export or API instructions and avoid exposing tokens or assuming cross-environment IDs.

## Related Concepts

 - [What does the workspace dashboard show?](workspace-dashboard.md)
 - [How do I export a workspace?](../workflow/export-workspace.md)
