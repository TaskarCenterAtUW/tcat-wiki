#!/usr/bin/env python3
"""
Convert ADA Curb Ramp GeoJSON to OSW 0.3 format for TDEI upload.

Reads a GeoJSON file of curb ramp point features and produces an OpenSidewalks
(OSW) 0.3 compliant .zip package ready for upload to the TDEI Portal as a new
dataset.

USAGE
    python convert-curb-ramps.py <input.geojson> [output.zip]

    If output.zip is not specified, the output is saved alongside the input
    file with "-osw.zip" appended to the name (e.g., curb_ramps-osw.zip).

ADAPTING FOR OTHER DATASETS
    Edit the CONFIGURATION section below to match your dataset's field names
    and coordinate system. No other changes are required. The script requires
    Python 3.8+. The `pyproj` package (pip install pyproj) is required only
    when SOURCE_CRS is set to a non-WGS84 coordinate system.
"""

import json
import math
import os
import re
import sys
import zipfile
from datetime import datetime, timezone
from typing import Any


# =============================================================================
# CONFIGURATION  ← Edit this section to match your dataset
# =============================================================================

# Dataset source metadata included in the output OSW file header.
DATA_SOURCE_NAME = "Seattle Department of Transportation"
DATA_SOURCE_LICENSE = ""

# CORE PROPERTIES
# ---------------
# Standard OSW schema values applied to every output feature.
# "barrier": "kerb" is correct for curbs and ramps.
# Only change this if your dataset represents a different feature type.
CORE_PROPERTIES = {
    "barrier": "kerb",     # All curb ramp features use barrier=kerb in OSW
}

# RAMP WIDTH
# ----------
# Name of the source field containing ramp width data.
# Expected to be in INCHES — the script converts to meters automatically.
# Set to None to skip width if your dataset does not include it.
RAMP_WIDTH_FIELD = "RAMP_WIDTH"

# UNIQUE IDENTIFIER
# -----------------
# Source field that uniquely identifies each feature. Used to build the OSW _id.
ID_FIELD = "UNITID"  # Change to your dataset's unique identifier field name
ID_PREFIX = "ramp_"   # OSW _ids must start with a letter; this prefix ensures that

# EXTENSION FIELDS
# ----------------
# Source fields to preserve in the output under the OSW "ext:" prefix.
# These carry agency-specific data beyond the standard OSW schema.
#
# Format: "ext:output_name": "SOURCE_FIELD_NAME"
#
# Add, remove, or rename entries to match your dataset's available fields.
# Values that are empty, null, or "None" in the source are automatically omitted.
EXT_FIELDS = {
    "ext:unit_id":   "UNITID",        # Original SDOT unit identifier
    "ext:ada":       "ADA_COMPLIANT",  # ADA compliance status
    "ext:desc":      "INT_UNITDESC",  # Intersection/location description
    "ext:side":      "SW_STSIDE",     # Which side of the street
    "ext:direction": "DIRECTION",     # Direction the ramp faces
    "ext:condition": "CONDITION",     # Physical condition rating
    "ext:style":     "STYLE",         # Ramp style/construction type
}

# SOURCE COORDINATE SYSTEM
# -------------------------
# EPSG code of the coordinate system used by your source data.
# Many city open data portals publish datasets in a local projected system
# rather than WGS84. You can find the EPSG code in the dataset's metadata or
# by inspecting the coordinate values: WGS84 longitudes are between -180 and
# 180 and latitudes are between -90 and 90. Values far outside those ranges
# indicate a projected system.
#
# When set to anything other than WGS84, the pyproj package is required:
#   pip install pyproj
#
# Set to None if your data is already in WGS84 / EPSG:4326.
SOURCE_CRS = "EPSG:2926"  # SDOT data: Washington State Plane South, US feet

# =============================================================================
# END OF CONFIGURATION — no changes needed below this line
# =============================================================================

# Reprojection transformer — initialized once at startup when SOURCE_CRS is set
_transformer = None
if SOURCE_CRS and SOURCE_CRS.upper() not in ("EPSG:4326", "WGS84", "CRS84"):
    try:
        from pyproj import Transformer
        _transformer = Transformer.from_crs(
            SOURCE_CRS, "EPSG:4326", always_xy=True)
    except ImportError:
        import sys as _sys
        print(
            "Error: reprojection requires the pyproj package.\n"
            "Install it by running:  pip install pyproj",
            file=_sys.stderr,
        )
        _sys.exit(1)


def _strip_z(coords: list[Any]) -> list[Any]:
    """Recursively remove the Z (third) dimension from GeoJSON coordinate arrays."""
    if not coords:
        return coords
    if isinstance(coords[0], (int, float)):
        return coords[:2]
    return [_strip_z(c) for c in coords]


def _reproject_point(coords):
    """
    Reproject a 2D coordinate pair [x, y] from SOURCE_CRS to WGS84.
    Returns [longitude, latitude] as required by GeoJSON RFC 7946.
    No-op when _transformer is None (i.e. source data is already WGS84).
    """
    if _transformer is None:
        return coords
    lon, lat = _transformer.transform(coords[0], coords[1])
    return [lon, lat]


def _clean(value):
    """
    Return None if the value is missing or a null-like string; otherwise return
    the value unchanged. Handles Python None, JSON null, "None", "null", "NaN".
    """
    if value is None:
        return None
    if isinstance(value, float) and (value != value or math.isinf(value)):
        return None
    if isinstance(value, str) and value.strip().lower() in ("", "none", "null", "nan", "n/a"):
        return None
    return value


def _inches_to_meters(raw):
    """Convert an inches value to meters, rounded to 2 decimal places."""
    v = _clean(raw)
    if v is None:
        return None
    try:
        m = float(v) * 0.0254
        return round(m, 2) if m > 0 else None
    except (TypeError, ValueError):
        return None


def _make_osw_id(raw_id):
    """Build a safe OSW _id string from a raw source identifier."""
    return ID_PREFIX + re.sub(r'[^a-zA-Z0-9_]', '_', str(raw_id)).lower()


def _convert_feature(raw_feature, seen_ids):
    """
    Convert one source GeoJSON feature to an OSW node feature.
    Returns the converted feature dict, or None if the feature should be skipped.
    """
    props = raw_feature.get("properties") or {}
    geom = raw_feature.get("geometry")

    # Must have Point geometry with coordinates
    if not geom or geom.get("type") != "Point" or not geom.get("coordinates"):
        return None

    # Validate and de-duplicate by OSW _id
    raw_id = _clean(props.get(ID_FIELD))
    if raw_id is None:
        return None
    osw_id = _make_osw_id(raw_id)
    if osw_id in seen_ids:
        return None
    seen_ids.add(osw_id)

    # Strip Z coordinates (OSW 0.3 uses 2D geometry only), then reproject
    # from SOURCE_CRS to WGS84 if the source uses a projected coordinate system.
    coords = _strip_z(geom["coordinates"])
    coords = _reproject_point(coords)

    # Validate that the result is a plausible WGS84 coordinate
    lon: float = float(coords[0])
    lat: float = float(coords[1])
    if lon < -180 or lon > 180 or lat < -90 or lat > 90:
        return None

    geom = {**geom, "coordinates": coords}

    # Build output properties
    out: dict[str, str | float] = {"_id": osw_id}
    out.update(CORE_PROPERTIES)

    # Ramp width converted from inches to meters, stored as an extension field
    if RAMP_WIDTH_FIELD:
        width = _inches_to_meters(props.get(RAMP_WIDTH_FIELD))
        if width is not None:
            out["ext:width"] = width

    # Agency-specific extension fields
    for osw_key, src_field in EXT_FIELDS.items():
        value = _clean(props.get(src_field))
        if value is not None:
            out[osw_key] = value

    return {"type": "Feature", "geometry": geom, "properties": out}


def convert(input_path, output_zip):
    """Read the source GeoJSON, convert all features, and write the output .zip."""
    print(f"Reading {input_path} ...")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    features_in = data.get("features", [])
    print(f"  {len(features_in):,} features found")

    seen_ids, features_out, skipped = set(), [], 0
    for feat in features_in:
        result = _convert_feature(feat, seen_ids)
        if result is not None:
            features_out.append(result)
        else:
            skipped += 1

    print(f"  {len(features_out):,} converted, {skipped:,} skipped "
          f"(missing geometry, ID, or duplicate)")

    osw_dataset = {
        "$schema":       "https://sidewalks.washington.edu/opensidewalks/0.3/schema.json",
        "type":          "FeatureCollection",
        "dataSource":    {"name": DATA_SOURCE_NAME, "license": DATA_SOURCE_LICENSE},
        "dataTimestamp": datetime.now(timezone.utc).isoformat(),
        "features":      features_out,
    }

    # The file inside the zip must end in .nodes.geojson for OSW to recognize it
    base = os.path.splitext(os.path.basename(input_path))[0]
    nodes_filename = base + ".nodes.geojson"
    geojson_str = json.dumps(osw_dataset, indent=2, ensure_ascii=False)

    print(f"Writing {output_zip} ...")
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(nodes_filename, geojson_str)

    print(f"Done.")
    print(f"  Output     : {output_zip}")
    print(f"  Inner file : {nodes_filename}")
    print(f"  Features   : {len(features_out):,}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_zip = (sys.argv[2] if len(sys.argv) >= 3
                  else os.path.splitext(input_path)[0] + "-osw.zip")

    convert(input_path, output_zip)


if __name__ == "__main__":
    main()
