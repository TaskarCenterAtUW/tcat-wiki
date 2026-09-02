---
uid: 01a52d4b-20dc-4828-b9be-b79b923b8e60
title: How do team invitations work?
slug: team-invitations
doc_type: concept
questions:
    - How do team invitations work?
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
        - Team invitations grant workspace access or RBAC permissions.
        - Team invitations are managed through the production Workspaces site.
        - QR codes or invitation links automatically expire or can be revoked from the UI.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/teams-vs-project-groups.md
    - assistant/workspaces/workflow/invite-to-workspace-team.md
tags:
    - Assistant
---

<!-- @format -->

# How do team invitations work?

## Short Answer

To invite people to a Workspaces team, create the team in an existing workspace and open its QR-code or sharing dialog. The dialog provides a QR code and a shareable link that contributors can use to associate themselves with the team. Teams are attribution labels, not access-control permissions, and the supplied workflow identifies this feature as available on the stage environment only.

## Significance

A team invitation can help a manager organize contributions from different groups working in one workspace. Separating team attribution supports review of work by task or group, while keeping team invitations distinct from TDEI Project Group membership and workspace permissions.

## What This Means

- The workspace must already exist before a team can be created for it.
- A manager opens the workspace settings, goes to the Teams section, creates a named team, and opens the team's QR-code control.
- The resulting dialog contains a QR code and shareable link; it also provides controls to download the QR code or close the dialog.
- Contributors use the QR code or link to associate themselves with the team, after which subsequent edits can be attributed to that team.
- The supplied workflow identifies the feature as available on the stage environment, not the production site.

## What This Does Not Mean

- A team invitation is not a permission grant or an RBAC role.
- Joining a team is not the same as joining a TDEI Project Group.
- The workflow does not establish that QR codes or links automatically expire or can be revoked from the UI.
- The stage workflow does not establish production availability.

## How To Use This

Before inviting contributors, confirm that they have the required account and project-group or workspace access. In the applicable environment, open the workspace's **Settings → Teams**, create a descriptive team, then share the displayed QR code or link with the intended contributors. Verify the current deployment status before relying on stage-specific controls or URLs.

## Example

A project lead creates a team named **Downtown accessibility survey** in an existing workspace, opens its QR-code dialog, and shares the displayed link with the assigned contributors. The contributors use that invitation information for team attribution; it does not by itself grant them workspace permissions.

## Assistant Guidance

Describe the invitation as a way to associate edits with a team, not as a way to grant access. Cite this article when explaining the invitation flow. Confirm the current environment and product version before giving exact UI directions, and abstain if the user's account, project-group access, or deployment context is missing.

## Related Concepts

- [What are teams in Workspaces?](teams.md)
- [How do teams differ from project groups?](teams-vs-project-groups.md)
- [Invite a team to a workspace](../workflow/invite-to-workspace-team.md)
