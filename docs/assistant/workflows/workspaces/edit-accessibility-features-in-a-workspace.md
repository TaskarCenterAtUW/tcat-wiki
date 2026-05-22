---
title: "Edit accessibility features in a workspace"
slug: edit-accessibility-features-in-a-workspace
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
  - editing
  - accessibility-data
  - osm-interoperability
  - multi-source-stewardship
risk_level: medium
authority_level: draft
review_status: draft
last_reviewed: "2026-05-22"
retrieval_priority: medium
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - Every edit in Workspaces is automatically correct or field-validated
    - Reference GeoJSON layers automatically become part of the official network without review
    - Bulk import of a full external dataset into a workspace replaces TDEI-level ingest
    - Edits in Workspaces immediately update OS-CONNECT, TDEI releases, or public OpenStreetMap
    - Using Rapid 3 is always more stable than Rapid 2 in every environment
related_pages:
  - assistant/workflows/workspaces/create-a-workspace-from-tdei.md
  - assistant/workflows/workspaces/review-workspace-edits.md
  - assistant/concepts/workspaces/private-osm.md
  - assistant/concepts/workspaces/multi-source-stewardship.md
  - assistant/concepts/workspaces/workspace-editors.md
  - assistant/concepts/workspaces/collaborative-accessibility-editing.md
  - assistant/questions/workspaces/what-editors-work-with-workspaces.md
  - assistant/questions/workspaces/how-are-accessibility-features-edited.md
  - assistant/questions/workspaces/can-geometry-be-edited.md
  - assistant/questions/workspaces/can-attribute-data-be-edited.md
  - workspaces/index.md
  - rapid/index.md
  - josm/index.md
  - aviv-scoutroute/index.md
---

# Edit accessibility features in a workspace

## Short Answer

After a workspace exists, edit pedestrian and accessibility features using OSM-compatible editors connected to Workspaces—typically **Rapid** (web), **JOSM** (desktop), or **AVIV ScoutRoute** (mobile). You can adjust **geometry** (for example sidewalk alignment), change **attributes/tags** (surface, crossings, curb ramps, connectivity), and add or update features in the OpenSidewalks-oriented network. Edits stay in the workspace sandbox until review and export; they do not automatically update TDEI, OS-CONNECT, or public OpenStreetMap.

## Significance

Workspaces is where per-feature stewardship happens. TDEI handles whole-dataset operations; Workspaces is aimed at GIS staff, contractors, and reviewers who need an OSM-familiar map to fix sidewalks, crossings, ramps, and related paths before the next release. Using the same editing patterns as OpenStreetMap lowers training cost and supports coordinated field-to-office workflows (mobile capture, desktop/web correction, manager review).

## What This Means

**Editors (choose by role and task)**

| Editor | Typical use | Notes from workshop |
|--------|-------------|---------------------|
| [Rapid](../../../rapid/index.md) | Web-based editing in the browser | Workspaces supports **Rapid 2** and **Rapid 3**; Rapid 2 was used as the more stable option when demoing |
| [JOSM](../../../josm/index.md) | Desktop editing | Works because Workspaces exposes modified OSM-style APIs |
| [AVIV ScoutRoute](../../../aviv-scoutroute/index.md) | Mobile / field-style capture | Often used for on-the-ground reporting; managers may follow up in Rapid for geometry |

Open a workspace from the dashboard, then launch the editor (for example **Open in Rapid 2**). The map shows **only that workspace’s data**, not the global OSM planet—otherwise the experience matches familiar OSM editing (zoom, select features, edit geometry, edit tags, add features).

**What you can edit**

- **Geometry** — Correct linework (for example remove a spurious bend in a sidewalk polyline).
- **Attributes / tags** — Update OpenSidewalks-relevant properties on sidewalks, crossings, curb ramps, and related features.
- **New mapping** — Add missing sidewalks, entrances, pathways, POIs, and connections when supported by your schema and project needs (workshop examples included venue POIs and pathways for event access planning).

**Imagery and context**

- Custom **imagery JSON** in workspace settings supports editing against aerial or other basemaps. Imagery is primarily **background context** for placing and adjusting features—not automatic extraction of sidewalks from tiles alone.
- Configure **AVIV ScoutRoute** quest definitions in workspace settings when mobile contributors need structured tasks.

**Reference layers (compare before you merge)**

- Teams often need to **see** jurisdictional GIS, curb-ramp inventories, or other GeoJSON alongside the network. In Rapid within Workspaces, you can bring in **GeoJSON reference files** (for example a city sidewalk centerline file) to compare against OS-CONNECT data.
- **Full bulk import** of a new authoritative dataset into the network is handled at the **TDEI** level, not as a one-click workspace import. The workspace is the place to **overlay, inspect, and manually reconcile** differences before edits are vetted and exported.
- Capability to merge reference data into the official editable layer via drag-and-drop was described as **coming soon** at the time of the workshop—confirm current product behavior before promising it.

**Review and attribution**

- Use the workspace **Review** view (role-dependent) to walk changesets in an OSM-changeset–style UI: who edited, which editor, sources used, and when.
- Large initial imports can produce very large changesets; filters and smaller workspaces are easier to QA.

## What This Does Not Mean

- **Not a substitute for field ADA inspections** — Tagging a curb ramp in the map does not prove legal compliance or safe real-world conditions.
- **Not automatic publication** — Saving in Rapid or JOSM does not release data to partners until your export/TDEI workflow completes.
- **Not live sync with TDEI** — Editing does not track a newer TDEI version unless you deliberately open a fresh workspace from that release.
- **Not identical to editing public OSM** — The private workspace graph is separate from the global OSM database.
- **Not guaranteed stability of every editor build** — Newer Rapid versions may have had defects during internal testing; prefer documented stable editor choices for production work.

## How To Use This

**Recommended flow**

1. [Create or open a workspace](create-a-workspace-from-tdei.md) with the correct TDEI dataset version and project group.
2. Confirm **imagery** and optional **ScoutRoute** settings if field teams are involved.
3. Choose an editor:
   - **Field / volunteer capture** → Aviv ScoutRoute (published workspaces only, per settings).
   - **Desktop GIS editing** → JOSM or Rapid.
   - **Manager geometry fixes** → Rapid after reviewing ScoutRoute or contractor submissions.
4. Edit features against imagery; use **reference GeoJSON** only as a guide unless your process explicitly promotes reconciled features into the network.
5. Run **Review** on changesets before export; document sources where the UI supports it.
6. Continue to [review](review-workspace-edits.md) and [export](export-workspace-edits-to-tdei.md) workflows when edits are ready for upstream release.

**Coordination tips**

- Align with schema conventions (OpenSidewalks / OS-CONNECT) before large tagging campaigns.
- Split work by geography or feature type so changesets stay reviewable.
- When comparing city GIS to OS-CONNECT, expect gaps (for example centerlines without network connections)—manual connection editing is often required.

## Example

A jurisdiction opens a Bremerton OS-CONNECT workspace in Rapid 2. A planner loads a city sidewalk GeoJSON as a **reference layer** and sees a newly built segment missing from OS-CONNECT. They draw the new sidewalk, connect it to the graph, and tag curb ramps at intersections. A manager uses **Review** to inspect yesterday’s changeset, checks editor and source metadata, and approves the batch for export to TDEI. The public OS-CONNECT release does not change until that export and release process completes.

## Assistant Guidance

- Clarify **editor choice** (Rapid vs JOSM vs ScoutRoute) and **role** (field vs desktop vs manager).
- Separate **reference overlay** from **authoritative ingest** (TDEI jobs vs in-map reconciliation).
- Do not promise **Rapid 3** or **drag-to-merge reference data** without checking current release notes.
- For “is this ADA compliant,” redirect to [ADA compliance boundaries](../../concepts/ada-compliance-boundaries.md) and abstain on legal proof.
- If the user describes attribute experiments on walksheds or routing outcomes, note that **Walksheds** and **AccessMap** consume released network data—they are downstream of workspace editing and export, not the same in-browser edit surface.
- Point procedural detail to [Workspaces overview](../../../workspaces/index.md) and editor manuals; avoid inventing tag keys or UI labels.

## Related Concepts

- [Create a workspace from TDEI](create-a-workspace-from-tdei.md)
- [Review workspace edits](review-workspace-edits.md)
- [Private OSM (Workspaces)](../../concepts/workspaces/private-osm.md)
- [Multi-source stewardship](../../concepts/workspaces/multi-source-stewardship.md)
- [Workspace editors](../../concepts/workspaces/workspace-editors.md) *(stub—author next)*
- [How are accessibility features edited?](../../questions/workspaces/how-are-accessibility-features-edited.md) *(stub—author next)*
