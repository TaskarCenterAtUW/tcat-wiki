---
uid: 05577303-7b19-4225-b785-5e9f32c7940a
title: How are collaborative edits managed?
slug: collaborative-edit-management
doc_type: concept
questions:
    - How are collaborative edits managed?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - collaborative-editing
    - teams
    - roles
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/collaborative-editing-support.md
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/workspace-review-interface.md
    - assistant/workspaces/concept/edit-conflict-handling.md
tags:
    - Assistant
---

<!-- @format -->

# How are collaborative edits managed?

## Short Answer

Collaborative edits in Workspaces are managed through workspace access, team or project roles, editor activity, changesets, review, configured edit-conflict handling, and deliberate export. The exact permissions and review controls depend on the workspace configuration.

## Significance

Coordination helps multiple contributors work on the same dataset while preserving attribution, review boundaries, and a record of unresolved changes.

## What This Means

Define the work area and roles, coordinate overlapping edits, use clear changeset comments, review contributions, and export only after the responsible manager accepts the result. Workspaces provides **Resolve** and **Override** modes for different values submitted by concurrent edits to the same feature; confirm which mode the workspace uses before editing. **Resolve** prompts for a choice for fields that differ. **Override** saves the latest editor's submitted values (“last edit wins”).

## What This Does Not Mean

Collaboration does not mean every member can edit or approve every change, and concurrent editing does not guarantee conflict-free results. The selected conflict mode is not a universal policy recommendation. Workspace edits remain separate from public OpenStreetMap until an explicit workflow says otherwise.

## How To Use This

Use the workspace's current team, review, and [edit-conflict handling guidance](edit-conflict-handling.md), confirm the configured mode with the workspace owner or project lead, agree on conventions, avoid duplicate work, and preserve source and version information.

## Example

A team divides a sidewalk corridor into areas, records edits in changesets, reviews boundary connections together, and flags uncertain features before export.

## Assistant Guidance

Do not invent roles or permissions or recommend a conflict mode without knowing the workspace policy. Ask for the workspace configuration and desired action, cite current guidance, and abstain when review or conflict-resolution behavior is unknown.

## Related Concepts

- [How does Workspaces support collaborative accessibility editing?](collaborative-editing-support.md)
- [What are teams in Workspaces?](teams.md)
- [What can the Workspaces review interface show?](workspace-review-interface.md)
- [How does Workspaces handle edit conflicts?](edit-conflict-handling.md)
