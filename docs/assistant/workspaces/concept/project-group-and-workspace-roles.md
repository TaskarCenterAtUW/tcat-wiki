---
uid: 51f6b51d-3caf-4def-8352-a3ba9b033ddd
title: How do TDEI project group roles differ from Workspaces roles?
slug: project-group-and-workspace-roles
doc_type: concept
questions:
    - How do TDEI project group roles differ from Workspaces roles?
    - What are the POC and member roles, and what can each role do?
    - What access does a TDEI project group member have in Workspaces?
    - Do Workspaces teams control access?
    - Can a Workspaces role grant TDEI export permission?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - roles
    - teams
    - sandbox-governance
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/roles.md
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/teams-vs-project-groups.md
    - assistant/tdei/concept/project-group.md
    - assistant/workspaces/index.md
    - workspaces/user-manual/settings/members.md
tags:
    - Assistant
---

<!-- @format -->

# How do TDEI project group roles differ from Workspaces roles?

## Short Answer

TDEI Project Group **POCs** (admins) have full control of the workspace and its settings. Project Group members can access and modify workspace data; within that workspace, **Owner** and **Validator** roles add review and settings privileges, while **Member** does not include those additional privileges.

Workspaces **teams** are separate from both. Teams organize contributors and metrics; they do not grant or revoke access.

## Significance

The layers affect different actions: workspace editing, workspace settings, review, project group administration, and TDEI export. Confusing them can cause incorrect access expectations.

## What This Means

- **POC / Project Group Admin** — the Workspaces manual describes POCs as having full control of the workspace and its settings; they can manage member roles when the controls are available.
- **Project Group member** — can access and modify data in the workspace.
- **Workspace Owner** — can review changesets and modify workspace settings.
- **Workspace Validator** — can review changesets.
- **Workspace Member** — can work with workspace data but does not have the additional Owner or Validator privileges.
- **TDEI `osw_data_generator`** — can export workspace data to TDEI; this is a separate TDEI role, not the workspace Member role.

Project Group membership and workspace roles are separate permission layers. Team membership is attribution, not permission.

## What This Does Not Mean

A workspace member list does not replace TDEI Project Group administration. A Team is not an access-control boundary. A workspace Owner is not automatically authorized to export to TDEI; verify the required TDEI role.

## How To Use This

For any access question, identify the project group, workspace, role, and requested action. For export, verify that the user has a POC or `osw_data_generator` role in at least one TDEI Project Group. Use Teams for contribution tracking, not permission changes.

## Example

A Project Group member edits workspace data. A Validator can review changesets and an Owner can also modify workspace settings, while a POC has full workspace control. Export still requires the separate TDEI role documented for that action.

## Assistant Guidance

This is provisional guidance, not a complete permission matrix. Cite current Workspaces and TDEI documentation. Abstain when the relevant role, workspace, project group, or export requirement cannot be verified.

## Related Concepts

- [Workspaces roles](roles.md)
- [Workspaces teams](teams.md)
- [Teams versus project groups](teams-vs-project-groups.md)
- [TDEI project groups](../../tdei/concept/project-group.md)
