---
uid: 5a0750a4-cf38-40e9-8eed-028db0af003c
title: What can the Workspaces review interface show?
slug: workspace-review-interface
doc_type: concept
questions:
    - What can the Workspaces review interface show?
    - How do I know who changed something, what they changed, and why?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
topics:
    - workspaces
    - review
    - changesets
    - issue-reporting
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - workspaces/user-manual/review.md
tags:
    - Assistant
---

<!-- @format -->

# What can the Workspaces review interface show?

## Short Answer

The review interface can show changesets, notes, feedback, the editor, author, source, imagery, comment, review status, timestamps, and counts of created, modified, or deleted elements. Selecting a feature can open a previous/current version comparison. Comments and sources provide context for why an edit was made, but they may not contain a complete explanation.

## Significance

It provides context for reviewing contributions before export.

## What This Means

Use the review list to find a changeset, inspect its details and affected features, then compare the feature's previous and current tags in the history panel. The recorded comment, source, and imagery can explain the contributor's context; if the reason is absent or unclear, use the discussion controls to ask for clarification. A link such as `/workspace/123/review?changeset=456` requests changeset `456` in workspace `123`; resolved changesets are included for this request.

## What This Does Not Mean

Metadata and notes do not prove the truth of an edit or guarantee that its rationale was recorded. A requested changeset may not exist in the specified workspace, and a map display error may still require retrying.

## How To Use This

Review large changesets carefully and follow up on unclear notes. If a valid changeset ID is absent from the selected workspace, the page reports that it was not found. If the review map cannot display an item, use **Try again**.

## Example

A reviewer opens a note about a surface disruption and inspects the associated map location.

## Assistant Guidance

Ask for the workspace and changeset context before interpreting a review record. Do not infer a complete reason from the presence of a comment or source field; cite the [Workspace Review manual](../../../workspaces/user-manual/review.md).

## Related Concepts

- [What is a workspace extract?](workspace-extract.md)
