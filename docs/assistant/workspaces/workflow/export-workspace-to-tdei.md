---
uid: 7693f966-2c3d-4712-b725-5484d75073fa
title: How do I export a workspace to TDEI?
slug: export-workspace-to-tdei
doc_type: workflow
questions:
    - How do I export a workspace to TDEI?
    - How do I publish completed workspace edits?
    - How do I export completed changes back to TDEI as a new dataset or version?
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
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/workspace-extract.md
    - assistant/tdei/concept/released-dataset-viewer.md
tags:
    - Assistant
---

<!-- @format -->

# How do I export a workspace to TDEI?

## Short Answer

Open the workspace's **Export** action, choose **Upload to TDEI**, select **Start**, and follow the prompts to upload the workspace as a new TDEI dataset. A TDEI **POC** or **osw_data_generator** role in at least one project group is required. Verify the resulting dataset in TDEI; upload does not by itself release it publicly.

## Significance

Export moves a collaborative workspace toward a managed dataset release. It preserves a deliberate checkpoint between editing and public viewing.

## What This Means

1. Review the workspace edits and confirm that the intended result is ready for export.
2. Open the workspace from the Dashboard, open its actions, and select **Export**.
3. In **Upload to TDEI**, select **Start** and follow the displayed prompts.
4. If you lack a TDEI **POC** or **osw_data_generator** role in at least one project group, request the required access before continuing.
5. After upload, verify the resulting dataset and its metadata in TDEI. Follow any separate validation, release, or viewer-access workflow that applies.

## What This Does Not Mean

The documented upload creates a new TDEI dataset; it does not establish that the source dataset is overwritten, that the workspace closes, or that the new dataset is publicly released. The current interface and permissions determine the available steps.

## How To Use This

Use the current Workspaces export page and confirm the user's TDEI role. If upload fails, preserve the displayed error and check current permissions and workspace status rather than assuming a release was created.

## Example

A workspace Owner or eligible data generator selects **Export → Upload to TDEI**, follows the prompts, and then checks that the new dataset appears in TDEI before describing it as released.

## Assistant Guidance

Ask whether the user means uploading a new dataset, validating it, releasing it, or making it visible in a viewer. Do not invent a version-number rule or treat those outcomes as automatic consequences of one upload action.

## Related Concepts

- [What is a workspace extract?](../concept/workspace-extract.md)
- [What is the TDEI released-dataset viewer?](../../tdei/concept/released-dataset-viewer.md)
- [Export a Workspace manual](../../../workspaces/user-manual/export.md)
