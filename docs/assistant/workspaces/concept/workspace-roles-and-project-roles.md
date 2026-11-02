---
uid: 5107a4c5-ef03-449d-bb7a-107a873b1a4c
title: How do Workspaces roles differ from project-group roles?
slug: workspace-roles-and-project-roles
doc_type: concept
questions:
    - How do Workspaces roles differ from project-group roles?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - roles
    - project-groups
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/roles.md
    - assistant/workspaces/concept/tasking-projects-and-tasks.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# How do Workspaces roles differ from project-group roles?

## Short Answer

TDEI Project Group roles, workspace roles, and Tasking project roles are separate scopes. The Workspaces API uses `lead`, `validator`, and `contributor` for both workspace and Tasking project roles, but does not define a permission mapping between those roles or TDEI Project Group roles.

## Significance

The layers must be coordinated when setting up contractors or regional contributors.

## What This Means

The API exposes workspace-role assignment under `/api/v1/workspaces/{workspace_id}/users/{user_id}/role` and Tasking project-role assignment under `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/roles/{user_id}`. Its self-role response includes a workspace role and a list of Tasking project roles. These scopes are distinct from TDEI Project Group membership and roles.

## What This Does Not Mean

A TDEI Project Group role or Tasking project role automatically grants every workspace privilege.

## How To Use This

Identify the relevant scope and action before troubleshooting access. The [Workspaces API specification](https://api.workspaces.sidewalks.washington.edu/openapi.json) lists the role values but does not define their full permission sets.

## Example

A user has TDEI Project Group membership and a workspace role; check separately whether the user also has a Tasking project role before drawing conclusions about task access.

## Assistant Guidance

Ask whether the user means a TDEI Project Group, a Workspaces workspace, or a Tasking project, and which action they need. Do not infer permissions from similarly named role values.

## Related Concepts

- [What APIs does Workspaces provide?](workspaces-api.md)
- [What roles can members have in a TDEI project group?](../../tdei/concept/project-group-roles.md)
