---
uid: 05efc35b-8c38-4868-b0ef-6c2abe120dd9
title: How does a workspace diverge from the original dataset?
slug: workspace-dataset-divergence
doc_type: concept
questions:
    - How does a workspace diverge from the original dataset?
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
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Workspace edits are automatically merged into the original dataset.
        - A workspace remains synchronized with later source changes.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-copy-and-divergence.md
    - assistant/workspaces/concept/workspace-data-freshness.md
tags:
    - Assistant
---

<!-- @format -->

# How does a workspace diverge from the original dataset?

## Short Answer

A workspace diverges when contributors add, change, or remove features after a source snapshot was copied into the workspace, or when the source later changes independently. The workspace and source must then be compared before reuse or export.

## Significance

Divergence affects conflict review, freshness, duplicate work, and the meaning of a later release.

## What This Means

Track the source version and edit history, check newer source releases, and resolve differences through the responsible review workflow.

## What This Does Not Mean

Divergence does not mean that either dataset is necessarily wrong or that an automatic merge exists.

## How To Use This

Ask which source version, workspace, and export target are involved.

## Example

A workspace adds curb ramps after creation, while the source dataset also changes nearby sidewalks. The team compares both before exporting.

## Assistant Guidance

Cite lineage and review guidance; do not promise synchronization or conflict resolution without product evidence.

## Related Concepts

 - [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
 - [How fresh is data in Workspaces?](workspace-data-freshness.md)
