---
uid: 01ed2c86-c164-45c2-aa45-f8ec8de639c1
title: How does Workspaces team membership differ from project access?
slug: workspace-team-membership
doc_type: concept
questions:
    - How does Workspaces team membership differ from project access?
audiences:
    - jurisdiction
    - planner
products:
    - Workspaces
topics:
    - workspaces
    - teams
    - roles
    - onboarding
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
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/workspace-roles-and-project-roles.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# How does Workspaces team membership differ from project access?

## Short Answer

A Workspaces team groups contributors within a workspace, while project-group membership controls broader access to project data.

## Significance

Teams can separate contractor groups or regional contributors without creating separate source projects.

## What This Means

Use team membership for organization and workspace-level participation. The API documents team-member routes separately from workspace-role routes; that separation does not define a complete access or permission matrix.

## What This Does Not Mean

A team QR code is not the same as a project-group invite.

## How To Use This

Confirm project membership before assigning or joining a team.

## Example

A regional coordinator creates one team for each contractor group within a shared workspace.

## Assistant Guidance

Ask whether the user needs team membership, a workspace role, or TDEI Project Group access. The [Workspaces API documentation](https://api.workspaces.sidewalks.washington.edu/docs) distinguishes the team-member and workspace-user routes but does not specify all permission effects.

## Related Concepts

- [What are Workspaces teams?](workspace-teams.md)
