---
uid: 2e3b7419-f07a-4770-b232-1f10799c536e
title: Does editing a workspace change the TDEI dataset?
slug: workspace-tdei-isolation
doc_type: concept
questions:
    - Does editing a workspace change the TDEI dataset?
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
        - Editing a workspace automatically changes the TDEI source dataset.
        - A workspace edit is public immediately.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-and-tdei-boundary.md
    - assistant/workspaces/workflow/export-workspace-edits-to-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# Does editing a workspace change the TDEI dataset?

## Short Answer

Editing a workspace does not by itself change the original TDEI dataset. A workspace is a separate editing environment; changes reach a managed TDEI destination only through an authorized export or publication workflow.

## Significance

Isolation protects source data while teams review and enrich a working copy.

## What This Means

Treat workspace changes as pending until the responsible team validates and exports them through the documented path.

## What This Does Not Mean

Isolation is not a guarantee about every user's visibility or the security of a deployment; permissions and publication settings still matter.

## How To Use This

Ask which source, workspace, export, and release are involved.

## Example

A mapper edits a TDEI-derived workspace, and the source dataset remains unchanged until an approved export creates a later result.

## Assistant Guidance

Cite the boundary and export documentation. Do not promise a live source update without evidence.

## Related Concepts

 - [What is the Workspaces and TDEI boundary?](workspace-and-tdei-boundary.md)
 - [How do I export workspace edits to TDEI?](../workflow/export-workspace-edits-to-tdei.md)
