---
uid: 10fa8424-575f-4d06-b988-c879ba2fa47a
title: What is a workspace in technical terms?
slug: workspace-technical-definition
doc_type: concept
questions:
    - What is a workspace in technical terms?
audiences:
    - developer
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
    - tasking-manager
    - documentation
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-30
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/workspace-as-dataset-copy.md
    - assistant/workspaces/concept/private-osm.md
    - assistant/workspaces/concept/tasking-projects-and-tasks.md
    - assistant/workspaces/concept/workspaces-api.md
    - assistant/workspaces/concept/osm-api-emulation.md
tags:
    - Assistant
---

<!-- @format -->

# What is a workspace in technical terms?

## Short Answer

A workspace is a web-based, controlled editing environment for a selected pedestrian or accessibility dataset. Technically, it combines a dataset copy, workspace identity and metadata, access controls, editing tools, and workflows for review and export. The API specification models workspace records and related workspace-scoped resources; it describes API contracts, not every user-interface behavior or permission.

## Significance

This definition distinguishes the collaborative working environment from a source dataset, a viewer, and a published release.

## What This Means

The [Workspaces API reference](https://api.workspaces.sidewalks.washington.edu/docs) documents several resource groups:

- Workspace operations for listing, creating (including from a file), retrieving, updating, deleting, checking names, and retrieving a bounding box.
- Workspace-scoped team and member-role operations, imagery settings, long-quest settings, and job records.
- Tasking projects, areas of interest, project roles, tasks, task locks and submissions, feedback, and project or task audit events. See [Tasking projects and tasks](tasking-projects-and-tasks.md).
- Changeset augmented-diff and resolution operations, plus OSM capability-document paths. See [OSM API emulation](osm-api-emulation.md).

Use documented interfaces and APIs for workspace settings. Follow the [workspace export workflow](../workflow/export-workspace-to-tdei.md) for downstream release; this API specification does not list a dedicated export or publish endpoint.

## What This Does Not Mean

A workspace is not automatically a public dataset, a GIS replacement, or a synchronized source database. The API specification does not define every role permission, UI availability, or publication outcome.

## How To Use This

Ask for the workspace environment, source, roles, and intended operation when technical behavior matters.

## Example

A developer uses the workspace's OSM-compatible API and editor to modify a controlled copy, then exports the reviewed result separately.

## Assistant Guidance

Cite the current Workspaces documentation, including the API reference when describing endpoint contracts. Distinguish documented schema from observed implementation behavior, permissions, and the conceptual definition.

## Related Concepts

 - [Is a workspace a copy or the original dataset?](workspace-as-dataset-copy.md)
 - [What does private OSM mean?](private-osm.md)
- [How do Tasking projects and tasks work in Workspaces?](tasking-projects-and-tasks.md)
 - [What APIs does Workspaces provide?](workspaces-api.md)
 - [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
