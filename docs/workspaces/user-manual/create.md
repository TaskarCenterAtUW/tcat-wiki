---
title: Create a Workspace
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Create a Workspace

This section explains how to create a blank workspace, import a dataset from TDEI, or upload an OpenSidewalks data file.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Choose a creation method

1. **Open** **Create Workspace** in the navigation bar
2. Review the three available creation methods:
    - **Blank Workspace** creates an empty workspace with no data.
    - **From TDEI** creates a workspace by importing an asset stored in TDEI.
    - **From File** creates a workspace from an OpenSidewalks data file on your computer.

3. **Select** **Start** on the method that matches your source data

![Workspaces Create a Workspace page showing Blank Workspace, From TDEI, and From File options](../../resources/images/workspaces/user-manual/03-create/01-create-workspace-light.avif#only-light)
![Workspaces Create a Workspace page showing Blank Workspace, From TDEI, and From File options](../../resources/images/workspaces/user-manual/03-create/01-create-workspace-dark.avif#only-dark)

---

### Create a blank workspace

1. **Select** **Start** under **Blank Workspace**
2. Enter a name in **Workspace Title**
3. Select a **Project Group**
4. Under **Dataset Type**, select **OpenSidewalks** or **GTFS Pathways**
5. **Select** **Create Workspace**

![Create a Blank Workspace form with Workspace Title, Project Group, Dataset Type, and Create Workspace](../../resources/images/workspaces/user-manual/03-create/02-blank-light.avif#only-light)
![Create a Blank Workspace form with Workspace Title, Project Group, Dataset Type, and Create Workspace](../../resources/images/workspaces/user-manual/03-create/02-blank-dark.avif#only-dark)

---

### Create a workspace from TDEI

1. **Select** **Start** under **From TDEI**
2. Enter a name in **Workspace Title**
3. Select a **Project Group**
4. Select a **Dataset** from the available TDEI datasets
5. Review the dataset information and map preview
6. **Select** **Create Workspace**

The dataset information panel can include the dataset name, description, dataset type, status, TDEI dataset ID, project group, service, collection date, publication date, and OpenSidewalks schema version.

![Create a Workspace from the TDEI form with a selected dataset, dataset information, and map preview](../../resources/images/workspaces/user-manual/03-create/03-from-tdei-light.avif#only-light)
![Create a Workspace from the TDEI form with a selected dataset, dataset information, and map preview](../../resources/images/workspaces/user-manual/03-create/03-from-tdei-dark.avif#only-dark)

!!! note "Import behavior"

    Creating a workspace from TDEI creates a *copy* of the selected dataset. The workspace is a separate editing context from the source dataset, which remains unchanged.

---

### Create a workspace from a file

1. **Select** **Start** under **From File**
2. Enter a name in **Workspace Title**
3. Select a **Project Group**
4. Under **Dataset Type**, select **OpenSidewalks** or **GTFS Pathways**
5. Under **Dataset File**, **select** **Browse...** and choose the data file from your computer
6. **Select** **Create Workspace**

![Create a Workspace from a File form with Workspace Title, Project Group, Dataset Type, Dataset File, and Create Workspace](../../resources/images/workspaces/user-manual/03-create/04-from-file-light.avif#only-light)
![Create a Workspace from a File form with Workspace Title, Project Group, Dataset Type, Dataset File, and Create Workspace](../../resources/images/workspaces/user-manual/03-create/04-from-file-dark.avif#only-dark)

---

### Monitor workspace setup

After creating a workspace from a dataset, Workspaces may show the workspace with a **Setting up...** status while the data is being populated. The workspace actions may remain unavailable during setup.

![Workspaces Dashboard showing a newly created workspace with the Setting up... status](../../resources/images/workspaces/user-manual/03-create/05-setting-up-light.avif#only-light)
![Workspaces Dashboard showing a newly created workspace with the Setting up... status](../../resources/images/workspaces/user-manual/03-create/05-setting-up-dark.avif#only-dark)

!!! tip "Wait for setup to finish"

    Refresh the workspace status and wait for setup to finish before trying to open workspace-dependent actions.

---

**Previous:** [Getting Started](getting-started.md) | **Next:** [Dashboard](dashboard.md)
