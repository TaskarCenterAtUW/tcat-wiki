---
uid: da46b16f-aab5-4136-bdc9-d8316b4fd5c0
title: Is a workspace a copy or the original dataset?
slug: workspace-as-dataset-copy
doc_type: concept
questions:
    - Is a workspace a copy or the original dataset?
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
        - A workspace is the original source dataset.
        - Editing a workspace automatically changes the source dataset.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-copy-and-divergence.md
    - assistant/workspaces/concept/dataset-lineage.md
tags:
    - Assistant
---

<!-- @format -->

# Is a workspace a copy or the original dataset?

## Short Answer

A workspace is an editable copy or imported dataset environment, not the original source dataset. It can contain edits that diverge from the source until an authorized export or publication workflow creates a later managed result.

## Significance

This separation protects source data and gives teams a place to review changes before release.

## What This Means

Record the source and version, edit within the workspace, and use the documented export path when changes are ready for review or publication.

## What This Does Not Mean

Creating or editing a workspace does not automatically update the source or make the workspace public.

## How To Use This

Ask which source, workspace, and export destination are involved.

## Example

A team creates a workspace from a TDEI dataset, adds accessibility features, and reviews the copy before exporting a new version.

## Assistant Guidance

Cite lineage and export documentation; abstain when the source relationship is not recorded.

## Related Concepts

 - [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
 - [What is dataset lineage?](dataset-lineage.md)
