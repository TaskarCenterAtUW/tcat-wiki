---
title: What metadata is stored for edits?
slug: edit-metadata
doc_type: concept
questions:
    - What metadata is stored for edits?
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
    - assistant/workspaces/concept/changeset-tracking.md
    - assistant/workspaces/concept/change-authorship.md
    - assistant/workspaces/concept/workspace-review-interface.md
tags:
    - Assistant
---

<!-- @format -->

# What metadata is stored for edits?

## Short Answer

Edit metadata may include the contributor, editor or platform, timestamp, changeset, comment, source, affected feature, and review status. The exact fields depend on the workspace, editor, and current product version.

## Significance

Metadata helps reviewers reconstruct what changed, who or what contributed it, when it was made, and what evidence was cited.

## What This Means

Inspect the edit or changeset record, preserve identifiers and timestamps, review source and comments, and compare before-and-after geometry or attributes where available.

## What This Does Not Mean

Metadata does not prove that an edit is accurate, current, accessible, approved, or legally authoritative. Missing metadata does not automatically make an edit false.

## How To Use This

Use the current review interface and workspace documentation, protect personal information, and ask the manager about records that are incomplete or ambiguous.

## Example

A reviewer records the contributor, editor, source imagery date, changeset comment, and affected feature before deciding whether an attribute edit is ready for further review.

## Assistant Guidance

Name only fields documented for the relevant version. Do not infer facts from absent metadata, and abstain when a specific edit record cannot be accessed.

## Related Concepts

- [How are changesets tracked?](changeset-tracking.md)
- [How can users identify who made a change?](change-authorship.md)
- [What can the Workspaces review interface show?](workspace-review-interface.md)
