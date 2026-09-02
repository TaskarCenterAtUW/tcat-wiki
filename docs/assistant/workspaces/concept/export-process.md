---
uid: 691f8f6e-c407-44c7-aea2-79c56537de65
title: What happens during export?
slug: export-process
doc_type: concept
questions:
    - What happens during export?
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
    - assistant/workspaces/concept/export-overwrite-behavior.md
    - assistant/workspaces/concept/export-versioning.md
    - assistant/workspaces/concept/edit-upload-to-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# What happens during export?

## Short Answer

During export, reviewed workspace data are prepared and transferred or made available through the documented TDEI workflow. The process may include validation, job processing, creation of a dataset or release, and status or error reporting.

## Significance

Export is the boundary between private editing and a possible shared or released dataset. Understanding each step helps prevent accidental publication and lost lineage.

## What This Means

Review edits, confirm the source and target, start the documented operation, monitor its status, inspect validation results, and record resulting identifiers and errors.

## What This Does Not Mean

Starting export does not guarantee success, overwrite behavior, publication, or that every edit passes validation.

## How To Use This

Use current environment-specific instructions, retain the workspace and source release, resolve failures before retrying, and verify the resulting dataset separately.

## Example

A manager exports a reviewed workspace, monitors the processing result, records the new TDEI identifier, and confirms which release contains the changes.

## Assistant Guidance

Do not invent interface steps or job states. Ask for the environment and target, cite current documentation, and abstain when export behavior is not verified.

## Related Concepts

- [Does export overwrite the original dataset?](export-overwrite-behavior.md)
- [What versioning occurs during export?](export-versioning.md)
- [How are edits uploaded back to TDEI?](edit-upload-to-tdei.md)
