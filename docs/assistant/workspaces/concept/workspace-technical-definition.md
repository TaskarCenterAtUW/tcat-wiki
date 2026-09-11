---
uid: 10fa8424-575f-4d06-b988-c879ba2fa47a
title: What is a workspace in technical terms?
slug: workspace-technical-definition
doc_type: concept
questions:
    - What is a workspace in technical terms?
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
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace is the same thing as a public OpenStreetMap dataset.
        - A workspace is a live synchronized view of every source dataset.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/concept/private-osm.md
tags:
    - Assistant
---

<!-- @format -->

# What is a workspace in technical terms?

## Short Answer

A workspace is a web-based, controlled editing environment for a selected pedestrian or accessibility dataset. Technically, it combines a dataset copy, workspace identity and metadata, access controls, editing tools, and workflows for review and export.

## Significance

This definition distinguishes the collaborative working environment from a source dataset, a viewer, and a published release.

## What This Means

Use the workspace for bounded edits and review; use the documented interfaces and APIs for settings, exports, and downstream publication.

## What This Does Not Mean

A workspace is not automatically a public dataset, a GIS replacement, or a synchronized source database.

## How To Use This

Ask for the workspace environment, source, roles, and intended operation when technical behavior matters.

## Example

A developer uses the workspace's OSM-compatible API and editor to modify a controlled copy, then exports the reviewed result separately.

## Assistant Guidance

Cite the current Workspaces documentation and distinguish observed implementation behavior from the conceptual definition.

## Related Concepts

 - [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
 - [What does private OSM mean?](private-osm.md)
