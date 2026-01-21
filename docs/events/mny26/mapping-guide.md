---
title: Mapping Guide
tags:
    - Guide
    - External
    - User
# exclude-from-parent-guides-list
# exclude-from-main-guides-list
---

<!-- @format -->

# Mapping Guide

This guide covers how to map pedestrian infrastructure for the Mappy New Year 2026 event.

---

## Quick Links

- **Project**: [#1017 - Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks](https://tasks.openstreetmap.us/projects/1017)

## Getting Started

### 1. Log In to the Tasking Manager

1. **Create an OpenStreetMap account** at [openstreetmap.org](https://www.openstreetmap.org/user/new) if you don't already have one.
2. **Log in to the OSM US Tasking Manager** at [tasks.openstreetmap.us](https://tasks.openstreetmap.us) using your OSM account.
3. **Join the OpenSidewalks Mappers Team** by visiting [tasks.openstreetmap.us/teams/27/membership/](https://tasks.openstreetmap.us/teams/27/membership/) and selecting **Join team** at the bottom right.
4. **Navigate to the Tacoma project** by opening [tasks.openstreetmap.us/projects/1017](https://tasks.openstreetmap.us/projects/1017)

### 2. Select a Task

1. Select **Contribute** on the bottom right of the project page
2. **Choose** an available task (white tiles on the map)
3. Select **Map selected task** to open the iD Editor

You'll see the iD Editor on the left and task information on the right. The magenta boundary shows your task area.

---

## What to Map

We're mapping the **pedestrian network**: sidewalks, crossings, and curbs. These features enable routing applications to provide pedestrian directions.

### Priority Order

1. **Crossings** - Map these first to anchor the network at intersections

    1a. **Curbs** - Mark curb types at crossing endpoints

2. **Sidewalks** - Draw sidewalk centerlines along streets

    2b. **Connectors** - Link sidewalks to curbs!

---

## Mapping Crossings

Crossings are paths pedestrians traverse to cross streets.

### How to Map

1. Select the **Line** tool
2. Click at one edge of the street (curb location)
3. Click where your line meets the road centerline (this connects to the road network)
4. Double-click at the opposite curb to finish

### Tagging

Search for these presets in the iD Editor:

| Crossing Type                   | iD Preset           | Tags                                                             |
|---------------------------------|---------------------|------------------------------------------------------------------|
| **Marked** (has painted lines)  | "Marked Crosswalk"  | `highway=footway` + `footway=crossing` + `crossing:markings=yes` |
| **Unmarked** (no painted lines) | "Unmarked Crossing" | `highway=footway` + `footway=crossing` + `crossing:markings=no`  |

### Tag the Crossing Node

The middle point where the crossing intersects the roadway should be tagged:

- `highway=crossing`
- `crossing:markings=yes` or `crossing:markings=no`

### Additional Crossing Tags

If you'd like to add additional detail that is important for accessibility-focused routing:

| Tag                | Values                 | Description                   |
|--------------------|------------------------|-------------------------------|
| `crossing:signals` | `yes` / `no`           | Are there pedestrian signals? |
| `crossing:island`  | `yes` / `no`           | Is there a pedestrian island? |
| `surface`          | `concrete` / `asphalt` | Crossing surface material     |

---

## Mapping Curbs

Curbs are points at the edge of the street where crossings begin and end.

### How to Map

The endpoints of your crossing line are curb nodes. Select each endpoint and tag it.

### Tagging

| Curb Type   | iD Preset      | Tags                            | Description            |
|-------------|----------------|---------------------------------|------------------------|
| **Lowered** | "Lowered Curb" | `barrier=kerb` + `kerb=lowered` | Curb ramp present      |
| **Raised**  | "Raised Curb"  | `barrier=kerb` + `kerb=raised`  | Standard curb, no ramp |
| **Flush**   | "Flush Curb"   | `barrier=kerb` + `kerb=flush`   | Level with street      |

### Additional Curb Tags

| Tag              | Values       | Description                         |
|------------------|--------------|-------------------------------------|
| `tactile_paving` | `yes` / `no` | Detectable warning surface presence |

---

## Mapping Sidewalks

Sidewalks are pedestrian paths along streets.

### How to Map

1. Select the **Line** tool
2. Draw a line along the **center** of the sidewalk
3. Search for "Sidewalk" and select the preset

### Tagging

| Feature      | iD Preset  | Tags                                   |
|--------------|------------|----------------------------------------|
| **Sidewalk** | "Sidewalk" | `highway=footway` + `footway=sidewalk` |

### Additional Sidewalk Tags

| Tag       | Values                 | Description      |
|-----------|------------------------|------------------|
| `surface` | `concrete` / `asphalt` | Surface material |

### Important Rules

- Draw sidewalks down the **center** of the path
- Connect sidewalks to service roads (driveways, alleys) where they intersect by adding a node (point) that both ways (lines) share

---

## Tagging Crossing Links

Optionally, the short sidewalk **connector** segments between sidewalk centerlines and curb nodes can be tagged with `crossing_link=yes` to help identify these features, which often have different properties such as an incline or different surface material.

### How to Map

1. Select the **Line** tool
2. Click on a curb node (at the end of a crossing)
3. Draw a line to the sidewalk centerline
4. Double-click on the sidewalk to connect
5. Search for "Sidewalk" and select the preset
6. Add the `crossing_link=yes` tag

### Tagging

| Feature      | iD Preset  | Tags                                   |
|--------------|------------|----------------------------------------|
| **Sidewalk** | "Sidewalk" | `highway=footway` + `footway=sidewalk` |

---

## Tagging Quick Reference

### Essentials

| Feature          | Tags                                                                  |
|------------------|-----------------------------------------------------------------------|
| Sidewalk (Line)  | `highway=footway` + `footway=sidewalk`                                |
| Crossing (Line)  | `highway=footway` + `footway=crossing` + `crossing:markings=yes`/`no` |
| Crossing (Point) | `highway=crossing` + `crossing:markings=yes`/`no`                     |
| Curb (Point)     | `barrier=kerb` + `kerb=lowered`/`raised`                              |

### Details

| Tag                | Applies To           | Values                |
|--------------------|----------------------|-----------------------|
| `surface`          | Sidewalks, Crossings | `concrete`, `asphalt` |
| `crossing:signals` | Crossings            | `yes`, `no`           |
| `tactile_paving`   | Curbs                | `yes`, `no`           |

---

## Saving Your Work

1. Click **Save** in the iD Editor (top right)
2. The changeset comment should be automatically filled out:

    `#osmus-tasks-1017 | Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks #MappyNewYear2026`

3. Click **Upload**
4. In the Tasking Manager panel on the right, mark the task status by answering: "_Is this task completely mapped?_"
    - Select **Yes** if you finished adding all of the essentials in the area
    - Select **No** if more mapping is needed.
5. Click **Submit task**

Done! **Thank you** so much for contributing to this project. Your contributions directly impact the lives of pedestrians in the area that use OpenStreetMap-based applications to safely navigate their environment.

---

## Tips

- **Use street-level imagery**: Open the Map Data panel on the right and, under the Photo Overlays menu, check Bing Streetside or Mapillary layers for street-level imagery, which can be helpful for determining curb types.
- **When in doubt, don't guess!** It's better to not include a detail (such as a curb type) when you aren't confident about it - this allows on-the-ground surveyors to add the missing data and prevents routing applications from suggesting a route that isn't actually accessible.
- **Connect to roads**: Ensure crossing midpoints share a node (point) with the road they cross!
- **Check existing features**: Some areas may already have partial mapping - verify the existing data and update it as necessary.
