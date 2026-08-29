---
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

# Does export overwrite the original dataset?

## Short Answer

Export should be treated as a separate publication or dataset-creation step, not assumed to overwrite the original TDEI dataset. The exact behavior depends on the current Workspaces and TDEI workflow and target.

## Significance

Knowing overwrite behavior protects source data and helps users preserve lineage and reversibility.

## What This Means

Confirm the target dataset, export mode, permissions, resulting identifier, validation status, and publication step in the current documentation before proceeding.

## What This Does Not Mean

An export is not automatically a destructive replacement, and the absence of overwrite does not mean that the result is published or reviewed.

## How To Use This

Use a reviewed workspace, record source and target identifiers, check the confirmation or job result, and verify where the exported data is available.

## Example

A manager exports reviewed edits and records a new dataset or release identifier while retaining the original source for comparison.

## Assistant Guidance

Do not promise overwrite behavior without current evidence. Ask for the target and environment, cite the workflow, and abstain when the operation is unclear.

## Related Concepts

- [What happens during export?](export-process.md)
- [What versioning occurs during export?](export-versioning.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
