---
uid: 2101da94-061a-4cfb-a3bd-022da2d0914a
title: Workspaces data freshness
slug: workspace-data-freshness
doc_type: concept
questions:
    - How fresh is data in Workspaces?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - data-freshness
    - dataset-lineage
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace automatically receives later source-dataset updates.
        - The workspace's creation date proves that its features are current.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-copy-and-divergence.md
    - assistant/workspaces/concept/workspace-abstention-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# Workspaces data freshness

## Short Answer

Workspace data is as current as its source snapshot and subsequent edits or imports; later source changes do not automatically make an existing workspace current. Freshness must be evaluated against the source release and update history.

## Significance

Stale data can affect routing, accessibility analysis, review, and publication decisions.

## What This Means

Record source and version dates, compare with newer releases, and validate important features locally before using the workspace for current-condition decisions.

## What This Does Not Mean

A workspace is not a live synchronized view and its title or creation date is not a freshness guarantee.

## How To Use This

Ask for the workspace source, version, creation date, and latest edit or import when freshness matters.

## Example

A reviewer discovers that a newer TDEI release exists, compares it with the workspace, and decides whether to refresh or re-review before export.

## Assistant Guidance

Cite source and release records. Abstain from current-condition claims when freshness evidence is missing.

## Related Concepts

 - [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
 - [Workspaces abstention boundaries](workspace-abstention-boundaries.md)
