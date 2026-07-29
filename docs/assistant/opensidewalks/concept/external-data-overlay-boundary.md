---
title: "What is the boundary between an external overlay and workspace data?"
slug: external-data-overlay-boundary
doc_type: concept
questions:
    - Does loading external data add it to a workspace?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
    - Workspaces
topics:
    - opensidewalks
    - workspaces
    - interoperability
    - editing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-12
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Viewing external data as an overlay validates it or adds it to the official dataset.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/workspaces/workflow/import-external-geojson-for-reference.md
tags:
    - Assistant
---

<!-- @format -->

# What is the boundary between an external overlay and workspace data?

## Short Answer

An external overlay is reference data loaded for comparison; official workspace data is the dataset being edited and reviewed.

## Significance

The distinction prevents accidental publication of unvalidated external features.

## What This Means

Compare sources first, then deliberately add or convert features through the supported workflow.

## What This Does Not Mean

A visible external layer is not automatically part of the workspace.

## How To Use This

Record source, license, and intended disposition before incorporating anything.

## Example

A city sidewalk layer is displayed over OS-CONNECT to identify possible gaps.

## Assistant Guidance

Ask whether the user wants an overlay, an edit, or a dataset merge.

## Related Concepts

- [How can I load external GeoJSON for reference in Workspaces?](../../workspaces/workflow/import-external-geojson-for-reference.md)
