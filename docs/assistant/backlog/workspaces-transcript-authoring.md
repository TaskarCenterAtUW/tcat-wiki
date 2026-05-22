---
title: Workspaces transcript authoring queue
slug: workspaces-transcript-authoring
doc_type: workflow
products:
  - Workspaces
audiences:
  - planner
  - jurisdiction
topics:
  - workspaces
  - backlog
  - authoring
risk_level: low
authority_level: draft
review_status: draft
last_reviewed: "2026-05-22"
retrieval_priority: low
assistant_behavior:
  allow_inference: false
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - This queue is authoritative product documentation without human review.
related_pages:
  - assistant/workflows/workspaces/index.md
  - assistant/concepts/workspaces/index.md
  - assistant/questions/workspaces/index.md
  - assistant/sources/README.md
---

# Workspaces transcript authoring queue

## Short Answer

This page tracks the **human-in-the-loop** loop for filling Workspaces assistant stubs from workshop transcripts: agent drafts → you review → commit/push → next stub.

## Authoring loop (repeat per page)

| Step | Owner | Action |
|------|--------|--------|
| 1 | Agent | Pick the next **pending** row below; read transcript excerpts + existing wiki (`docs/workspaces/`, authored concepts). |
| 2 | Agent | Replace all `TODO` sections; set `last_reviewed` to the authoring date; fix `related_pages` to `assistant/...` paths; add `do_not_claim` where needed. |
| 3 | Agent | **Stop** and tell you: **“Your turn to review”** with a link to the file. |
| 4 | You | Edit in Cursor; save when satisfied. |
| 5 | You | Reply **“approved”** or **“commit”** (or ask for revisions). |
| 6 | Agent | `git add` that file only → commit → push branch → mark row **done** → go to step 1. |

Do not batch-commit multiple reviewed pages unless you ask for it.

## Source material

| Part | File | Status |
|------|------|--------|
| 1 (2026-05-12) | [GMT20260512-OH_Workspaces1_Recording.transcript.vtt](../sources/workspaces-workshop/GMT20260512-OH_Workspaces1_Recording.transcript.vtt) | ✅ in repo |
| 2 (2026-05-19) | [GMT20260519-OH_Workspaces2_Recording.transcript.vtt](../sources/workspaces-workshop/GMT20260519-OH_Workspaces2_Recording.transcript.vtt) | ✅ in repo |

**Also cite** (already in wiki): `docs/workspaces/`, `docs/rapid/`, `docs/josm/`, `docs/aviv-scoutroute/`, and authored concepts [private-osm](../concepts/workspaces/private-osm.md), [multi-source-stewardship](../concepts/workspaces/multi-source-stewardship.md).

## Grounding rules (every page)

- Keep all nine RAG sections per [schema](../../rag/schema.md).
- Preserve **abstention**: no auto-publication to OSM, no ADA/legal proof, no guaranteed timelines unless documented.
- `authority_level` stays `draft` until staff sets `reviewed`.
- Prefer workshop + wiki facts; mark gaps as “confirm with TCAT” in **Assistant Guidance**, not invented UI.
- `related_pages`: paths relative to `docs/`, e.g. `assistant/concepts/workspaces/private-osm.md`.

## Queue — Phase A: workflows (do first)

| # | Page | Path | Status |
|---|------|------|--------|
| A1 | Create a workspace from TDEI | [create-a-workspace-from-tdei.md](../workflows/workspaces/create-a-workspace-from-tdei.md) | done (`95e795e`) |
| A2 | Edit accessibility features in a workspace | [edit-accessibility-features-in-a-workspace.md](../workflows/workspaces/edit-accessibility-features-in-a-workspace.md) | done (`9571426`) |
| A3 | Configure imagery layers | [configure-imagery-layers.md](../workflows/workspaces/configure-imagery-layers.md) | **next** |
| A4 | Invite a team to a workspace | [invite-a-team-to-a-workspace.md](../workflows/workspaces/invite-a-team-to-a-workspace.md) | pending |
| A5 | Review workspace edits | [review-workspace-edits.md](../workflows/workspaces/review-workspace-edits.md) | pending |
| A6 | Export workspace edits to TDEI | [export-workspace-edits-to-tdei.md](../workflows/workspaces/export-workspace-edits-to-tdei.md) | pending |
| A7 | Jurisdiction stewardship | [use-workspaces-for-jurisdiction-stewardship.md](../workflows/workspaces/use-workspaces-for-jurisdiction-stewardship.md) | pending |
| A8 | Community validation | [use-workspaces-for-community-validation.md](../workflows/workspaces/use-workspaces-for-community-validation.md) | pending |

## Queue — Phase B: concepts (stubs)

| # | Page | Path | Status |
|---|------|------|--------|
| B1 | Workspace sandbox | [workspace-sandbox.md](../concepts/workspaces/workspace-sandbox.md) | pending |
| B2 | TDEI vs Workspaces | [tdei-vs-workspaces.md](../concepts/workspaces/tdei-vs-workspaces.md) | pending |
| B3 | Dataset lineage | [dataset-lineage.md](../concepts/workspaces/dataset-lineage.md) | pending |
| B4 | Workspace export | [workspace-export.md](../concepts/workspaces/workspace-export.md) | pending |
| B5 | Project groups | [project-groups.md](../concepts/workspaces/project-groups.md) | pending |
| B6 | Workspace editors | [workspace-editors.md](../concepts/workspaces/workspace-editors.md) | pending |
| B7 | Imagery layers | [imagery-layers.md](../concepts/workspaces/imagery-layers.md) | pending |
| B8 | Changesets | [changesets.md](../concepts/workspaces/changesets.md) | pending |
| B9 | Collaborative accessibility editing | [collaborative-accessibility-editing.md](../concepts/workspaces/collaborative-accessibility-editing.md) | pending |
| — | Private OSM | [private-osm.md](../concepts/workspaces/private-osm.md) | **done** (pre-authored) |
| — | Multi-source stewardship | [multi-source-stewardship.md](../concepts/workspaces/multi-source-stewardship.md) | **done** (pre-authored) |

## Queue — Phase C: policies (stubs)

| # | Page | Path | Status |
|---|------|------|--------|
| C1 | Export and publication caveats | [workspace-export-and-publication-caveats.md](../policies/workspaces/workspace-export-and-publication-caveats.md) | pending |
| C2 | Public vs private data | [workspace-public-vs-private-data.md](../policies/workspaces/workspace-public-vs-private-data.md) | pending |
| C3 | Abstention boundaries | [workspace-abstention-boundaries.md](../policies/workspaces/workspace-abstention-boundaries.md) | pending |
| C4 | Editing authority | [workspace-editing-authority.md](../policies/workspaces/workspace-editing-authority.md) | pending |
| C5 | Data freshness | [workspace-data-freshness.md](../policies/workspaces/workspace-data-freshness.md) | pending |

## Queue — Phase D: questions (301–400)

Author after Phases A–C, or in parallel when a question directly supports a finished workflow. Full numbered list: [Workspaces questions](../questions/workspaces/index.md) (100 stubs).

## Completed in this branch (outside queue)

| Page | Commit |
|------|--------|
| OS-CONNECT destination access (helpline) | `4e37482` |

## Assistant Guidance

When transcripts are missing, do not invent workshop detail—use wiki manuals only and flag **Assistant Guidance** for transcript pass after files land.
