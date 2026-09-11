---
uid: 74d0f041-51ba-4de5-af68-5906d73bb777
title: How can users trace the source dataset?
slug: source-dataset-tracing
doc_type: concept
questions:
    - How can users trace the source dataset?
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
        - A workspace's source dataset can always be inferred from its title.
        - Workspace edits automatically update the source dataset.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/dataset-lineage.md
    - assistant/workspaces/concept/workspace-metadata-and-lineage.md
tags:
    - Assistant
---

<!-- @format -->

# How can users trace the source dataset?

## Short Answer

Trace a workspace's source by checking its metadata, creation method, source dataset or file, version, geography, and any recorded export history. The workspace title alone is not sufficient evidence.

## Significance

Source tracing supports reproducibility, correction review, and safe comparison with later releases.

## What This Means

Record the source and version before editing, then retain the lineage when deriving or exporting data.

## What This Does Not Mean

A workspace does not automatically retain every external source detail or synchronize with later source changes.

## How To Use This

Ask for the workspace identifier and inspect current metadata or TDEI records. Abstain when the source or version cannot be verified.

## Example

A reviewer finds the source release in workspace metadata and uses it to compare an edit with later TDEI data before export.

## Assistant Guidance

Cite the metadata or dataset record used for the answer; do not reconstruct lineage from naming conventions alone.

## Related Concepts

 - [What is dataset lineage?](dataset-lineage.md)
 - [How is workspace metadata and lineage recorded?](workspace-metadata-and-lineage.md)
