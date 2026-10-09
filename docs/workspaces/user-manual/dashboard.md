---
title: Dashboard
nav_order: 4
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Dashboard

This section explains how to select a project group, find a workspace, and review workspace information on the Workspaces Dashboard.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Select a project group

1. **Open** **Dashboard** from the navigation bar
2. Open the **Project Group** selector
3. **Select** the project group that contains the workspace you want to open

The workspace list updates to show workspaces in the selected project group.

---

### Find and select a workspace

1. Optionally, enter a workspace name in **Search Workspaces** to filter the list
2. **Select** a workspace in the **Workspaces** list
3. Review the selected workspace's status, dataset type, project count, update time, and available actions

The selected workspace appears in the main panel with its map preview and workspace information.

![Workspaces Dashboard showing a selected workspace, map preview, and workspace information](../../resources/images/workspaces/user-manual/04-dashboard/01-dashboard-light.avif#only-light)
![Workspaces Dashboard showing a selected workspace, map preview, and workspace information](../../resources/images/workspaces/user-manual/04-dashboard/01-dashboard-dark.avif#only-dark)

---

### Pin a workspace

Use the pin control on a workspace card to keep that workspace in the **Pinned Workspace** group at the top of the list. Select the control again to unpin it. Only one workspace per project group can be pinned; pinning another workspace in the same group replaces the existing pin.

Pins are saved in the current browser for the signed-in TDEI user. They are not a shared project-group setting.

---

### Review workspace information

The **Workspace Information** panel includes:

- **Projects** — the number of projects in the workspace
- **TDEI Dataset Version** — the version associated with the workspace
- **Workspace ID** — the identifier to use when referring to or opening this workspace
- **Updated At** — the most recent update time
- **Created By** — the user who created the workspace
- **My Role** — your role in the workspace
- **App Access** — whether application access is enabled or disabled
- **From TDEI Dataset ID** — the source TDEI dataset identifier, when applicable
- **TDEI Project Group ID** — the TDEI project group identifier

When the workspace has no dataset-area metadata, the panel displays **No dataset area has been set for this workspace.** This metadata notice is separate from the map preview: when a workspace has no map data, the preview displays **This workspace is empty.**

### Open a workspace from a link

The dashboard URL can identify a workspace with the `workspace` query parameter. For example, `https://workspaces.sidewalks.washington.edu/dashboard?workspace=123` requests workspace ID `123`. Replace `123` with the Workspace ID shown in the information panel. The requested workspace is selected when it is available to your account. If it does not exist or you do not have permission to access it, Workspaces displays **Workspace not found**.

---

### Use workspace actions

The available actions depend on the workspace status and your role. The dashboard may provide controls to:

- **Refresh workspace status**
- Open **Projects**
- Open **Rapid Editor**
- Open the workspace actions menu

When a workspace is still setting up, workspace actions may be disabled until setup finishes.

Open **More workspace actions** to access:

- **Review** — open the workspace review interface
- **Export** — open workspace export options
- **Settings** — open workspace settings

The **My Role** value in **Workspace Information** helps explain why some actions are unavailable. A **Member** can work with workspace data, but role-restricted actions such as reviewing changesets, changing settings, or uploading an export to TDEI require the appropriate workspace or TDEI project-group role.

---

**Previous:** [Create a Workspace](create.md) | **Next:** [Workspace Settings](settings/index.md)
