---
uid: 49a58c6e-5226-47f2-958b-88e53fe57b8e
title: When should edits be exported back to TDEI?
slug: export-timing
doc_type: concept
questions:
    - When should edits be exported back to TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - sandbox-governance
    - dataset-lineage
    - publication-workflow
risk_level: high
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
    - assistant/workspaces/concept/pre-export-review.md
    - assistant/workspaces/concept/export-process.md
    - assistant/workspaces/concept/workspace-dataset-divergence.md
tags:
    - Assistant
---

<!-- @format -->

# When should edits be exported back to TDEI?

## Short Answer

Edits should be exported back to TDEI when the workspace work has met the project's review, quality, governance, and publication criteria and the responsible manager has confirmed the target and timing.

## Significance

Exporting too early can publish unreviewed or conflicting data; waiting may leave a workspace or local dataset divergent from current needs.

## What This Means

Check changesets, unresolved issues, source versions, validation results, permissions, intended use, and whether the target release should be created now or retained privately.

## What This Does Not Mean

There is no universal export schedule, and a complete review does not guarantee that export or publication will succeed.

## How To Use This

Keep edits private while evidence, ownership, conflicts, or acceptance criteria remain unresolved. Record the decision and resulting release when export occurs.

## Example

A jurisdiction waits to export until volunteer edits are reviewed and local conflicts are resolved, then records the target TDEI release for downstream users.

## Assistant Guidance

Do not prescribe timing without the project's criteria and current workflow. Ask for the workspace, review status, target use, and release context.

## Related Concepts

- [How should review happen before export?](../workflow/pre-export-review.md)
- [What happens during export?](export-process.md)
- [How does a workspace diverge from its source dataset?](workspace-dataset-divergence.md)
