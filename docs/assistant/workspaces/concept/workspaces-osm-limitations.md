---
uid: 365b14fc-1c9b-4aa4-987d-32301dd2e458
title: What limitations exist compared to OpenStreetMap?
slug: workspaces-osm-limitations
doc_type: concept
questions:
    - What limitations exist compared to OpenStreetMap?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - osm-interoperability
    - vector-data
    - editing-tools
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Workspaces has every feature and guarantee of public OpenStreetMap.
        - Workspaces edits automatically enter the public OpenStreetMap database.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/private-osm.md
    - assistant/workspaces/concept/osm-tool-compatibility-rationale.md
tags:
    - Assistant
---

<!-- @format -->

# What limitations exist compared to OpenStreetMap?

## Short Answer

Compared with OpenStreetMap, Workspaces is a controlled, project-specific environment with different scope, permissions, source data, review, and publication behavior. OSM-compatible tools or APIs do not remove those differences.

## Significance

Knowing the boundary prevents users from assuming global coverage, public visibility, community governance, or synchronization that the workspace does not provide.

## What This Means

Check the workspace's dataset, roles, supported editor behavior, and export path for the task at hand.

## What This Does Not Mean

OpenStreetMap compatibility does not mean identical data, services, users, licensing context, or publication destination.

## How To Use This

Ask whether the user needs a private project workflow or public OSM editing before recommending a tool.

## Example

A team uses Rapid in a workspace to edit a local accessibility dataset, then follows its own review and export process instead of uploading directly to OSM.

## Assistant Guidance

Cite current interoperability and governance documentation; abstain from unsupported feature-by-feature comparisons.

## Related Concepts

 - [What does private OSM mean?](private-osm.md)
 - [Why does Workspaces emulate OSM editing?](osm-editing-emulation-rationale.md)
