---
title: Why should duplicate workspace copies be avoided?
slug: workspace-duplicate-copy-risk
doc_type: concept
questions:
    - Why should duplicate workspace copies be avoided?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - dataset-lineage
    - workspace-management
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Opening a dataset always reuses an existing workspace copy.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Why should duplicate workspace copies be avoided?

## Short Answer

Opening the same dataset version repeatedly can create separate workspace copies. These copies can diverge and confuse review or publication.

## Significance

Coordination prevents edits from being split across competing sandboxes.

## What This Means

Check whether an active workspace already represents the dataset before creating another.

## What This Does Not Mean

A duplicate copy does not change the original dataset automatically.

## How To Use This

Record workspace IDs and agree on the project copy before editing.

## Example

A team reuses one Olympia workspace rather than opening several copies of version 1.9.

## Assistant Guidance

Ask for source version and existing workspace context.

## Related Concepts

- [How can a workspace diverge from its source dataset?](workspace-copy-and-divergence.md)
