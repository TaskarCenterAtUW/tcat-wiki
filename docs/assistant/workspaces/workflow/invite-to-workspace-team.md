---
uid: 4c35b3d6-cbad-43e0-9cb5-6cc7b0a56540
title: How do I invite people to a team in Workspaces?
slug: invite-to-workspace-team
doc_type: workflow
questions:
    - How do I invite people to a team in Workspaces?
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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
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

# How do I invite people to a team in Workspaces?

## Short Answer

To invite people to a team, create the team in a workspace and then open its QR/share dialog. The dialog displays a QR code, a shareable link, and controls to download the QR code or close the dialog. Teams are attribution labels for edits, not an access-control or permission system.

## Significance

The procedure identifies the visible controls needed to create a team and share its invitation information.

## What This Means

**Prerequisites**

- You need a Workspaces account with access to the relevant project group.
- The workspace must already exist (see [Create a workspace from TDEI](create-a-workspace-from-tdei.md)).

**Step-by-step**

1. **Open Workspaces** and **log in**.
2. **Switch project group** if needed.
3. **Select the workspace**.
4. **Open Settings**.
5. **Switch to the Teams section**.
6. Select **New Team**.
7. In the **Create a Team** popup, enter a **Team Name**.
8. Select **Create**.
9. Select the **QR code button** for the new team.
10. In the **Join this Team** popup, use the displayed QR code or shareable link to provide the invitation information to the people you want to invite. The popup also includes **Download QR Code** and **Close** buttons.

Contributors who use the displayed QR code or shareable link can associate their subsequent edits with the team for attribution.

## What This Does Not Mean

- **Not an access-control mechanism** — Teams are attribution labels for edits; they do not grant or revoke workspace permissions.
- **Not the same as TDEI Project Groups** — Project groups are a TDEI-level organizational structure; workspace teams are workspace-scoped attribution labels.

## How To Use This

**Recommended flow**

1. Ensure you have a **Workspaces account** and belong to the correct project group.
2. Open an existing workspace.
3. Open **Settings → Teams**.
4. Create the team and open its **Join this Team** popup.
5. Share the displayed link or downloaded QR code with the intended invitees.

## Example

A project lead opens **Settings → Teams**, creates a team named **Downtown accessibility survey**, and selects its QR code button. The lead then shares the link from the **Join this Team** popup with the people invited to the team.

## Assistant Guidance

- Distinguish **workspace teams** from **TDEI Project Groups** and avoid inferring a relationship between them.

## Related Concepts

- [Create a workspace from TDEI](create-a-workspace-from-tdei.md)
- [Edit accessibility features in a workspace](edit-accessibility-features-in-a-workspace.md)
- [Review workspace edits](review-workspace-edits.md)
- [Configure imagery layers](configure-imagery-layers.md)
- [Project groups (Workspaces)](../concept/project-groups.md)
- [How do team invitations work?](../concept/team-invitations.md)
- [Workspace Settings](../../../workspaces/user-manual/workspace-settings.md)
