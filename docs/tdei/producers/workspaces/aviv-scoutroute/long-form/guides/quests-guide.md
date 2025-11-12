---
title: Long Form Quests Guide
tags:
  - External
  - Developer
---

<!-- @format -->

# Long Form Quests Guide

This guide explains how to create a Workspace from the TDEI Portal, configure it for AVIV ScoutRoute, and define Long Form Quests for field data collection.  
It also covers Custom Imagery setup and JSON schema references.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../../../../../guides-list/index.md)._

---

## Overview

This document explains how to create a **Workspace** from the **TDEI Portal**, configure it for **AVIV ScoutRoute**, and define **Long Form Quests** for field data collection.  
It also includes details on **Custom Imagery** setup and JSON schema references.

This guide explains the **structure**, **components**, and **usage examples**, including **element definitions**, **question logic**, and **custom imagery configuration**.

---

## Creating a Workspace from TDEI Portal

Before configuring Long Form Quests, create a Workspace linked to a dataset in the TDEI Portal.

### Steps

1. **Navigate to Datasets**
    - Open the **TDEI Portal**.  
    - Select the dataset you want to use.

   ![Datasets](../../../../../../resources/images/aviv-scoutroute/long-form/01-datasets.png){ width="800" }

2. **Open in Workspaces**
    - Click the **three-dot menu (⋮)** next to the dataset.  
    - Select **“Open in Workspaces.”**

    ![Open in Workspaces](../../../../../../resources/images/aviv-scoutroute/long-form/02-open-in-workspaces.png){ width="800" }

3. **Create Workspace**
    - You’ll be redirected to **TDEI Workspaces**.  
    - You will find pre-filled:
        - **Workspace Title**
        - **Project Group**
    - Click **Create Workspace**.

    ![Create Workspace](../../../../../../resources/images/aviv-scoutroute/long-form/03-create-workspace.png){ width="800" }

4. **Verify Workspace**
    - Your new workspace appears in the list under your project group.  
    - You’ll see:
        - Map bounding box auto-filled from dataset geometry  
        - Metadata (dataset version, creator, etc.)  
        - Access control (enabled/disabled)

    ![Verify Workspace](../../../../../../resources/images/aviv-scoutroute/long-form/04-verify-workspace.png){ width="800" }

---

## Understanding Long Form Quests (v3.0.0)

Once the workspace is created, you can add Long Form Quests that define the survey questions displayed in AVIV ScoutRoute.

### Purpose
Long Form Quests define the data collected in the field (e.g., sidewalk continuity, surface material, width).

### File Location
The quest definition can be:
* Defined directly within Workspaces (using the JSON editor), or  
* Loaded from an external JSON URL.

---

## Adding Long Form Quests to a Workspace

### Option A – Define Quests in Workspaces

1. Open the workspace in TDEI Workspaces.  
2. Click the **Settings (⚙️)** icon.  
3. Scroll to **External Apps → AVIV ScoutRoute Long Form Quest Definitions.**  
4. Select **“Define quests in Workspaces.”**  
5. Paste your Long Form Quest JSON into the editor.  
6. Click **Save.**

![Adding Quests](../../../../../../resources/images/aviv-scoutroute/long-form/05-adding-quests.png){ width="800" }

### Option B – Load Quests from External URL

If quest definitions are managed centrally (e.g., on GitHub):

1. Choose **“Load quest definitions from external URL.”**  
2. Enter the hosted JSON URL (e.g., GitHub raw link).  
3. Click **Save.**

![External Apps](../../../../../../resources/images/aviv-scoutroute/long-form/06-external-apps.png){ width="800" }

_See also:_  
* [Long Form Schema](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-quests/refs/heads/main/schema/schema.json)  
* [Example JSON](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-quests/refs/heads/main/examples/example.json)

---

## Long Form JSON Structure Explained
Below is the detailed breakdown of the JSON format used in AVIV ScoutRoute (v3.0.0).

### Top-Level Structure

Every Long Form JSON file has two primary keys:

| Field | Description |
| :---- | :---- |
| **version** | Indicates the schema version being used (e.g., `"3.0.0"`). |
| **elements** | An array of element objects, each representing a type of physical feature (like sidewalks, curbs, or crossings). |

```json
{
  "version": "3.0.0",
  "elements": [ ... ]
}
```

This top-level format ensures backward compatibility with future schema versions while allowing multiple element types within a single quest file.

---

### Element Object

Each **element** represents a physical feature on the map that users will collect data for.  
 For example: sidewalks, crossings, curbs, or bus stops.

| Field | Type | Description |
| :---- | :---- | :---- |
| **element\_type** | string | The name of the feature (e.g., `"Sidewalk"`, `"Crossing"`). |
| **quest\_query** | string | A query expression that defines which map features this element applies to. For example, `"ways with (highway=footway and footway=sidewalk)"`. |
| **element\_type\_icon** | string | The icon name or identifier shown in the ScoutRoute app. |
| **quests** | array | List of **Question Objects** that define what to ask the user for this element. |

```json
{
  "element_type": "Sidewalk",
  "quest_query": "ways with (highway=footway and footway=sidewalk)",
  "element_type_icon": "sidewalk_icon",
  "quests": [ ... ]
}
```


---

### Question Object

Defines each field question.

| Field | Required | Description |
| :---- | :---- | :---- |
| **quest\_id** | Yes | Unique numeric ID |
| **quest\_title** | Yes | Displayed question |
| **quest\_description** | Yes | Instructions |
| **quest\_type** | Yes | Input type (ExclusiveChoice, MultipleChoice, Numeric, TextEntry) |
| **quest\_tag** | Yes | Data tag stored in OSM or export |
| **quest\_answer\_choices** | Optional | For choice-based questions |
| **quest\_answer\_validation** | Optional | For numeric limits |
| **quest\_answer\_dependency** | Optional | To show conditionally |

```json
{
  "element_type": "Sidewalk",
  "quest_query": "ways with (highway=footway and footway=sidewalk)",
  "element_type_icon": "sidewalk_icon",
  "quests": [
    {
      "quest_id": 1,
      "quest_title": "Is the sidewalk continuous?",
      "quest_description": "Select whether the sidewalk is continuous or interrupted.",
      "quest_type": "ExclusiveChoice",
      "quest_tag": "sidewalk:continuous",
      "quest_answer_choices": [
        { "value": "yes", "choice_text": "Yes" },
        { "value": "no", "choice_text": "No" }
      ]
    }
  ]
}
```

---

### Quest Types Summary
| Type | Input | Example |
| :---- | :---- | :---- |
| **Exclusive Choice** | One option only | Yes / No / Unknown |
| **MultipleChoice** | Multiple selections | Ramp, Tactile paving, Warning tiles |
| **Numeric** | Number entry | Width (m), gradient (%) |
| **TextEntry** | Free text | Notes or comments |

**Validation Example (Numeric)**

```json
{
  "quest_id": 301,
  "quest_title": "What is the width of the sidewalk?",
  "quest_description": "Enter width in meters.",
  "quest_type": "Numeric",
  "quest_tag": "width",
  "quest_answer_validation": { "min": 0.5, "max": 10 }
}
```

**Dependency Example**

```json
"quest_answer_dependency": {
  "question_id": 101,
  "required_value": "yes"
}
```
→ The dependent question appears only if Question 101 \= “yes”.
---

## Configuring Custom Imagery

Add Custom Imagery (e.g., Esri satellite maps or other tile servers) to enhance the workspace.

### **Steps**

1. Go to the **Custom Imagery** section in Workspace Settings.  
2. Paste a valid JSON definition (see below).  
3. Click **Save**.

![Custom Imagery](../../../../../../resources/images/aviv-scoutroute/long-form/07-custom-imagery.png){ width="800" }

**Example**

```json
[
  {
    "id": "EsriWorldImageryClarity",
    "name": "Esri World Imagery (Clarity) Beta",
    "type": "xyz",
    "url": "https://clarity.maptiles.arcgis.com/arcgis/rest/services/World_Imagery/MapServer/tile/{zoom}/{y}/{x}"
  }
]
```
**Reference**

* [Custom Imagery Schema](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/schema/schema.json)  
* [Custom Imagery Example](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/examples/example.json)

---

## Quick Summary

### Imagery Definition
The imagery JSON describes a list of imagery sources — for example, aerial or satellite imagery layers used in the application. Each imagery entry tells the app where the images come from, how to display them, and what attribution text to show.

In simple terms, each entry \= one imagery provider (like Bing, Mapbox, or local city maps).

### **Structure Overview** 

Each object represents one imagery source and must include these fields:

```json
{
   "attribution": {...},
   "description": "...",
   "extent": {...},
   "icon": "...",
   "id": "...",
   "name": "...",
   "type": "...",
   "url": "..."
 }

```
### **Fields Explained**

| Field | Description | Example |
| :---- | :---- | :---- |
| **id** | A unique identifier for the imagery source. Keep it short, lowercase, and descriptive. This acts as a reference key internally. | `bing_aerial`, `mapbox_satellite` |
| **name** | The display name shown to users in the app UI or dropdown lists. Should be readable and descriptive. | `Bing Aerial`, `Mapbox Satellite` |
| **description** | A short summary describing what the imagery source provides or how it differs from others. | `High-resolution satellite imagery from Bing Maps.` |
| **icon** | URL of a small image or logo used to visually represent the imagery source in the interface. | `https://example.com/icons/bing.png` |
| **url** | The base URL template used to fetch map tiles. Supports `{z}`, `{x}`, and `{y}` placeholders. | `https://example.com/tiles/{z}/{x}/{y}.jpg` |
| **type** | Type of imagery service. Supported values: `xyz`, `tms`, or `wmts`. Most sources use `xyz`. | `xyz` |

### **Imagery Type Details**

| Type | Description |
| :---- | :---- |
| **tms** | Tile Map Service. Tiles start from the bottom-left corner. |
| **wmts** | Web Map Tile Service. Similar to TMS but more standardized. |
| **xyz** | Most common format. Tiles start from the top-left corner. |

#### **Attribution** 

Information about who owns or provides the imagery. It has three parts:  
 \- required: Whether attribution must be shown (true/false)  
 \- text: The credit text (e.g., © Bing Maps)  
 \- url: The provider's website link.

#### **Extent**

Defines where the imagery is valid and how deep you can zoom in.  
 \- max\_zoom: Highest zoom level available (e.g., 19 \= very close view)  
 \- polygon: The area coverage, defined as a set of \[longitude, latitude\] coordinates.

**Example of Complete Imagery Entry**
```json
{
   "id": "bing_aerial",
   "name": "Bing Aerial",
   "description": "High-resolution aerial imagery from Bing Maps.",
   "icon": "https://example.com/icons/bing.png",
   "type": "xyz",
   "url": "https://bing.com/tiles/{z}/{x}/{y}.jpg",
   "attribution": {
     "required": true,
     "text": "© Bing Maps",
     "url": "https://bing.com/maps"
   },
   "extent": {
     "max_zoom": 19,
     "polygon": [[ [77.0,17.0],[78.0,17.0],[78.0,18.0],[77.0,18.0],[77.0,17.0] ]]
   }
 }
```
### Quick Summary

| Field | What It Means | Example |
| :---- | :---- | :---- |
| id | Internal unique name | bing\_aerial |
| name | Display name | Bing Aerial |
| description | Short explanation | Satellite imagery from Bing |
| icon | Image or logo URL | https://example.com/icon.png |
| type | Type of map service | xyz |
| url | Tile fetch link | https://.../{z}/{x}/{y}.jpg |
| attribution | Credits to the imagery provider | © Bing Maps |
| extent | Area coverage & zoom level | max\_zoom: 19, polygon: \[coords\] |
