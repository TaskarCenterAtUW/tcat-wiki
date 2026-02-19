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

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

### Map Overview

The AVIV ScoutRoute map displays an overhead view of the workspace area. The app is designed for use in a variety of settings, from dense urban areas to smaller towns and rural communities, and quests often use a common vocabulary for pedestrian infrastructure components.

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Annotated map overview | ../../resources/images/aviv-scoutroute/android/map-overview-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Annotated map overview | ../../resources/images/aviv-scoutroute/android/map-overview-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Annotated map overview | ../../resources/images/aviv-scoutroute/ios/map-overview-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Annotated map overview | ../../resources/images/aviv-scoutroute/ios/map-overview-light.png#only-light{ width="300" } -->

---

### Pedestrian Environment Terminology Basics

Understanding these terms will help you complete quests accurately:

| Term                     | Definition                                                                                                                     |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| **Crossing** (Crosswalk) | A designated pedestrian path between curbs, crossing a road; these are spaces shared with vehicles                             |
| **Curb**                 | The edge where a sidewalk meets the road                                                                                       |
| **Curb Extension**       | An area where the curb extends into the street; shortens crossing distances, calms traffic, and improves pedestrian visibility |
| **Island**               | A designated, protected space in the middle of a crossing that allows pedestrians to stand safely mid-street                   |
| **Tactile Paving**       | Purpose-built textured ground surface indicators that provide navigation cues                                                  |

<!-- IMAGE PLACEHOLDER: Annotated diagram showing intersection terminology | ../../resources/images/aviv-scoutroute/shared/intersection-terminology-dark.png#only-dark{ width="400" } -->
<!-- IMAGE PLACEHOLDER: Annotated diagram showing intersection terminology | ../../resources/images/aviv-scoutroute/shared/intersection-terminology-light.png#only-light{ width="400" } -->

---

### Quest Icons

Quests appear as icons on the map. Each icon type represents a different type of feature, such as:

| Quest Type   | Appearance                                                           | Scope                                                                    | Example Questions                                        |
|:-------------|:---------------------------------------------------------------------|:-------------------------------------------------------------------------|:---------------------------------------------------------|
| **Sidewalk** | A path icon separating two differently colored areas (grey and blue) | A sidewalk segment along a road, often from one intersection to the next | Surface material, width, obstructions along the sidewalk |
| **Crossing** | A white pedestrian figure in a crossing on a blue background         | A single crosswalk at an intersection or a mid-block crossing            | Crossing markings, pedestrian signals, audio cues        |
| **Curb**     | A white wheelchair at a curb on a blue background                    | A specific curb point at the start of a crossing                         | Curb ramp presence, tactile paving, curb height          |

---

### Navigating the Map

#### Zooming

- **Pinch to zoom:** Use two fingers to zoom in or out
- **Double-tap:** Quickly zoom in on a specific location
- **Icons:** Plus ++plus++ and minus ++minus++ icons at the bottom right

!!! important

    Quest icons stack up when zoomed out to reduce visual clutter on the map. You should **always zoom in** to see all available quests in an area.

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Comparison of zoomed out vs zoomed in view | ../../resources/images/aviv-scoutroute/android/zoom-comparison-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Comparison of zoomed out vs zoomed in view | ../../resources/images/aviv-scoutroute/android/zoom-comparison-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Comparison of zoomed out vs zoomed in view | ../../resources/images/aviv-scoutroute/ios/zoom-comparison-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Comparison of zoomed out vs zoomed in view | ../../resources/images/aviv-scoutroute/ios/zoom-comparison-light.png#only-light{ width="300" } -->

#### Panning

- **Drag:** Touch and drag the map to move to different areas
- **Your location:** The app uses your device's GPS to show your current position
- **Center on position:** Compass icon in the bottom right

#### Changing Imagery

You can switch between different background map imagery sources (aerial imagery, street maps, etc.), if they are configured for that workspace, using the Layers button.

Refer to [App Settings - Imagery Layer Control](app-settings.md#imagery-layer-control) for details.

---

### Undo Changes

If you submit the wrong answer by mistake, misidentify a feature, or accidentally submit before ready, you can undo your recent edits.

#### Steps to Undo

1. Tap the **Undo button** at the bottom left
2. Review the list of recent edits
3. Tap the edit you want to review
4. Tap **Undo** to undo the submission

The quest should reappear on the map, allowing you to answer it again with the correct information.

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Undo panel with recent edits | ../../resources/images/aviv-scoutroute/android/undo-changes-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Undo panel with recent edits | ../../resources/images/aviv-scoutroute/android/undo-changes-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Undo panel with recent edits | ../../resources/images/aviv-scoutroute/ios/undo-changes-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Undo panel with recent edits | ../../resources/images/aviv-scoutroute/ios/undo-changes-light.png#only-light{ width="300" } -->

!!! note

    If the Undo menu is not visible, the quest cannot be rolled back through the app - contact your project leader for help with undoing older changes.

---

### Hide Quest

The Hide Quest feature lets you temporarily remove specific quests from view. This is useful when you want to skip certain quests without seeing them repeatedly.

#### Hiding a Quest

1. Tap on a quest icon to open its answer panel
2. Tap **Hide** (eye icon)
3. Answer **Yes** to the confirmation pop-up
4. The quest disappears from the map

#### Restoring Hidden Quests

To restore an **individual** hidden quest:

1. Open the Undo menu
2. Tap on the quest you want to unhide
3. Select **Undo**

To restore **all** hidden quests at once:

1. Open the hamburger menu and tap **Settings**
2. Navigate down to **Advanced**
3. Tap **Restore hidden quests**
4. Select **Restore** on the confirmation pop-up

!!! info

    Hidden quests are stored locally on your device. They remain hidden until you choose to restore them.

---

### Imagery Layer Control

The Imagery Layer control lets you switch between different map background sources, if they have been configured for your workspace.

<!-- === "Android" -->

<!-- IMAGE PLACEHOLDER: Imagery layer selector | ../../resources/images/aviv-scoutroute/android/imagery-layer-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Imagery layer selector | ../../resources/images/aviv-scoutroute/android/imagery-layer-light.png#only-light{ width="300" } -->

<!-- === "iOS (Apple)" -->

<!-- IMAGE PLACEHOLDER: Imagery layer selector | ../../resources/images/aviv-scoutroute/ios/imagery-layer-dark.png#only-dark{ width="300" } -->
<!-- IMAGE PLACEHOLDER: Imagery layer selector | ../../resources/images/aviv-scoutroute/ios/imagery-layer-light.png#only-light{ width="300" } -->

**How to access:**

1. Tap the **Layers** icon in the top toolbar

**Available imagery types may include:**

- Satellite imagery
- Street maps
- Custom basemaps configured by your project

!!! note

    Available imagery sources depend on what has been configured for your workspace. Contact your project administrator if you need specific imagery options.

---

### Next Steps

- Learn [how to complete quests](completing-quests.md)
- Review the different [quest types](quest-types.md) and how to answer them
