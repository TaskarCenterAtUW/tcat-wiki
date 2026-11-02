---
uid: fe334631-ca62-41b1-b4f6-0684ddc62d02
title: What roles exist in Workspaces?
slug: roles
doc_type: concept
questions:
    - What roles exist in Workspaces?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - collaborative-editing
    - teams
    - roles
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-30
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-roles-and-project-roles.md
    - assistant/workspaces/concept/manager-role.md
    - assistant/workspaces/concept/tasking-projects-and-tasks.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# What roles exist in Workspaces?

## Short Answer

Workspaces documents workspace-scoped roles and separate Tasking project-scoped roles. The API schema uses `lead`, `validator`, and `contributor` for both role types, but does not define the permissions attached to those labels. TDEI Project Group roles are a separate layer.

## Significance

Explicit role boundaries help teams delegate edits and review without confusing organizational membership with dataset authority.

## What This Means

The API documents workspace-role operations under `/api/v1/workspaces/{workspace_id}/users` and Tasking project-role operations under `/api/v1/workspaces/{workspace_id}/tasking/projects/{project_id}/roles`. Both role enums contain `lead`, `validator`, and `contributor`. The schema does not specify the exact permissions granted by each value.

## What This Does Not Mean

A role label alone does not establish that a user can view, edit, review, export, or publish every workspace. Matching labels at workspace and Tasking project scope do not establish matching permissions or equivalence to TDEI Project Group roles.

## How To Use This

Identify whether the question concerns a TDEI Project Group, a workspace, or a Tasking project. Verify the current role and action in the relevant product documentation rather than inferring permissions from the role name.

## Example

A project member can see a workspace but needs a workspace-specific editor or reviewer role to perform the requested action.

## Assistant Guidance

Ask which workspace, Tasking project, TDEI Project Group, and action are involved. Cite the [Workspaces API documentation](https://api.workspaces.sidewalks.washington.edu/docs) for the role values, but do not infer their permission matrix from the schema.

## Related Concepts

- [How do workspace and project-group roles differ?](workspace-roles-and-project-roles.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [What does the manager role do?](manager-role.md)
