---
uid: b8f25f3c-5640-4e76-9c60-00339a908f46
title: Workspaces export and publication caveats
slug: workspace-export-and-publication-caveats
doc_type: concept
questions:
    - What caveats apply to exporting and publishing from Workspaces?
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
        - Exporting a workspace automatically makes the data public.
        - Export success proves that the dataset is complete or approved.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/workflow/export-workspace-edits-to-tdei.md
    - assistant/workspaces/concept/workspace-review-and-publication-gates.md
tags:
    - Assistant
---

<!-- @format -->

# Workspaces export and publication caveats

## Short Answer

Exporting moves workspace data to a destination or processing service; publication and viewer visibility are separate outcomes that depend on configuration, permissions, validation, and release procedures.

## Significance

Export is a consequential handoff. Reviewers need to preserve lineage, scope, version, attribution, and unresolved limitations.

## What This Means

Review edits, confirm the target and version, check permissions, validate the result, and verify release or viewer settings separately.

## What This Does Not Mean

An export does not guarantee processing success, public visibility, source updates, or legal compliance.

## How To Use This

Use the current export tutorial and identify whether the user wants a local file, a TDEI upload, a managed release, or viewer visibility.

## Example

A jurisdiction exports a reviewed workspace as a new TDEI version, validates it, and then follows the separate release configuration process.

## Assistant Guidance

Cite the export and release documentation. Abstain when target, permissions, or release state is unknown.

## Related Concepts

 - [How do I export workspace edits to TDEI?](../workflow/export-workspace-edits-to-tdei.md)
 - [How should review happen before export?](../workflow/pre-export-review.md)
