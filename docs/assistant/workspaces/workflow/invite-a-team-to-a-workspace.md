---
title: Invite a team to a workspace
slug: invite-a-team-to-a-workspace
doc_type: workflow
questions:
    - How do I invite a team to a workspace?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - teams
    - collaborative-editing
    - roles
risk_level: low
authority_level: provisional
publication_status: draft
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
    - assistant/workspaces/workflow/create-workspace-from-tdei-dataset.md
    - assistant/workspaces/workflow/edit-accessibility-features-in-a-workspace.md
    - assistant/workspaces/workflow/configure-imagery-layers.md
    - assistant/tdei/concept/project-group.md
    - workspaces/index.md
    - workspaces/user-manual/workspace-settings.md
tags:
    - Assistant
---

<!-- @format -->

# Invite a team to a workspace

## Short Answer

The stage Workspaces interface includes a **Teams** section where a manager can create a team and open a QR/share dialog. The observed interface does not establish whether teams control access, associate contributors, attribute edits, or support review filtering. To inspect the available controls: open Workspaces, log in, switch to the correct project group if needed, select the workspace, open **Settings**, navigate to the **Teams** section, select **New Team**, enter a name, and select **Create**.

> ⚠️ **This feature is currently deployed on the stage environment only.** Teams functionality is not yet available on the production Workspaces site. Confirm the current deployment status with TCAT before directing users to this workflow.

## Significance

Workspaces supports multi-user editing, and the stage interface exposes a Teams control. The available evidence confirms the control sequence and a QR/share dialog, but does not confirm the feature's operational semantics or production availability.

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

    _The following controls were observed in the stage environment; their operational effect is not confirmed:_

6. Select the **New Team** button.
7. In the **"Create a Team"** popup, enter a **Team Name**.
8. Select **Create**.
9. The new team appears. Select the **QR code button** next to the team.
10. A **"Join this Team"** popup appears, showing:
    - A **QR code** that contributors scan to associate themselves with the team.
    - A **shareable link** to distribute to contributors.
    - **Download QR Code** button to save the QR image.
    - **Close** button to dismiss the popup.

The observed dialog includes a QR code, a shareable link, a **Download QR Code** button, and a **Close** button. Do not infer from these controls that contributor association, edit attribution, permissions, or review filtering is available.

## What This Does Not Mean

- **Not confirmed as an access-control mechanism** — The observed stage interface does not establish whether Teams grant or revoke permissions.
- **Not confirmed as a role or permission system** — Do not equate Teams with TDEI roles or project-group membership without current product documentation.
- **Not confirmed as an attribution system** — The observed QR/share dialog does not establish how edits or contributors are recorded.
- **Not a basis for credential assumptions** — Do not treat a QR code or link as a password, API key, or permission grant.
- **Not available in production yet** — This workflow is only on the stage environment. Confirm deployment status before directing users.

## How To Use This

**Recommended flow**

1. Ensure you have a **Workspaces account** and belong to the correct project group.
2. [Create a workspace](create-a-workspace-from-tdei.md) or open an existing one.
3. Open **Settings → Teams**.
4. Create a team with a descriptive name (for example "Curb Ramp Survey - Team A").
5. Share the **QR code** or **link** with the contributors assigned to that task.
6. Confirm the current behavior with TCAT before distributing the QR code or link or relying on it for project operations.

**Practical tips for managers**

- Use descriptive team names only if the feature's intended operational use has been confirmed.
- Do not rely on the displayed link or QR code for access, attribution, or review workflows until those behaviors are documented.
- Confirm with TCAT whether this feature has been promoted to production before publishing instructions that reference the stage URL.

## Example

A transit agency inspects the stage Teams interface while preparing a downtown accessibility survey. The project lead opens **Settings → Teams**, creates a team, and records the controls displayed in the resulting QR/share dialog. The agency confirms the intended semantics with TCAT before distributing the link or using the feature for field operations.

## Assistant Guidance

- **Always confirm deployment status** before directing users to this workflow. The feature is on stage only as of June 2026; do not assume production availability.
- If a user asks about inviting teams on the production site, state clearly that the feature is not yet deployed there and suggest they confirm with TCAT.
- Do not claim that Teams provide access control, contributor association, edit attribution, or review filtering until those behaviors are confirmed.
- Distinguish **workspace teams** from **TDEI Project Groups** and avoid inferring a relationship from the stage UI.
- Do not reproduce a specific stage workspace/team URL in answers.

## Related Concepts

- [Create a workspace from TDEI](create-a-workspace-from-tdei.md)
- [Edit accessibility features in a workspace](edit-accessibility-features-in-a-workspace.md)
- [Review workspace edits](review-workspace-edits.md)
- [Configure imagery layers](configure-imagery-layers.md)
- [Project groups (Workspaces)](../concept/project-groups.md)
- [How do team invitations work?](../concept/team-invitations.md)
- [Workspace Settings](../../../workspaces/user-manual/workspace-settings.md)
