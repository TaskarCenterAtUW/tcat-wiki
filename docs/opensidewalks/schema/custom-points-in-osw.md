---
title: Custom Points in OSW
tags:
    - Guide
    - External
    - Developer
    - OSW 0.3
---

<!-- @format -->

# Custom Points in OSW

This guide shows how to add custom non-routable point features (like bus stops) to an OpenSidewalks dataset using the Custom Points entity type.

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

## What are Custom Points?

Custom Points in OpenSidewalks are user-defined non-routable point features that extend the schema beyond the predefined Core Entities and Adjacent Entities point types. While OpenSidewalks includes many built-in point types like fire hydrants, benches, and street lamps, Custom Points let you add any custom feature!

Doing so is simple - just prefix `ext:` before the tags that are not in the OSW schema.

This approach allows for immediately adding custom data, preserving data from existing systems.

## Common Use Cases

Custom Points are perfect for adding:

-   **Transit infrastructure**: Bus stops, public transport shelters
-   **Accessibility features**: Accessible parking spaces, wheelchair-accessible entrances, elevators
-   **Wayfinding aids**: Information kiosks, signage
-   **Points of interest**: Water fountains, ATMs, restrooms

## Case Study: GTFS Bus Stops to OSW Custom Points

In this example, we'll convert bus stop data from a GTFS `stops.txt` file into OpenSidewalks Custom Points. This is a common scenario for transit agencies and cities wanting to integrate public transportation data with pedestrian network information.

### Understanding the Source Data

A typical GTFS `stops.txt` file contains bus stop information like this:

```csv
stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station
1001,1001,Main St & 1st Ave,Northbound stop,47.6062,-122.3321,,http://example.com/stops/1001,0,
1002,1002,Main St & 2nd Ave,Southbound stop,47.6065,-122.3325,,http://example.com/stops/1002,0,
```

### The Target: OSW Custom Points

We want to convert each bus stop into an OpenSidewalks Custom Point that looks like this:

```json
{
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [-122.3321, 47.6062]
    },
    "properties": {
        "_id": "bus_stop_1001",
        "ext:stop_id": "1001",
        "ext:stop_code": "1001",
        "ext:stop_name": "Main St & 1st Ave",
        "ext:stop_desc": "Northbound stop",
        "ext:stop_url": "http://example.com/stops/1001"
    }
}
```

## Step-by-Step Conversion Process

### Step 1: Prepare Your Data

Start with your GTFS `stops.txt` file. You'll need these key fields:

-   `stop_lat` and `stop_lon` (for coordinates)
-   `stop_id` (for unique identification)
-   Any other fields you want to preserve (name, description, etc.)

**Quality check your data:**

-   Remove any stops with missing coordinates
-   Ensure stop_id values are unique
-   Verify coordinates are in decimal degrees (WGS84)

### Step 2: Map Fields to OSW Structure

Create a mapping between your GTFS fields and OSW Custom Point properties:

| GTFS Field             | Goes in OSW as         | Notes                                               |
| ---------------------- | ---------------------- | --------------------------------------------------- |
| `stop_lon`, `stop_lat` | `geometry.coordinates` | Longitude first, then latitude                      |
| `stop_id`              | `_id`                  | Create unique OSW ID (e.g., "bus_stop\_" + stop_id) |
| `stop_id`              | `ext:stop_id`          | Keep original ID for reference                      |
| `stop_name`            | `ext:stop_name`        | Preserve original name                              |
| `stop_desc`            | `ext:stop_desc`        | Optional description                                |
| `stop_code`            | `ext:stop_code`        | Display code, if different from ID                  |
| `stop_url`             | `ext:stop_url`         | Link to more information                            |

A note on the `_id` field: Every OSW entity needs a unique `_id` (string with at least one character). For bus stops, consider using a prefix like "bus_stop\_" + the original stop_id to avoid conflicts with other features. Letters, numbers, and underscores are all fine!

### Step 3: Create the GeoJSON Structure

-   **Required fields** like `_id` go directly in `properties`
-   **Custom fields** get the `ext:` prefix and go in `properties`
-   **Geometry** goes in the `geometry` section, not `properties`

Your Custom Points need to be formatted as GeoJSON Features within a FeatureCollection. Here's how the field mapping from Step 2 translates into actual JSON:

```json
{
    "$schema": "https://sidewalks.washington.edu/opensidewalks/0.3/schema.json",
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-122.3321, 47.6062] // stop_lon, stop_lat
            },
            "properties": {
                "_id": "bus_stop_1001", // Required OSW field
                "ext:stop_id": "1001", // Original GTFS stop_id
                "ext:stop_name": "Main St & 1st Ave", // Original GTFS stop_name
                "ext:stop_desc": "Northbound stop" // Original GTFS stop_desc
            }
        }
    ]
}
```

**Key Structure Points:**

-   All of the GTFS data fields (except coordinates) go in the `properties` section
-   Custom fields like `ext:stop_name` are the actual field names in your JSON
-   The `ext:` prefix is part of the field name, not a folder structure

### Step 4: Add Dataset Metadata

Include required OpenSidewalks metadata at the dataset level:

```json
{
    "$schema": "https://sidewalks.washington.edu/opensidewalks/0.3/schema.json",
    "type": "FeatureCollection",
    "dataSource": {
        "name": "Metro Transit GTFS",
        "license": "Public Domain"
    },
    "dataTimestamp": "2024-12-01T00:00:00Z",
    "features": [
        // ... your custom points here
    ]
}
```

## Conversion Tools

### Option 1: Purpose-built Scripts

In the specific case of GTFS stops, a script such as this one created by TCAT, [gtfs-to-tdei-converter.ps1](https://github.com/TaskarCenterAtUW/tdei-tools/blob/main/utilities/gtfs-to-tdei-converter.ps1), can be used.

### Option 2: Online JSON Tools

Use your spreadsheet software of choice to add `ext:` prefix to column headers, then convert CSV to GeoJSON:

-   https://geojson.io/
-   https://mapbox.github.io/csv2geojson/

## Validation and Quality Assurance

### Check Your Output

Before using your Custom Points, verify:

1. **Valid GeoJSON**: Use geojson.io or a JSON validator
2. **Coordinate format**: Longitude first, then latitude
3. **Unique IDs**: Each `_id` appears only once
4. **Required fields**: Every Custom Point has an `_id` and valid coordinates
5. **Custom fields**: All additional data uses the `ext:` prefix

### Common Issues and Fixes

| Problem              | Solution                                        |
| -------------------- | ----------------------------------------------- |
| Coordinates reversed | Longitude should be first: `[lng, lat]`         |
| Missing `_id` field  | Add unique identifier to each feature           |
| Invalid JSON         | Use a JSON validator to find syntax errors      |
| Coordinate precision | GTFS uses 6+ decimal places; preserve precision |

## Integration with Existing OSW Data

### Manual Adding to Existing Datasets

To add Custom Points to an existing OpenSidewalks dataset:

1. Load your existing .osw file
2. Add your Custom Point features to the `features` array
3. Ensure all `_id` values remain unique across the entire dataset

### Coordinate System Compatibility

OpenSidewalks uses WGS84 (EPSG:4326) coordinates in decimal degrees. GTFS data is already in this format, so no conversion is needed. If your source data uses a different coordinate system, you'll need to reproject it first.

## Best Practices

### Fields

-   Use descriptive `ext:` field names: `ext:stop_name` not `ext:name`
-   Keep original field names when possible for easier maintenance
-   Be consistent across all your Custom Points
-   Remove unnecessary fields to keep file sizes manageable
