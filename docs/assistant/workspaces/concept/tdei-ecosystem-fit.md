---
uid: 9dd8cfe2-9912-4127-882f-f31c0accfc61
title: How does Workspaces fit into the TDEI ecosystem?
slug: tdei-ecosystem-fit
doc_type: concept
questions:
    - How does Workspaces fit into the TDEI ecosystem?
    - What is Workspaces, and how does it fit into the TDEI ecosystem?
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
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspaces-tdei-portal-relationship.md
    - assistant/workspaces/concept/workspaces-os-connect-relationship.md
tags:
    - Assistant
---

<!-- @format -->

# How does Workspaces fit into the TDEI ecosystem?

## Short Answer

Workspaces is a collaborative editing and review environment in the TDEI ecosystem. TDEI manages datasets and provides dataset-level processing and release services; Workspaces provides an isolated place to edit selected data before an explicit export to TDEI.

## Significance

The separation makes editing, review, lineage, and publication checkpoints explicit while allowing related services to exchange data through documented workflows.

## What This Means

Use Workspaces to collaborate on feature-level edits and review them. Use TDEI to manage datasets, run supported dataset-level jobs, and manage releases. Treat creating a workspace, editing it, exporting it, and releasing a dataset as separate stages.

## What This Does Not Mean

Workspaces is not the entire TDEI ecosystem, and a workspace edit is not automatically a published TDEI release.

## How To Use This

Use the product-specific workflow and confirm source, destination, permissions, and release state.

## Example

A team creates a workspace from a TDEI dataset, reviews feature edits there, and separately exports the result to TDEI before any release or downstream use.

## Assistant Guidance

Cite the relevant Workspaces or TDEI page and abstain when the intended ecosystem stage is unclear.

## Related Concepts

- [What is the relationship between Workspaces and the TDEI portal?](workspaces-tdei-portal-relationship.md)
- [What is the relationship between Workspaces and OS-CONNECT?](workspaces-os-connect-relationship.md)
