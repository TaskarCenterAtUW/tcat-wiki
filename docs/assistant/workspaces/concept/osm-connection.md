---
uid: 890f5e4b-ca48-4c8a-b49e-c2a3d9304ef0
title: Is Workspaces connected to the public OSM database?
slug: osm-connection
doc_type: concept
questions:
    - Is Workspaces connected to the public OSM database?
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
risk_level: high
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
    - assistant/workspaces/concept/osm-api-emulation.md
    - assistant/workspaces/concept/osm-editing-emulation-rationale.md
    - assistant/workspaces/concept/workspace-as-private-osm.md
tags:
    - Assistant
---

<!-- @format -->

# Is Workspaces connected to the public OSM database?

## Short Answer

Workspaces is not the public OpenStreetMap database. It can use OSM-like editing concepts and may support imports or compatible tools, but workspace data and edits remain governed by the workspace's source, permissions, review, and export workflows.

## Significance

The separation protects private or project-specific data and makes workspace lineage and review explicit.

## What This Means

Check whether data were imported from OSM, how the workspace API is configured, who can access it, and whether an explicit export or publication step exists.

## What This Does Not Mean

A workspace edit does not automatically update public OSM, and an OSM edit does not automatically update a workspace or OS-CONNECT release.

## How To Use This

Preserve source attribution and licenses, use documented import or export procedures, and review changes before sharing them.

## Example

A project imports an OSM extract into a workspace, edits pedestrian features privately, and later decides whether and how a reviewed result is exported.

## Assistant Guidance

Do not promise synchronization or public visibility. Cite current workspace and OSM guidance and abstain when the source or publication path is unknown.

## Related Concepts

- [How does Workspaces emulate OSM APIs?](osm-api-emulation.md)
- [Why does Workspaces emulate OSM editing?](osm-editing-emulation-rationale.md)
- [What does private OSM mean?](private-osm-explained.md)
