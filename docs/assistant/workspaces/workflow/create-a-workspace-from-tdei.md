---
title: "Create a workspace from TDEI"
tags:
    - Assistant
slug: create-a-workspace-from-tdei
doc_type: workflow
products:
    - Workspaces
    - TDEI
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - onboarding
    - workspace-management
    - tdei-ecosystem
    - sandbox-governance
    - dataset-lineage
risk_level: low
authority_level: draft
review_status: draft
last_reviewed: 2026-05-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a workspace automatically updates the TDEI dataset
        - A workspace stays synchronized when TDEI publishes a newer dataset version
        - Opening a workspace edits the public OpenStreetMap database
        - Every partner has permission to open every TDEI dataset in Workspaces
related_pages:
    - assistant/concepts/workspaces/private-osm.md
    - assistant/concepts/workspaces/workspace-sandbox.md
    - assistant/concepts/workspaces/dataset-lineage.md
    - assistant/concepts/workspaces/tdei-vs-workspaces.md
    - assistant/questions/workspaces/how-do-i-create-a-workspace-from-tdei.md
    - assistant/questions/workspaces/what-happens-when-i-create-a-workspace-from-a-tdei-dataset.md
    - assistant/questions/workspaces/is-a-workspace-a-copy-or-the-original-dataset.md
    - assistant/questions/workspaces/does-editing-a-workspace-change-the-tdei-dataset.md
    - workspaces/index.md
---

<!-- @format -->

# Create a workspace from TDEI

## Short Answer

To create a workspace from TDEI, open a dataset that is already stored in the [TDEI portal](https://portal.tdei.us/) and use **Open in Workspaces** (or the equivalent action on that dataset). Workspaces copies the **current TDEI dataset version** into a private editing sandbox. Edits happen in Workspaces first; they do not change the TDEI release until you export or upload through your jurisdiction's publication workflow.

You can also start from the Workspaces dashboard (**Create Workspace** → **From TDEI**), pick a project group, and select the dataset — same outcome, different starting screen.

## Significance

TDEI is built to manage **whole datasets** (inventory, metadata, jobs, releases). Workspaces is built for **per-feature editing** in an OSM-compatible sandbox. The "open from TDEI" step is the handoff between those roles: planners and data managers find the authoritative release in TDEI; GIS and mapping staff edit a **copy** in Workspaces without risking the stored release until review and export.

## What This Means

**Two equivalent entry points**

1. **From TDEI portal** — Browse to the dataset (for example under a project group), use the dataset action menu, and choose **Open in Workspaces**. This copies that dataset **as it exists at that version** (for example "version 2") into a new workspace.
2. **From Workspaces** — Sign in with the **same TDEI portal account**, use **Create Workspace** (dashboard or **New workspace**), choose **From TDEI**, select the **project group**, then select the dataset from the list.

**What gets copied**

- Workspaces loads a **snapshot** of the pedestrian network data from TDEI into a **private OSM-style** workspace environment.
- The workspace dashboard records lineage metadata such as **from TDEI dataset ID**, **project group**, and **version**, so you can trace the workspace back to the source release in TDEI.
- Creation may take from a few seconds to several minutes depending on area size and data density.

**Accounts and access**

- Workspaces uses **TDEI portal credentials** (same login as TDEI, Aviv ScoutRoute, and related tools).
- You must have access to the relevant **project group** and dataset in TDEI before you can open it in Workspaces.

**After the workspace exists**

- Edit with supported tools (embedded Rapid, JOSM, Aviv ScoutRoute where published, and related workflows).
- Review changes in Workspaces before any publication step.
- When ready, **export or upload** back to TDEI (see [Export workspace edits to TDEI](export-workspace-edits-to-tdei.md)) or use other approved export paths described in product documentation.

## What This Does Not Mean

- **Not live sync** — The workspace is a **copy**. If TDEI metadata or a newer dataset version is published later, the workspace does **not** automatically update to match.
- **Not in-place editing of TDEI** — Changing features in the workspace does **not** change the TDEI stored dataset until an explicit export/upload and downstream release process.
- **Not public OSM** — Workspaces data is separate from the global OpenStreetMap database unless your organization follows a distinct OSM contribution process.
- **Not the only creation path** — Partners can also create workspaces from **blank**, **local OpenSidewalks/OSW files**, or pipelines that first register data in TDEI (for example OSM PBF → TDEI convert job → file upload into Workspaces). Those paths are different workflows.

## How To Use This

**Typical agency workflow (OS-CONNECT / released pedestrian data in TDEI)**

1. Confirm the correct **released dataset and version** in the TDEI portal (check project group, release status, and recency).
2. **Open in Workspaces** from that dataset, or create from TDEI inside Workspaces as described above.
3. On the workspace dashboard, note **from TDEI dataset ID** and **version** for audit trails and support questions.
4. Configure workspace settings if needed (title, external app publish toggles, imagery JSON — see the [Workspaces user manual](../../../workspaces/user-manual/workspace-settings.md)).
5. Edit in the chosen editor; coordinate teams so multiple groups do not assume they are editing the same live TDEI release without communication.
6. Run review in Workspaces, then follow your jurisdiction's steps to **export to TDEI** and publish or download as required.

**When TDEI is the right starting point**

- The authoritative copy for your program already lives in TDEI.
- You need a sandbox to correct or enrich **OS-CONNECT-class** pedestrian data before the next release.
- You want dataset-level jobs (convert, reformat, bulk operations) finished in TDEI **before** opening the result for interactive editing.

**When to confirm with TCAT**

- You lack project group access, cannot see the dataset, or **Open in Workspaces** is unavailable.
- You need edits in TDEI on a schedule not covered by public documentation.
- You are unsure whether prod, stage, or dev environments apply ([Workspaces](https://workspaces.sidewalks.washington.edu/) and matching TDEI portal hosts).

## Example

A city has an OS-CONNECT pedestrian dataset for its service area stored in TDEI at version 2. A GIS analyst opens that dataset in the TDEI portal and selects **Open in Workspaces**. Workspaces creates a new workspace under the city's project group with **from TDEI dataset ID** and **version 2** shown on the dashboard. The analyst edits curb ramps and crossings in Rapid over several weeks. The TDEI release remains unchanged until the team completes review and performs an export back to TDEI. Meanwhile, if TDEI publishes version 3, the existing workspace still reflects version 2 unless the team deliberately creates a new workspace from the newer release.

## Assistant Guidance

- Lead with the **copy / sandbox** boundary: TDEI stores releases; Workspaces edits a diverging copy.
- Ask for **project group**, **dataset ID**, and **version** when troubleshooting "wrong" or stale data.
- Distinguish **TDEI dataset managers** (inventory, releases, jobs) from **Workspaces editors** (feature-level GIS work)—both may be the same person in small agencies.
- Point procedural detail to the [TCAT Wiki Workspaces section](../../index.md) and TDEI portal user manual for jobs and registration; do not invent UI labels beyond what documentation and the cited workshop materials describe.
- For export, publication, and legal or ADA claims, defer to [export workflow](export-workspace-edits-to-tdei.md) and [ADA compliance boundaries](../../concepts/ada-compliance-boundaries.md).
- If environment, permissions, or release timing are unknown, **abstain** from stating what the user will see or when data will go live.

## Related Concepts

- [Private OSM (Workspaces)](../../workspaces/private-osm.md)
- [Workspace sandbox](../../workspaces/workspace-sandbox.md) _(stub — author next)_
- [Dataset lineage (Workspaces and TDEI)](../../workspaces/dataset-lineage.md) _(stub — author next)_
- [TDEI vs Workspaces](../../workspaces/tdei-vs-workspaces.md) _(stub — author next)_
- [How do I create a workspace from TDEI?](../../workspaces/how-do-i-create-a-workspace-from-tdei.md) _(stub — author next)_
- [What happens when I create a workspace from a TDEI dataset?](../../workspaces/what-happens-when-i-create-a-workspace-from-a-tdei-dataset.md) _(stub — author next)_
- [Workspaces (product overview)](../../../workspaces/index.md)
