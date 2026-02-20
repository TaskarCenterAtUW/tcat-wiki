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

This section introduces the AccessMap interface, including the sidebar, map controls, and legend.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Map Overview

The AccessMap interface consists of two main areas: the **sidebar** on the left, which contains controls for search, profile selection, and preferences; and the **map view** on the right, which displays the pedestrian network and any planned route.

![Full AccessMap interface](../../resources/images/accessmap/user-manual/interface/overview-light.png#only-light)
![Full AccessMap interface](../../resources/images/accessmap/user-manual/interface/overview-dark.png#only-dark)

---

### Sidebar

The left sidebar is the primary control panel for AccessMap. It contains:

| Element             | Location      | Description                                                                       |
|:--------------------|:--------------|:----------------------------------------------------------------------------------|
| **Main Menu**       | Top left      | Opens the main menu (☰ "hamburger" icon)                                          |
| **Region Selector** | Top bar       | Displays the currently selected region (e.g., "Seattle, WA"); select to switch    |
| **Tasks**           | Top bar       | Opens the tasks panel, showing how the data collection process was organized      |
| **Search Bar**      | Below top bar | Search for an address or location to use as a waypoint in your route              |
| **Profile Panel**   | Below search  | Select a pre-defined mobility profile or customize individual routing preferences |

---

### Main Menu

Select the **Main Menu** button (☰) at the top left of the sidebar to open a panel with the following options:

| Option                    | Description                                                      |
|:--------------------------|:-----------------------------------------------------------------|
| **About**                 | Opens a popup with information about AccessMap                   |
| **Contact**               | Opens a popup with contact information                           |
| **Tracking for research** | Toggle to opt in or out of anonymous usage tracking for research |
| **Developer mode**        | Toggle to enable developer-oriented features                     |

![Main menu open](../../resources/images/accessmap/user-manual/interface/main-menu-light.png#only-light)
![Main menu open](../../resources/images/accessmap/user-manual/interface/main-menu-dark.png#only-dark)

---

### Map Controls

Controls are positioned around the edges of the map view in two groups.

#### Top Right

<table>
  <thead><tr><th>Control</th><th>Description</th><th style="border-left: 1px solid var(--md-typeset-table-color);">Image</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Take a tour</strong></td>
      <td>Opens a series of guided popups introducing the AccessMap interface</td>
      <td rowspan="2" style="vertical-align: top; border-left: 1px solid var(--md-typeset-table-color);">
        <img src="../../../resources/images/accessmap/user-manual/interface/top-right-light.png#only-light" alt="Top right menu" />
        <img src="../../../resources/images/accessmap/user-manual/interface/top-right-dark.png#only-dark" alt="Top right menu" />
      </td>
    </tr>
    <tr>
      <td><strong>Map Legend</strong></td>
      <td>Opens a right sidebar displaying the map legend (see <a href="#map-legend">Map Legend</a>)</td>
    </tr>
  </tbody>
</table>

#### Bottom Right

<table>
  <thead><tr><th>Control</th><th>Description</th><th style="border-left: 1px solid var(--md-typeset-table-color);">Image</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Start route from your location</strong></td>
      <td>Centers the map on your current location</td>
      <td rowspan="2" style="vertical-align: top; border-left: 1px solid var(--md-typeset-table-color);">
        <img src="../../../resources/images/accessmap/user-manual/interface/bottom-right-light.png#only-light" alt="Bottom right menu" />
        <img src="../../../resources/images/accessmap/user-manual/interface/bottom-right-dark.png#only-dark" alt="Bottom right menu" />
      </td>
    </tr>
    <tr>
      <td><strong>Zoom In / Zoom Out</strong></td>
      <td>Increase / decrease the map zoom level</td>
    </tr>
  </tbody>
</table>

---

![Map legend](../../resources/images/accessmap/user-manual/interface/map-legend-light.png#only-light){ .img-right }
![Map legend](../../resources/images/accessmap/user-manual/interface/map-legend-dark.png#only-dark){ .img-right }

### Map Legend

Select the **Map Legend** button (top right of the map) to open a right sidebar that explains the symbols and colors used on the map. The legend is organized into the following sections:

**Movement Speed Due to Incline**

Sidewalks and footways are color-coded by how their incline affects movement speed:

- **Blue** solid line — High speed (flat)
- **Pink** solid line — Medium speed (moderate incline)
- **Orange** solid line — Low speed (steep)
- **Red** dotted line — Inaccessible

**Crossings**

- **Light gray** line — Unmarked crossing
- **Striped** line — Marked crossing
- **Red** dotted line — Inaccessible

**Stairs**

- **Black** dashed blocks — Accessible
- **Red** dashed blocks — Inaccessible

**Points**

Point features (such as curb ramps, signals, and other landmarks) are displayed as small dots on the map.

**Buildings**

Buildings are shown as shaded shapes and can be referenced in screen reader alerts during navigation.

**Indoor Navigation**

Walkways, stairs, moving sidewalks/travelators, escalators, elevators, fare gates, exit gates, and inaccessible paths are all displayed on the map in different colors.

---

### Incline Bar

At the very bottom of the screen, a horizontal bar displays a color gradient labeled **Speed at incline %**. This bar maps incline percentages (from flat to steep) to the colors used on the map, which update in real time based on the currently selected mobility profile's maximum uphill and downhill steepness settings, providing a quick reference for interpreting path colors without opening the full map legend.

<div class="only-light">
<img-comparison-slider>
  <img slot="first" src="../../../resources/images/accessmap/user-manual/interface/incline-bar-min-light.png" alt="Incline bar at minimum settings" />
  <img slot="second" src="../../../resources/images/accessmap/user-manual/interface/incline-bar-max-light.png" alt="Incline bar at maximum settings" />
</img-comparison-slider>
</div>
<div class="only-dark">
<img-comparison-slider>
  <img slot="first" src="../../../resources/images/accessmap/user-manual/interface/incline-bar-min-dark.png" alt="Incline bar at minimum settings" />
  <img slot="second" src="../../../resources/images/accessmap/user-manual/interface/incline-bar-max-dark.png" alt="Incline bar at maximum settings" />
</img-comparison-slider>
</div>

!!! tip

    The image comparison slider above compares two map views: once where the steepness values are set to the minimum possible, and once where the steepness values are set to the maximum possible. This highlights how the steepness sliders, incline bar, and map colors all update in sync.

---

### Inspecting a Feature

You can tap or click on any feature on the map — such as a sidewalk, crossing, or curb ramp — to view its details. A **popup** appears at the bottom of the screen showing:

| Field           | Description                                            | Example                      |
|:----------------|:-------------------------------------------------------|:-----------------------------|
| **Type**        | The kind of feature (shown as the popup title)         | Sidewalk                     |
| **Description** | A human-readable description of the feature's location | Sidewalk SE of Lenora Street |
| **Incline**     | The slope grade of the feature, as a percentage        | 4%                           |
| **Surface**     | The surface material                                   | Concrete                     |

The popup also provides three action buttons:

| Button              | Description                                                        |
|:--------------------|:-------------------------------------------------------------------|
| **Route From Here** | Sets this feature's location as the route origin (waypoint A)      |
| **Route To Here**   | Sets this feature's location as the route destination (waypoint B) |
| **Share Feedback**  | Opens the [Share Feedback](feedback.md) form for this feature      |

![Feature popup with details and action buttons](../../resources/images/accessmap/user-manual/interface/feature-popup-light.png#only-light)
![Feature popup with details and action buttons](../../resources/images/accessmap/user-manual/interface/feature-popup-dark.png#only-dark)

!!! tip

    Tapping a feature is a quick way to start planning a route — select **Route From Here** or **Route To Here** to use that location as a waypoint without needing to search for an address.

---

### Trip Options

At the bottom of the sidebar (below the profile panel), the **Trip options** section allows you to set a departure date and time for your route. This can be useful when planning a trip in advance.

<div class="only-light">
<img-comparison-slider>
  <img slot="first" src="../../../resources/images/accessmap/user-manual/interface/time-open-light.png" alt="Route through building when open" />
  <img slot="second" src="../../../resources/images/accessmap/user-manual/interface/time-closed-light.png" alt="Route around building when closed" />
</img-comparison-slider>
</div>
<div class="only-dark">
<img-comparison-slider>
  <img slot="first" src="../../../resources/images/accessmap/user-manual/interface/time-open-dark.png" alt="Route through building when open" />
  <img slot="second" src="../../../resources/images/accessmap/user-manual/interface/time-closed-dark.png" alt="Route around building when closed" />
</img-comparison-slider>
</div>

!!! tip

    The image comparison slider above compares two departure times for the same route: early morning, when a building is closed and AccessMap routes around it, versus the afternoon, when the building is open and the route passes through it.

---

Previous: [Getting Started](getting-started.md)

Next: [Mobility Profiles and Preferences](profiles.md)
