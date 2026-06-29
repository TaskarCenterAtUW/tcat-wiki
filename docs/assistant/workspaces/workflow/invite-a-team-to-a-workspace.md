---
title: "Invite a team to a workspace"
tags:
    - Assistant
slug: invite-a-team-to-a-workspace
doc_type: workflow
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - teams
    - collaboration
    - roles
risk_level: low
authority_level: draft
review_status: draft
last_reviewed: 2026-06-03
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Team invitations are managed through the production Workspaces site
        - Teams control access permissions or RBAC roles within a workspace
        - Teams are the same as TDEI Project Group membership
        - QR codes or invitation links automatically expire or can be revoked from the UI
        - Creating a team is required before editing or viewing a workspace
related_pages:
    - assistant/workflows/workspaces/create-a-workspace-from-tdei.md
    - assistant/workflows/workspaces/edit-accessibility-features-in-a-workspace.md
    - assistant/workflows/workspaces/configure-imagery-layers.md
    - assistant/concepts/workspaces/project-groups.md
    - assistant/questions/workspaces/how-do-team-invitations-work.md
    - workspaces/index.md
    - workspaces/user-manual/workspace-settings.md
---

<!-- @format -->

# Invite a team to a workspace

## Short Answer

Workspaces uses **Teams** as an **attribution label** to track which group of collaborators made which edits. Teams are not an access-control or permission system — they let managers differentiate activity (for example "Team 1 worked on Task A; Team 2 worked on Task B"). To create a team: open Workspaces, log in, switch to the correct project group if needed, select the workspace, open **Settings**, navigate to the **Teams** section, select **New Team**, enter a name, and select **Create**. A **QR code** and shareable link are then available so contributors can associate themselves with that team and have their edits attributed accordingly.

> ⚠️ **This feature is currently deployed on the stage environment only.** Teams functionality is not yet available on the production Workspaces site. Confirm the current deployment status with TCAT before directing users to this workflow.

## Significance

Workspaces supports multi-user editing where different groups may work on different tasks within the same workspace — for example, one team surveys curb ramps while another maps sidewalk connectivity. Teams provide an attribution mechanism so managers can distinguish which edits came from which group, without mixing the two scopes of work in the review or changeset view. The QR code and shareable link make it easy for contributors to join the team that matches their assigned task.

Teams are **separate from** TDEI Project Group membership and roles (RBAC). Project groups are a TDEI-level organizational structure; workspace teams are simply labels on edits for attribution and differentiation.

## What This Means

**Prerequisites**

- You need a Workspaces account with access to the relevant project group.
- The workspace must already exist (see [Create a workspace from TDEI](create-a-workspace-from-tdei.md)).
- This workflow is currently available **on the stage environment** (`workspaces-stage.sidewalks.washington.edu`).

**Step-by-step**

1. **Open Workspaces** and **log in** with your credentials.
2. **Switch project group** if you belong to multiple groups and need to access workspaces under a different group.
3. **Select the workspace** you want to set up teams in.
4. **Open Settings** for that workspace.
5. **Switch to the Teams section** in the settings panel.

    _The following steps are confirmed from the stage environment:_

6. Select the **New Team** button.
7. In the **"Create a Team"** popup, enter a **Team Name**.
8. Select **Create**.
9. The new team appears. Select the **QR code button** next to the team.
10. A **"Join this Team"** popup appears, showing:
    - A **QR code** that contributors scan to associate themselves with the team.
    - A **shareable link** to distribute to contributors.
    - **Download QR Code** button to save the QR image.
    - **Close** button to dismiss the popup.

Example link format:

```
https://workspaces-stage.sidewalks.washington.edu/workspace/1893/teams/7
```

Once contributors scan the QR code or follow the link and log in, their subsequent edits in that workspace are attributed to that team. Managers can then filter or review edits by team in the changeset or review views.

## What This Does Not Mean

- **Not an access-control mechanism** — Teams do not grant or revoke permissions to edit a workspace. They are attribution labels only. Contributors do not need to join a team to edit; teams simply let managers differentiate who did what.
- **Not a role or permission system** — Workspace teams are separate from the TDEI RBAC system (roles, project group memberships). See [Review workspace edits](review-workspace-edits.md) for the review/changeset UI.
- **Not the same as TDEI Project Groups** — Project groups are a TDEI-level organizational structure (see [Project groups](../concept/project-groups.md)). Workspace teams are workspace-scoped attribution labels and are independent of project group membership.
- **Not a permanent authentication credential** — Sharing a link or QR code is an attribution aid, not a password, API key, or permission grant.
- **Not required for solo editing** — You can edit a workspace without creating or joining any team. Teams are only needed when you want to differentiate activity between groups.
- **Not available in production yet** — This workflow is only on the stage environment. Confirm deployment status before directing users.

## How To Use This

**Recommended flow**

1. Ensure you have a **Workspaces account** and belong to the correct project group.
2. [Create a workspace](create-a-workspace-from-tdei.md) or open an existing one.
3. Open **Settings → Teams**.
4. Create a team with a descriptive name (for example "Curb Ramp Survey – Team A").
5. Share the **QR code** or **link** with the contributors assigned to that task.
6. Contributors scan the QR code or open the link to associate themselves with the team.
7. Their edits are now attributed to that team in the Workspaces review view.

**Practical tips for managers**

- Name teams according to the task or scope they are assigned to (for example by geography, feature type, or shift), so the attribution is meaningful in review.
- You can create multiple teams per workspace — for example "Team 1 – Downtown Sidewalks" and "Team 2 – Downtown Crossings"—to separate workstreams.
- The shared link follows the format `https://workspaces-stage.sidewalks.washington.edu/workspace/{id}/teams/{team_id}` — you can copy and send it through email, chat, or printed materials.
- Download the QR code for physical handouts at events or field meetings.
- Confirm with TCAT whether this feature has been promoted to production before publishing instructions that reference the stage URL.

## Example

A transit agency creates a workspace for a downtown accessibility survey. The project lead creates two teams in **Settings → Teams**: "Team 1 – Curb Ramps" and "Team 2 – Sidewalk Connectivity." At an event, Team 1 volunteers scan the QR code for their team and field-edit curb ramp data in AVIV ScoutRoute; Team 2 volunteers scan a different QR code and map sidewalk connections. Later, the manager opens the review view, filters by team, and inspects each group's changesets separately — seeing clearly which edits came from which team without having to ask contributors to self-report their assignments.

## Assistant Guidance

- **Always confirm deployment status** before directing users to this workflow. The feature is on stage only as of June 2026; do not assume production availability.
- If a user asks about inviting teams on the production site, state clearly that the feature is not yet deployed there and suggest they confirm with TCAT.
- **Teams are attribution labels, not access control.** If a user asks whether team invites grant edit permissions, clarify the distinction.
- Distinguish **workspace teams** from **TDEI Project Groups** when users confuse the two concepts. Link to the [Project groups](../concept/project-groups.md) concept page.
- The example link (`workspaces-stage.sidewalks.washington.edu/workspace/1893/teams/7`) is illustrative; workspace and team IDs will differ per workspace. Do not hardcode specific IDs in answers.
- For questions about review and filtering by team, refer to [Review workspace edits](review-workspace-edits.md).
- The [How do team invitations work?](../concept/team-invitations.md) question stub is a companion page for assistant Q&A — link there when a user asks a direct question about team invitations.

## Related Concepts

- [Create a workspace from TDEI](create-a-workspace-from-tdei.md)
- [Edit accessibility features in a workspace](edit-accessibility-features-in-a-workspace.md)
- [Review workspace edits](review-workspace-edits.md)
- [Configure imagery layers](configure-imagery-layers.md)
- [Project groups (Workspaces)](../concept/project-groups.md)
- [How do team invitations work?](../concept/team-invitations.md)
- [Workspace Settings](../../../workspaces/user-manual/workspace-settings.md)
