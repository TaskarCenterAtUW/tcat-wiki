---
title: How are changesets tracked?
slug: changeset-tracking
doc_type: concept
questions:
    - How are changesets tracked?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - review
    - changesets
    - qa-qc
risk_level: low
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
    - assistant/workspaces/concept/changesets.md
    - assistant/workspaces/concept/edit-metadata.md
    - assistant/workspaces/concept/workspace-review-interface.md
tags:
    - Assistant
---

<!-- @format -->

# How are changesets tracked?

## Short Answer

Workspaces tracks edits in changesets or related edit-history records that group uploaded changes and retain available metadata such as author, time, source, comment, and affected features. Exact fields and interface behavior depend on the workspace and current version.

## Significance

Tracking changesets provides an auditable review unit and helps managers understand what changed before export or publication.

## What This Means

Review the changeset list and individual edit details, compare before-and-after values, inspect sources and comments, and record review or follow-up status where the interface supports it.

## What This Does Not Mean

A tracked changeset is not automatically reviewed, correct, authoritative, or published to OpenStreetMap or TDEI. Metadata does not prove the physical condition represented by an edit.

## How To Use This

Use changesets as review units, retain workspace and version context, investigate unclear edits, and complete the deliberate review and export steps required by the workflow.

## Example

A manager opens a changeset containing several sidewalk edits, reviews the affected features and source comments, and requests clarification before approving the workspace for export.

## Assistant Guidance

Ask for the workspace and changeset context. Cite current Workspaces documentation, do not infer approval from tracking alone, and abstain when a specific record cannot be accessed.

## Related Concepts

- [Changesets in Workspaces](changesets.md)
- [What metadata is stored for edits?](edit-metadata.md)
- [What can the Workspaces review interface show?](workspace-review-interface.md)
