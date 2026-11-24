---
uid: c17f4997-b289-43b3-a0ea-50329ed41f50
title: Review workspace edits
slug: review-workspace-edits
doc_type: workflow
questions:
    - How do I review workspace edits?
    - How does review work, and when can reviewers provide feedback on changesets?
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
    - qa-qc
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/review-interface.md
    - assistant/workspaces/workflow/pre-export-review.md
tags:
    - Assistant
---

<!-- @format -->

# Review workspace edits

## Short Answer

Review happens after edits have been committed to the workspace. Open the workspace's **Review** view, inspect the relevant changeset and feature history, and use its discussion to provide feedback or request clarification. Workspace Owners and Validators can mark flagged changesets as reviewed.

## Significance

Review is the control point that separates collaborative editing from a trusted downstream result.

## What This Means

1. Open the workspace from the Dashboard and select **Review** from its actions.
2. Choose whether to show **Changesets**, **Feedback**, or **Notes**; use **Needs Review Only** or **Show Resolved** when appropriate.
3. Select a changeset and inspect its map location, details, editor, source, imagery, comment, affected-element counts, and review status.
4. Select a feature to compare its previous and current versions. Use the discussion control to add a comment or request clarification once the changeset is visible.
5. If you are a workspace Owner or Validator and have completed the review, select **Mark as Reviewed** for a flagged changeset.

## What This Does Not Mean

Review does not delay the original edit submission, guarantee complete or legally compliant data, or publish the workspace to TDEI. A comment or discussion entry is feedback, not by itself a review decision.

## How To Use This

Use project instructions and available evidence to review edits. Escalate disputed or high-impact changes to the responsible steward; ask a workspace Owner or Validator to perform the review action if your role does not allow it.

## Example

A reviewer opens a committed changeset, compares a curb-ramp feature's previous and current tags, and posts a discussion comment requesting evidence. An authorized Owner or Validator later marks the changeset as reviewed after the project criteria are met.

## Assistant Guidance

Cite the [Workspace Review manual](../../../workspaces/user-manual/review.md) and current role guidance. Distinguish discussion feedback from **Mark as Reviewed**, and abstain when the workspace or review configuration is unknown.

## Related Concepts

- [What is the review interface?](../concept/review-interface.md)
- [How should review happen before export?](pre-export-review.md)
- [How do I review AVIV ScoutRoute contributions in Workspaces?](review-quest-contributions.md)
