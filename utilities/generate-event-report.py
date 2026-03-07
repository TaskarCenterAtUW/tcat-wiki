#!/usr/bin/env python3
"""Generate an event summary report for the TCAT Wiki.

Reads event metadata from an event's ``index.md`` frontmatter, runs
the appropriate stats generators, fills section templates, and
concatenates the intro + activity sections + outro into a final
``report.md``.

Supports two activity types (either or both per event):
  - **Tasking Manager** (``tasking_manager_event: true``)
  - **AVIV ScoutRoute** (``aviv_scoutroute_event: true``)

Usage:
    python generate-event-report.py --event olympia-connected
    python generate-event-report.py --event mny26 --skip-stats
    python generate-event-report.py --event nda-vancouver --skip-tm-stats
"""

import argparse
import os
import subprocess
import sys

# Ensure the event-reports package is importable
sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "event-reports"))

from common import (
    clean_blank_lines,
    event_dir,
    fill_template,
    fix_article,
    read_event_frontmatter,
    read_json,
    strip_html_comments,
    templates_dir,
    validate_required_fields,
)

# =============================================================================
# Constants
# =============================================================================

_INTRO_TEMPLATE = "event-report-intro.md"
_OUTRO_TEMPLATE = "event-report-outro.md"
_TM_SECTION_TEMPLATE = "event-report-tm-section.md"
_ASR_SECTION_TEMPLATE = "event-report-asr-section.md"

_TM_STATS_FILE = "tasking-manager-event-stats.json"
_TM_PART_FILE = "tasking-manager-event-report.md.part"
_ASR_STATS_FILE = "aviv-scoutroute-event-stats.json"
_ASR_PART_FILE = "aviv-scoutroute-event-report.md.part"


# =============================================================================
# Common replacements (from unprefixed frontmatter)
# =============================================================================

def _common_replacements(fm):
    """Build ``{{PLACEHOLDER}} → value`` for the intro and outro templates."""
    return {
        "EVENT_NAME": fm.get("event_name") or fm.get("title", ""),
        "EVENT_DATE": fm.get("event_date", ""),
        "EVENT_TIME_RANGE": fm.get("event_time_range", ""),
        "EVENT_FORMAT": fm.get("event_format", ""),
        "EVENT_LOCATION": fm.get("event_location", ""),
        "TARGET_AREA": fm.get("target_area", ""),
        "ORGANIZERS": fm.get("organizers", ""),
        "PARTICIPANT_COUNT": fm.get("participant_count", ""),
        "EVENT_PURPOSE": fm.get("event_purpose", ""),
    }


# =============================================================================
# Tasking Manager section generation
# =============================================================================

def _tm_replacements(fm, stats):
    """Build replacements for the TM section template."""
    project_id = fm.get("tm_project", "")
    tm_name = fm.get("tm_project_name", "")
    tm_url = (
        fm.get("tm_project_url")
        or (f"https://tasks.openstreetmap.us/projects/{project_id}"
            if project_id else "")
    )

    replacements = {
        "TM_PROJECT_ID": str(project_id),
        "TM_PROJECT_NAME": tm_name,
        "TM_PROJECT_URL": tm_url,
        "TM_GEOGRAPHIC_COVERAGE": fm.get("tm_geographic_coverage", ""),
    }

    osm = stats.get("osm_stats")
    if osm:
        replacements.update({
            "TM_MAPPER_COUNT": str(osm["mapper_count"]),
            "TM_CHANGESET_COUNT": str(osm["changeset_count"]),
            "TM_EDIT_COUNT": f"{osm['total_elements']:,}",
            "TM_FOOTWAY_MILES": str(osm["all_footway_miles"]),
            "TM_CROSSING_COUNT": str(osm["crossing_node_count"]),
            "TM_CURB_COUNT": str(osm["curb_node_count"]),
        })

    task = stats.get("task_stats")
    if task:
        replacements.update({
            "TM_TASKS_MAPPED": str(task["mapped"]),
            "TM_TASKS_VALIDATED": str(task["validated"]),
            "TM_PERCENT_MAPPED": str(task["percent_done"]),
        })

    return replacements


def generate_tm_section(fm, event_slug):
    """Generate the TM section ``.md.part`` file.

    Reads the TM section template, fills it with stats from the
    previously generated ``tasking-manager-event-stats.json``, and
    writes the result to ``tasking-manager-event-report.md.part``.
    """
    stats_path = os.path.join(event_dir(event_slug), _TM_STATS_FILE)
    if not os.path.isfile(stats_path):
        print(f"✗ TM stats not found: {stats_path}", file=sys.stderr)
        print("  Run the TM stats generator first, or use --skip-stats.",
              file=sys.stderr)
        sys.exit(1)

    stats = read_json(stats_path)

    template_path = os.path.join(templates_dir(), _TM_SECTION_TEMPLATE)
    with open(template_path, encoding="utf-8") as f:
        template_text = f.read()

    replacements = _tm_replacements(fm, stats)
    section = fill_template(template_text, replacements)
    section = strip_html_comments(section)

    part_path = os.path.join(event_dir(event_slug), _TM_PART_FILE)
    with open(part_path, "w", encoding="utf-8") as f:
        f.write(section)

    print(f"  ✓ TM section written: {_TM_PART_FILE}")
    return part_path


# =============================================================================
# AVIV ScoutRoute section generation
# =============================================================================

def _asr_replacements(fm, stats):
    """Build replacements for the ASR section template."""
    replacements = {
        "ASR_TARGET_AREA": fm.get("asr_target_area", fm.get("target_area", "")),
        "ASR_WORKSPACE_NAME": fm.get("asr_workspace_name", ""),
        "ASR_ROUTE_DESCRIPTION": fm.get("asr_route_description", ""),
        "ASR_ROUTE_DISTANCE": fm.get("asr_route_distance", ""),
        "ASR_ROUTE_LINKS": fm.get("asr_route_links", ""),
    }

    ws = stats.get("workspace_stats")
    if ws:
        replacements.update({
            "ASR_CONTRIBUTOR_COUNT": str(ws.get("contributor_count", 0)),
            "ASR_TOTAL_ELEMENTS": str(ws.get("total_elements", 0)),
            "ASR_NODE_COUNT": str(ws.get("node_count", 0)),
            "ASR_WAY_COUNT": str(ws.get("way_count", 0)),
            "ASR_FOOTWAY_MILES": str(ws.get("all_footway_miles", 0)),
            "ASR_CROSSING_COUNT": str(ws.get("crossing_node_count", 0)),
            "ASR_CURB_COUNT": str(ws.get("curb_node_count", 0)),
        })

    return replacements


def generate_asr_section(fm, event_slug):
    """Generate the ASR section ``.md.part`` file.

    Reads the ASR section template, fills it with stats from the
    previously generated ``aviv-scoutroute-event-stats.json``, and
    writes the result to ``aviv-scoutroute-event-report.md.part``.
    """
    stats_path = os.path.join(event_dir(event_slug), _ASR_STATS_FILE)
    if not os.path.isfile(stats_path):
        print(f"✗ ASR stats not found: {stats_path}", file=sys.stderr)
        print("  Run the ASR stats generator first, or use --skip-stats.",
              file=sys.stderr)
        sys.exit(1)

    stats = read_json(stats_path)

    template_path = os.path.join(templates_dir(), _ASR_SECTION_TEMPLATE)
    with open(template_path, encoding="utf-8") as f:
        template_text = f.read()

    replacements = _asr_replacements(fm, stats)
    section = fill_template(template_text, replacements)
    section = strip_html_comments(section)

    part_path = os.path.join(event_dir(event_slug), _ASR_PART_FILE)
    with open(part_path, "w", encoding="utf-8") as f:
        f.write(section)

    print(f"  ✓ ASR section written: {_ASR_PART_FILE}")
    return part_path


# =============================================================================
# Stats generator runners
# =============================================================================

def _run_tm_stats(fm, event_slug, extra_args=None):
    """Run ``generate-tm-event-stats.py`` as a subprocess."""
    script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "event-reports",
        "generate-tm-event-stats.py",
    )
    cmd = [
        sys.executable, script,
        "--event", event_slug,
    ]
    if extra_args:
        cmd.extend(extra_args)

    print(f"\n  Running TM stats generator …")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        stats_path = os.path.join(event_dir(event_slug), _TM_STATS_FILE)
        if not os.path.isfile(stats_path):
            print("✗ TM stats generator failed.", file=sys.stderr)
            sys.exit(1)
        print("  ⚠ TM stats generator had warnings; using partial results.")


def _run_asr_stats(fm, event_slug, extra_args=None):
    """Run ``generate-asr-event-stats.py`` as a subprocess."""
    script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "event-reports",
        "generate-asr-event-stats.py",
    )
    cmd = [
        sys.executable, script,
        "--event", event_slug,
    ]
    if extra_args:
        cmd.extend(extra_args)

    print(f"\n  Running ASR stats generator …")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        stats_path = os.path.join(event_dir(event_slug), _ASR_STATS_FILE)
        if not os.path.isfile(stats_path):
            print("✗ ASR stats generator failed.", file=sys.stderr)
            sys.exit(1)
        print("  ⚠ ASR stats generator had warnings; using partial results.")


# =============================================================================
# Report assembly
# =============================================================================

def _clean_empty_optionals(text):
    """Clean up artifacts from empty optional placeholder values."""
    import re
    # Remove table rows where the value cell is empty (e.g. missing time)
    text = re.sub(
        r"^\|[^|]+\|\s*\|\s*$\n?",
        "",
        text,
        flags=re.MULTILINE,
    )
    return text


def assemble_report(fm, event_slug, has_tm, has_asr):
    """Concatenate intro + activity sections + outro into ``report.md``."""
    tpl_dir = templates_dir()
    ev_dir = event_dir(event_slug)

    # Fall back to stats-derived contributor count when participant_count is empty
    if not fm.get("participant_count"):
        if has_tm:
            tm_stats_path = os.path.join(ev_dir, _TM_STATS_FILE)
            if os.path.isfile(tm_stats_path):
                tm_data = read_json(tm_stats_path)
                osm = tm_data.get("osm_stats", {})
                count = osm.get("mapper_count")
                if count:
                    fm = dict(fm, participant_count=str(count))
        elif has_asr:
            asr_stats_path = os.path.join(ev_dir, _ASR_STATS_FILE)
            if os.path.isfile(asr_stats_path):
                asr_data = read_json(asr_stats_path)
                ws = asr_data.get("workspace_stats", {})
                count = ws.get("contributor_count")
                if count:
                    fm = dict(fm, participant_count=str(count))

    common = _common_replacements(fm)

    # ── Intro ────────────────────────────────────────────────────────────
    intro_path = os.path.join(tpl_dir, _INTRO_TEMPLATE)
    with open(intro_path, encoding="utf-8") as f:
        intro = f.read()
    intro = fill_template(intro, common)

    # ── Activity sections (from .md.part files) ──────────────────────────
    sections = []
    if has_tm:
        tm_part = os.path.join(ev_dir, _TM_PART_FILE)
        if os.path.isfile(tm_part):
            with open(tm_part, encoding="utf-8") as f:
                sections.append(f.read())
        else:
            print(f"  ⚠ TM section not found: {tm_part}", file=sys.stderr)

    if has_asr:
        asr_part = os.path.join(ev_dir, _ASR_PART_FILE)
        if os.path.isfile(asr_part):
            with open(asr_part, encoding="utf-8") as f:
                sections.append(f.read())
        else:
            print(f"  ⚠ ASR section not found: {asr_part}", file=sys.stderr)

    # ── Outro ────────────────────────────────────────────────────────────
    outro_path = os.path.join(tpl_dir, _OUTRO_TEMPLATE)
    with open(outro_path, encoding="utf-8") as f:
        outro = f.read()
    outro = fill_template(outro, common)

    # ── Concatenate & clean ──────────────────────────────────────────────
    parts = [intro] + sections + [outro]
    report = "\n\n".join(part.strip() for part in parts if part.strip())
    report = _clean_empty_optionals(report)
    report = fix_article(report)
    report = clean_blank_lines(report)

    return report


# =============================================================================
# CLI
# =============================================================================

def main():
    ap = argparse.ArgumentParser(
        description="Generate an event summary report for the TCAT Wiki.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python generate-event-report.py --event olympia-connected\n"
            "  python generate-event-report.py --event mny26 --skip-stats\n"
            "  python generate-event-report.py --event nda-vancouver "
            "--skip-tm-stats\n"
        ),
    )
    ap.add_argument(
        "--event", required=True,
        help="Event folder name under docs/events/",
    )
    ap.add_argument(
        "--skip-stats", action="store_true",
        help="Skip ALL stats generation; use existing JSON files",
    )
    ap.add_argument(
        "--skip-tm-stats", action="store_true",
        help="Skip TM stats generation; use existing TM JSON",
    )
    ap.add_argument(
        "--skip-asr-stats", action="store_true",
        help="Skip ASR stats generation; use existing ASR JSON",
    )
    ap.add_argument(
        "--output", "-o",
        help="Output file path (default: docs/events/<event>/report.md)",
    )
    # Pass-through arguments for stats generators
    ap.add_argument("--overpass-url", help="Pin a specific Overpass server")
    ap.add_argument("--skip-overpass", action="store_true",
                    help="Skip Overpass query (TM task stats only)")
    ap.add_argument("--aoi-file", help="Local GeoJSON AOI file (TM)")
    ap.add_argument("--tasks-file", help="Local GeoJSON tasks file (TM)")
    ap.add_argument("--pad-before", type=float,
                    help="Hours before event start (TM Overpass)")
    ap.add_argument("--pad-after", type=float,
                    help="Hours after event end (TM Overpass)")

    args = ap.parse_args()
    event_slug = args.event

    # ── 1. Read frontmatter ──────────────────────────────────────────────
    print(f"=== Event Report — {event_slug} ===\n")
    fm = read_event_frontmatter(event_slug)

    validate_required_fields(
        fm,
        ["tasking_manager_event", "aviv_scoutroute_event"],
        context="event type flags",
    )

    event_name = fm.get("event_name") or fm.get("title", event_slug)
    has_tm = fm.get("tasking_manager_event", "").lower() == "true"
    has_asr = fm.get("aviv_scoutroute_event", "").lower() == "true"

    print(f"  Event: {event_name}")
    print(f"  Tasking Manager: {'yes' if has_tm else 'no'}")
    print(f"  AVIV ScoutRoute: {'yes' if has_asr else 'no'}")

    if not has_tm and not has_asr:
        print("✗ Neither tasking_manager_event nor aviv_scoutroute_event "
              "is true. Nothing to generate.", file=sys.stderr)
        sys.exit(1)

    # ── 2. Generate stats ────────────────────────────────────────────────
    skip_all = args.skip_stats

    if has_tm and not skip_all and not args.skip_tm_stats:
        extra = []
        if args.overpass_url:
            extra.extend(["--overpass-url", args.overpass_url])
        if args.skip_overpass:
            extra.append("--skip-overpass")
        if args.aoi_file:
            extra.extend(["--aoi-file", args.aoi_file])
        if args.tasks_file:
            extra.extend(["--tasks-file", args.tasks_file])
        if args.pad_before is not None:
            extra.extend(["--pad-before", str(args.pad_before)])
        if args.pad_after is not None:
            extra.extend(["--pad-after", str(args.pad_after)])
        _run_tm_stats(fm, event_slug, extra)

    if has_asr and not skip_all and not args.skip_asr_stats:
        _run_asr_stats(fm, event_slug)

    # ── 3. Generate section .md.part files ───────────────────────────────
    print()
    if has_tm:
        generate_tm_section(fm, event_slug)
    if has_asr:
        generate_asr_section(fm, event_slug)

    # ── 4. Assemble final report ─────────────────────────────────────────
    report = assemble_report(fm, event_slug, has_tm, has_asr)

    output_path = args.output or os.path.join(
        event_dir(event_slug), "report.md"
    )
    out_dir = os.path.dirname(os.path.abspath(output_path))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n{'=' * 60}")
    print(f"  Report written to {output_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
