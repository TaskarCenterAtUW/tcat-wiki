---
uid: 055ad2f1-86d6-48c8-89ba-edd1559cfbe5
title: What happens if two groups edit separate copies?
slug: parallel-workspace-editing
doc_type: concept
questions:
    - What happens if two groups edit separate copies?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - sandbox-governance
    - dataset-lineage
    - publication-workflow
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/multiple-workspaces-per-dataset.md
    - assistant/workspaces/concept/workspace-dataset-divergence.md
    - assistant/workspaces/concept/editing-coordination.md
tags:
    - Assistant
---

<!-- @format -->

# What happens if two groups edit separate copies?

## Short Answer

If two groups edit separate workspace copies, each copy develops its own changes, history, review state, and lineage. The edits do not synchronize automatically and must be reconciled deliberately if a shared result is needed.

## Significance

Separate copies can support independent projects but create risks of duplicated work, conflicting values, and divergent versions.

## What This Means

Record source release and workspace IDs, compare scopes and changesets, identify overlaps, reconcile differences, review the combined result, and preserve both source histories.

## What This Does Not Mean

Neither workspace automatically becomes authoritative, and exporting one copy does not automatically incorporate the other's work or update the source dataset.

## How To Use This

Use a documented merge or publication process, communicate ownership, and avoid presenting one copy as a complete replacement without review.

## Example

Two groups edit sidewalk data from the same release in separate workspaces. A manager compares their changes, resolves a boundary conflict, and records the resulting lineage before export.

## Assistant Guidance

Ask for the source release, workspace IDs, overlap, and intended output. Do not promise merging or synchronization without current documentation.

## Related Concepts

- [Can multiple workspaces exist from the same dataset?](multiple-workspaces-per-dataset.md)
- [How does a workspace diverge from its source dataset?](workspace-dataset-divergence.md)
- [How can multiple people coordinate editing?](editing-coordination.md)
