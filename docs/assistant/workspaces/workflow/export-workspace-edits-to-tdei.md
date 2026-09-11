---
uid: e82a23a4-e888-4999-9454-3b870772536f
title: Export workspace edits to TDEI
slug: export-workspace-edits-to-tdei
doc_type: workflow
questions:
    - How do I export workspace edits to TDEI?
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
        - Exporting workspace edits automatically publishes a public dataset.
        - Export success proves that every edit is correct.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-export-and-publication-caveats.md
    - assistant/workspaces/workflow/pre-export-review.md
tags:
    - Assistant
---

<!-- @format -->

# Export workspace edits to TDEI

## Short Answer

Before exporting workspace edits to TDEI, complete review, confirm the target dataset and version, verify permissions and service configuration, run the current export workflow, and validate the resulting TDEI record. Treat publication or viewer visibility as a separate step.

## Significance

Export is a controlled handoff from a working copy to a managed data service, so lineage and validation must be preserved.

## What This Means

Confirm source scope, workspace ID, target service, version, review status, and authorization. Record the export result and any processing errors.

## What This Does Not Mean

Export does not automatically release data, close the workspace, or resolve data-quality issues.

## How To Use This

Use the current Workspaces and TDEI instructions; ask which environment and target service are involved before giving operational steps.

## Example

A jurisdiction exports a reviewed workspace as a new TDEI version, checks the result, and only then follows its release process.

## Assistant Guidance

Cite the current export guide and abstain when permissions, target, or source version is missing.

## Related Concepts

 - [What caveats apply to export and publication?](../concept/workspace-export-and-publication-caveats.md)
 - [How should review happen before export?](pre-export-review.md)
