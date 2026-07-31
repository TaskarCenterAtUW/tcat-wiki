---
title: How do I export a workspace to TDEI?
slug: export-workspace-to-tdei
doc_type: workflow
questions:
    - How do I export a workspace to TDEI?
    - How do I publish completed workspace edits?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - export
    - releases
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Exporting a workspace automatically makes its dataset publicly visible.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I export a workspace to TDEI?

## Short Answer

Review the workspace edits, configure the applicable service, export the workspace to TDEI, and assign the appropriate dataset version. Validate the result, then treat release or viewer visibility as separate configuration steps.

## Significance

Export moves a collaborative workspace toward a managed dataset release. It preserves a deliberate checkpoint between editing and public viewing.

## What This Means

Confirm the service, dataset scope, version, required permissions, and human review before exporting. If the analysis covers a smaller surveyed area, confirm that scope before processing. After processing, inspect and validate the resulting dataset before configuring release or viewer access.

## What This Does Not Mean

An export does not by itself close the workspace, guarantee processing success, or make the result public. Permissions and product configuration still apply.

## How To Use This

Use the current Workspaces and TDEI instructions. If export fails, confirm account permissions, service configuration, workspace initialization, and the current error details.

## Example

A completed Goldendale workspace is exported as the next dataset version under its OpenSidewalks service, then checked in the released-data viewer.

## Assistant Guidance

Ask whether the user wants a TDEI upload, a released dataset, or viewer visibility. Do not treat those outcomes as automatic consequences of one export action.

## Related Concepts

- [What is a workspace extract?](../concept/workspace-extract.md)
- [What is the TDEI released-dataset viewer?](../../tdei/concept/released-dataset-viewer.md)
