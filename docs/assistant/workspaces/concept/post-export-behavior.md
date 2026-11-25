---
uid: 65d73d85-848b-449f-b803-b30fc9f9ba3a
title: What happens after export to TDEI?
slug: post-export-behavior
doc_type: concept
questions:
    - What happens after export to TDEI?
    - What happens to the Workspace after the edited data is returned to TDEI?
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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

Uploading a workspace through **Upload to TDEI** creates a new TDEI dataset. The workspace remains open for editing and is unchanged by the export; it remains a separate record from both the source dataset and the uploaded result.

## Significance

Post-export handling determines where users find the result, which identifier and version to cite, and whether another publication or processing step is needed.

## What This Means

After upload, check the TDEI dataset record, identifier, available version metadata, validation and release status, and visibility. The workspace remains available for further editing; a later workspace edit does not itself update the already-uploaded TDEI dataset.

## What This Does Not Mean

Export does not close, reset, or delete the workspace, overwrite the source dataset, synchronize other products, or make the new dataset public.

## How To Use This

Retain the workspace and source history, record the resulting TDEI identifier, and verify the new dataset's validation and release status separately.

## Example

A manager records the new TDEI dataset identifier after upload, continues editing the still-open workspace, and tells users whether the uploaded dataset has also been validated or released.

## Assistant Guidance

Explain that export leaves the workspace open and unchanged while creating a separate TDEI dataset. Do not promise that later workspace edits update the exported dataset or that the upload is a public release; cite the current export documentation and verify the dataset's status.

## Related Concepts

- [What happens during export?](export-process.md)
- [What versioning occurs during export?](export-versioning.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
