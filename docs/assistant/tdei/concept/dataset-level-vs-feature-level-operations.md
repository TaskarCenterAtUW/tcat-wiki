---
uid: 4ec42c15-7528-4644-a1e9-1e5ec43d3720
title: What is the difference between dataset-level and feature-level operations?
slug: dataset-level-vs-feature-level-operations
doc_type: concept
questions:
    - What is the difference between dataset-level and feature-level operations?
    - What can I do to an entire dataset in TDEI versus individual elements in Workspaces?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - Workspaces
topics:
    - tdei
    - workspaces
    - editing
    - automation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/tdei/concept/job-processing.md
    - assistant/workspaces/concept/workspace-editing-boundary.md
    - assistant/workspaces/concept/changesets.md
    - assistant/workspaces/concept/workspace-and-tdei-boundary.md
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between dataset-level and feature-level operations?

## Short Answer

TDEI jobs take datasets as inputs and support operations such as validation, sanitization, format conversion, bounding-box filtering, spatial joins, unions, and quality calculations; check each job's documentation for its inputs and output. Workspaces lets contributors select map features and edit their geometry or attributes, with edits recorded in changesets. This is a difference in operation scope, not an absolute product boundary: TDEI jobs can process feature content across a dataset, while Workspaces also supports broader review and export workflows.

## Significance

This distinction helps users choose a dataset-processing job or a feature-editing workflow and understand whether the result will be a job output or a reviewed workspace change.

## What This Means

Use TDEI for dataset jobs such as validation, sanitization, conversion, filtering, spatial joins, unions, and quality calculations. Check each job's documentation to see whether it returns transformed data, metrics, a report, or another result. Use Workspaces when a contributor needs to select one or more map features and change their geometry or attributes. Changesets record workspace edits; exporting reviewed edits back to TDEI is a separate workflow.

## What This Does Not Mean

A dataset-level job does not necessarily change every feature or overwrite its input; some jobs validate, filter, or calculate results instead of replacing dataset content. A feature-level workflow does not mean only one feature can be edited: changesets can include multiple feature edits, and Workspaces also supports broader review and export actions. Editing a workspace does not automatically publish changes to TDEI.

## How To Use This

Clarify whether the user needs a dataset job or targeted map edits, and ask what outcome they want. For TDEI, identify the dataset and intended job, then confirm its documented inputs and outputs; for Workspaces, identify the workspace and feature or features, intended geometry or attribute changes, and review or export needs. Do not infer the available operation from the product name alone.

## Example

A jurisdiction runs an OSW validation job and reviews its result for a dataset; a mapper who needs to correct one sidewalk's geometry edits that feature in a Workspaces editor, where the edit is recorded in a changeset. Exporting workspace results to TDEI is a separate step.

## Assistant Guidance

Ask whether the user needs a dataset-level job or targeted feature edits. Treat this as a difference in operation scope, not an absolute product boundary. Cite job-specific TDEI documentation for exact inputs and outputs, and Workspaces editing or changeset guidance for feature edits. Do not claim a job overwrites its source or that workspace changes publish to TDEI unless the specific workflow documents that behavior.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
- [Where are TDEI datasets edited?](../../workspaces/concept/workspace-editing-boundary.md)
- [Changesets (Workspaces)](../../workspaces/concept/changesets.md)
- [What is the boundary between Workspaces and TDEI?](../../workspaces/concept/workspace-and-tdei-boundary.md)
- [TDEI Portal Jobs guide](../../../tdei/portal/user-manual/jobs/index.md)
