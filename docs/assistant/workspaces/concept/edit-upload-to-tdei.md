---
title: How are edits uploaded back to TDEI?
slug: edit-upload-to-tdei
doc_type: concept
questions:
    - How are edits uploaded back to TDEI?
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
    - assistant/workspaces/concept/workspace-editing-boundary.md
tags:
    - Assistant
---

<!-- @format -->

# How are edits uploaded back to TDEI?

## Short Answer

Edits are uploaded back to TDEI through the documented Workspaces export or publication workflow after the workspace changes have been reviewed and the responsible user initiates the operation. Exact steps and permissions depend on the current product configuration.

## Significance

Separating editing, review, export, and release protects the source dataset and makes the resulting version traceable.

## What This Means

Complete review gates, confirm the target dataset and release context, export using the current workflow, check validation or job status, and preserve source, workspace, and resulting identifiers.

## What This Does Not Mean

Uploading or exporting does not necessarily overwrite the original dataset, publish immediately, or update OpenStreetMap, AccessMap, or other products automatically.

## How To Use This

Use the current Workspaces and TDEI instructions, confirm permissions and target, and do not begin export until unresolved edits and conflicts are addressed.

## Example

A manager reviews workspace changesets, starts the documented export, records the resulting TDEI dataset or release information, and checks whether another publication step is required.

## Assistant Guidance

Do not invent buttons, job states, overwrite behavior, or permissions. Ask for the workspace and target release, cite current documentation, and abstain when the workflow is not verified.

## Related Concepts

- [What happens during export?](export-process.md)
- [What versioning occurs during export?](export-versioning.md)
- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
