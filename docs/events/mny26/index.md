---
title: Mappy New Year 2026

# ── Event type flags (required) ──────────────────────────────────────
# Set each to true or false. At least one must be true for report generation.
tasking_manager_event: true # true if the event uses the OSM US Tasking Manager
aviv_scoutroute_event: false # true if the event uses AVIV ScoutRoute / Workspaces

# ── Common event properties (used by report intro/outro) ─────────────
event_name: "Mappy New Year 2026" # Full event name as it appears in the report title
event_date: "January 19th, 2026" # Human-readable event date (e.g. "February 12th, 2026")
event_time_range: "9:00 AM PT – 12:00+ PM PT" # Display time range; use local timezone abbreviation
event_format: virtual # (virtual | in-person)
event_location: "Zoom" # Zoom or physical venue name + address
target_area: "Tacoma, WA" # Geographic area being mapped/surveyed (used throughout the report)
organizers: "Taskar Center for Accessible Technology (TCAT)" # Comma-separated list of organizing groups
event_purpose: "improving pedestrian infrastructure data to support accessibility-focused routing" # One-sentence purpose statement used in the report intro
participant_count: "" # Total number of participants; leave blank if unknown until after the event

# ── Tasking Manager properties (when tasking_manager_event: true) ────
tm_project: 1017 # Numeric TM project ID (e.g. 1017); used to build URLs and fetch task stats
tm_project_name: "Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks" # TM project title as shown on tasks.openstreetmap.us
tm_project_url: "" # Override project URL; leave blank to auto-build from tm_project ID
tm_event_start: "2026-01-19T17:00:00Z" # ISO 8601 UTC timestamp for event start (used for Overpass stats window)
tm_event_end: "2026-01-19T21:00:00Z" # ISO 8601 UTC timestamp for event end (used for Overpass stats window)
tm_bbox: "" # Overpass bounding box "south,west,north,east" (decimal degrees); leave blank to fetch from TM API
tm_geographic_coverage: "" # Human-readable description of area covered (e.g. "Downtown Olympia"); leave blank if not applicable
---

<!-- @format -->

## Mappy New Year 2026

Mappy New Year 2026 is a virtual mapathon focused on improving pedestrian infrastructure data in **Tacoma, WA**.

### Event Details

- **Date**: January 19th, 2026
- **Time**: 9:00 AM PT - 12:00+ PM PT
- **Location**: Virtual ([Zoom](https://washington.zoom.us/j/94796548308))
- **TCAT Calendar**: [Mappy New Year 2026](https://tcat.cs.washington.edu/events/mappy-new-year-w-tcat/)

### Project

We'll be mapping pedestrian infrastructure in Tacoma, WA using the OSM US Tasking Manager:

**[#1017 - Tacoma, WA, US: Pedestrian Infrastructure | #OpenSidewalks](https://tasks.openstreetmap.us/projects/1017)**

### Getting Started

We'll cover this in the intro, but if you'd like a head start, before the event:

1. **Create** an OpenStreetMap account at [openstreetmap.org](https://www.openstreetmap.org/user/new) if you don't already have one.
2. **Log in** to the OSM US Tasking Manager at [tasks.openstreetmap.us](https://tasks.openstreetmap.us) using your OSM account.
3. **Join** the OpenSidewalks Mappers Team by visiting [tasks.openstreetmap.us/teams/27/membership](https://tasks.openstreetmap.us/teams/27/membership) and selecting **Join team** at the bottom right.
4. **Review** the [Mapping Guide](mapping-guide.md) to familiarize yourself with the tagging schema

### Resources

#### Mapping Guide

Visit the [Mapping Guide](mapping-guide.md) for guidance on how to map pedestrian infrastructure for the Mappy New Year 2026 event.

#### Validation Guide

Visit the [Validation Guide](validation-guide.md) for directions on how to validate mapped pedestrian infrastructure tasks in the OSM US Tasking Manager for the Mappy New Year 2026 event.

### Questions?

TCAT staff will be available throughout the event to answer questions.

Alternatively, you may email [uwtcat@uw.edu](mailto:uwtcat@uw.edu) or [amykateb@uw.edu](mailto:amykateb@uw.edu).
