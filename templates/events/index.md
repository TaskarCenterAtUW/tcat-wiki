---
title: Event Name # Short display title shown in the page header and navigation

# ── Event type flags (required) ──────────────────────────────────────
# Set each to true or false. At least one must be true for report generation.
tasking_manager_event: true # true if the event uses the OSM US Tasking Manager
aviv_scoutroute_event: false # true if the event uses AVIV ScoutRoute / Workspaces

# ── Common event properties (used by report intro/outro) ─────────────
event_name: "Full Event Name" # Full event name as it appears in the report title
event_date: "Month Nth, YYYY" # Human-readable event date (e.g. "February 12th, 2026")
event_time_range: "H:MM AM PT – H:MM PM PT" # Display time range; use local timezone abbreviation
event_format: virtual # (virtual | in-person)
event_location: "Virtual (Platform) | Venue Name, City, ST" # Zoom URL or physical venue name + address
target_area: "City, ST" # Geographic area being mapped/surveyed (used throughout the report)
organizers: "Taskar Center for Accessible Technology (TCAT)" # Comma-separated list of organizing groups
event_purpose: "improving pedestrian infrastructure data in City, ST for accessibility-focused routing" # One-sentence purpose statement used in the report intro
participant_count: "" # Total number of participants; leave blank if unknown until after the event

# ── Tasking Manager properties (when tasking_manager_event: true) ────
tm_project: 0000 # Numeric TM project ID (e.g. 1017); used to build URLs and fetch task stats
tm_project_name: "City, ST, Country: Pedestrian Infrastructure | #OpenSidewalks" # TM project title as shown on tasks.openstreetmap.us
tm_project_url: "" # Override project URL; leave blank to auto-build from tm_project ID
tm_event_start: "YYYY-MM-DDTHH:MM:SSZ" # ISO 8601 UTC timestamp for event start (used for Overpass stats window)
tm_event_end: "YYYY-MM-DDTHH:MM:SSZ" # ISO 8601 UTC timestamp for event end (used for Overpass stats window)
tm_bbox: "" # Overpass bounding box "south,west,north,east" (decimal degrees); leave blank to fetch from TM API
tm_geographic_coverage: "" # Human-readable description of area covered (e.g. "Downtown Olympia"); leave blank if not applicable

# ── AVIV ScoutRoute properties (when aviv_scoutroute_event: true) ────
asr_workspace_id: 0 # Numeric Workspaces workspace ID (from the Workspaces platform)
asr_workspace_env: "prod" # Workspaces environment: "prod", "stage", or "dev"
asr_workspace_name: "" # Display name of the workspace (e.g. "NDA Vancouver")
asr_event_start: "YYYY-MM-DDTHH:MM:SSZ" # ISO 8601 UTC timestamp for event start (used for time filtering)
asr_event_end: "YYYY-MM-DDTHH:MM:SSZ" # ISO 8601 UTC timestamp for event end (used for time filtering)
asr_target_area: "" # Area description specific to the ScoutRoute event; defaults to target_area if blank
asr_route_description: "" # Short description of the walking route (e.g. "Gaiser Hall to Washington Street")
asr_route_distance: "" # Total route distance as a display string (e.g. "1.2 miles")
asr_route_links: "" # Markdown link(s) to AccessMap or other route visualization(s)
asr_api_key_env_var: "" # Name of the env var holding the TDEI API key; defaults to TDEI_API_KEY if blank
---

<!-- @format -->

## Event Name

Brief description of the event.

### Event Details

- **Date**: Month Nth, YYYY
- **Time**: H:MM AM PT – H:MM PM PT
- **Location**: Virtual ([Zoom](https://washington.zoom.us/j/XXXXXXXXX))
- **TCAT Calendar**: [Event Name](https://tcat.cs.washington.edu/events/event-slug/)

### Project

We'll be mapping pedestrian infrastructure in City, ST using the OSM US Tasking Manager:

**[#XXXX - City, ST, Country: Pedestrian Infrastructure | #OpenSidewalks](https://tasks.openstreetmap.us/projects/XXXX)**

### Getting Started

We'll cover this in the intro - but if you'd like a head start before the event:

1. **Create** an OpenStreetMap account at [openstreetmap.org](https://www.openstreetmap.org/user/new) if you don't already have one.
2. **Log in** to the OSM US Tasking Manager at [tasks.openstreetmap.us](https://tasks.openstreetmap.us) using your OSM account.
3. **Join** the OpenSidewalks Mappers Team by visiting [tasks.openstreetmap.us/teams/27/membership](https://tasks.openstreetmap.us/teams/27/membership) and selecting [**Join team**]{ .osmustm-green } at the bottom right.
4. **Review** the [Mapping Guide](mapping-guide.md) to familiarize yourself with the tagging schema.

### Resources

#### Mapping Guide

Visit the [Mapping Guide](mapping-guide.md) for guidance on how to map pedestrian infrastructure for the event.

#### Validation Guide

Visit the [Validation Guide](validation-guide.md) for directions on how to validate mapped pedestrian infrastructure tasks in the OSM US Tasking Manager for the event.

### Questions?

TCAT staff will be available throughout the event to answer questions.

Alternatively, you may email [uwtcat@uw.edu](mailto:uwtcat@uw.edu).
