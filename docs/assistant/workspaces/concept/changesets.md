---
uid: b8059826-25f7-4427-ae3f-fba72215ea92
title: Changesets (Workspaces)
slug: changesets
doc_type: concept
questions:
    - What are changesets in Workspaces?
    - What is a changeset, and how are changesets automatically recorded when I edit?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - changesets
    - review
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
    - assistant/workspaces/how-are-changesets-tracked.md
    - assistant/workspaces/how-can-edits-be-audited.md
    - assistant/workspaces/what-metadata-is-stored-for-edits.md
    - assistant/workspaces/concept/tasking-projects-and-tasks.md
    - assistant/workspaces/concept/workspaces-api.md
    - assistant/workspaces/how-can-users-inspect-edit-history.md
tags:
    - Assistant
---

<!-- @format -->

# Changesets (Workspaces)

## Short Answer

In Workspaces, a **changeset** is a group of edits uploaded together and recorded for review and history. When edits are submitted to a workspace, Workspaces records them in changesets; AVIV ScoutRoute quest answers are committed to the workspace through a changeset when submitted. Available details can include the editor, author, timestamps, comment, source, imagery, and affected elements.

## Significance

Changesets provide the audit trail for every modification made inside a Workspaces sandbox. Changesets answer who changed what, when, and why.

## What This Means

- A changeset groups edits uploaded together; the available documentation does not establish that every editor or submission always creates exactly one changeset.
- Changesets can include geometry or attribute changes affecting one or more features.
- The review interface can show the editor, author, comment, source, imagery, review status, timestamps, and counts of created, modified, or deleted elements.
- Reviewers can inspect the changeset, discuss it, and compare previous and current feature versions. Workspace Owners and Validators can mark changesets as reviewed.
- The API specification documents a changeset augmented-diff `GET` route whose response contains actions with a type and `new` and `old` elements. It also documents a separate changeset `PUT` resolve operation. The specification does not define review states or the business effect of resolving a changeset.

## What This Does Not Mean

- Workspaces changesets are **not** published to the public OpenStreetMap database; they remain private to the workspace sandbox.
- A changeset does **not** automatically publish or export data to TDEI; the workspace export workflow is separate.
- The presence of a changeset does **not** by itself mean the edits have been reviewed or approved. AVIV answers are committed to the workspace before review.
- Changeset comments are freeform and do **not** constitute a legal attestation of data accuracy; they are editorial notes, not sworn statements.

## How To Use This

**Planners and jurisdiction staff**: Use changesets to inspect workspace edits against your agency's data standards. Browse the review interface to confirm who made each change and what imagery or source was recorded.

**Advocates and community mappers**: When uploading your edits, always write a clear changeset comment describing what you changed and why. This helps reviewers — including jurisdiction partners — understand your contributions.

**Reviewers and workspace managers**: Treat each changeset as a review unit. Inspect the affected features and available evidence, use discussion to request clarification, and mark a changeset as reviewed only when your role permits and your project's review criteria are met.

## Example

A city transportation planner opens the review interface for a Workspaces sandbox and sees a changeset with a comment about added curb ramps. She inspects its affected features, source and imagery details, compares feature history, and uses discussion to ask about an unclear edit. An Owner or Validator can mark a flagged changeset as reviewed after applying the project's criteria.

## Assistant Guidance

Cite this page and the current Workspaces review manual when a user asks how edits are recorded. Do not promise one changeset per upload or claim that a changeset is accepted automatically. If a user asks about a specific changeset, abstain unless you can access the relevant workspace review record. Do not claim that changesets are visible in public OpenStreetMap or that they automatically sync there or to TDEI.

## Related Concepts

- [How are changesets tracked?](changeset-tracking.md)
- [How can edits be audited?](edit-auditing.md)
- [What metadata is stored for edits?](edit-metadata.md)
- [How can users inspect edit history?](edit-history.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [Workspace Review manual](../../../workspaces/user-manual/review.md)
