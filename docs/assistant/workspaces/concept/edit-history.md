---
title: How can users inspect edit history?
slug: edit-history
doc_type: concept
questions:
    - How can users inspect edit history?
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
    - assistant/workspaces/concept/edit-auditing.md
    - assistant/workspaces/concept/workspace-review-interface.md
tags:
    - Assistant
---

<!-- @format -->

# How can users inspect edit history?

## Short Answer

Users can inspect edit history through the workspace's current changeset, feature-history, or review interfaces when they have the required access. History may show what changed, who contributed it, when it changed, sources, comments, and review status.

## Significance

History helps users understand the sequence of edits and identify changes that need review or clarification.

## What This Means

Select the workspace and feature or changeset, inspect before-and-after values and metadata, compare source and version information, and record questions without overwriting history.

## What This Does Not Mean

History does not prove that an edit is correct, current, or approved. Visibility of a record does not imply that a user can modify or export it.

## How To Use This

Use the current review documentation, preserve identifiers and timestamps, and ask the workspace manager when records are missing or inaccessible.

## Example

A reviewer opens a sidewalk's history, sees a geometry change followed by an attribute update, and checks both changesets before approving the feature.

## Assistant Guidance

Ask for the workspace, feature, and access context. Do not invent interface controls or infer physical truth from history alone.

## Related Concepts

- [How are changesets tracked?](changeset-tracking.md)
- [How can edits be audited?](edit-auditing.md)
- [What can the Workspaces review interface show?](workspace-review-interface.md)
