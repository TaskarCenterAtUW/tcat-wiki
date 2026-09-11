---
uid: 299c33bf-9f17-4b43-a5e9-91cf8b24ff82
title: How do I create a workspace?
slug: create-workspace
doc_type: workflow
questions:
    - How do I create a workspace?
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
        - Every workspace creation path has the same steps and metadata.
        - Creating a workspace makes its data publicly available.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-creation-methods.md
    - assistant/workspaces/concept/workspace-creation-mechanics.md
tags:
    - Assistant
---

<!-- @format -->

# How do I create a workspace?

## Short Answer

Choose the appropriate creation path, provide a title and project group, supply the source dataset or file, submit the request, and verify initialization in the dashboard. Record source, version, environment, and workspace ID.

## Significance

A consistent creation preflight protects lineage and prevents teams from editing the wrong source or project.

## What This Means

Check permissions, source format, dataset scope, title, project group, and current environment before submitting.

## What This Does Not Mean

Creation does not guarantee successful conversion, current data, access for every collaborator, or publication.

## How To Use This

Use the TDEI or Workspaces workflow matching the source. Preserve any conversion errors and do not retry blindly if the source or destination is uncertain.

## Example

A team converts a prepared dataset, creates the workspace, waits for processing, and confirms the new workspace before inviting editors.

## Assistant Guidance

Cite the relevant creation method and abstain when the source or environment is unspecified.

## Related Concepts

 - [What are the workspace creation methods?](../concept/workspace-creation-methods.md)
 - [What happens during creation?](../concept/workspace-creation-mechanics.md)
