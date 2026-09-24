---
title: Workspace Settings — Members
nav_order: 7
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Workspace Settings — Members

This section explains how to review workspace roles, assigned member roles, and member privileges in the **Members** section of Workspace Settings.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._{ .guides-list-ref }

---

### Open Members

1. **Open** a workspace from the [Dashboard](../dashboard.md)
2. **Open** **Workspace Settings**
3. **Select** **Members**

When you have the required TDEI Point of Contact (POC) role in the project group, the **Members** page can provide controls for managing workspace member roles. Without that role, Workspaces may restrict role management while still displaying the available role groups.

![Workspace Settings Members page showing project group admins, data generators, and workspace members](../../../resources/images/workspaces/user-manual/05-settings/07-members/01-members-light.avif#only-light)
![Workspace Settings Members page showing project group admins, data generators, and workspace members](../../../resources/images/workspaces/user-manual/05-settings/07-members/01-members-dark.avif#only-dark)

### Review member role groups

The **Members** page organizes roles into three groups:

- **Project Group Admins** — TDEI project group admins, also called POCs, have full control of the workspace and all workspace settings. Listed admins can display a `poc` label.
- **Data Generators** — members with the TDEI `osw_data_generator` role can export workspace data to the TDEI.
- **Workspace Members** — members of the TDEI project group can access and modify data in the workspace.

The **Workspace Members** section identifies additional workspace privileges:

- **Owner** can review changesets and modify workspace settings.
- **Validator** can review changesets.

The page lists workspace members with their assigned roles. When role management is available, a member's role control can show **Owner**, **Validator**, or **Member**.

The page can display an informational message when no member has a particular role. A **Member** role does not provide the additional Owner or Validator privileges. Project Group Admins (POCs) have full control of the workspace and its settings, and Data Generators can export workspace data to the TDEI.

---

### Understand access requirements

The Members page is role-restricted. Do not interpret an empty role group as proof that no users belong to the broader TDEI project group; it indicates that no users with that displayed role are available in the current context.

For team-based attribution labels, refer to [Workspace Settings — Teams](teams.md). Teams are separate from TDEI project group membership and workspace roles.

---

**Previous:** [Workspace Settings — General](general.md) | **Next:** [Workspace Settings — Teams](teams.md)
