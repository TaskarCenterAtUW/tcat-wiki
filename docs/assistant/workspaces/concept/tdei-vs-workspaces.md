---
uid: 70f4fa39-5c72-4751-9eed-7c0ff2cc236b
title: TDEI vs Workspaces
slug: tdei-vs-workspaces
doc_type: concept
questions:
    - How do TDEI and Workspaces differ?
    - What is the difference between TDEI and Workspaces?
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
risk_level: medium
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
    - assistant/workspaces/concept/tdei-ecosystem-fit.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
tags:
    - Assistant
---

<!-- @format -->

# TDEI vs Workspaces

## Short Answer

TDEI is the broader data ecosystem for managing datasets, services, processing, and releases. Workspaces is a collaborative editing environment for working on selected data in a separate workspace before an explicit export to TDEI.

## Significance

The distinction helps users choose the right interface and understand why editing and release are separate operations.

## What This Means

| Task                                                                            | Use                                                                           |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Find or manage datasets, run a supported dataset-level job, or manage a release | TDEI                                                                          |
| Edit individual features, coordinate contributors, or review workspace changes  | Workspaces                                                                    |
| Make reviewed workspace data available as a TDEI dataset                        | Follow the documented Workspaces export workflow, then verify the TDEI result |

## What This Does Not Mean

The two names do not describe identical permissions, interfaces, or publication outcomes.

## How To Use This

Ask whether the task is editing, processing, dataset management, or viewing a release.

## Example

A planner opens a TDEI dataset in Workspaces, edits and reviews individual features in the separate workspace, then uses the documented export path to upload the result as a new TDEI dataset.

## Assistant Guidance

Cite current product documentation and do not promise synchronization or publication without a specific workflow.

## Related Concepts

- [How does Workspaces fit into TDEI?](tdei-ecosystem-fit.md)
- [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
