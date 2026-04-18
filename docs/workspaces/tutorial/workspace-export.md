---
title: Workspace Export Guide
tags:
    - Tutorial
    - Internal
    - Developer
---

<!-- @format -->

## Workspace Export Guide

This tutorial explains how to directly export a dataset in `.osm` format from Workspaces.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Instructions

#### 1. Determine your environment

1. Prod: [portal.tdei.us](https://portal.tdei.us/) + [workspaces.sidewalks.washington.edu](https://workspaces.sidewalks.washington.edu/)

2. Stage: [portal-stage.tdei.us](https://portal-stage.tdei.us/) + [workspaces-stage.sidewalks.washington.edu](https://workspaces-stage.sidewalks.washington.edu/)

3. Dev: [portal-dev.tdei.us](https://portal-dev.tdei.us/login) + [workspaces-dev.sidewalks.washington.edu](https://workspaces-dev.sidewalks.washington.edu/)

#### 2. Find your API key

1. Log in and navigate to the Dashboard section of your environment's TDEI Portal

![Screenshot of the Dashboard section of the TDEI Portal, with a highlight on the Copy button next to the My API Key box](../../resources/images/workspaces/tutorial/workspace-export/dashboard-h-api-key-copy-light.png#only-light)
![Screenshot of the Dashboard section of the TDEI Portal, with a highlight on the Copy button next to the My API Key box](../../resources/images/workspaces/tutorial/workspace-export/dashboard-h-api-key-copy-dark.png#only-dark)

#### 3. Find the Workspace ID

1. Extract the ID from the Workspace link, for example `1074`:

    [https://workspaces-stage.sidewalks.washington.edu/workspace/**1074**/settings](https://workspaces-stage.sidewalks.washington.edu/workspace/1074/settings)

#### 4. Export the Workspace

**Option 1: Workspace Export Utility _(Recommended!)_**

1. Download the [Workspaces Export Script](https://github.com/TaskarCenterAtUW/tdei-tools/blob/main/utilities/workspaces-export.ps1) from the [TDEI Tools](https://github.com/TaskarCenterAtUW/tdei-tools) repository.

2. Run the script and follow the instructions.

**Option 2: Manually Query the Workspaces API**

1. Find the dataset's bbox
    1. In your browser, substitute the target Workspace ID and open:

        Example URL:

        [https://osm.workspaces-stage.sidewalks.washington.edu/api/0.6/workspaces/**1074**/bbox.json](https://osm.workspaces-stage.sidewalks.washington.edu/api/0.6/workspaces/1074/bbox.json)

        Example output:

        ```json
        {
            "min_lat": 47.6558706,
            "min_lon": -122.3134287,
            "max_lat": 47.6563239,
            "max_lon": -122.3122227
        }
        ```

2. Construct request URL with above bbox query output, in `min_lon,min_lat,max_lon,max_lat` format.

    `https://osm.workspaces.sidewalks.washington.edu/api/0.6/map?bbox=-122.3134287,47.6558706,-122.3122227,47.6563239`

3. In PowerShell: (replace `TDEI_TOKEN` with your copied API key, `WORKSPACE_ID` with the Workspace ID, `QUERY_URL` with the URL containing the bbox, and `FILE_NAME` with your desired file name)

    It is recommended to follow a file name convention like `export-ENV-ID-DATE-N.osm` (example: `export-stage-1074-20260417-01.osm`)

    ```ps
    $headers = @{ Authorization = 'TDEI_TOKEN'; 'X-Workspace' = 'WORKSPACE_ID' }; Invoke-WebRequest -Uri 'QUERY_URL' -Headers $headers -OutFile 'FILE_NAME.osm'
    ```

    Example:

    ```ps
    $headers = @{ Authorization = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'; 'X-Workspace' = '1074' }; Invoke-WebRequest -Uri 'https://osm.workspaces-stage.sidewalks.washington.edu/api/0.6/map?bbox=-122.3134287,47.6558706,-122.3122227,47.6563239' -Headers $headers -OutFile 'export-stage-1074-20260417-01.osm'
    ```

4. This outputs a `FILE_NAME.osm` file in the current directory.
