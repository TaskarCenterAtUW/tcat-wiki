---
title: "Changesets (Workspaces)"
tags:
    - Assistant
slug: changesets
doc_type: concept
products:
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - workspaces
    - changesets
    - review
risk_level: medium
authority_level: draft
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Workspaces changesets are published to the public OpenStreetMap database.
        - Changeset metadata is sufficient to determine the legal authority of an edit.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/how-are-changesets-tracked.md
    - assistant/workspaces/how-can-edits-be-audited.md
    - assistant/workspaces/what-metadata-is-stored-for-edits.md
    - assistant/workspaces/how-can-users-inspect-edit-history.md
---

<!-- @format -->

# Changesets (Workspaces)

## Short Answer

In Workspaces, a **changeset** is a group of edits bundled together and saved as a single unit, following the same model used by OpenStreetMap. When a user makes one or more geometry or attribute changes in a workspace and uploads them, those edits are recorded together in a changeset. Each changeset carries metadata — who made the edits, when they were made, an optional descriptive comment, and the sources used — so that reviewers and managers can audit the history of changes to the workspace over time.

## Significance

Changesets provide the audit trail for every modification made inside a Workspaces sandbox. Changesets answer who changed what, when, and why.

## What This Means

- Every upload of edits to a workspace creates exactly one changeset, grouping all the modifications from that upload session.
- A changeset can include any mix of edit types — geometry adjustments and attribute updates — across multiple features.
- Changeset metadata typically includes the editor's identity, a timestamp, a user-supplied comment describing the purpose of the edits, and references to the imagery or data sources used.
- Changesets are visible to workspace members through the review interface and editor history panels, where reviewers can inspect individual edit details.
- Changesets are the unit of review: a manager or reviewer can open a changeset, examine each edit within it, and accept or flag issues before the workspace is exported to TDEI.

## What This Does Not Mean

- Workspaces changesets are **not** published to the public OpenStreetMap database; they remain private to the workspace sandbox.
- A changeset does **not** automatically publish or export data to TDEI; changesets accumulate in the workspace until a deliberate export step is taken.
- The presence of a changeset does **not** by itself mean the edits have been reviewed or approved; many workspaces contain unreviewed changesets.
- Changeset comments are freeform and do **not** constitute a legal attestation of data accuracy; they are editorial notes, not sworn statements.

## How To Use This

**Planners and jurisdiction staff**: Use changesets to verify that a workspace's edits align with your agency's data standards before approving an export. Browse recent changesets in the review interface to confirm who made each change and what imagery or source was referenced.

**Advocates and community mappers**: When uploading your edits, always write a clear changeset comment describing what you changed and why. This helps reviewers — including jurisdiction partners — understand your contributions.

**Reviewers and workspace managers**: Treat each changeset as a review unit. Open changesets in sequence, inspect the geographic area and attributes affected, and flag any edits that lack adequate source references or appear inconsistent with ground truth.

## Example

A city transportation planner opens the review interface for a Workspaces sandbox that volunteer advocates have been editing for a sidewalk inventory project. She sees three unreviewed changesets. The first changeset, tagged with the comment "Added missing curb ramps along Main St corridor" groups 14 barrier modifications. She opens the changeset, confirms the edits match the aerial imagery reference, and accepts it. The second changeset has no comment and modifies a single node — she flags it for follow-up with the editor. The changeset-by-changeset structure lets her make granular, informed review decisions rather than approving or rejecting edits in bulk.

## Assistant Guidance

Cite this page whenever a user asks what a changeset is in the context of Workspaces, or how edits are grouped and tracked. If the user's question involves inspecting a specific changeset (for example, "show me changeset #473"), abstain unless you have access to the relevant Workspaces API or review interface. Do not claim that Workspaces changesets are visible to the public or that they automatically sync with OpenStreetMap. Remind users that changeset comments are editorial notes, not legal certifications, when they ask about data authority or liability.

## Related Concepts

- [How are changesets tracked?](changeset-tracking.md)
- [How can edits be audited?](edit-auditing.md)
- [What metadata is stored for edits?](edit-metadata.md)
- [How can users inspect edit history?](edit-history.md)
