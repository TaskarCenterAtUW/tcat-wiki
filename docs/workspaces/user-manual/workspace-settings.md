---
title: Workspace Settings
tags:
    - Guide
    - External
    - User
---

<!-- @format -->

## Workspace Settings

This section explains how to use the Workspaces platform to configure Workspace Settings.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Workspace Settings

![Screenshot of the Workspace Settings page in Workspaces.](../../resources/images/workspaces/user-manual/workspace-settings/workspace-settings.png){ width="400" }

#### General

![Screenshot of the General section of the Workspace Settings page in Workspaces.](../../resources/images/workspaces/user-manual/workspace-settings/general.png){ width="400" }

- **Workspace Title**

To rename a Workspace, enter a name into the **"Workspace Title"** text entry box, then select **"Rename"**.

If successful, a toast with the message **"Workspace renamed successfully."** will appear at the top right of the page.

![Screenshot of the General section of the Workspace Settings page with a name entered in Workspace Title and the Rename button highlighted.](../../resources/images/workspaces/user-manual/workspace-settings/general-h-rename.png){ width="400" } ![Screenshot of the General section of the Workspace Settings page with a name entered in Workspace Title and the Rename Success toast.](../../resources/images/workspaces/user-manual/workspace-settings/general-t-rename.png){ width="400" }

#### External Apps

![Screenshot of the External Apps section of the Workspace Settings page in Workspaces.](../../resources/images/workspaces/user-manual/workspace-settings/external-apps.png){ width="400" }

- **Publish**

To control the visibility of a Workspace in external apps such as [AVIV ScoutRoute](../../aviv-scoutroute/index.md), select the toggle button next to **"Publish this Workspace for external apps"** then select **"Save"**.

If successful, the message **"Changes saved."** will appear below the **"Save"** button.

![Screenshot of the External Apps section of the Workspace Settings page with the Publish toggle highlighted.](../../resources/images/workspaces/user-manual/workspace-settings/external-apps-h-publish.png){ width="400" } ![Screenshot of the External Apps section of the Workspace Settings page with the Save button highlighted.](../../resources/images/workspaces/user-manual/workspace-settings/external-apps-h-save.png){ width="400" }

- **AVIV ScoutRoute Long Form Quest Definitions**

To set the [AVIV ScoutRoute Long Form Quest Definition](../../aviv-scoutroute/quests/index.md) for a Workspace, there are two options available:

1. Define quests in Workspaces

Selecting **"Define quests in Workspaces"** expands a **"JSON Quest Definition"** text entry box in which a full AVIV ScoutRoute Long Form Quest Definition can be directly entered.

Workspaces also supports **drag-and-drop** of a JSON file into the **"JSON Quest Definition"** text entry box. If successful, a toast with the message **"JSON file loaded successfully."** will appear at the top right of the page.

Once entered using either method, be sure to select **"Save"**. If successful, the message **"Changes saved."** will appear below the **"Save"** button.

![Screenshot of the External Apps section of the Workspace Settings page with the Define button selected and a quest definition entered in JSON Quest Definition.](../../resources/images/workspaces/user-manual/workspace-settings/external-apps-define.png){ width="400" }

1. Load quest definitions from an external URL

Selecting **"Load quest definitions from an external URL"** expands a **"Quest Definition URL"** text entry box in which a direct link to a full AVIV ScoutRoute Long Form Quest Definition can be entered.

Once entered, be sure to select **"Save"**. If successful, the message **"Changes saved."** will appear below the **"Save"** button.

![Screenshot of the External Apps section of the Workspace Settings page with the Load button selected and a link to a quest definition entered in Quest Definition URL.](../../resources/images/workspaces/user-manual/workspace-settings/external-apps-load.png){ width="400" }

Links are provided below the text box to the AVIV ScoutRoute Long Form Quest Definition [JSON Schema](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-quests/refs/heads/main/schema/schema.json) and an [example](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-quests/refs/heads/main/examples/example.json).

Note that when loading quest definitions from an external URL, Workspaces does not store the quest definition. Instead, the contents of the specified URL will be fetched at runtime when AVIV ScoutRoute requests the quest definition for that Workspace.

- **Custom Imagery**

To set the Custom Imagery list for a Workspace, enter a Custom Imagery Definition into the **"Imagery JSON Definition"** text entry box.

Workspaces also supports **drag-and-drop** of a JSON file into the **"Imagery JSON Definition"** text entry box. If successful, a toast with the message **"JSON file loaded successfully."** will appear at the top right of the page.

Once entered using either method, be sure to select **"Save"**. If successful, the message **"Changes saved."** will appear below the **"Save"** button.

![Screenshot of the Custom Imagery section of the Workspace Settings page with a custom imagery definition entered in Imagery JSON Definition.](../../resources/images/workspaces/user-manual/workspace-settings/custom-imagery.png){ width="400" }

Links are provided below the text box to the AVIV ScoutRoute Custom Imagery Definition [JSON Schema](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/schema/schema.json) and an [example](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/examples/example.json).

- **Delete Workspace**

**Caution! Deleting a Workspace is permanent and cannot be undone.**

This will not remove any TDEI datasets outside of Workspaces.

To delete a Workspace, navigate to the bottom of the Workspace Settings page and select **"I understand, and I want to delete this Workspace."**

![Screenshot of the Delete Workspace section of the Workspace Settings page.](../../resources/images/workspaces/user-manual/workspace-settings/delete-workspace.png){ width="400" }

Then, to confirm that you would like to delete the currently selected Workspace, type "delete" in the deletion confirmation text entry box.

![Screenshot of the Delete Workspace section of the Workspace Settings page.](../../resources/images/workspaces/user-manual/workspace-settings/delete-workspace-delete.png){ width="400" }

Following a short delay after the "Delete this Workspace." button is selected, you will be returned to the Dashboard page.
