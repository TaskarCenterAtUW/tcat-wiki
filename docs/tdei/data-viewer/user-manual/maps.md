---
title: Maps and Dataset Features
nav_order: 3
tags:
    - Guide
    - External
    - User
# exclude-from-main-guides-list
---

<!-- @format -->

## Maps and Dataset Features

This section describes the group map, dataset map view, map controls, feature legend, and map-based feature details.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../guides-list/index.md)._{ .guides-list-ref }

---

### Group Map

The **Dataset Map** on a project group page displays dataset boundaries. Each dataset card's **Zoom To Dataset Boundary** control selects its boundary and frames it in the map. **Zoom in**, **Zoom out**, and **Reset bearing to north** adjust the map view. The **Draw rectangle** control applies an area filter, and **Clear selection** removes that filter. The map instructions identify **Escape** as the way to exit drawing mode and describe keyboard access to map controls.

![TDEI Data Viewer group map with a dataset boundary selected and its card highlighted](../../../resources/images/tdei/data-viewer/user-manual/03-maps/group-map-dataset-boundary-selected-light.avif#only-light)
![TDEI Data Viewer group map with a dataset boundary selected and its card highlighted](../../../resources/images/tdei/data-viewer/user-manual/03-maps/group-map-dataset-boundary-selected-dark.avif#only-dark)

The separator between the dataset list and map is keyboard-resizable: when focused, **Left Arrow** and **Right Arrow** move the divider.

### Dataset Map View

Selecting **Explore** on a dataset card opens the dataset-specific map. Its heading area displays the dataset name, dataset ID, project group, and version. The back control identifies the project group page it returns to. The **Show boundary** checkbox toggles the dataset boundary on the map.

The map includes **Zoom in**, **Zoom out**, and **Reset bearing to north** controls. Its legend identifies the feature categories displayed:

- Sidewalk
- Crossing Marked
- Crossing Unmarked
- Footway
- Traffic Island
- Others
- Kerb Lowered
- Kerb Flushed
- Kerb Raised

![TDEI Data Viewer dataset map showing the enabled boundary, feature legend, and mapped features](../../../resources/images/tdei/data-viewer/user-manual/03-maps/dataset-map-overview-light.avif#only-light)
![TDEI Data Viewer dataset map showing the enabled boundary, feature legend, and mapped features](../../../resources/images/tdei/data-viewer/user-manual/03-maps/dataset-map-overview-dark.avif#only-dark)

### Feature Details on the Map

Hovering over a mapped feature displays its available properties as key/value pairs. The properties depend on the selected feature.

![TDEI Data Viewer map showing property values for a hovered sidewalk feature](../../../resources/images/tdei/data-viewer/user-manual/03-maps/map-feature-hover-details-light.avif#only-light)
![TDEI Data Viewer map showing property values for a hovered sidewalk feature](../../../resources/images/tdei/data-viewer/user-manual/03-maps/map-feature-hover-details-dark.avif#only-dark)

The group map attribution identifies MapLibre, CARTO, and OpenStreetMap contributors. The dataset map attribution identifies CARTO and OpenStreetMap contributors.

---

**Previous:** [Project Groups and Datasets](project-groups.md) | **Next:** [Feature Inspection and Feedback](feature-inspection-and-feedback.md)
