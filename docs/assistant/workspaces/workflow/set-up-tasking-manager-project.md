---
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
last_reviewed: 2026-08-20
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

Log in to [Workspaces](https://workspaces.sidewalks.washington.edu/), select a project group and workspace, open **Projects**, and select **New Project**. Complete the project details, area of interest, settings, and review sections. After creating the project, open its **Tasks** tab and define the task area size.

## Significance

This workflow creates the project container and its initial configuration. The project is created in **Draft** status, and task areas still need to be generated or defined from the **Tasks** tab before the project is ready for task-based work.

## What This Means

### Open the project creation form

1. Open [Workspaces](https://workspaces.sidewalks.washington.edu/).
2. Select **Sign In** or open the [Workspaces sign-in page](https://workspaces.sidewalks.washington.edu/signin), then log in.
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

- **Lock Timeout** — sets the number of hours before a task lock automatically expires.
- **Review Required** — requires validator review before tasks can be completed.
- **Assign Validators** — assigns validators to the project when available.
- **Instructions** — provides instructions for project participants.

### Review and create the project

1. In **Section 04 - Review**, review the project details and select the control to create the project.
2. Confirm the success message. A newly created example project reports that it was created successfully, that tasks can be generated and saved from the **Tasks** tab, and that the project is in **Draft** status.
3. Open the project and select the **Tasks** tab.
4. Define the task area size.

## What This Does Not Mean

Creating the project does not by itself mean that task areas have been generated, that the project is published, or that contributors can begin work. Confirm the task configuration and project status separately.

## How To Use This

Use this workflow when a project group and workspace already exist and a project manager needs to create a new task-based project. Before creating the project, prepare the project name, optional description, optional imagery reference, area-of-interest geometry, participant instructions, and validator assignments.

## Example

A project manager selects a project group and workspace, opens **Projects → New Project**, enters **Downtown sidewalk survey prep**, imports a `.geojson` area, sets a lock timeout, requires validator review, adds instructions, and creates the project. The manager then opens **Tasks**, defines the task area size, and keeps the project in **Draft** until its configuration is ready.

## Assistant Guidance

- Distinguish creating the project from defining task areas and from publishing or opening the project to contributors.
- Describe **Lock Timeout** as the period after which a task lock automatically expires.

## Related Concepts

- [Project groups (Workspaces)](../concept/project-groups.md)
- [How do I create a workspace?](create-workspace.md)
- [How do I create a workspace from TDEI?](create-workspace-from-tdei.md)
