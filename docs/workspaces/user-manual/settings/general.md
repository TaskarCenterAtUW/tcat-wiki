---
title: Workspace Settings — General
nav_order: 6
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Workspace Settings — General

This section explains how to rename a workspace, configure external app access, define custom imagery, and delete a workspace.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._{ .guides-list-ref }

---

### Workspace settings

![Workspaces Workspace Settings page showing the General, External Apps, Custom Imagery, and Delete Workspace sections](../../../resources/images/workspaces/user-manual/05-settings/06-general/01-general-light.avif#only-light)
![Workspaces Workspace Settings page showing the General, External Apps, Custom Imagery, and Delete Workspace sections](../../../resources/images/workspaces/user-manual/05-settings/06-general/01-general-dark.avif#only-dark)

#### General

Use the **General** section to rename the workspace and configure contributor changeset review.

Workspace owners and TDEI Project Group admins (POCs) can change workspace settings. Other members can view the settings page, but controls such as **Rename**, workspace publishing, quest-definition settings, imagery settings, and deletion can be disabled.

![Workspace General settings showing the Workspace Title field, Rename button, and contributor changeset review toggle](../../../resources/images/workspaces/user-manual/05-settings/06-general/02-title-and-flag-light.avif#only-light)
![Workspace General settings showing the Workspace Title field, Rename button, and contributor changeset review toggle](../../../resources/images/workspaces/user-manual/05-settings/06-general/02-title-and-flag-dark.avif#only-dark)

- **Workspace Title**

To rename a workspace, enter the new name in **Workspace Title**, then select **Rename**.

- **Auto-flag contributor changesets for review**

Enable this option to automatically flag changesets created by contributors for review in the review queue. Contributors are described in the page as non-leads and non-validators.

#### External Apps

Use the **External Apps** section to publish the workspace for external apps, configure AVIV ScoutRoute Long Form Quest Definitions, and define custom imagery.

![External Apps settings showing workspace publishing, quest-definition options, Quest Definition URL, and Save](../../../resources/images/workspaces/user-manual/05-settings/06-general/03-external-apps-light.avif#only-light)
![External Apps settings showing workspace publishing, quest-definition options, Quest Definition URL, and Save](../../../resources/images/workspaces/user-manual/05-settings/06-general/03-external-apps-dark.avif#only-dark)

- **Publish the workspace**

Enable **Publish this workspace for external apps** to make the workspace available for contributions through [AVIV ScoutRoute](../../../aviv-scoutroute/index.md), then select **Save**.

- **AVIV ScoutRoute Long Form Quest Definitions**

Choose one of the available quest-definition sources:

1. **Define quests in Workspaces** to enter the definition in JSON format directly on Workspaces.
2. **Load quest definitions from an external URL** to provide the address of a quest-definition JSON document in **Quest Definition URL**.

Select **Save** after changing the quest-definition settings.

#### Custom Imagery

Enter a Custom Imagery Definition in **Imagery JSON Definition**, then select **Save**. The help text below the field links to the required **JSON Schema** and an **example**.

![Custom Imagery settings showing the Imagery JSON Definition field, schema and example links, and Save](../../../resources/images/workspaces/user-manual/05-settings/06-general/04-custom-imagery-light.avif#only-light)
![Custom Imagery settings showing the Imagery JSON Definition field, schema and example links, and Save](../../../resources/images/workspaces/user-manual/05-settings/06-general/04-custom-imagery-dark.avif#only-dark)

!!! note "JSON definitions"

    Enter valid JSON in the definition fields. Refer to the [AVIV ScoutRoute Long Form Quest Definition guide](../../../aviv-scoutroute/quests/index.md) for quest-definition concepts.

#### Delete Workspace

!!! danger "Permanent action"

    Deleting a workspace is permanent. It does not modify TDEI datasets outside Workspaces.

![Delete Workspace section showing the permanent-action warning and delete confirmation button](../../../resources/images/workspaces/user-manual/05-settings/06-general/05-delete-light.avif#only-light)
![Delete Workspace section showing the permanent-action warning and delete confirmation button](../../../resources/images/workspaces/user-manual/05-settings/06-general/05-delete-dark.avif#only-dark)

To begin deleting the workspace, select **I understand, and I want to delete this workspace**. Follow the confirmation step shown by Workspaces before completing the deletion.

When you are not an owner, Workspaces displays that only workspace owners can delete the workspace and disables the delete control.

---

**Previous:** [Workspace Settings](index.md) | **Next:** [Workspace Settings — Members](members.md)
