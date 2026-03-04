---
title: Import OSM Data into Workspaces
tags:
    - Tutorial
    - External
    - Developer
---

<!-- @format -->

## Import OSM Data into Workspaces

This tutorial explains how to download an area of interest from OpenStreetMap, convert it to the OpenSidewalks format, and upload it to Workspaces.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Step 1: Download Area of Interest from OpenStreetMap

1. Open [SliceOSM](https://slice.openstreetmap.us/) in your browser.

    ![SliceOSM landing page](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-landing-light.png#only-light)
    ![SliceOSM landing page](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-landing-dark.png#only-dark)

2. Search for a location or use the map to navigate to your area of interest, **draw a bounding box** (or other shape) around it, and enter a name for the area.

    ![SliceOSM bounding box selection](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-bbox-light.png#only-light)
    ![SliceOSM bounding box selection](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-bbox-dark.png#only-dark)

3. Select **Generate Slice**, then select **Download .osm.pbf** once the slice is ready.

    ![SliceOSM download](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-download-light.png#only-light)
    ![SliceOSM download](../../resources/images/workspaces/tutorial/osm-to-workspaces/sliceosm-download-dark.png#only-dark)

---

### Step 2: Convert OSM Data to OSW Format

Use the [TDEI Portal](https://portal.tdei.us/jobs) to create and run a new **OSW - Convert** job to convert the `.osm.pbf` file to an OSW-format `.zip` package. For more information, refer to the [OSW - Convert](../../tdei/portal/user-manual/jobs/osw-convert.md) guide.

1. Log in to the [TDEI Portal](https://portal.tdei.us/).

2. Navigate to **Jobs** and select **Create Job**.

3. Set **Job Type** to **OSW - Convert**, **Source Format** to **OSM**, and **Target Format** to **OSW**. Upload your `.osm.pbf` file, then select **Create**.

    ![TDEI Portal create OSW - Convert job](../../resources/images/workspaces/tutorial/osm-to-workspaces/tdei-portal-create-job-light.png#only-light)
    ![TDEI Portal create OSW - Convert job](../../resources/images/workspaces/tutorial/osm-to-workspaces/tdei-portal-create-job-dark.png#only-dark)

4. After submitting, a popup will prompt you to navigate to the **Jobs** page. Go there and find your **Dataset-Reformat** job at the top of the list. Once it shows **Completed**, select **Download Result** to download the output, which will be named `<JobId>.zip`.

    ![TDEI Portal completed job with Download Result](../../resources/images/workspaces/tutorial/osm-to-workspaces/tdei-portal-job-completed-light.png#only-light)
    ![TDEI Portal completed job with Download Result](../../resources/images/workspaces/tutorial/osm-to-workspaces/tdei-portal-job-completed-dark.png#only-dark)

---

### Step 3: Upload to Workspaces

1. Navigate to [Create Workspace from File](https://workspaces.sidewalks.washington.edu/workspace/create/file) and sign in. Alternatively, use the top navigation: **Create Workspace** > **From File** > **Start**.

2. Fill in the **Workspace Title** and **Project Group**, set **Dataset Type** to **OpenSidewalks**, and upload the `<JobId>.zip` from the previous step. Select **Create Workspace**.

    ![Workspaces create workspace form](../../resources/images/workspaces/tutorial/osm-to-workspaces/workspaces-create-workspace-light.png#only-light)
    ![Workspaces create workspace form](../../resources/images/workspaces/tutorial/osm-to-workspaces/workspaces-create-workspace-dark.png#only-dark)

3. The page will show **Converting dataset...** while the file is processed, followed by **Initializing workspace...** and then **Importing dataset to workspace...** before the process completes and the page automatically refreshes.

    !!! question "Taking a while?"

        This process can take anywhere from a few seconds to several minutes, depending on the size of the area and the density of mapped features.

4. Once complete, you will be taken to the dashboard with the newly created workspace selected.

    ![Workspaces dashboard with new workspace](../../resources/images/workspaces/tutorial/osm-to-workspaces/workspaces-created-workspace-light.png#only-light)
    ![Workspaces dashboard with new workspace](../../resources/images/workspaces/tutorial/osm-to-workspaces/workspaces-created-workspace-dark.png#only-dark)

!!! success "You have now successfully created a new workspace using the latest OSM data!"

For more information on using the Workspaces platform, refer to the [Workspaces User Manual](../user-manual/index.md).
