---
uid: 7bc49a18-d5ce-4c01-a99f-4561b8b49ddb
title: What metadata identifies a workspace?
slug: workspace-metadata-and-lineage
doc_type: concept
questions:
    - What metadata identifies a workspace?
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
    - workspace-management
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Workspace metadata alone proves that its contents are current.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What metadata identifies a workspace?

## Short Answer

Workspace metadata can include its coverage, creation date, creator, project group, source dataset ID, source version, and app-access state.

## Significance

These fields support discovery, lineage, and troubleshooting.

## What This Means

Use metadata to identify what the workspace contains and where it came from.

## What This Does Not Mean

Metadata does not replace reviewing the actual geometry, attributes, or current source.

## How To Use This

Record the workspace ID and source version when sharing a link or report.

## Example

A manager checks the source dataset ID before deciding whether a workspace is ready for export.

## Assistant Guidance

Ask for the workspace and source identifiers when context is missing.

## Related Concepts

- [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
