---
uid: d8b89de0-a416-4f65-98d9-d01197a458eb
title: Private OSM (Workspaces)
slug: private-osm
doc_type: concept
questions:
    - What does private OSM mean in Workspaces?
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
    - sandbox-governance
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
        - A private OSM workspace is part of the public OpenStreetMap database.
        - Workspace edits automatically reach OpenStreetMap.
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/private-osm-explained.md
    - assistant/workspaces/concept/osm-api-emulation.md
tags:
    - Assistant
---

<!-- @format -->

# Private OSM (Workspaces)

## Short Answer

Private OSM describes the OpenStreetMap-like editing model used by Workspaces for a controlled dataset. It supports familiar OSM-compatible tools and concepts without making the workspace a public OpenStreetMap database.

## Significance

The model lets teams use established editing patterns while keeping project data and review within the workspace workflow.

## What This Means

Treat the workspace as a separate dataset, use its permissions and review process, and verify the destination before exporting data.

## What This Does Not Mean

Private OSM does not mean private data is automatically secure, globally synchronized, or published to OpenStreetMap.

## How To Use This

Ask which workspace, users, and export destination are involved before explaining visibility or synchronization.

## Example

A team edits a pedestrian dataset with an OSM-compatible editor in Workspaces and reviews the changes before any authorized export.

## Assistant Guidance

Distinguish OSM-compatible behavior from membership in the public OSM database. Cite current Workspaces documentation for permissions and export behavior.

## Related Concepts

 - [How is private OSM explained?](private-osm-explained.md)
 - [What is the workspace relationship to OpenStreetMap?](workspace-as-private-osm.md)
