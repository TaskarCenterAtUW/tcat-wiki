---
uid: 87222545-eb8a-4e8e-a918-d3462951eaca
title: What does the workspace dashboard show?
slug: workspace-dashboard
doc_type: concept
questions:
    - What does the workspace dashboard show?
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
last_reviewed: 2026-09-29
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The workspace dashboard is the dataset editor itself.
        - Dashboard metadata proves that the data is current or published.
        - Workspace pins are shared project-group settings.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-metadata.md
    - assistant/workspaces/workflow/create-workspace.md
    - workspaces/user-manual/dashboard.md
tags:
    - Assistant
---

<!-- @format -->

# What does the workspace dashboard show?

## Short Answer

The workspace dashboard is where users select and inspect workspaces, including a map preview, project-group context, and workspace metadata such as the Workspace ID. Users can pin one workspace per project group and open a selected workspace through a `workspace` URL query parameter.

## Significance

The dashboard helps users identify the right workspace before editing, reviewing, or changing settings.

## What This Means

Verify the workspace title, Workspace ID, source context, project group, and current status before taking action. Pins are stored in the current browser for the signed-in TDEI user, not as a project-group setting. A dashboard link such as `/dashboard?workspace=123` selects workspace ID `123` when the user can access it.

## What This Does Not Mean

Dashboard information does not by itself prove data completeness, current synchronization, review approval, or public release. The **No dataset area has been set for this workspace** notice concerns dataset-area metadata; the map preview's **This workspace is empty** message concerns the absence of map data. These messages are not interchangeable.

## How To Use This

Use the dashboard to select the workspace, then open the task-specific editor or settings workflow. Workspaces uses TDEI SSO through **TDEI Login**. When the session expires, users can sign in again from the recovery prompt and return to the requested page; login and logout changes synchronize across open Workspaces tabs. Do not promise that unsaved edits survive a session expiry.

## Example

A coordinator checks the dashboard's workspace title and project-group information before inviting a contributor.

## Assistant Guidance

Cite current interface documentation and ask for the environment or workspace ID when the dashboard differs.

## Related Concepts

 - [What metadata is stored with a workspace?](workspace-metadata.md)
 - [How do I create a workspace?](../workflow/create-workspace.md)
