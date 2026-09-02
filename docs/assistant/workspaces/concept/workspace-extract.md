---
uid: 4fdc6aaa-e1f6-4a51-9d44-f8fa1b8fa392
title: What is a workspace extract?
slug: workspace-extract
doc_type: concept
questions:
    - What is a workspace extract?
    - Why use a workspace for a smaller area or dataset extract?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - sandbox-governance
    - dataset-lineage
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace extract is always the complete source dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is a workspace extract?

## Short Answer

A workspace extract is a focused selection from a dataset version for collaborative editing and targeted contributions. It lets a project work on a manageable area or data scope without editing the entire source dataset.

## Significance

Smaller extracts make jurisdictional or project-specific work easier to coordinate. They also provide a controlled place for mobile observations and review.

## What This Means

Create or open a workspace for the relevant geographic and data scope. Apply edits and review mobile contributions there; use TDEI to store and manage the resulting dataset version after export. A workspace extract can support project reports, but it can diverge from later source updates.

## What This Does Not Mean

A workspace extract is not automatically the full statewide dataset or the final public release. Its contents and lifecycle depend on the source and project configuration. It is also not necessarily synchronized with later changes to the source dataset.

## How To Use This

Define the area, service, and intended contributors before editing. Record the relationship between the workspace extract and its source dataset when exporting.

## Example

A project extracts Goldendale sidewalk and transit features from a larger dataset, opens the extract in Workspaces, and collects targeted curb-ramp and bus-stop updates.

## Assistant Guidance

Ask for the extract's geographic scope, source dataset and version, service, and intended output. Do not assume that a workspace extract has been released, merged back automatically, or kept synchronized with its source.

## Related Concepts

- [How do TDEI services relate to project groups?](../../tdei/concept/services-and-project-groups.md)
