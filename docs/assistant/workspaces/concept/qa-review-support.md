---
title: How does Workspaces support QA review?
slug: qa-review-support
doc_type: concept
questions:
    - How does Workspaces support QA review?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - review
    - changesets
    - qa-qc
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
    - assistant/workspaces/concept/workspace-review-interface.md
    - assistant/workspaces/concept/edit-auditing.md
    - assistant/workspaces/concept/manager-edit-review.md
tags:
    - Assistant
---

<!-- @format -->

# How does Workspaces support QA review?

## Short Answer

Workspaces can support QA review by providing reviewable changesets, feature history, source and contributor metadata, workspace roles, notes, and interfaces for inspecting edits before export.

## Significance

QA review can catch geometry, attribute, source, consistency, and workflow issues before a result is released.

## What This Means

Define criteria and scope, inspect edits and sources, compare before and after values, check connectivity and schema, document findings, and resolve or escalate issues.

## What This Does Not Mean

Workspace review does not prove that every physical condition is accurate, accessible, current, or legally compliant.

## How To Use This

Use risk-based review, preserve the audit trail, involve appropriate local or technical reviewers, and complete publication gates deliberately.

## Example

A reviewer checks a set of curb-ramp edits against source imagery and field notes, flags uncertain changes, and approves only the reviewed subset for export.

## Assistant Guidance

Name the workspace, criteria, source, and review scope. Do not imply complete QA from a status label and abstain when records are unavailable.

## Related Concepts

- [What is the review interface?](review-interface.md)
- [How can edits be audited?](edit-auditing.md)
- [How can managers review edits?](manager-edit-review.md)
