---
uid: e87309e2-9ce5-40ac-944d-5d2212d312da
title: Can multiple workspaces exist from the same dataset?
slug: multiple-workspaces-per-dataset
doc_type: concept
questions:
    - Can multiple workspaces exist from the same dataset?
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
risk_level: medium
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
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/concept/parallel-workspace-editing.md
    - assistant/workspaces/concept/dataset-lineage-in-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# Can multiple workspaces exist from the same dataset?

## Short Answer

Multiple workspaces can represent separate working copies or projects derived from the same source dataset when the current Workspaces workflow permits it.

## Significance

Separate workspaces can support different jurisdictions, teams, experiments, or review scopes while preserving isolated edits.

## What This Means

Record the source dataset and release, workspace identifiers, purpose, owners, differences, and intended merge or export path. Coordinate duplicate work before combining results.

## What This Does Not Mean

Separate workspaces do not synchronize automatically, and edits in one workspace do not update another or the source dataset by themselves.

## How To Use This

Use separate workspaces when scope or governance requires isolation, then reconcile and review differences before creating a shared release.

## Example

Two groups create workspaces from the same release for separate areas. A manager tracks both lineages and resolves overlap before export.

## Assistant Guidance

Ask for the source release, workspace IDs, and intended relationship. Do not promise merging or synchronization without current documentation.

## Related Concepts

- [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
- [What happens if two groups edit separate copies?](parallel-workspace-editing.md)
- [What is dataset lineage in TDEI?](dataset-lineage-in-tdei.md)
