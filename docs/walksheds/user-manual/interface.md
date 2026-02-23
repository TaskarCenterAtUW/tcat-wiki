---
title: Interface Overview
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Interface Overview

This section introduces the Walkshed Tool interface, including the sidebar tabs, map controls, and action pop-up.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Overview

The tool is organized around a left sidebar with several tabs, a main map view, and an action pop-up at the bottom of the screen.

---

### Reading the Map

The walkshed is displayed on the map with all reachable paths (sidewalks, crossings, and other paths) highlighted in **blue**. Areas excluded by slope limits, obstacle avoidance, or street avoidance settings appear as gaps, reflecting real barriers in the pedestrian environment.

Individual walkways are color-coded by how their incline affects movement speed: flat edges appear **blue**, moderately inclined edges shift toward **pink** and **orange**, and edges that exceed the slope limit appear as **red** dotted lines. The [Incline Bar](#incline-bar) at the bottom of the screen provides a live reference for this color scale, updating automatically as you adjust steepness preferences.

---

### Sidebar

The left sidebar houses the controls used to configure the walkshed.

| Tab          | Icon             | Purpose                                                                                                                                                                        |
| ------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Walkshed** | Network          | Search for an address and configure walkshed preferences: slope limits, barrier avoidance, and street avoidance using sliders and toggles, and time of day using date/time pickers. See [Mobility Profiles and Preferences](preferences.md). |
| **Changes**  | Pencil           | Review, manage, or remove [edge attribute edits](editing.md) and saved [walkshed scenarios](scenarios.md).                                                                     |
| **Cost Fn**  | (none)           | View and edit the Python cost function used to weight network edges. See [Custom Cost Function](custom-cost-function.md).                                                      |
| **Dataset**  | Settings (gear)  | Select a TDEI dataset and build the routing graph. See [TDEI Datasets](../../tdei/portal/user-manual/datasets.md).                                                             |

---

### Map Controls

A **map legend** button in the top-right corner of the screen opens a menu with toggles that control the visibility of the following map features:

- **Points:** Non-network point features in the dataset (light poles, benches, etc.).
- **Cost Nodes:** Network nodes color-coded with their computed travel cost from the origin. The four colors (green, yellow, orange, and red) correspond to isochrones representing quartiles of travel cost from the origin.
- **Convex Hull:** The outer boundary polygon of the walkshed with color-coded isochrones representing quartiles of travel cost from the origin.

---

### Action Pop-up

The action pop-up at the bottom of the screen changes based on context:

- **When an edge or feature is selected** (see [Inspecting and Editing Features](editing.md)), it displays the feature's attributes and action buttons.
- **After a walkshed is generated**, it displays walkshed summary actions (see below).

#### Walkshed Actions

**Walkshed Info:** Opens a sidebar displaying summary statistics about the walkshed, including the number of sidewalk edges, crossing edges, and the total length of all included edges.

**Download Walkshed:** Saves the walkshed network as an OpenSidewalks GeoJSON document for use in external tools.

**Save Scenario:** Enter a name in the text input box to save the current walkshed as a named scenario for later comparison. See [Scenarios](scenarios.md) for more information.

---

### Incline Bar

At the very bottom of the screen, a horizontal bar displays a color gradient labeled **Speed at incline %**. This bar maps incline percentages (from flat to steep) to the colors used on the map, which update in real time based on the currently selected mobility profile's maximum uphill and downhill steepness settings, providing a quick reference for interpreting path colors without opening the full map legend.

---

Previous: [Getting Started](getting-started.md)

Next: [Mobility Profiles and Preferences](preferences.md)
