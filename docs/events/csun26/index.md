---
title: CSUN 2026 Walkabout

# ── Event type flags (required) ──────────────────────────────────────
# Set each to true or false. At least one must be true for report generation.
tasking_manager_event: false # true if the event uses the OSM US Tasking Manager
aviv_scoutroute_event: true # true if the event uses AVIV ScoutRoute / Workspaces

# ── Common event properties (used by report intro/outro) ─────────────
event_name: "CSUN 2026 Walkabout" # Full event name as it appears in the report title
event_date: "March 9th-13th, 2026" # Human-readable event date (e.g. "February 12th, 2026")
# event_time_range: "H:MM AM PT – H:MM PM PT" # Display time range; use local timezone abbreviation
event_format: in-person # (virtual | in-person)
event_location: "Anaheim, CA" # Physical venue name + address
target_area: "Anaheim, CA" # Geographic area being mapped/surveyed (used throughout the report)
organizers: "Taskar Center for Accessible Technology (TCAT)" # Comma-separated list of organizing groups
event_purpose: "demonstrating the on-the-ground data collection process and gathering feedback on AccessMap and the AVIV ScoutRoute app" # One-sentence purpose statement used in the report intro
participant_count: "10" # Total number of participants; leave blank if unknown until after the event

# ── AVIV ScoutRoute properties (when aviv_scoutroute_event: true) ────
asr_workspace_id: 1286 # Numeric Workspaces workspace ID (from the Workspaces platform)
asr_workspace_env: "prod" # Workspaces environment: "prod", "stage", or "dev"
asr_workspace_name: "CSUN 2026" # Display name of the workspace (e.g. "NDA Vancouver")
asr_event_start: "2026-03-09T00:00:00Z" # ISO 8601 UTC timestamp for event start (used for time filtering)
asr_event_end: "2026-03-14T00:00:00Z" # ISO 8601 UTC timestamp for event end (used for time filtering)
asr_target_area: "Anaheim Convention Center" # Area description specific to the ScoutRoute event; defaults to target_area if blank
asr_route_description: "Anaheim Marriott to Anaheim GardenWalk" # Short description of the walking route (e.g. "Gaiser Hall to Washington Street")
asr_route_distance: "0.75 miles" # Total route distance as a display string (e.g. "1.2 miles")
asr_route_links: "[AccessMap](https://www.accessmap.app/dir?wp=-117.918313_33.799592%27-117.911555_33.8051782&region=ca.anaheim&lon=-117.9160288&lat=33.8023852&z=16.85&sa=1&mu=0.14&md=0.14&ab=0&aps=0)" # Markdown link(s) to AccessMap or other route visualization(s)
# asr_api_key_env_var: "" # Name of the env var holding the TDEI API key; defaults to TDEI_API_KEY if blank
---

<!-- @format -->

## CSUN 2026 Walkabout

Staff from the Taskar Center for Accessible Technology (TCAT) are attending the [CSUN 2026 Assistive Technology Conference](https://conference.csun.at/event/2026/summary) and will be presenting two talks, engaging the community from a table in the Exhibit Hall, and conducting brief walkabouts throughout the week to demonstrate AccessMap and AVIV ScoutRoute.

### Event Details

- **Date(s)**: March 9th–13th, 2026
- **Location**: Anaheim, CA

### Purpose

During these walkabouts, participants will review and verify sidewalk and pedestrian infrastructure data. Participants can:

- Use **[AccessMap](../../accessmap/index.md)** to view the route and receive step-by-step navigation
- Leave **feedback** in AccessMap about barriers or issues encountered
- Review and contribute pedestrian accessibility data through **[AVIV ScoutRoute](../../aviv-scoutroute/index.md)**

### Pre-Event Checklist

To ensure the event goes smoothly, we recommend completing the following:

- [ ] **Register** for a TDEI Portal account - Follow the [registration instructions](../../aviv-scoutroute/user-manual/installation.md)
- [ ] **Install** AVIV ScoutRoute - Follow the [installation instructions](../../aviv-scoutroute/user-manual/installation.md)
- [ ] **Log in** to AVIV ScoutRoute with your TDEI account
- [ ] **Confirm** the "CSUN 2026" workspace is visible

### Event Route

The walkabout route runs from the Anaheim Marriott to Anaheim GardenWalk (~0.75 miles):

- [**AccessMap: Anaheim Marriott to Anaheim GardenWalk**](https://www.accessmap.app/dir?wp=-117.918313_33.799592%27-117.911555_33.8051782&region=ca.anaheim&lon=-117.9160288&lat=33.8023852&z=16.85&sa=1&mu=0.14&md=0.14&ab=0&aps=0)

### Learn More

To learn more about the projects and initiatives behind this event:

- [OpenSidewalks](../../opensidewalks/index.md) - The open data standard for pedestrian infrastructure
- [TDEI](../../tdei/index.md) - The Transportation Data Exchange Initiative
- [AccessMap](../../accessmap/index.md) - Accessibility-focused pedestrian trip planning and navigation
- [AVIV ScoutRoute](../../aviv-scoutroute/index.md) - Crowdsourced accessibility data collection

### Event Summary Report

Check out the [Event Summary Report](report.md) for more information!
