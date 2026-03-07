---
title: Clark County Walk/Roll Event

# ── Event type flags (required) ──────────────────────────────────────
# Set each to true or false. At least one must be true for report generation.
tasking_manager_event: false # true if the event uses the OSM US Tasking Manager
aviv_scoutroute_event: true # true if the event uses AVIV ScoutRoute / Workspaces

# ── Common event properties (used by report intro/outro) ─────────────
event_name: "Clark County Walk/Roll Event" # Full event name as it appears in the report title
event_date: "January 20th, 2026" # Human-readable event date (e.g. "February 12th, 2026")
# event_time_range: "H:MM AM PT – H:MM PM PT" # Display time range; use local timezone abbreviation
event_format: in-person # (virtual | in-person)
event_location: "Gaiser Hall, Vancouver, WA" # Zoom or physical venue name + address
target_area: "Vancouver, WA" # Geographic area being mapped/surveyed (used throughout the report)
organizers: "the Nondrivers Alliance (NDA) and the Taskar Center for Accessible Technology (TCAT)" # Comma-separated list of organizing groups
event_purpose: "improving pedestrian infrastructure data in Vancouver, WA for accessibility-focused routing" # One-sentence purpose statement used in the report intro
# participant_count: "" # Total number of participants; leave blank if unknown until after the event

# ── AVIV ScoutRoute properties (when aviv_scoutroute_event: true) ────
asr_workspace_id: 931 # Numeric Workspaces workspace ID (from the Workspaces platform)
asr_workspace_env: "prod" # Workspaces environment: "prod", "stage", or "dev"
asr_workspace_name: "NDA Vancouver Walk/Roll" # Display name of the workspace (e.g. "NDA Vancouver")
asr_event_start: "2026-01-20T00:00:00Z" # ISO 8601 UTC timestamp for event start (used for time filtering)
asr_event_end: "2026-01-21T00:00:00Z" # ISO 8601 UTC timestamp for event end (used for time filtering)
asr_target_area: "Vancouver, WA" # Area description specific to the ScoutRoute event; defaults to target_area if blank
asr_route_description: "Gaiser Hall to Washington Street" # Short description of the walking route (e.g. "Gaiser Hall to Washington Street")
asr_route_distance: "1.6 miles" # Total route distance as a display string (e.g. "1.2 miles")
asr_route_links: "[**Route 1: Gaiser Hall to Washington Elementary**](https://www.accessmap.app/dir?wp=-122.650576_45.6362821%27-122.65249_45.643354&region=97cb53e5-831e-4fed-8688-86d0eecd1c0b&lon=-122.6569414&lat=45.6383421&z=14.38&sa=1&mu=0.095&md=0.12&ab=0&aps=0) and [**Route 2: Washington Elementary to Washington Street**](https://www.accessmap.app/dir?wp=-122.6548741_45.6425172%27-122.671873_45.642222&region=97cb53e5-831e-4fed-8688-86d0eecd1c0b&lon=-122.6688821&lat=45.6410701&z=14.58&sa=1&mu=0.095&md=0.12&ab=0&aps=0)" # Markdown link(s) to AccessMap or other route visualization(s)
asr_api_key_env_var: "TDEI_API_KEY" # Name of the env var holding the TDEI API key; defaults to TDEI_API_KEY if blank
---

<!-- @format -->

## Clark County Walk/Roll Event

The **Clark County Walk/Roll Event** is an in-person pedestrian accessibility audit led by the [Nondrivers Alliance](https://nondrivers.org/) (NDA) in coordination with the Taskar Center for Accessible Technology (TCAT).

### Event Details

- **Date**: January 20th, 2026
- **Starting Location**: Gaiser Hall, Vancouver, WA
- **Contact**: [uwtcat@uw.edu](mailto:uwtcat@uw.edu)

### Purpose

During this walkabout, participants will review and verify sidewalk and pedestrian infrastructure data collected as part of [OS-CONNECT](https://sidewalks.washington.edu) - Washington State's standardized sidewalk data initiative based on the [OpenSidewalks](../../opensidewalks/index.md) data standard. Participants can:

- Use **[AccessMap](../../accessmap/index.md)** to view the route and receive step-by-step navigation
- Leave **comments** in AccessMap about barriers or issues encountered
- Review and contribute pedestrian accessibility data through **[AVIV ScoutRoute](../../aviv-scoutroute/index.md)**

### Pre-Event Checklist

To ensure the event goes smoothly, we recommend completing the following:

- [ ] **Register** for a TDEI Portal account - Follow the [registration instructions](aviv-scoutroute.md#step-1-register)
- [ ] **Install** AVIV ScoutRoute - Follow the [installation instructions](aviv-scoutroute.md#installation)
- [ ] **Log in** to AVIV ScoutRoute with your TDEI account
- [ ] **Confirm** the "NDA Vancouver" workspace is visible

### Event Routes

The walking route from Gaiser Hall to Washington Street is split into two AccessMap segments:

- [**Route 1: Gaiser Hall to Washington Elementary**](https://www.accessmap.app/dir?wp=-122.650576_45.6362821%27-122.65249_45.643354&region=97cb53e5-831e-4fed-8688-86d0eecd1c0b&lon=-122.6569414&lat=45.6383421&z=14.38&sa=1&mu=0.095&md=0.12&ab=0&aps=0)
- [**Route 2: Washington Elementary to Washington Street**](https://www.accessmap.app/dir?wp=-122.6548741_45.6425172%27-122.671873_45.642222&region=97cb53e5-831e-4fed-8688-86d0eecd1c0b&lon=-122.6688821&lat=45.6410701&z=14.58&sa=1&mu=0.095&md=0.12&ab=0&aps=0)

### Resources

#### AccessMap

Visit the [AccessMap Guide](accessmap.md) for information about accessing and using AccessMap at this event.

#### AVIV ScoutRoute

Visit the [AVIV ScoutRoute Guide](aviv-scoutroute.md) for information about installing and using the AVIV ScoutRoute mobile application at this event.

### Explore the Data

Review the current sidewalk and pedestrian data for the route area using the OSConnect Data Viewer:

[**OSConnect Data Viewer - Vancouver, WA**](https://osconnect-viewer.tdei.us/#map=15/45.64/-122.65)

### Learn More

To learn more about the projects and initiatives behind this event:

- [OpenSidewalks](../../opensidewalks/index.md) - The open data standard for pedestrian infrastructure
- [TDEI](../../tdei/index.md) - The Transportation Data Exchange Initiative
- [AccessMap](../../accessmap/index.md) - Accessibility-focused pedestrian trip planning
- [AVIV ScoutRoute](../../aviv-scoutroute/index.md) - Crowdsourced accessibility data collection
