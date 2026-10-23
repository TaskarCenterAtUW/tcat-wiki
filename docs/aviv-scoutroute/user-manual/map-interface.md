---
title: Map Interface
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Map Interface

This section explains the main AVIV ScoutRoute map interface, including how to navigate the map, understand quest icons, and interpret common pedestrian feature terminology.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._{ .guides-list-ref }

---

### Map Overview

The AVIV ScoutRoute map displays an overhead view of the workspace area. The app is designed for use in a variety of settings, from dense urban areas to smaller towns and rural communities, and quests often use a common vocabulary for pedestrian infrastructure components.

---

### Pedestrian Environment Terminology Basics

Understanding these terms will help you complete quests accurately:

| Term                     | Definition                                                                                                                     |
| :----------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **Crossing** (Crosswalk) | A designated pedestrian path between curbs, crossing a road; these are spaces shared with vehicles                             |
| **Curb**                 | The edge where a sidewalk meets the road                                                                                       |
| **Curb Extension**       | An area where the curb extends into the street; shortens crossing distances, calms traffic, and improves pedestrian visibility |
| **Island**               | A designated, protected space in the middle of a crossing that allows pedestrians to stand safely mid-street                   |
| **Tactile Paving**       | Purpose-built textured ground surface indicators that provide navigation cues                                                  |

---

### Quest Icons

Quests appear as icons on the map. Each icon type represents a different type of feature, such as:

| Quest type        | Icon cue                      | Example questions                                   |
| :---------------- | :---------------------------- | :-------------------------------------------------- |
| **Sidewalks**     | Walking-person icon on a path | Surface material, width, and obstructions           |
| **Crossings**     | Pedestrian-crossing icon      | Crossing markings, signals, and audio cues          |
| **Curbs**         | Wheelchair icon at a curb     | Curb ramp presence, tactile paving, and curb height |
| **Bus Stops**     | Bus icon                      | Shelter, bench, and trash can presence              |
| **Intersections** | Traffic-signal icon           | Signal types and safety observations                |
| **Bench**         | Bench icon                    | Backrest and armrest presence                       |
| **Bathroom**      | Restroom icon                 | Accessibility features and access rules             |

---

### Navigating the Map

#### Zooming

- **Pinch to zoom:** Use two fingers to zoom in or out
- **Double-tap:** Quickly zoom in on a specific location
- **Zoom buttons:** Use the **+** and **-** controls at the lower right when they are shown. You can also enable **Show map zoom buttons** in [App Settings](app-settings.md).

!!! important "Quest icons stack up when zoomed out to reduce visual clutter on the map. You should **always zoom in** to see all available quests in an area."

#### Panning

- **Drag:** Touch and drag the map to move to different areas
- **Your location:** The app uses your device's GPS to show your current position
- **Current location:** Select the target-shaped control at the lower right to return to your device location

#### Changing Imagery

You can switch between map imagery sources configured for the workspace by opening **Select Imagery Source** from the layers control.

![AVIV ScoutRoute imagery selector with the default and a configured aerial source](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/06-select-imagery-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" } ![AVIV ScoutRoute map with accessibility quests displayed over aerial imagery](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/19-aerial-imagery-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" }
![AVIV ScoutRoute imagery selector with the default and a configured aerial source](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/06-select-imagery-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" } ![AVIV ScoutRoute map with accessibility quests displayed over aerial imagery](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/19-aerial-imagery-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

!!! note "Available imagery sources depend on what has been configured for your workspace. Contact your project administrator if you need specific imagery options."

---

![Manage Quests list with enabled checkboxes for feature types](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/01-manage-quests-light.avif#only-light){ .img-right style="--img-width: 33%;" }
![Manage Quests list with enabled checkboxes for feature types](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/01-manage-quests-dark.avif#only-dark){ .img-right style="--img-width: 33%;" }

### Manage Quests

Open **Manage Quests** from the map controls to show or hide individual items or entire quest types. Use the checkboxes in the **Enabled** column to change which features appear on the map.

---

### Screen Reader Mode

Select **Screen Reader Mode** from the map controls to view nearby quests in a text list. Each item gives the quest type, distance, and direction. Select **Refresh list** to update the list.

Select a quest to open its action panel. Choose **Start answering the questions**, **Hide this quest**, or **Not now**. The list also includes **Undo Edits** and **Go back to map view** controls.

![Screen Reader Mode list of nearby quests with distances and directions](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/02-screen-reader-mode-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" } ![Screen Reader Mode action panel for a selected sidewalk quest](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/03-srm-quest-selected-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" }
![Screen Reader Mode list of nearby quests with distances and directions](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/02-screen-reader-mode-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" } ![Screen Reader Mode action panel for a selected sidewalk quest](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/03-srm-quest-selected-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

---

### Download Map Data

Select the downward-arrow control on the map to download data for the visible area. Downloading data can help prepare for a survey with limited connectivity, but does not guarantee that every app operation will work offline.

---

### Undo Changes

If you submit the wrong answer by mistake, misidentify a feature, or accidentally submit before ready, you can undo your recent edits.

#### Steps to Undo

1. Select **Undo Edits** from the map or Screen Reader Mode controls.
2. Review the recent edits and select the entry you want to revert.
3. Review the changes in the confirmation panel.
4. Select **Revert Changes** or **Undo**, depending on the label shown for that edit.

When an edit is reverted, check the map to see whether the quest is available again.

![Undo Edits list showing a recent quest change](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/04-srm-undo-list-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" } ![Undo confirmation showing the changes to be reverted](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/05-srm-undo-confirm-light.avif#only-light){ .img-contained .img-inline style="--img-width: 25%;" }
![Undo Edits list showing a recent quest change](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/04-srm-undo-list-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" } ![Undo confirmation showing the changes to be reverted](../../resources/images/aviv-scoutroute/user-manual/04-map-interface/05-srm-undo-confirm-dark.avif#only-dark){ .img-contained .img-inline style="--img-width: 25%;" }
{: .img-row }

!!! note "If the Undo menu is not visible, the quest cannot be rolled back through the app - contact your project leader for help with undoing older changes."

---

### Hide Quest

The Hide Quest feature lets you temporarily remove specific quests from view. This is useful when you want to skip certain quests without seeing them repeatedly.

#### Hiding a Quest

1. Open a quest and select **Hide this quest**.
2. To restore an individually hidden quest, open **Undo Edits**, select the entry that says **You hid it**, and select **Undo**.

Hidden quests are local to the app view; hiding a quest does not remove the feature from the workspace for other contributors.

---

### Next Steps

- Learn [how to complete quests](completing-quests.md)
- Review the different [quest types](quest-types.md) and how to answer them
