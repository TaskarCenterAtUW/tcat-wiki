---
uid: 5557b51a-9b2d-4dc4-b0cc-767a4c0d1419
title: How do I set up a Tasking Manager project in Workspaces?
slug: set-up-tasking-manager-project
doc_type: workflow
questions:
    - How do I set up the Tasking Manager in Workspaces?
    - How do I create a project and define task areas in Workspaces?
audiences:
    - planner
    - jurisdiction
    - advocate
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - tasking-manager
    - onboarding
    - project-groups
    - workspace-management
    - collaborative-editing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a project automatically generates task areas.
        - A project in Draft status is ready for contributors to use.
related_pages:
    - assistant/workspaces/concept/project-groups.md
    - assistant/workspaces/workflow/create-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# How do I set up a Tasking Manager project in Workspaces?

## Short Answer

Sign in to [Workspaces](https://workspaces.sidewalks.washington.edu/), select a project group and workspace, open **Projects**, and select **New Project**. Complete the project details, area of interest, settings, and review sections. After creating the project, set the task area size, generate and save tasks, then activate the project when it is ready.

## Significance

This workflow creates the project container and its initial configuration. The project starts in **Draft** status. Generate and save its task areas from the **Tasks** tab, then activate the project when it is ready for contributors.

## What This Means

### Open the project creation form

1. Open [Workspaces](https://workspaces.sidewalks.washington.edu/).
2. Select **TDEI Login** on the Workspaces sign-in page and complete sign-in through TDEI.
3. Open the [Workspaces dashboard](https://workspaces.sidewalks.washington.edu/dashboard).
4. Select the relevant **Project Group**.
5. Select the relevant **Workspace**.
6. Select **Projects**.
7. Select **New Project**.

### Complete Project Details

In **Section 01 - Project Details**, enter the **Project Name**. You can also provide:

- **Description** — optional project information.
- **Imagery URL** — optional imagery JSON or a URL reference for later validation.

### Define the Area of Interest

In **Section 02 - Area of Interest**, define the project area by drawing it on the map or importing a file.

- To draw the area, select the map to insert polygon points and double-click to finish the shape.
- To import the area, upload a `.json` or `.geojson` file. A boundary prepared with a tool such as [geojson.io](https://geojson.io/) can be used as the source file.

### Configure project settings

In **Section 03 - Settings**, configure the project settings:

- **Lock Timeout** — sets when a task lock automatically expires.
- **Review Required** — requires validator review before tasks can be completed.
- **Assign Validators** — assigns validators to the project when available.
- **Instructions** — provides instructions for project participants.

### Review and create the project

1. In **Section 04 - Review**, review the project details and select the control to create the project.
2. Confirm the success message; the project starts in **Draft** status.
3. Open the project and select the **Tasks** tab.
4. Set the task area size between `0.25 km²` and `1 km²`.
5. Select **Generate Tasks** and review the generated task grid.
6. Select **Save Tasks** and confirm that tasks are saved.
7. Select **Continue**, then select **Activate Project** when the project is ready to leave **Draft** status.

## What This Does Not Mean

Creating the project does not by itself mean that task areas have been generated and saved or that the project has been activated for contributors. Confirm the task configuration and project status separately.

## How To Use This

Use this workflow when a project group and workspace already exist and a project manager needs to create a new task-based project. Before creating the project, prepare the project name, optional description, optional imagery reference, area-of-interest geometry, participant instructions, and validator assignments.

## Example

A project manager selects a project group and workspace, opens **Projects → New Project**, enters **Downtown sidewalk survey prep**, imports a `.geojson` area, sets a lock timeout, requires validator review, adds instructions, and creates the project. The manager then opens **Tasks**, sets the task area size, generates and saves the tasks, and selects **Activate Project** once the project is ready for contributors.

## Assistant Guidance

- Distinguish creating the project from generating and saving task areas and from activating the project for contributors.
- Describe **Lock Timeout** as controlling when a task lock automatically expires; do not assume a time unit that the current project guide does not specify.
- Cite the [Workspaces project-creation manual](../../../workspaces/user-manual/projects/create.md) for current task-generation and activation steps.
- Explain that Workspaces and the TDEI Portal use a shared sign-in flow; a redirect between them is part of authentication, not a separate project or workspace.

## Related Concepts

- [Project groups (Workspaces)](../concept/project-groups.md)
- [How do I create a workspace?](create-workspace.md)
- [How do I create a workspace from TDEI?](create-workspace-from-tdei.md)
- [Workspaces project creation manual](../../../workspaces/user-manual/projects/create.md)
