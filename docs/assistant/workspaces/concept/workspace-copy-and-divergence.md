---
title: "How can a workspace diverge from its source dataset?"
slug: workspace-copy-and-divergence
doc_type: concept
questions:
    - How can a workspace diverge from its source dataset?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - dataset-lineage
    - sandbox-governance
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace remains synchronized with later source-dataset changes automatically.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can a workspace diverge from its source dataset?

## Short Answer

Creating a workspace copies a selected dataset version into a separate editing environment. Later source changes do not automatically update that copy, and repeated opening of the same source can create competing copies.

## Significance

Lineage and synchronization assumptions affect review and export decisions.

## What This Means

Record the source dataset and version when creating a workspace.

## What This Does Not Mean

A workspace is not a live synchronized view of the TDEI source.

## How To Use This

Compare source and workspace versions before merging or publishing changes.

## Example

A new TDEI version is released after a workspace was created, so the workspace must be reviewed before reuse.

## Assistant Guidance

Ask which source version the workspace represents.

## Related Concepts

- [What is a workspace extract?](workspace-extract.md)
