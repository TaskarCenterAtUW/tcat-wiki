---
uid: 65d73d85-848b-449f-b803-b30fc9f9ba3a
title: What happens after export to TDEI?
slug: post-export-behavior
doc_type: concept
questions:
    - What happens after export to TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - export
    - publication-workflow
    - dataset-lineage
risk_level: high
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
    - assistant/workspaces/concept/export-process.md
    - assistant/workspaces/concept/export-versioning.md
    - assistant/workspaces/concept/dataset-lineage-in-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# What happens after export to TDEI?

## Short Answer

After export to TDEI, the result follows the target workflow's validation, dataset, release, permissions, and publication behavior. The workspace, source dataset, and exported result remain separate records unless the current workflow explicitly relates them.

## Significance

Post-export handling determines where users find the result, which identifier and version to cite, and whether another publication or processing step is needed.

## What This Means

Check export or job status, validation results, target dataset and release metadata, visibility, lineage, and whether downstream products need a separate update.

## What This Does Not Mean

Export does not guarantee immediate public availability, overwrite of the source, synchronization with other products, or correctness of every edit.

## How To Use This

Retain the workspace and source history, record the resulting identifier, verify access and release status, and communicate limitations to downstream users.

## Example

A manager records the new TDEI dataset identifier after export, checks validation status, and tells users which release contains the reviewed changes.

## Assistant Guidance

Do not invent post-export states or promise downstream updates. Ask for the environment and target, cite current workflow documentation, and abstain when status is unknown.

## Related Concepts

- [What happens during export?](export-process.md)
- [What versioning occurs during export?](export-versioning.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
