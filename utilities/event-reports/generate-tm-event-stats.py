#!/usr/bin/env python3
"""Generate Tasking Manager mapping-event statistics as JSON.

Reads ``tm_``-prefixed frontmatter from an event's ``index.md``,
fetches mapping statistics from the Tasking Manager and Overpass APIs,
and writes ``tasking-manager-event-stats.json``.

Can be run standalone or called by ``generate-event-report.py``.

Usage:
    python generate-tm-event-stats.py --event mny26
    python generate-tm-event-stats.py --event mny26 --skip-overpass
    python generate-tm-event-stats.py --event mny26 --bbox 47.17,-122.56,47.32,-122.35
"""

import argparse
import datetime
import json
import os
import sys
import urllib.error
import urllib.parse

# Ensure the common module is importable when invoked directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (
    METERS_PER_MILE,
    event_dir,
    fetch_json,
    haversine,
    print_separator,
    prompt_for_file,
    read_event_frontmatter,
    validate_required_fields,
    way_length_m,
    write_json,
)


# =============================================================================
# Constants
# =============================================================================

TM_BASE = "https://tasks.openstreetmap.us/backend"
TM_FRONTEND = "https://tasks.openstreetmap.us"

OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]

_STATS_FILE = "tasking-manager-event-stats.json"


# =============================================================================
# Tasking Manager helpers
# =============================================================================

def _bbox_from_geojson(geojson):
    """Extract bounding box from a GeoJSON geometry or FeatureCollection."""
    lats, lons = [], []

    def _collect_coords(obj):
        if obj.get("type") == "FeatureCollection":
            for feat in obj.get("features", []):
                _collect_coords(feat.get("geometry", {}))
        elif obj.get("type") == "Feature":
            _collect_coords(obj.get("geometry", {}))
        elif obj.get("type") == "MultiPolygon":
            for polygon in obj["coordinates"]:
                for ring in polygon:
                    for lon, lat in ring:
                        lats.append(lat)
                        lons.append(lon)
        elif obj.get("type") == "Polygon":
            for ring in obj["coordinates"]:
                for lon, lat in ring:
                    lats.append(lat)
                    lons.append(lon)

    _collect_coords(geojson)
    if not lats:
        raise RuntimeError("Could not extract coordinates from GeoJSON")
    return {
        "south": min(lats), "west": min(lons),
        "north": max(lats), "east": max(lons),
    }


def load_aoi_bbox_from_file(path):
    """Load AOI bounding box from a local GeoJSON file."""
    with open(path, encoding="utf-8") as f:
        geojson = json.load(f)
    return _bbox_from_geojson(geojson)


def fetch_aoi_bbox(project_id):
    """Return ``{south, west, north, east}`` for the project AOI."""
    url = f"{TM_BASE}/api/v2/projects/{project_id}/queries/aoi/?as_file=true"
    geojson = fetch_json(url)
    return _bbox_from_geojson(geojson)


def _task_stats_from_geojson(geojson):
    """Compute task-status counts from a tasks GeoJSON FeatureCollection."""
    counts = {}
    for feat in geojson.get("features", []):
        status = feat["properties"].get("taskStatus", "UNKNOWN")
        counts[status] = counts.get(status, 0) + 1

    total = sum(counts.values())
    mapped = counts.get("MAPPED", 0)
    validated = counts.get("VALIDATED", 0)
    done = mapped + validated

    return {
        "total": total,
        "status_counts": counts,
        "mapped": mapped,
        "validated": validated,
        "done": done,
        "percent_done": round(done / total * 100, 1) if total else 0.0,
    }


def load_task_stats_from_file(path):
    """Load task stats from a local tasks GeoJSON file."""
    with open(path, encoding="utf-8") as f:
        geojson = json.load(f)
    return _task_stats_from_geojson(geojson)


def fetch_task_stats(project_id):
    """Fetch task stats from the TM API."""
    url = f"{TM_BASE}/api/v2/projects/{project_id}/tasks/?as_file=true"
    geojson = fetch_json(url)
    return _task_stats_from_geojson(geojson)


# =============================================================================
# Overpass API
# =============================================================================

def query_overpass(ql, urls=None):
    """POST an Overpass QL query, trying each URL until one works."""
    urls = list(urls or OVERPASS_URLS)
    body = urllib.parse.urlencode({"data": ql}).encode("utf-8")
    last_err = None

    for i, url in enumerate(urls, 1):
        label = f"[{i}/{len(urls)}] {url.split('//', 1)[-1].split('/')[0]}"
        print(f"  Trying {label} …", end=" ", flush=True)
        try:
            result = fetch_json(url, data=body)
            print("OK")
            return result
        except Exception as exc:
            short = type(exc).__name__
            if isinstance(exc, urllib.error.HTTPError):
                short = f"HTTP {exc.code}"
            print(f"failed ({short})")
            last_err = exc

    # All built-in URLs failed — interactive fallback
    print(f"\n  ⚠ All {len(urls)} Overpass servers failed.")
    print(f"    Last error: {last_err}")
    print("  Enter an alternate Overpass API URL, or press Enter to skip.")
    try:
        response = input("  Overpass URL> ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    if not response:
        return None
    print(f"  Trying {response} …", end=" ", flush=True)
    try:
        result = fetch_json(response, data=body)
        print("OK")
        return result
    except Exception as exc:
        print(f"failed ({exc})")
        return None


def build_stats_query(bbox, t_start, t_end):
    """Build the Overpass QL query for event statistics."""
    s, w, n, e = bbox["south"], bbox["west"], bbox["north"], bbox["east"]
    return (
        f'[out:json][timeout:300];\n'
        f'(\n'
        f'  way["highway"="footway"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  way["highway"="steps"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  node["highway"="crossing"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  node["barrier"="kerb"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f');\n'
        f'out meta geom;\n'
    )


# =============================================================================
# Changeset filtering
# =============================================================================

_OSM_API_BASE = "https://api.openstreetmap.org/api/0.6"
_HASHTAG = "#OpenSidewalks"


def _fetch_changesets(cs_ids):
    """Fetch changeset metadata for a list of changeset IDs.

    Returns a list of changeset dicts from the OSM API.
    The OSM API accepts up to ~100 IDs per request.
    """
    all_changesets = []
    batch_size = 100
    for i in range(0, len(cs_ids), batch_size):
        batch = cs_ids[i:i + batch_size]
        ids_param = ",".join(str(c) for c in batch)
        url = f"{_OSM_API_BASE}/changesets.json?changesets={ids_param}"
        data = fetch_json(url)
        all_changesets.extend(data.get("changesets", []))
    return all_changesets


def _changesets_with_hashtag(cs_ids, hashtag):
    """Return the subset of changeset IDs that mention *hashtag*.

    Checks both the changeset ``comment`` tag and the ``hashtags`` tag.
    Matching is case-insensitive.
    """
    if not cs_ids:
        return set()
    needle = hashtag.lower()
    changesets = _fetch_changesets(sorted(cs_ids))
    matched = set()
    for cs in changesets:
        cs_id = cs.get("id", 0)
        tags = cs.get("tags", {})
        comment = (tags.get("comment") or "").lower()
        hashtags = (tags.get("hashtags") or "").lower()
        if needle in comment or needle in hashtags:
            matched.add(cs_id)
    return matched


def filter_by_hashtag(overpass_result, hashtag=_HASHTAG):
    """Filter Overpass elements to those from changesets mentioning *hashtag*.

    Returns a new result dict with only matching elements.
    """
    elements = overpass_result.get("elements", [])
    cs_ids = {el["changeset"] for el in elements if el.get("changeset")}
    print(f"  Checking {len(cs_ids)} changesets for '{hashtag}' …")
    matched_cs = _changesets_with_hashtag(cs_ids, hashtag)
    filtered = [el for el in elements if el.get("changeset") in matched_cs]
    dropped = len(elements) - len(filtered)
    print(f"  {len(matched_cs)}/{len(cs_ids)} changesets matched")
    if dropped:
        print(
            f"  Filtered out {dropped} elements from non-matching changesets")
    return {**overpass_result, "elements": filtered}


# =============================================================================
# Stats computation
# =============================================================================

def compute_stats(overpass_result):
    """Derive all stats from the raw Overpass JSON."""
    elements = overpass_result.get("elements", [])

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
            else:
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
        "mapper_count": len(users),
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
        "changesets": sorted(changesets),
    }


# =============================================================================
# Visualization queries
# =============================================================================

def overpass_viz_query(bbox, t_start, t_end):
    """Overpass QL for visualizing elements changed during the event."""
    s, w, n, e = bbox["south"], bbox["west"], bbox["north"], bbox["east"]
    return (
        f"// Pedestrian infrastructure changed during the event\n"
        f"// Time window: {t_start} - {t_end}\n"
        f"[out:json][timeout:120];\n"
        f"(\n"
        f'  way["highway"="footway"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  way["highway"="steps"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  node["highway"="crossing"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f'  node["barrier"="kerb"]({s},{w},{n},{e})'
        f'(changed:"{t_start}","{t_end}");\n'
        f");\n"
        f"out body geom;\n"
    )


def postpass_viz_query(bbox):
    """Postpass SQL for current-state pedestrian infrastructure."""
    s, w, n, e = bbox["south"], bbox["west"], bbox["north"], bbox["east"]
    return (
        f"-- Current pedestrian infrastructure in the project area\n"
        f"-- Footways\n"
        f"SELECT osm_id, tags, geom\n"
        f"FROM postpass_line\n"
        f"WHERE tags->>'highway' = 'footway'\n"
        f"  AND geom && ST_MakeEnvelope({w}, {s}, {e}, {n}, 4326);\n"
        f"\n"
        f"-- Crossings\n"
        f"SELECT osm_id, tags, geom\n"
        f"FROM postpass_point\n"
        f"WHERE tags->>'highway' = 'crossing'\n"
        f"  AND geom && ST_MakeEnvelope({w}, {s}, {e}, {n}, 4326);\n"
        f"\n"
        f"-- Curbs\n"
        f"SELECT osm_id, tags, geom\n"
        f"FROM postpass_point\n"
        f"WHERE tags->>'barrier' = 'kerb'\n"
        f"  AND geom && ST_MakeEnvelope({w}, {s}, {e}, {n}, 4326);\n"
    )


# =============================================================================
# Pretty printing
# =============================================================================

def print_stats(osm, task):
    """Print a human-readable stats summary."""
    print_separator("Mapping Statistics")

    print(f"  Elements edited : {osm['total_elements']}")
    print(f"    Ways           : {osm['total_ways']}")
    print(f"    Nodes          : {osm['total_nodes']}")
    print(f"  Changesets      : {osm['changeset_count']}")
    print(f"  Mappers         : {osm['mapper_count']}")

    print_separator("Feature Breakdown")

    total_mi = osm["all_footway_miles"]
    total_m = osm["all_footway_length_m"]
    print(f"  Footway-class ways : {total_mi} mi  ({total_m:,.0f} m)")

    if osm["footway_way_count"]:
        mi = round(osm["footway_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    highway=footway  : {osm['footway_way_count']} ways, {mi} mi")
    if osm["sidewalk_way_count"]:
        mi = round(osm["sidewalk_way_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    footway=sidewalk : {osm['sidewalk_way_count']} ways, {mi} mi")
    if osm["crossing_way_count"]:
        mi = round(osm["crossing_way_length_m"] / METERS_PER_MILE, 1)
        print(
            f"    footway=crossing : {osm['crossing_way_count']} ways, {mi} mi")
    if osm["steps_count"]:
        mi = round(osm["steps_length_m"] / METERS_PER_MILE, 1)
        print(f"    highway=steps    : {osm['steps_count']} ways, {mi} mi")

    print(f"  Crossing nodes     : {osm['crossing_node_count']}")
    print(f"  Curb nodes         : {osm['curb_node_count']}")

    if task:
        print_separator("Task Progress")
        print(f"  Total tasks     : {task['total']}")
        for status, cnt in sorted(task["status_counts"].items()):
            print(f"    {status:12s} : {cnt}")
        print(f"  Mapped+Validated: {task['done']} ({task['percent_done']}%)")


# =============================================================================
# CLI
# =============================================================================

def main():
    ap = argparse.ArgumentParser(
        description="Generate Tasking Manager event statistics as JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python generate-tm-event-stats.py --event mny26\n"
            "  python generate-tm-event-stats.py --event mny26 --skip-overpass\n"
        ),
    )
    ap.add_argument(
        "--event", required=True,
        help="Event folder name under docs/events/",
    )
    ap.add_argument("--aoi-file",
                    help="Local GeoJSON file for the project AOI")
    ap.add_argument("--tasks-file",
                    help="Local GeoJSON tasks file")
    ap.add_argument("--bbox",
                    help="Explicit bbox as south,west,north,east")
    ap.add_argument("--output", "-o",
                    help="Output JSON path (default: auto)")
    ap.add_argument("--json", action="store_true",
                    help="Also print JSON to console")
    ap.add_argument("--ultra", action="store_true",
                    help="Print visualization queries")
    ap.add_argument("--skip-overpass", action="store_true",
                    help="Skip Overpass query (TM stats only)")
    ap.add_argument("--overpass-url",
                    help="Use only this Overpass API URL")
    ap.add_argument("--pad-before", type=float, default=24,
                    help="Hours before event start (default: 24)")
    ap.add_argument("--pad-after", type=float, default=24,
                    help="Hours after event end (default: 24)")

    args = ap.parse_args()
    event_slug = args.event

    # ── Read frontmatter ─────────────────────────────────────────────────
    fm = read_event_frontmatter(event_slug)
    validate_required_fields(
        fm,
        ["tm_project", "tm_event_start", "tm_event_end"],
        context="TM stats",
    )

    project_id = int(fm["tm_project"])
    t_start = fm["tm_event_start"]
    t_end = fm["tm_event_end"]

    # Compute padded query window
    dt_start = datetime.datetime.fromisoformat(t_start.replace("Z", "+00:00"))
    dt_end = datetime.datetime.fromisoformat(t_end.replace("Z", "+00:00"))
    q_start = (dt_start - datetime.timedelta(hours=args.pad_before)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    q_end = (dt_end + datetime.timedelta(hours=args.pad_after)).strftime(
        "%Y-%m-%dT%H:%M:%SZ")

    print(f"=== TM Event Statistics — Project #{project_id} ===")
    print(f"Event window : {t_start}  →  {t_end}")
    print(f"Query window : {q_start}  →  {q_end}")
    print(f"  (padded {args.pad_before}h before, {args.pad_after}h after)\n")

    # ── 1. AOI bbox ──────────────────────────────────────────────────────
    bbox = None
    if args.bbox:
        parts = [float(x) for x in args.bbox.split(",")]
        if len(parts) != 4:
            ap.error("--bbox requires exactly 4 values: south,west,north,east")
        bbox = {"south": parts[0], "west": parts[1],
                "north": parts[2], "east": parts[3]}
    elif fm.get("tm_bbox"):
        parts = [float(x) for x in fm["tm_bbox"].split(",")]
        bbox = {"south": parts[0], "west": parts[1],
                "north": parts[2], "east": parts[3]}
    elif args.aoi_file:
        print(f"Loading AOI from {args.aoi_file} …")
        bbox = load_aoi_bbox_from_file(args.aoi_file)
    else:
        print("Fetching AOI from Tasking Manager …")
        try:
            bbox = fetch_aoi_bbox(project_id)
        except RuntimeError:
            print("  ⚠ Could not fetch AOI from Tasking Manager API.")
            path = prompt_for_file(
                "AOI", f"{TM_FRONTEND}/projects/{project_id}")
            if path:
                bbox = load_aoi_bbox_from_file(path)
            else:
                print("  ✗ AOI is required. Use --bbox or --aoi-file.")
                sys.exit(1)

    print(f"  bbox: {bbox['south']:.6f}, {bbox['west']:.6f}, "
          f"{bbox['north']:.6f}, {bbox['east']:.6f}")

    # ── 2. Task stats ────────────────────────────────────────────────────
    task_stats = None
    if args.tasks_file:
        print(f"\nLoading tasks from {args.tasks_file} …")
        task_stats = load_task_stats_from_file(args.tasks_file)
    else:
        print("\nFetching task grid …")
        try:
            task_stats = fetch_task_stats(project_id)
        except RuntimeError:
            print("  ⚠ Could not fetch tasks from Tasking Manager API.")
            path = prompt_for_file(
                "Tasks Grid", f"{TM_FRONTEND}/projects/{project_id}")
            if path:
                task_stats = load_task_stats_from_file(path)
            else:
                print("  Skipping task stats.")
    if task_stats:
        print(f"  {task_stats['total']} tasks  "
              f"({task_stats['done']} done, {task_stats['percent_done']}%)")

    # ── 3. Overpass query ────────────────────────────────────────────────
    osm_stats = None
    if not args.skip_overpass:
        print("\nQuerying Overpass API (this may take a minute) …")
        ql = build_stats_query(bbox, q_start, q_end)
        overpass_urls = [args.overpass_url] if args.overpass_url else None
        result = query_overpass(ql, urls=overpass_urls)
        if result is not None:
            result = filter_by_hashtag(result)
            osm_stats = compute_stats(result)
            print_stats(osm_stats, task_stats)
        else:
            print("  Skipping Overpass statistics.")
    else:
        if task_stats:
            print_separator("Task Progress (Overpass skipped)")
            print(f"  Total tasks     : {task_stats['total']}")
            for status, cnt in sorted(task_stats["status_counts"].items()):
                print(f"    {status:12s} : {cnt}")
            print(f"  Mapped+Validated: {task_stats['done']} "
                  f"({task_stats['percent_done']}%)")
        else:
            print_separator("Overpass & Task Stats skipped")

    # ── 4. JSON output ───────────────────────────────────────────────────
    blob = {
        "project_id": project_id,
        "time_window": {"start": t_start, "end": t_end},
        "query_window": {"start": q_start, "end": q_end},
        "bbox": bbox,
        "task_stats": task_stats,
    }
    if osm_stats:
        blob["osm_stats"] = {
            k: v for k, v in osm_stats.items() if k != "changesets"
        }

    if args.json:
        print_separator("JSON")
        print(json.dumps(blob, indent=2))

    output_path = args.output or os.path.join(
        event_dir(event_slug), _STATS_FILE)
    write_json(output_path, blob)
    print_separator("Output")
    print(f"  Stats written to {output_path}")

    # ── 5. Visualization queries ─────────────────────────────────────────
    if args.ultra:
        print_separator(
            "Overpass Visualization Query  (paste into overpass-turbo.eu)")
        print(overpass_viz_query(bbox, q_start, q_end))
        print_separator(
            "Postpass Visualization Query  (paste into Ultra / Postpass)")
        print(postpass_viz_query(bbox))


if __name__ == "__main__":
    main()
