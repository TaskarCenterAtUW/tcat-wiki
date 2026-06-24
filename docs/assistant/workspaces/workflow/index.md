---
title: Workspaces Workflows — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-workspaces-workflows
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
    - publication-workflow
    - collaboration
    - teams
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/workspaces/index.md
    - assistant/workflows/index.md
    - assistant/dispatch.md
---

# Workspaces Workflows — Assistant Knowledge Base

## Short Answer

This section contains step-level workflow pages for common Workspaces tasks: creating a workspace from TDEI data, editing accessibility features, configuring imagery layers, inviting a team, reviewing edits, and exporting to TDEI. These pages provide assistant-layer summaries of end-to-end task sequences.

## Significance

Workspaces users — jurisdiction staff, advocates, GIS technicians — frequently ask how to accomplish specific tasks rather than asking conceptual questions. Workflow pages answer "how do I do X?" with sequential, role-aware guidance.

## What This Means

- Pages in `workspaces/workflows/` describe task sequences for common Workspaces operations.
- For conceptual questions about Workspaces features, see the [Workspaces knowledge base](../index.md).
- For cross-product workflows (e.g., OS-CONNECT for ADA planning), see [workflows/](../../workflows/index.md).

## What This Does Not Mean

- Not a substitute for the [Workspaces User Manual](../../../workspaces/user-manual/index.md) for authoritative step-by-step procedures.
- Workflow pages provide assistant-layer summaries; actual UI steps may differ from descriptions if the product has been updated.

## How To Use This

**Agents**: Match user queries to the closest workflow page. For imagery configuration, retrieve `workspaces/workflows/configure-imagery-layers.md`. For team management, retrieve `workspaces/workflows/invite-a-team-to-a-workspace.md`.

**Authors**: Eight workflow pages are planned. Start with the highest-traffic workflows: `create-a-workspace-from-tdei.md` and `export-workspace-edits-to-tdei.md`.

## Example

A jurisdiction GIS technician asks: _"How do I export my workspace edits back to TDEI?"_ Retrieve `workspaces/workflows/export-workspace-edits-to-tdei.md`.

## Assistant Guidance

Workflow answers should always note the sandbox boundary: changes made in Workspaces are not visible externally until exported and published through TDEI. Include a note about human review steps in the export-and-publication workflow.

## Related Concepts

- [Workspaces knowledge base](../index.md)
- [Workspaces policies](../policies/index.md)
- [Cross-product workflows](../../workflows/index.md)
- [Dispatch — full file registry](../../dispatch.md)

## Planned Pages

| File | Workflow |
|------|----------|
| `workspaces/workflows/configure-imagery-layers.md` | Setting up imagery sources in a workspace |
| `workspaces/workflows/create-a-workspace-from-tdei.md` | Creating a new workspace from an existing TDEI dataset |
| `workspaces/workflows/edit-accessibility-features-in-a-workspace.md` | Editing sidewalks, crossings, and curb ramps in a workspace |
| `workspaces/workflows/export-workspace-edits-to-tdei.md` | Exporting completed workspace edits to TDEI for publication |
| `workspaces/workflows/invite-a-team-to-a-workspace.md` | Inviting collaborators to a workspace |
| `workspaces/workflows/review-workspace-edits.md` | Manager review of edits before export |
| `workspaces/workflows/use-workspaces-for-community-validation.md` | Running a community mapping session using Workspaces |
| `workspaces/workflows/use-workspaces-for-jurisdiction-stewardship.md` | Ongoing stewardship workflow for jurisdiction data managers |
