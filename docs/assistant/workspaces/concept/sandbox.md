---
uid: 51b46963-5a2c-4b1d-9e8d-21e76f34f5c2
title: What does sandbox mean in Workspaces?
slug: sandbox
doc_type: concept
questions:
    - What does sandbox mean in Workspaces?
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
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace sandbox is automatically synchronized with its source.
        - Sandbox edits are automatically public or authoritative.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/concept/workspace-public-vs-private-data.md
tags:
    - Assistant
---

<!-- @format -->

# What does sandbox mean in Workspaces?

## Short Answer

In Workspaces, a sandbox is a controlled editing environment where a team can inspect and improve a dataset before an authorized export or publication decision.

## Significance

Sandboxing lets contributors work without treating every exploratory edit as an immediate public release. It also makes review and lineage important.

## What This Means

Use a sandbox to bound editing, assign roles, track source and changes, and establish review gates before release.

## What This Does Not Mean

A sandbox is not automatically private from every user, synchronized with its source, or suitable for unreviewed public claims.

## How To Use This

Confirm visibility, membership, source version, and export destination for the specific workspace.

## Example

A team tests a proposed sidewalk correction in a workspace, reviews it with local evidence, and exports only the approved result.

## Assistant Guidance

Cite workspace governance and abstain when visibility or publication state is unclear.

## Related Concepts

 - [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
 - [How does public and private data work?](workspace-public-vs-private-data.md)
