---
uid: 6e8d733d-2d88-487b-a459-540f8eb240d4
title: Does export overwrite the original dataset?
slug: export-overwrite-behavior
doc_type: concept
questions:
    - Does export overwrite the original dataset?
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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Uploading a Workspaces export to TDEI overwrites the source dataset.
related_pages:
    - assistant/workspaces/concept/export-process.md
    - assistant/workspaces/concept/export-versioning.md
    - assistant/workspaces/concept/dataset-lineage-in-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# Does export overwrite the original dataset?

## Short Answer

In the Workspaces export flow, users can upload an export to TDEI or download it as a file. Uploading creates a new TDEI dataset; it does not modify the source dataset from which the workspace was created.

## Significance

Knowing whether an export creates a separate dataset helps users protect source data, preserve lineage, and distinguish an upload from publication of a release.

## What This Means

Choose the TDEI upload option to create a new dataset in the selected project group, or choose download to save an export file for processing or another upload workflow. Record the resulting dataset identifier and version, confirm its visibility and validation status, and check separately whether it has been released. The original source remains distinct from the new exported dataset.

## What This Does Not Mean

The TDEI upload is not a destructive replacement of the source. Creating a new dataset does not by itself mean that it is reviewed, released, or publicly visible.

## How To Use This

Before exporting, review the workspace and confirm the source, project group, intended target, and export mode. After an upload, record the new dataset identifier and version and check the project-dataset and release views rather than assuming that the source was overwritten or the export was published.

## Example

A manager uploads reviewed workspace edits to TDEI. The upload creates a separate dataset while leaving the original source unchanged; the manager checks the new dataset's version and release status before sharing it.

## Assistant Guidance

Distinguish downloading an export from uploading it to TDEI, and distinguish creating a dataset from releasing it. Ask which source, project group, export mode, and target are involved. Do not claim that a new export replaced the source or became public without checking the resulting dataset.

## Related Concepts

- [What happens during export?](export-process.md)
- [What versioning occurs during export?](export-versioning.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
