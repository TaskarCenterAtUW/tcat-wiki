#!/usr/bin/env python3
"""Generate AVIV ScoutRoute event statistics as JSON.

Reads ``asr_``-prefixed frontmatter from an event's ``index.md``,
fetches workspace data from the Workspaces OSM-like API, parses the
OSM XML, and writes ``aviv-scoutroute-event-stats.json``.

Can be run standalone or called by ``generate-event-report.py``.

Authentication uses a TDEI API key passed via an environment variable
(default ``TDEI_API_KEY``, overridable with ``asr_api_key_env_var``
frontmatter or ``--api-key-env-var``).

Usage:
    python generate-asr-event-stats.py --event nda-vancouver
    python generate-asr-event-stats.py --event nda-vancouver --osm-file data.osm
"""

import argparse
import datetime
import os
import sys
import xml.etree.ElementTree as ET

# Ensure the common module is importable when invoked directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (
    METERS_PER_MILE,
    event_dir,
    fetch_bytes,
    fetch_json,
    haversine,
    print_separator,
    read_event_frontmatter,
    validate_required_fields,
    way_length_m,
    write_json,
)


# =============================================================================
# Constants
# =============================================================================

_STATS_FILE = "aviv-scoutroute-event-stats.json"
_DEFAULT_API_KEY_ENV_VAR = "TDEI_API_KEY"


# =============================================================================
# Workspaces API helpers
# =============================================================================

def _env_postfix(env):
    """Return the URL postfix for a Workspaces environment."""
    if env == "dev":
        return "-dev"
    if env == "stage":
        return "-stage"
    return ""  # prod


def _osm_base_url(env):
    """Return the OSM-like API base URL for the given environment."""
    return f"https://osm.workspaces{_env_postfix(env)}.sidewalks.washington.edu"


def _workspaces_api_url(env):
    """Return the Workspaces API base URL."""
    return f"https://new-api.workspaces{_env_postfix(env)}.sidewalks.washington.edu"


def _auth_headers(api_key, workspace_id):
    """Build authorization headers for the Workspaces API."""
    return {
        "Authorization": api_key,
        "X-Workspace": str(workspace_id),
    }


def fetch_workspace_bbox(env, workspace_id, api_key):
    """Fetch the bounding box for a workspace.

    Returns ``{min_lat, min_lon, max_lat, max_lon}``.
    """
    url = (f"{_osm_base_url(env)}/api/0.6"
           f"/workspaces/{workspace_id}/bbox.json")
    headers = _auth_headers(api_key, workspace_id)
    return fetch_json(url, headers=headers)


def fetch_workspace_map_xml(env, workspace_id, api_key, bbox):
    """Fetch OSM XML map data for the workspace bounding box.

    Returns raw XML bytes.
    """
    min_lon = bbox["min_lon"]
    min_lat = bbox["min_lat"]
    max_lon = bbox["max_lon"]
    max_lat = bbox["max_lat"]
    url = (f"{_osm_base_url(env)}/api/0.6"
           f"/map?bbox={min_lon},{min_lat},{max_lon},{max_lat}")
    headers = _auth_headers(api_key, workspace_id)
    headers["Accept"] = "application/xml, text/xml, */*"
    body, _ = fetch_bytes(url, headers=headers)
    return body


# =============================================================================
# OSM XML parsing
# =============================================================================

def parse_osm_xml(xml_bytes):
    """Parse OSM XML into a list of element dicts.

    Each element has:
      - ``type``: ``"node"`` or ``"way"``
      - ``id``: int
      - ``tags``: dict of key→value
      - ``user``: str or None
      - ``changeset``: int or None
      - ``lat``, ``lon``: float (nodes only)
      - ``nd_refs``: list of int (ways only)

    This function is intentionally a thin adapter so that swapping
    to ``pyosmium`` later only requires replacing this function.
    """
    root = ET.fromstring(xml_bytes)
    elements = []
    nodes_by_id = {}

    # First pass: collect all nodes (for way geometry resolution)
    for nd in root.iter("node"):
        nid = int(nd.get("id", "0"))
        lat = float(nd.get("lat", 0))
        lon = float(nd.get("lon", 0))
        tags = {tag.get("k"): tag.get("v") for tag in nd.iter("tag")}
        user = nd.get("user")
        cs = nd.get("changeset")
        ts = nd.get("timestamp")

        nodes_by_id[nid] = (lat, lon)
        elements.append({
            "type": "node",
            "id": nid,
            "lat": lat,
            "lon": lon,
            "tags": tags,
            "user": user,
            "changeset": int(cs) if cs else None,
            "timestamp": ts,
        })

    # Second pass: collect ways with resolved geometry
    for way in root.iter("way"):
        wid = int(way.get("id", "0"))
        tags = {tag.get("k"): tag.get("v") for tag in way.iter("tag")}
        user = way.get("user")
        cs = way.get("changeset")
        ts = way.get("timestamp")

        nd_refs = [int(nd.get("ref", "0")) for nd in way.iter("nd")]
        geometry = []
        for ref in nd_refs:
            if ref in nodes_by_id:
                lat, lon = nodes_by_id[ref]
                geometry.append((lat, lon))

        elements.append({
            "type": "way",
            "id": wid,
            "tags": tags,
            "user": user,
            "changeset": int(cs) if cs else None,
            "timestamp": ts,
            "nd_refs": nd_refs,
            "geometry": geometry,
        })

    return elements


def filter_by_time(elements, t_start, t_end):
    """Filter elements to those whose timestamp falls within [t_start, t_end].

    *t_start* and *t_end* are ISO 8601 strings (UTC).
    """
    dt_start = datetime.datetime.fromisoformat(t_start.replace("Z", "+00:00"))
    dt_end = datetime.datetime.fromisoformat(t_end.replace("Z", "+00:00"))
    filtered = []
    for el in elements:
        ts = el.get("timestamp")
        if not ts:
            continue
        dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if dt_start <= dt <= dt_end:
            filtered.append(el)
    dropped = len(elements) - len(filtered)
    if dropped:
        print(f"  Filtered to {len(filtered)} elements within time window "
              f"(dropped {dropped})")
    return filtered


# =============================================================================
# Stats computation
# =============================================================================

def compute_stats(elements):
    """Compute workspace statistics from parsed OSM elements.

    Mirrors the TM stats structure for consistency.
    """
    changesets = set()
    users = set()

    footway_length_m = 0.0
    crossing_way_length_m = 0.0
    sidewalk_way_length_m = 0.0
    steps_length_m = 0.0
    footway_way_count = 0
    crossing_way_count = 0
    sidewalk_way_count = 0
    steps_count = 0
    crossing_node_count = 0
    curb_node_count = 0
    total_ways = 0
    total_nodes = 0

    for el in elements:
        cs = el.get("changeset")
        if cs is not None:
            changesets.add(cs)
        user = el.get("user")
        if user:
            users.add(user)

        tags = el.get("tags", {})

        if el["type"] == "way":
            total_ways += 1
            geom = el.get("geometry", [])
            length = way_length_m(geom) if geom else 0.0
            highway = tags.get("highway", "")
            footway_tag = tags.get("footway", "")

            if highway == "steps":
                steps_count += 1
                steps_length_m += length
            elif footway_tag == "crossing":
                crossing_way_count += 1
                crossing_way_length_m += length
            elif footway_tag == "sidewalk":
                sidewalk_way_count += 1
                sidewalk_way_length_m += length
            elif highway == "footway":
                footway_way_count += 1
                footway_length_m += length

        elif el["type"] == "node":
            total_nodes += 1
            if tags.get("highway") == "crossing":
                crossing_node_count += 1
            if tags.get("barrier") == "kerb":
                curb_node_count += 1

    all_footway_length_m = (
        footway_length_m + crossing_way_length_m
        + sidewalk_way_length_m + steps_length_m
    )

    return {
        "total_elements": len(elements),
        "total_ways": total_ways,
        "total_nodes": total_nodes,
        "changeset_count": len(changesets),
        "contributor_count": len(users),
        "footway_way_count": footway_way_count,
        "footway_length_m": round(footway_length_m, 1),
        "crossing_way_count": crossing_way_count,
        "crossing_way_length_m": round(crossing_way_length_m, 1),
        "sidewalk_way_count": sidewalk_way_count,
        "sidewalk_way_length_m": round(sidewalk_way_length_m, 1),
        "steps_count": steps_count,
        "steps_length_m": round(steps_length_m, 1),
        "all_footway_length_m": round(all_footway_length_m, 1),
        "all_footway_miles": round(all_footway_length_m / METERS_PER_MILE, 1),
        "crossing_node_count": crossing_node_count,
        "curb_node_count": curb_node_count,
        "node_count": total_nodes,
        "way_count": total_ways,
    }


# =============================================================================
# Pretty printing
# =============================================================================

def print_stats(ws):
    """Print a human-readable workspace stats summary."""
    print_separator("Workspace Statistics")

    print(f"  Total elements   : {ws['total_elements']}")
    print(f"    Ways            : {ws['total_ways']}")
    print(f"    Nodes           : {ws['total_nodes']}")
    print(f"  Changesets       : {ws['changeset_count']}")
    print(f"  Contributors     : {ws['contributor_count']}")

    print_separator("Feature Breakdown")

    total_mi = ws["all_footway_miles"]
    total_m = ws["all_footway_length_m"]
    print(f"  Footway-class ways : {total_mi} mi  ({total_m:,.0f} m)")

    if ws["footway_way_count"]:
        mi = round(ws["footway_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    highway=footway  : {ws['footway_way_count']} ways, {mi} mi")
    if ws["sidewalk_way_count"]:
        mi = round(ws["sidewalk_way_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    footway=sidewalk : {ws['sidewalk_way_count']} ways, {mi} mi")
    if ws["crossing_way_count"]:
        mi = round(ws["crossing_way_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    footway=crossing : {ws['crossing_way_count']} ways, {mi} mi")
    if ws["steps_count"]:
        mi = round(ws["steps_length_m"] / METERS_PER_MILE, 1)
        print(f"    highway=steps    : {ws['steps_count']} ways, {mi} mi")

    print(f"  Crossing nodes     : {ws['crossing_node_count']}")
    print(f"  Curb nodes         : {ws['curb_node_count']}")

    print(f"  Contributors     : {ws['contributor_count']}")


# =============================================================================
# CLI
# =============================================================================

def main():
    ap = argparse.ArgumentParser(
        description="Generate AVIV ScoutRoute event statistics as JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python generate-asr-event-stats.py --event nda-vancouver\n"
            "  python generate-asr-event-stats.py --event nda-vancouver "
            "--osm-file data.osm\n"
        ),
    )
    ap.add_argument(
        "--event", required=True,
        help="Event folder name under docs/events/",
    )
    ap.add_argument(
        "--osm-file",
        help="Local .osm XML file (skip API fetch)",
    )
    ap.add_argument(
        "--api-key-env-var",
        help="Environment variable containing the TDEI API key "
             f"(default: {_DEFAULT_API_KEY_ENV_VAR})",
    )
    ap.add_argument(
        "--output", "-o",
        help="Output JSON path (default: auto)",
    )
    ap.add_argument(
        "--json", action="store_true",
        help="Also print JSON to console",
    )
    ap.add_argument(
        "--pad-before", type=float, default=2,
        help="Hours before event start (default: 2)",
    )
    ap.add_argument(
        "--pad-after", type=float, default=2,
        help="Hours after event end (default: 2)",
    )

    args = ap.parse_args()
    event_slug = args.event

    # ── Read frontmatter ─────────────────────────────────────────────────
    fm = read_event_frontmatter(event_slug)
    validate_required_fields(
        fm,
        ["asr_workspace_id", "asr_workspace_env",
         "asr_event_start", "asr_event_end"],
        context="ASR stats",
    )

    workspace_id = int(fm["asr_workspace_id"])
    workspace_env = fm["asr_workspace_env"]
    api_key_env = (
        args.api_key_env_var
        or fm.get("asr_api_key_env_var")
        or _DEFAULT_API_KEY_ENV_VAR
    )

    t_start = fm["asr_event_start"]
    t_end = fm["asr_event_end"]
    dt_start = datetime.datetime.fromisoformat(t_start.replace("Z", "+00:00"))
    dt_end = datetime.datetime.fromisoformat(t_end.replace("Z", "+00:00"))
    q_start = (dt_start - datetime.timedelta(hours=args.pad_before)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    q_end = (dt_end + datetime.timedelta(hours=args.pad_after)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")

    print(f"=== ASR Event Statistics — Workspace #{workspace_id} "
          f"({workspace_env}) ===")
    print(f"Event window : {t_start}  →  {t_end}")
    print(f"Query window : {q_start}  →  {q_end}")
    print(f"  (padded {args.pad_before}h before, {args.pad_after}h after)\n")

    # ── Get OSM XML ──────────────────────────────────────────────────────
    xml_bytes = None
    bbox_info = None

    if args.osm_file:
        print(f"Loading OSM data from {args.osm_file} …")
        with open(args.osm_file, "rb") as f:
            xml_bytes = f.read()
    else:
        # Get API key from environment
        api_key = os.environ.get(api_key_env)
        if not api_key:
            print(
                f"✗ Environment variable '{api_key_env}' is not set.\n"
                f"  Set it to your TDEI API key, or use --osm-file to "
                f"provide a local .osm file.\n"
                f"  API keys are available from the TDEI Portal:\n"
                f"    Dev:   https://portal-dev.tdei.us/\n"
                f"    Stage: https://portal-stage.tdei.us/\n"
                f"    Prod:  https://portal.tdei.us/",
                file=sys.stderr,
            )
            sys.exit(1)

        # Fetch bbox
        print("Fetching workspace bounding box …")
        try:
            bbox_info = fetch_workspace_bbox(
                workspace_env, workspace_id, api_key)
            print(f"  bbox: {bbox_info['min_lat']}, {bbox_info['min_lon']}, "
                  f"{bbox_info['max_lat']}, {bbox_info['max_lon']}")
        except Exception as exc:
            print(f"✗ Failed to fetch workspace bbox: {exc}",
                  file=sys.stderr)
            sys.exit(1)

        # Fetch map data
        print("\nFetching workspace map data …")
        try:
            xml_bytes = fetch_workspace_map_xml(
                workspace_env, workspace_id, api_key, bbox_info)
            print(f"  Received {len(xml_bytes):,} bytes of OSM XML")
        except Exception as exc:
            print(f"✗ Failed to fetch workspace data: {exc}",
                  file=sys.stderr)
            sys.exit(1)

    # ── Parse & compute stats ────────────────────────────────────────────
    print("\nParsing OSM XML …")
    elements = parse_osm_xml(xml_bytes)
    print(f"  {len(elements)} total elements parsed")

    elements = filter_by_time(elements, q_start, q_end)

    ws_stats = compute_stats(elements)
    print_stats(ws_stats)

    # ── JSON output ──────────────────────────────────────────────────────
    import json

    blob = {
        "workspace_id": workspace_id,
        "workspace_env": workspace_env,
        "workspace_stats": ws_stats,
    }
    if bbox_info:
        blob["bbox"] = bbox_info

    if args.json:
        print_separator("JSON")
        print(json.dumps(blob, indent=2))

    output_path = args.output or os.path.join(
        event_dir(event_slug), _STATS_FILE)
    write_json(output_path, blob)
    print_separator("Output")
    print(f"  Stats written to {output_path}")


if __name__ == "__main__":
    main()
