---
title: Element Type Icon Guide
---

# Element Type Icon Guide

This guide explains how to assign the correct value for the `element_type_icon` key in the Long Form Quest Definition JSON file used by AVIV ScoutRoute.

These icons help the mobile app display appropriate quest icons for each element type (like sidewalks, crossings, kerbs, etc.).

## Instructions
1. Open the [Icon Reference Website](https://provisodevstorage.blob.core.windows.net/projects/gig-element-icons/search.html)
2. Search for the Appropriate Icon
   1. Use the search bar on the website to search for an icon related to the element you're working with (e.g., "sidewalk", "crossing", "kerb").
3. Find the Icon Name
   1. Once you've located a suitable icon, click on it.
   2. Copy the exact icon name (e.g., sidewalk, car_charger_capacity).
4. Add It to Your Quest Definition
   1. Insert the icon name as the value for the the `element_type_icon` key.
   2. Make sure to not include any file extension (like .png or .svg)

## Example:
``` json hl_lines="2"
  "element_type": "Sidewalks",
  "element_type_icon": "sidewalk",
  "quest_query": "ways with (highway=footway and footway=sidewalk)",
  "quests": [ ... ]
```

## How the Mobile App Uses It
* The mobile app will parse the element_type_icon field from the JSON.
* If the value matches an icon available in the app, that icon is shown.
* If the value is missing or doesn't match, the app will fall back to a default icon.
