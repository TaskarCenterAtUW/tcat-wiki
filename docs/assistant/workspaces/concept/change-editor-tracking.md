---
uid: bd8adcfc-0f2f-4c7c-be33-e3613f350e4d
title: What editor created a change?
slug: change-editor-tracking
doc_type: concept
questions:
    - What editor created a change?
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
    - assistant/workspaces/concept/change-authorship.md
    - assistant/workspaces/concept/changeset-tracking.md
    - assistant/workspaces/concept/edit-metadata.md
tags:
    - Assistant
---

<!-- @format -->

# What editor created a change?

## Short Answer

The editor that created a change may be recorded in changeset or edit metadata when the workspace and source editor provide that information. Verify the current review interface and data fields rather than assuming every edit contains the same attribution.

## Significance

Editor provenance helps reviewers understand the workflow, available controls, and context in which a change was made.

## What This Means

Inspect the change record for its editor or platform field, timestamp, author, source, and affected features. Preserve the record when exporting or auditing changes.

## What This Does Not Mean

Editor metadata does not prove the edit is correct or that one editor is appropriate for every task. Missing metadata does not by itself prove that an edit is invalid.

## How To Use This

Use the exact workspace record and version, ask the manager when provenance is unclear, and review the edit itself rather than relying only on the editor label.

## Example

A reviewer sees that one changeset came from a mobile collection app and another from a desktop editor, then checks both against their stated source and the workspace review rules.

## Assistant Guidance

Do not infer editor provenance from visual style or a user's identity. Cite current Workspaces guidance and abstain when the record does not expose the editor.

## Related Concepts

- [How can users identify who made a change?](change-authorship.md)
- [How are changesets tracked?](changeset-tracking.md)
- [What metadata is stored for edits?](edit-metadata.md)
