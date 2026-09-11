---
uid: cb452c73-4317-40c1-82d2-5f2fe365b58f
title: How should review happen before export?
slug: pre-export-review
doc_type: workflow
questions:
    - How should review happen before export?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - export
    - publication-workflow
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
        - Passing a pre-export review proves that the dataset is legally compliant.
        - A reviewer must approve every edit without checking its context.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-review-and-publication-gates.md
    - assistant/workspaces/workflow/review-workspace-edits.md
tags:
    - Assistant
---

<!-- @format -->

# How should review happen before export?

## Short Answer

Before export, confirm the source and scope, inspect changes and metadata, check unresolved issues and conflicts, verify attribution and target configuration, and obtain the approval required by the responsible data steward.

## Significance

Pre-export review reduces accidental publication of unsupported, duplicate, or out-of-scope edits.

## What This Means

Use the review interface, compare important edits with source or local evidence, record decisions, and preserve the workspace lineage and release context.

## What This Does Not Mean

Review is not a guarantee of completeness, accessibility, legal compliance, or absence of undetected errors.

## How To Use This

Match the review depth to the dataset risk, edit type, and publication responsibility. Escalate disputed or high-impact changes.

## Example

A reviewer checks a new crossing, confirms its tags and evidence, resolves a conflict, and records approval before export.

## Assistant Guidance

Cite the review and publication guidance. Abstain when the reviewer role or destination's approval rules are unknown.

## Related Concepts

 - [How do I review workspace edits?](review-workspace-edits.md)
 - [What are workspace review and publication gates?](../concept/workspace-review-and-publication-gates.md)
