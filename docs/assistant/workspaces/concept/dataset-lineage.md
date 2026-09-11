---
uid: 3fa9ed5e-d219-4cfa-85c0-e05649f7b617
title: Dataset lineage (Workspaces and TDEI)
slug: dataset-lineage
doc_type: concept
questions:
    - What is dataset lineage in Workspaces and TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - dataset-lineage
    - publication-workflow
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace has no relationship to its source dataset.
        - Exporting a workspace automatically publishes every edit.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-metadata-and-lineage.md
    - assistant/workspaces/concept/workspace-copy-and-divergence.md
tags:
    - Assistant
---

<!-- @format -->

# Dataset lineage (Workspaces and TDEI)

## Short Answer

Dataset lineage records where a workspace dataset came from, including its source dataset or file, version or release, and subsequent workspace edits. It helps users distinguish the source from the editable copy and understand what an export represents.

## Significance

Lineage supports reproducibility, review, correction tracking, and responsible publication. Without it, users may compare or release data without knowing which source version was used.

## What This Means

 - Record the source dataset, version, geography, and creation context.
 - Track edits and review decisions made in the workspace.
 - Preserve lineage when exporting or creating a later dataset version.

## What This Does Not Mean

Lineage does not mean that a workspace remains synchronized with its source or that every edit is automatically authoritative or public.

## How To Use This

Use the workspace metadata and current TDEI records to identify the source and release. Ask for the workspace and dataset version when lineage affects an answer.

## Example

A reviewer finds that a workspace was created from an older TDEI release, records that fact, and checks for changes before exporting its edits.

## Assistant Guidance

Cite the relevant workspace or TDEI record. Abstain when source version, scope, or export history is missing.

## Related Concepts

 - [Workspaces — Assistant Knowledge Base](../index.md)
 - [How is workspace metadata and lineage recorded?](workspace-metadata-and-lineage.md)
 - [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
