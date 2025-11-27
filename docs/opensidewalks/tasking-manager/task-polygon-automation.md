---
title: Task Polygon Automation Guide
tags:
    - Guide
    - Internal
    - Developer
---

<!-- @format -->

# Task Polygon Automation Guide

This guide shows the steps for an automated workflow that generates task polygons for use in Tasking Manager.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

## Task Polygon Automation Process

This guide outlines the step-by-step process for automating task polygon generation for OpenSidewalks communities.

### Prerequisites

-   `poetry shell` environment activated
-   `osmium` command-line tool installed
-   `osw task` command available

### Process Overview

#### Step 1: Initialize Staging Directory

**Action:** Create the `staging_directory` in `/projects/osw/opensidewalks_cli/`

**Command:**

```bash
mkdir staging_directory
```

#### Step 2: Create State Structure

**Action:** Create a folder for each **state** within the staging directory.

**Directory structure:**

```
staging_directory/
└── <state>/
```

#### Step 3: Create County Structure

**Action:** Create a subfolder for each **county** within each state folder.

**Directory structure:**

```
staging_directory/
└── <state>/
    └── <county>/
```

#### Step 4: Create Community Structure

**Action:** Create a subfolder for each **community** within each county folder.

**Directory structure:**

```
staging_directory/
└── <state>/
    └── <county>/
        └── <community>/
```

#### Step 5: Create Working Subfolders

**Action:** Create **working subfolders** (`data_sources`, `intermediate_data`, `output`) for each community.

**Directory structure:**

```
staging_directory/
└── <state>/
    └── <county>/
        └── <community>/
            ├── data_sources/
            ├── intermediate_data/
            └── output/
```

#### Step 6: Obtain OSM PBF Files

**Action:** Obtain an **OSM PBF file** for each state and store it in the `/<state>/` folder.

**File location:**

```
/<state>/<state>-latest.osm.pbf
```

#### Step 7: Obtain Community Target Data

**Action:** Obtain the **GeoJSON data for the bbox** of each community target mapping area and store it in the corresponding `intermediate_data` subfolder.

**File location:**

```
/<state>/<county>/<community>/intermediate_data/<community>.geojson
```

#### Step 8: Extract Community Data with Osmium

**Action:** For each `<community>`, run `osmium extract` to trim the state `osm.pbf` file to the target mapping area.

**Command:**

```bash
osmium extract -p <path-to-geojson> <path-to-pbf> -o <path-to-new-pbf>
```

**Example:**

```bash
osmium extract -p ../<state>/<county>/<community>/intermediate_data/<community>.geojson ../<state>/<state>-latest.osm.pbf -o ../<state>/<county>/<community>/data_sources/<community>.osm.pbf
```

**Important:** This command must be run from the `../opensidewalks_cli/staging_directory/` directory!

#### Step 9: Generate Task Polygons with OSW Task

**Action:** For each `<community>`, run `osw task` to generate the task polygon files (`crossing_tasks.geojson` and `sidewalk_tasks.geojson`) corresponding to the target mapping area.

**Command:**

```bash
osw task <path-to-pbf> <path-to-geojson> <output-path>
```

**Example:**

```bash
osw task ../<state>/<county>/<community>/data_sources/<community>.osm.pbf ../<state>/<county>/<community>/intermediate_data/<community>.geojson .../<state>/<county>/<community>/output
```

#### Step 10: Rename Output Files

**Action:** For each `<community>`, rename the `crossing_tasks.geojson` and `sidewalks_tasks.geojson` files in the `../<community>/output` directory to more easily identify them as they are uploaded into the Tasking Manager.

**Rename pattern:**

```bash
mv ../<community>/output/crossing_tasks.geojson ../<community>/output/<community>_crossing_tasks.geojson
mv ../<community>/output/sidewalk_tasks.geojson ../<community>/output/<community>_sidewalk_tasks.geojson
```

## Final Directory Structure

After completing all steps, your directory structure should look like:

```
staging_directory/
├── <state>/
│   ├── <state>-latest.osm.pbf
│   └── <county>/
│       └── <community>/
│           ├── data_sources/
│           │   └── <community>.osm.pbf
│           ├── intermediate_data/
│           │   └── <community>.geojson
│           └── output/
│               ├── <community>_crossing_tasks.geojson
│               └── <community>_sidewalk_tasks.geojson
│
└── [Additional states follow same pattern]
```

## Next Steps

The generated task polygon files (`<community>_crossing_tasks.geojson` and `<community>_sidewalk_tasks.geojson`) are now ready to be uploaded to the Tasking Manager for community mapping activities.
