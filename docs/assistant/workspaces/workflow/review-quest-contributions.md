---
uid: 85d9b699-b1ce-4438-b4af-e859f36014c7
title: How do I review AVIV ScoutRoute contributions in Workspaces?
slug: review-quest-contributions
doc_type: workflow
questions:
    - How do I review AVIV ScoutRoute contributions in Workspaces?
    - What does it mean for AVIV ScoutRoute to be configured for review?
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
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

AVIV ScoutRoute answers are committed to the workspace through changesets when submitted. If **Auto-flag contributor changesets for review** is enabled in **Workspace Settings → General**, contributor changesets are flagged in the review queue; this flag does not delay submission.

## Significance

Review connects field collection with trusted dataset publication.

## What This Means

Open the workspace's **Review** view and inspect the submitted changeset, its affected features, details, and previous/current values. When automatic flagging is enabled, flagged changesets receive distinct styling in the review view. A user with the workspace **Validator** or **Owner** role can select **Mark as Reviewed** after inspection. Reviewers can add discussion comments or make follow-up edits; follow-up edits are committed through changesets as well.

## What This Does Not Mean

A changeset record does not prove that the observation is correct, and marking a changeset as reviewed does not by itself publish the entire dataset. This changeset-review setting is separate from the Tasking project's **Review Required** option.

## How To Use This

Follow this process to review additions, modifications, notes, and deletions submitted to Workspaces.

## Example

A validator opens a flagged changeset containing field-collected sidewalk changes, compares the prior and current values, marks it as reviewed after the check, and makes a follow-up correction through a new changeset when needed.

## Assistant Guidance

Ask for the workspace, changeset, automatic-flag configuration, reviewer role, and current review status when troubleshooting. Do not imply that an answer waits for review before being saved to the workspace. Cite the [Workspace Settings — General manual](../../../workspaces/user-manual/settings/general.md).

## Related Concepts

- [What can the Workspaces review interface show?](../concept/workspace-review-interface.md)
