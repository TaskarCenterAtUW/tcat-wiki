---
uid: 85d9b699-b1ce-4438-b4af-e859f36014c7
title: How do I review AVIV ScoutRoute contributions in Workspaces?
slug: review-quest-contributions
doc_type: workflow
questions:
    - How do I review AVIV ScoutRoute contributions in Workspaces?
audiences:
    - jurisdiction
    - planner
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - review
    - changesets
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A submitted quest answer is automatically approved or published.
related_pages:
    - assistant/workspaces/concept/workspace-review-interface.md
    - assistant/workspaces/concept/workspace-review-and-publication-gates.md
    - assistant/aviv-scoutroute/concept/quest-contributions.md
tags:
    - Assistant
---

<!-- @format -->

# How do I review AVIV ScoutRoute contributions in Workspaces?

## Short Answer

Open the workspace's **Changeset Review** feature, inspect the submitted changeset, compare previous and current attributes, and make any follow-up edits required by the project's review process. Submitted AVIV ScoutRoute answers are already committed to the workspace; review does not operate on a separate uncommitted holding area.

## Significance

Review connects field collection with trusted dataset publication.

## What This Means

Use metadata, platform, author, timestamps, comments, and changed values to assess the contribution. When the workspace is configured to flag changesets for review, flagged changesets receive distinct styling in the review view. A user with the workspace **validator** or **owner** role can select **Mark as Reviewed** after inspecting a flagged changeset; the changeset then returns to the normal styling. Reviewers can make follow-up edits, and those edits are committed through changesets as well.

## What This Does Not Mean

A changeset record does not prove that the observation is correct, and marking a changeset as reviewed does not by itself publish the entire dataset.

## How To Use This

Follow this process to review additions, modifications, notes, and deletions submitted to Workspaces.

## Example

A validator opens a flagged changeset containing field-collected sidewalk changes, compares the prior and current values, marks it as reviewed after the check, and makes a follow-up correction through a new changeset when needed.

## Assistant Guidance

Ask for the workspace, changeset, review-flag configuration, reviewer role, and current review status when troubleshooting. Do not imply that an answer waits for review before being saved to the workspace.

## Related Concepts

- [What can the Workspaces review interface show?](../concept/workspace-review-interface.md)
