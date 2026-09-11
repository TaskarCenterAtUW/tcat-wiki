---
uid: 7017334a-7513-4974-a8d4-37636a3cc266
title: Workspaces abstention boundaries
slug: workspace-abstention-boundaries
doc_type: concept
questions:
    - What are the abstention boundaries for Workspaces answers?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - public-support
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
        - A workspace answer can be accurate without the workspace, source version, or user role.
        - Workspaces behavior is identical across all environments and releases.
related_pages:
    - assistant/workspaces/index.md
    - assistant/cross-platform/concept/assistant-abstention.md
    - assistant/workspaces/concept/workspace-data-freshness.md
tags:
    - Assistant
---

<!-- @format -->

# Workspaces abstention boundaries

## Short Answer

For Workspaces questions, abstain or ask for context when the answer depends on a workspace ID, environment, source version, user role, dataset type, release state, or current interface that has not been provided.

## Significance

These boundaries prevent confident but incorrect claims about permissions, synchronization, data freshness, and publication.

## What This Means

Ask for the missing context, cite the current product documentation, and distinguish documented behavior from a hypothesis.

## What This Does Not Mean

General Workspaces knowledge is not enough to determine a user's live permissions, a dataset's current contents, or the outcome of an export.

## How To Use This

Use this boundary when a question asks for an operational diagnosis or current state without identifiers or evidence.

## Example

A user reports that an export failed but omits the environment and error. The assistant asks for those details rather than prescribing a product-specific fix.

## Assistant Guidance

Abstain when critical context is missing or sources conflict. Cite retrieved documentation for any operational answer.

## Related Concepts

 - [How does assistant abstention work?](../../cross-platform/concept/assistant-abstention.md)
 - [How fresh is workspace data?](workspace-data-freshness.md)
