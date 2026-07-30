---
title: How do TDEI project group roles differ from Workspaces roles?
slug: project-group-and-workspace-roles
doc_type: concept
questions:
    - How do TDEI project group roles differ from Workspaces roles?
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
last_reviewed: 2026-07-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A Workspaces team is an access-control mechanism.
        - Every per-workspace owner can export data to TDEI.
        - A project group member can be removed from editing a workspace by changing only the workspace member list.
related_pages:
    - assistant/workspaces/concept/roles.md
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/teams-vs-project-groups.md
    - assistant/tdei/concept/project-group.md
    - assistant/workspaces/index.md
tags:
    - Assistant
---

<!-- @format -->

# How do TDEI project group roles differ from Workspaces roles?

## Short Answer

TDEI **project group membership** and Workspaces **workspace roles** are separate permission layers. Project group membership may provide baseline access to associated Workspaces data; workspace roles add permissions within a specific workspace.

Workspaces **teams** are separate from both. Teams organize contributors and metrics; they do not grant or revoke access.

## Significance

The layers affect different actions: workspace editing, workspace settings, review, project group administration, and TDEI export. Confusing them can cause incorrect access expectations.

## What This Means

- Check TDEI project group membership first for baseline access.
- Check the per-workspace role for workspace-specific privileges.
- Workspace role changes do not necessarily change project group membership.
- Team membership does not change permissions.
- TDEI roles or dataset checks may still be required for export.

## What This Does Not Mean

A workspace member list does not replace TDEI project group administration. A Team is not an access-control boundary. Identical role labels do not guarantee identical privileges, and a workspace owner is not automatically authorized to export.

## How To Use This

For any access question, identify the project group, workspace, role, and requested action. For export, verify current TDEI authorization and dataset requirements. Use Teams for contribution tracking, not permission changes.

## Example

A project group member edits a workspace with baseline access. A workspace role may permit review or settings management, but TDEI authorization may still be required for export. Joining a Team changes reporting, not access.

## Assistant Guidance

This is provisional guidance, not a complete permission matrix. Cite current Workspaces and TDEI documentation. Abstain when the relevant role, workspace, project group, or export requirement cannot be verified.

## Related Concepts

- [Workspaces roles](roles.md)
- [Workspaces teams](teams.md)
- [Teams versus project groups](teams-vs-project-groups.md)
- [TDEI project groups](../../tdei/concept/project-group.md)
