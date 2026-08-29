---
title: Why is the dataset not global like OSM?
slug: non-global-dataset-rationale
doc_type: concept
questions:
    - Why is the dataset not global like OSM?
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
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/concept/osm-connection.md
    - assistant/workspaces/concept/workspaces-osm-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why is the dataset not global like OSM?

## Short Answer

A Workspaces dataset is not global like OpenStreetMap because a workspace is a bounded project or dataset environment with defined source, geography, permissions, and stewardship.

## Significance

Bounded scope supports project-specific editing, review, privacy, data lineage, and governance rather than one public global database.

## What This Means

Check the workspace source, geographic extent, access model, release, and relationship to OSM. Treat each workspace as its own project context.

## What This Does Not Mean

Non-global scope does not mean the data are unimportant or disconnected from OSM concepts, and it does not imply that a workspace is a live global OSM mirror.

## How To Use This

Use the workspace for its defined area and purpose, preserve lineage, and export or share data only through the documented workflow.

## Example

A city workspace covers a local pedestrian network while OpenStreetMap covers a global collaborative database; the workspace keeps project edits and review separate.

## Assistant Guidance

Do not claim global coverage or automatic OSM synchronization. Cite the workspace and source documentation and abstain when scope is unknown.

## Related Concepts

- [Is Workspaces connected to the public OSM database?](osm-connection.md)
- [What limitations exist compared to OpenStreetMap?](workspaces-osm-limitations.md)
- [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
