---
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
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Teams control access permissions or RBAC roles within a workspace.
        - Teams are the same as TDEI Project Group membership.
        - Creating a team is required before editing or viewing a workspace.
        - Workspaces Teams are available on the production site.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/team-invitations.md
    - assistant/workspaces/concept/teams-vs-project-groups.md
    - assistant/workspaces/concept/workspace-teams.md
tags:
    - Assistant
---

<!-- @format -->

# What are teams in Workspaces?

## Short Answer

Workspaces Teams are attribution labels for tracking which group of collaborators made edits. They help managers distinguish activity, but they are not an access-control or permissions system. The supplied workflow describes the feature as available on the stage environment, so current deployment status should be confirmed before directing users to it.

## Significance

Teams can help managers separate contributions when different groups work on different tasks in the same workspace. This supports clearer review and attribution without treating a team as a replacement for TDEI Project Group membership or roles.

## What This Means

- A workspace can use separate teams to label different groups or workstreams, such as curb-ramp and sidewalk-connectivity mapping.
- Contributors can associate themselves with a team through a QR code or shareable link made available for that team.
- Team labels distinguish edits; they do not grant or revoke workspace permissions.
- Teams are separate from TDEI Project Groups and their roles.

## What This Does Not Mean

- A team does not control workspace access, permissions, or RBAC roles.
- A team is not the same as TDEI Project Group membership.
- A team is not required for editing or viewing a workspace.
- The feature is not confirmed as available on the production Workspaces site; the supplied workflow identifies the stage environment only.

## How To Use This

Use Teams when a workspace manager needs to distinguish contributions by group, task, or area. First confirm that contributors have the necessary Workspaces and project-group access; then provide the appropriate team QR code or shareable link if attribution grouping is needed. Confirm the current environment and deployment status before giving UI-specific directions.

## Example

A project manager creates separate workspace teams for a curb-ramp survey and a sidewalk-connectivity survey. Contributors use the corresponding QR code or link so their edits can be attributed to the appropriate group, while access permissions continue to come from the existing project and workspace arrangements.

## Assistant Guidance

Explain that Teams label contributions and do not replace permissions or TDEI Project Groups. Cite this article when describing the concept. Because the supplied workflow identifies stage-only availability, verify the current deployment environment before giving exact instructions, and abstain when the user's access or current product version is unclear.

## Related Concepts

- [How do team invitations work?](team-invitations.md)
- [How do teams differ from project groups?](teams-vs-project-groups.md)
- [What are Workspaces teams?](workspace-teams.md)
