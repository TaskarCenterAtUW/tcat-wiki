---
title: "Configure imagery layers in a workspace"
tags:
    - Assistant
slug: configure-imagery-layers
doc_type: workflow
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - imagery
    - configuration
    - aviv-scoutroute
risk_level: medium
authority_level: draft
review_status: draft
last_reviewed: 2026-05-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Imagery JSON automatically imports aerial photos into the pedestrian network
        - Custom basemaps in workspace settings control every editor (Rapid, JOSM) the same way as AVIV ScoutRoute
        - Raster basemap pixels become sidewalk or crossing features without manual mapping
        - Any tile URL works regardless of authentication, CORS, or licensing
        - Custom imagery by URL is available when only paste-in JSON is documented
related_pages:
    - assistant/workflows/workspaces/create-a-workspace-from-tdei.md
    - assistant/workflows/workspaces/edit-accessibility-features-in-a-workspace.md
    - assistant/concepts/workspaces/imagery-layers.md
    - assistant/questions/workspaces/how-do-imagery-layers-work.md
    - assistant/questions/workspaces/can-custom-imagery-be-added.md
    - assistant/questions/workspaces/what-is-imagery-json.md
    - workspaces/user-manual/workspace-settings.md
    - aviv-scoutroute/index.md
---

# Configure imagery layers in a workspace

## Short Answer

In **Workspace Settings**, paste or drag-and-drop a **Custom Imagery Definition** (JSON) into **Imagery JSON Definition**, then **Save**. That list defines which **raster basemap layers** field contributors can switch among in **AVIV ScoutRoute** for that workspace. The JSON points to tile URLs — it does not upload imagery into TDEI or OS-CONNECT. The workspace must be **published for external apps** for ScoutRoute to use the configuration.

## Significance

Field teams need current, jurisdiction-specific backgrounds (aerials, local tile services, public-domain orthophotos) to place sidewalks, crossings, and curb ramps accurately. Centralizing imagery in workspace settings keeps mobile capture aligned with the same sandbox GIS staff edit in Rapid or JOSM, without treating basemap pixels as authoritative network data.

## What This Means

**Where to configure**

1. Open the workspace **Settings** page (from the dashboard).
2. Under **Custom Imagery**, use **Imagery JSON Definition**.
3. Either paste the full JSON or **drag-and-drop** a `.json` file (success toast: "JSON file loaded successfully.").
4. Select **Save** ("Changes saved." below the button).

Procedural detail and screenshots: [Workspace Settings](../../../workspaces/user-manual/workspace-settings.md).

**What the JSON does**

- The definition is a **list of basemap options** (names + tile template URLs), following the [AVIV ScoutRoute Custom Imagery schema](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/schema/schema.json).
- Example structure: [asr-imagery-list example](https://raw.githubusercontent.com/TaskarCenterAtUW/asr-imagery-list/refs/heads/main/examples/example.json).
- demos included a minimal list using **standard OSM raster basemaps**; jurisdictions can add orthophotos or other **raster tile** sources they are licensed to use.
- **Raster tiles only** for custom imagery (image tiles, not vector style JSON). Vector vs raster distinction matters for OSM editing elsewhere, but custom workspace imagery is for **background visualization**, not selectable map objects.

**Who sees which layers**

- Layers appear in ScoutRoute’s **imagery layer control** (map interface). Available backgrounds depend on what was configured for **that workspace** (see [AVIV ScoutRoute](../../../aviv-scoutroute/index.md) user manual).
- Configure **Publish this Workspace for external apps** in the same Settings area so ScoutRoute can access the workspace.

**Paste vs URL (product gap)**

- **Quest definitions** can be pasted in full or loaded from an external URL.
- **Custom imagery** must be pasted **in full** in the Imagery JSON box; a **custom imagery URL** (is a planned UX improvement). Do not tell users they can point Settings at a GitHub HTML page instead of raw JSON — invalid JSON can break workspace configuration (similar lesson raised for quest URLs).

**Licensing and access**

- Teams may self-host definitions in their own repos or paste project-specific JSON.
- Tile endpoints must be reachable by client apps; confirm whether URLs require API keys, VPN, or referer restrictions with your provider and TCAT support.
- Prefer sources you have rights to redistribute to field volunteers.

**Relationship to other editing surfaces**

| Surface | Imagery source |
|--------|----------------|
| AVIV ScoutRoute | Workspace **Imagery JSON Definition** |
| Rapid / JOSM in Workspaces | Editor basemap controls (OSM-style); not driven by the same Settings JSON |
| Reference GeoJSON in Rapid | Separate overlay for comparison — not basemap tiles ([edit workflow](edit-accessibility-features-in-a-workspace.md)) |

Basemaps are **context for human mapping**: you move sidewalk or crossing geometry against the background; the basemap does not auto-create network features.

## What This Does Not Mean

- **Not a dataset import** — Imagery JSON does not replace TDEI ingest of sidewalks or curb ramps.
- **Not automatic feature extraction** — New pavement visible on aerials still requires manual digitizing and tagging.
- **Not guaranteed in Rapid** — Saving imagery JSON does not by itself change which layers appear inside embedded Rapid until product behavior says otherwise; confirm with current release notes.
- **Not proof of conditions** — A clear aerial does not document ADA compliance, slope, or tactile paving without field verification and attributes.
- **Not vector tile styling** — Custom imagery list is for raster tile templates, not MapLibre style JSON.

## How To Use This

**Recommended flow**

1. [Create or open a workspace](create-a-workspace-from-tdei.md) for the jurisdiction and dataset version.
2. Draft imagery JSON using the schema and an example from [asr-imagery-list](https://github.com/TaskarCenterAtUW/asr-imagery-list) (or your agency’s fork).
3. Paste or drag-and-drop into **Imagery JSON Definition** → **Save**.
4. Enable **Publish this Workspace for external apps** if ScoutRoute teams should map now.
5. Optionally configure **AVIV ScoutRoute Long Form Quest Definitions** in the same External Apps section (separate JSON).
6. Have a field tester open ScoutRoute, switch basemaps, and confirm tiles load over the workspace extent.
7. Proceed to [editing](edit-accessibility-features-in-a-workspace.md) in Rapid/JOSM for geometry QA using appropriate editor basemaps plus reference layers.

**Practical tips**

- Start with one reliable layer (for example ESRI/USGS or OSM standard tiles) before adding many experimental endpoints.
- Label layers clearly in JSON so volunteers pick the intended year or source.
- If tiles fail to load, check HTTPS, CORS, API keys, and that the URL is a **tile template** (`{z}/{x}/{y}`), not a static image of the whole city.
- Re-save Settings after edits; ScoutRoute picks up the saved definition for that workspace.

## Example

A city loads a workspace from the latest OS-CONNECT TDEI release. The project lead pastes imagery JSON with two raster layers: a public-domain orthophoto tile service and OpenStreetMap standard tiles. After **Save** and **Publish**, volunteers in ScoutRoute switch to the orthophoto to map a new crossing, while a GIS analyst in Rapid uses the editor’s basemap plus a city sidewalk GeoJSON reference to reconcile linework before export.

## Assistant Guidance

- Direct users to [Workspace Settings](../../../workspaces/user-manual/workspace-settings.md) for UI labels and save steps.
- Emphasize **ScoutRoute** as the primary consumer of Imagery JSON unless product docs state otherwise for Rapid.
- If asked for "imagery URL only," note the workshop gap (paste full JSON today; URL support may ship later — confirm with TCAT).
- Warn against pasting GitHub **web** links instead of raw JSON content for any Settings JSON field.
- For "can I use our ArcGIS tile server," abstain on auth/CORS specifics; suggest a small test workspace and staff verification.
- Pair with [imagery layers concept](../../workspaces/imagery-layers.md) *(stub)* when authored.

## Related Concepts

- [Create a workspace from TDEI](create-a-workspace-from-tdei.md)
- [Edit accessibility features in a workspace](edit-accessibility-features-in-a-workspace.md)
- [Imagery layers (Workspaces)](../../workspaces/imagery-layers.md) *(stub — author in Phase B)*
- [Workspace Settings (guide)](../../../workspaces/user-manual/workspace-settings.md)
- [AVIV ScoutRoute](../../../aviv-scoutroute/index.md)
