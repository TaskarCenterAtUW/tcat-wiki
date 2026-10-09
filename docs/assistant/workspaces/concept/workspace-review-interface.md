---
uid: 5a0750a4-cf38-40e9-8eed-028db0af003c
title: What can the Workspaces review interface show?
slug: workspace-review-interface
doc_type: concept
questions:
    - What can the Workspaces review interface show?
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
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The review interface proves that every workspace edit is correct.
related_pages:
    - workspaces/user-manual/review.md
tags:
    - Assistant
---

<!-- @format -->

# What can the Workspaces review interface show?

## Short Answer

The review interface can show changesets, notes, feedback, editors, sources, authorship, and timestamps for workspace activity. Selecting a changeset adds its ID to the review URL as the `changeset` query parameter.

## Significance

It provides context for reviewing contributions before export.

## What This Means

Use filters and change details to inspect what changed and why. Per-feature records can show before and after values, platform, author, timestamp, comments, and resolution state. A link such as `/workspace/123/review?changeset=456` requests changeset `456` in workspace `123`; resolved changesets are included for this request.

## What This Does Not Mean

Metadata and notes do not prove the truth of an edit. A requested changeset may not exist in the specified workspace, and a map display error may still require retrying.

## How To Use This

Review large changesets carefully and follow up on unclear notes. If a valid changeset ID is absent from the selected workspace, the page reports that it was not found. If the review map cannot display an item, use **Try again**.

## Example

A reviewer opens a note about a surface disruption and inspects the associated map location.

## Assistant Guidance

Ask for the workspace and change context before interpreting a review record.

## Related Concepts

- [What is a workspace extract?](workspace-extract.md)
