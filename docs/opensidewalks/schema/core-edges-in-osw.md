---
title: Core Edges in OSW
tags:
    - Guide
    - External
    - Developer
    - OSW 0.3
---

<!-- @format -->

# Core Edges in OSW

This guide shows how to convert existing sidewalk centerline datasets into OpenSidewalks (OSW) format for upload to the Transportation Data Exchange Initiative (TDEI).

_For a list of all guides on the TCAT Wiki, refer to the [Guides List](../../guides-list/index.md)._

---

## What Are Sidewalk Centerlines?

Sidewalk centerlines are linear GIS features representing the middle path of sidewalk infrastructure. These datasets are commonly maintained by city transportation departments and typically include attributes like:

-   **Width information**: Sidewalk dimensions and measurements
-   **Surface conditions**: Material type and maintenance status
-   **Location data**: Street names, sides, and block segments
-   **Maintenance records**: Installation dates and inspection history

Converting these datasets to OSW format enables pedestrian routing, accessibility analysis, and integration with other transportation data through TDEI.

## Case Study: Seattle Sidewalk Centerlines to OSW

This example demonstrates converting a city's sidewalk centerline dataset to OSW format using Seattle's sidewalk inventory data.

### Understanding the Source Data

Seattle's sidewalk dataset contains LineString features with detailed attributes:

```json
{
    "type": "Feature",
    "id": 22276849,
    "geometry": {
        "type": "LineString",
        "coordinates": [
            [1270173.15, 221881.27],
            [1270372.84, 221876.92]
        ]
    },
    "properties": {
        "OBJECTID": 22276849,
        "UNITID": "SDW-35269",
        "UNITDESC": "S KING ST BETWEEN 1ST AVE S AND OCCIDENTAL W AVE S, N SIDE",
        "SW_WIDTH": 124,
        "CONDITION": "POOR",
        "SURFTYPE": "PCC",
        "SIDE": "N",
        "PRIMARYCROSSSLOPE": 5.3,
        "INSTALL_DATE": null,
        "LAST_VERIFY_DATE": "Fri, 23 Jun 2017 00:00:00 GMT"
    }
}
```

### The Target: OSW Footway Edges

We want to convert each sidewalk centerline into an OpenSidewalks footway that looks like this:

```json
{
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [
            [-122.3321, 47.6062],
            [-122.3325, 47.6065]
        ]
    },
    "properties": {
        "_id": "sidewalk_sdw_35269",
        "highway": "footway",
        "footway": "sidewalk",
        "width": 3.78,
        "surface": "concrete",
        "ext:unit_id": "SDW-35269",
        "ext:description": "S KING ST BETWEEN 1ST AVE S AND OCCIDENTAL W AVE S, N SIDE",
        "ext:condition": "POOR",
        "ext:side": "N",
        "ext:cross_slope": 5.3,
        "ext:last_verify_date": "2017-06-23"
    }
}
```

## Step-by-Step Conversion Process

### Step 1: Coordinate System Transformation

Most city GIS datasets use local coordinate systems. Seattle uses EPSG:2926 - NAD83 / Washington South. OSW requires WGS84 decimal degrees (EPSG:4326).

**Transform coordinates before conversion:**

-   Use GIS software (QGIS, ArcGIS) or GDAL utilities

### Step 2: Map Fields to OSW Structure

Create a mapping between your dataset fields and OSW properties:

| Source Field             | Goes in OSW as         | Notes                                               |
|--------------------------|------------------------|-----------------------------------------------------|
| `<geometry coordinates>` | `geometry.coordinates` | Must be EPSG:4326 (WGS84)                           |
| `UNITID`                 | `_id`                  | Create unique OSW ID (e.g., "sidewalk\_" + unit_id) |
| `UNITID`                 | `ext:unit_id`          | Keep original ID for reference                      |
| `UNITDESC`               | `ext:description`      | Preserve location description                       |
| `SW_WIDTH`               | `width`                | Convert to meters if in different units             |
| `SURFTYPE`               | `surface`              | Map to OSW surface values (see Step 3)              |
| `CONDITION`              | `ext:condition`        | Preserve condition assessment                       |
| `SIDE`                   | `ext:side`             | Road side (N/S/E/W)                                 |
| `PRIMARYCROSSSLOPE`      | `ext:cross_slope`      | Cross slope percentage                              |
| `LAST_VERIFY_DATE`       | `ext:last_verify_date` | Convert to ISO 8601 format                          |

**Required OSW Core Entity Fields:**

-   `_id`: Unique identifier (string, letters/numbers/underscores)
-   `geometry`: LineString coordinates in WGS84
-   `highway=footway` + `footway=sidewalk`: Sidewalk Core Entity tag

### Step 3: Standardize Surface Types

Map your dataset's surface codes to OSW-compatible values:

| Source Code | OSW Surface Value | Description              |
|-------------|-------------------|--------------------------|
| `PCC`       | `concrete`        | Portland cement concrete |
| `AC`        | `asphalt`         | Asphalt concrete         |
| `UIMPRV`    | `unpaved`         | Unimproved/dirt surface  |
| `BR`        | `paving_stones`   | Brick pavers             |

### Step 4: Handle Width Measurements

Convert width measurements to meters and include in the `width` property.

### Step 5: Create the GeoJSON Structure

Build the complete OSW dataset:

```json
{
    "$schema": "https://sidewalks.washington.edu/opensidewalks/0.3/schema.json",
    "type": "FeatureCollection",
    "dataSource": {
        "name": "Seattle Department of Transportation",
        "license": "Open Data Commons Attribution License"
    },
    "dataTimestamp": "2025-09-10T00:00:00Z",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-122.3321, 47.6062],
                    [-122.3325, 47.6065]
                ]
            },
            "properties": {
                "_id": "sidewalk_sdw_35269",
                "highway": "footway",
                "footway": "sidewalk",
                "width": 3.78,
                "surface": "concrete",
                "ext:unit_id": "SDW-35269",
                "ext:description": "S KING ST BETWEEN 1ST AVE S AND OCCIDENTAL W AVE S, N SIDE",
                "ext:condition": "POOR"
            }
        }
    ]
}
```

## Conversion Tools and Scripts

As some processing of the existing data is usually necessary, consider creating Python scripts or using [ogr2ogr](https://gdal.org/en/stable/programs/ogr2ogr.html) to make the necessary changes.

_The following is an example, not intended to be used directly!_

### Example: GDAL/OGR Command Line

```bash
# Reproject to WGS84
ogr2ogr -s_srs EPSG:2926 -t_srs EPSG:4326 sidewalks_epsg4326.geojson sidewalks_epsg2926.geojson

# Use ogr2ogr with SQL to transform fields
ogr2ogr -f GeoJSON output.geojson sidewalks_epsg4326.geojson -sql "SELECT UNITID as ext_unit_id, UNITDESC as ext_description, 'footway' as highway, 'sidewalk' as footway, SW_WIDTH * 0.0254 as width, CASE WHEN SURFTYPE = 'PCC' THEN 'concrete' WHEN SURFTYPE = 'AC' THEN 'asphalt' ELSE 'unknown' END as surface FROM input_layer"
```

## Validation and Quality Assurance

### Data Quality Checks

1. **Coordinate System**: Verify all coordinates are in WGS84 decimal degrees
2. **Unique IDs**: Ensure all `_id` values are unique across the dataset
3. **Required Fields**: Every feature must have `_id`, `highway=footway`, and `footway=sidewalk`
4. **Geometry Validity**: All LineStrings should have at least 2 coordinate pairs

### Common Issues and Fixes

| Problem                         | Solution                                      |
|---------------------------------|-----------------------------------------------|
| Coordinates in wrong projection | Use `ogr2ogr` or GIS reprojection tools       |
| Duplicate IDs                   | Add prefixes or suffixes to ensure uniqueness |
| Missing width data              | Omit width property                           |
| Invalid surface types           | Create comprehensive surface mapping table    |
| Broken geometry                 | Use `ST_MakeValid()` or geometry repair tools |

### Validation Tools

-   **GeoJSON validation**: Use geojson.io or offline validators
-   **OSW schema validation**: Check against OpenSidewalks schema
-   **Visual inspection**: Load in QGIS or web mapping tools
-   **Attribute completeness**: Verify required and optional fields

## Integration with TDEI

### Best Practices for TDEI Upload

-   **Regular updates**: Plan for periodic data refreshes
-   **Quality documentation**: Document data collection methods and accuracy
-   **Contact information**: Provide maintainer contact for data issues

## Advanced Considerations

### Handling Complex Geometries

Some sidewalk centerlines may include:

-   **Multi-segment paths**: Keep as single LineString if continuous
-   **Branching sidewalks**: Split into separate features at intersections
-   **Curved sections**: Maintain vertex density for accurate representation

### Accessibility Attributes

Enhance OSW data with additional accessibility information:

```json
"properties": {
  "_id": "sidewalk_001",
  "highway": "footway",
  "footway": "sidewalk",
  "incline": "2%",
  "ext:condition": "good",
  "ext:cross_slope": 1.8,
  "ext:ada_compliance": "yes"
}
```

This comprehensive conversion creates routable pedestrian network data that integrates with transportation analysis tools and supports accessibility planning through the TDEI platform.
