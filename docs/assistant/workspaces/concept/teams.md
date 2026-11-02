---
uid: 1540374b-e992-403b-9bbd-61d57b48a163
title: What are teams in Workspaces?
slug: teams
doc_type: concept
questions:
    - What are teams in Workspaces?
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
risk_level: low
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
    - assistant/workspaces/concept/team-invitations.md
    - assistant/workspaces/concept/teams-vs-project-groups.md
    - assistant/workspaces/concept/workspace-teams.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# What are teams in Workspaces?

## Short Answer

Workspaces Teams group collaborators within a workspace and are described in existing workflow material as a way to distinguish contributions. The API reference documents team and membership operations, but does not define permission effects or confirm user-interface availability in a particular environment.

## Significance

Teams can help managers separate contributions when different groups work on different tasks in the same workspace. This supports clearer review and attribution without treating a team as a replacement for TDEI Project Group membership or roles.

## What This Means

- The API schema represents a team with an ID, name, and member count. It documents routes to list, create, retrieve, update, and delete workspace teams, and to list, join, add, or remove members.
- Existing workflow material describes teams as a way to distinguish contributor groups, including through QR codes or shareable links.
- Teams are separate from TDEI Project Groups and workspace roles. The API schema does not describe whether team membership changes edit attribution or access permissions.

## What This Does Not Mean

- Do not infer workspace access or RBAC permissions from team membership; the API schema does not define those effects.
- A team is not the same as TDEI Project Group membership.
- A team is not required for editing or viewing a workspace.
- The API reference at `api.workspaces.sidewalks.washington.edu` documents team routes, but that does not confirm which user-interface features are available in a particular environment.

## How To Use This

Use Teams when a workspace manager needs to distinguish contributions by group, task, or area. First confirm that contributors have the necessary Workspaces and project-group access; then use the current environment's team workflow if attribution grouping is needed. Verify UI availability before giving interface-specific directions.

## Example

A project manager creates separate workspace teams for a curb-ramp survey and a sidewalk-connectivity survey. Contributors use the corresponding QR code or link so their edits can be attributed to the appropriate group, while access permissions continue to come from the existing project and workspace arrangements.

## Assistant Guidance

Explain that Teams do not replace workspace roles or TDEI Project Groups. Cite the [Workspaces API documentation](https://api.workspaces.sidewalks.washington.edu/docs) for documented endpoints and current product documentation for attribution and UI behavior. Do not infer availability or permissions from the API schema alone.

## Related Concepts

- [How do team invitations work?](team-invitations.md)
- [How do teams differ from project groups?](teams-vs-project-groups.md)
- [What are Workspaces teams?](workspace-teams.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
