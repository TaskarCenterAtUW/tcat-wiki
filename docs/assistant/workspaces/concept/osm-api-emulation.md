---
uid: 2a273334-8212-440f-a6b2-9529b12c0c30
title: How does Workspaces emulate OSM APIs?
slug: osm-api-emulation
doc_type: concept
questions:
    - How does Workspaces emulate OSM APIs?
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
last_reviewed: 2026-10-30
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/osm-editing-emulation-rationale.md
    - assistant/workspaces/concept/osm-tool-compatibility-rationale.md
    - assistant/workspaces/concept/osm-connection.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# How does Workspaces emulate OSM APIs?

## Short Answer

Workspaces emulates selected OpenStreetMap API and editing patterns so compatible editors can work with workspace data through familiar concepts such as nodes, ways, changesets, and uploads. The API reference lists capability-discovery paths, but does not enumerate the complete supported OSM operation set.

## Significance

Familiar API patterns reduce the need to build a completely new editor workflow for project-specific pedestrian data.

## What This Means

The [Workspaces API specification](https://api.workspaces.sidewalks.washington.edu/openapi.json) lists capability endpoints at `/api/0.6/capabilities`, `/api/capabilities`, and `/api/capabilities.json`, along with workspace-prefixed variants under `/workspace/{workspace_id}/api/`. It also lists a generic catch-all route; that route does not establish which OSM operations are supported. The versioned `/api/v1/workspaces` resources for workspace management and Tasking projects are a separate API surface.

Check the current API and editor documentation for supported operations, authentication, geometry, changesets, limits, and differences from public OSM.

## What This Does Not Mean

API emulation does not make Workspaces the public OSM database, guarantee compatibility with every OSM tool, establish full OSM API parity, or publish edits to OSM automatically.

## How To Use This

Use only documented endpoints and workflows, test a small operation, preserve source and workspace identifiers, and review uploads before export.

## Example

A compatible editor connects to a workspace endpoint, downloads a bounded area, uploads a changeset, and displays the result in the workspace review interface.

## Assistant Guidance

Do not infer complete API parity from the capability paths or catch-all route. Cite the current API specification, ask for the endpoint and editor, and abstain when support is undocumented.

## Related Concepts

- [Why does Workspaces emulate OSM editing?](osm-editing-emulation-rationale.md)
- [Why is Workspaces compatible with OSM tools?](osm-tool-compatibility-rationale.md)
- [Is Workspaces connected to the public OSM database?](osm-connection.md)
- [What is a workspace in technical terms?](workspace-technical-definition.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
