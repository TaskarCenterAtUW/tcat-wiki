---
uid: 34430d5c-010a-42e3-b3a7-f67b5c5462a5
title: What are the different workspace creation methods?
slug: workspace-creation-methods
doc_type: concept
questions:
    - What are the different workspace creation methods?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - onboarding
    - project-groups
    - workspace-management
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
        - Every workspace creation method produces the same source and metadata.
        - Creating a workspace automatically publishes its data.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/workflow/create-workspace.md
    - assistant/workspaces/workflow/create-workspace-from-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# What are the different workspace creation methods?

## Short Answer

Workspaces can be created from a TDEI dataset or an uploaded file, and the appropriate method depends on the source, format, project group, and intended workflow. Each method creates a workspace that must still be reviewed and managed.

## Significance

Choosing the method affects lineage, conversion, scope, and the steps required before editing.

## What This Means

Choose a TDEI source when using a managed dataset and a file workflow when starting from a prepared local package. Record the source and creation context.

## What This Does Not Mean

The creation method does not guarantee identical metadata, freshness, permissions, or publication results.

## How To Use This

Ask where the data currently lives, its format, and the desired destination before recommending a method.

## Example

A team converts an OSM extract to OpenSidewalks format and creates a workspace from file, while another team creates a workspace from a selected TDEI dataset.

## Assistant Guidance

Cite the current creation workflow and abstain if the source format or environment is unknown.

## Related Concepts

 - [How do I create a workspace?](../workflow/create-workspace.md)
 - [How do I create a workspace from TDEI?](../workflow/create-workspace-from-tdei.md)
