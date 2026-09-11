---
uid: 077fab37-97a4-494e-a5c4-0066948ca98d
title: Why does Workspaces exist separately from TDEI?
slug: workspaces-tdei-separation
doc_type: concept
questions:
    - Why does Workspaces exist separately from TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - tdei-ecosystem
    - public-support
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Separating Workspaces from TDEI means the products cannot exchange data.
        - Editing in Workspaces automatically changes TDEI's source record.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/tdei-ecosystem-fit.md
    - assistant/workspaces/concept/workspace-tdei-isolation.md
tags:
    - Assistant
---

<!-- @format -->

# Why does Workspaces exist separately from TDEI?

## Short Answer

Workspaces exists separately from TDEI so collaborative editing, role-based review, sandboxing, and source-copy management can occur before downstream TDEI processing or publication. The systems can still exchange data through documented workflows.

## Significance

Separation creates a deliberate boundary between working changes and managed releases.

## What This Means

Use Workspaces for editing and review, then use the relevant TDEI handoff when changes are ready.

## What This Does Not Mean

Separation does not mean that the systems are unrelated or that every handoff is automatic.

## How To Use This

Ask which stage of the data lifecycle the user is trying to complete.

## Example

A jurisdiction maintains a working copy in Workspaces and submits a reviewed export to a TDEI service as a separate release step.

## Assistant Guidance

Cite the specific handoff workflow and abstain if the source or destination is not identified.

## Related Concepts

 - [How does Workspaces fit into TDEI?](tdei-ecosystem-fit.md)
 - [Does editing a workspace change the TDEI dataset?](workspace-tdei-isolation.md)
