---
uid: d86313df-89c4-4ebd-91b3-300e7ebca9dc
title: What editors work with Workspaces?
slug: compatible-editors
doc_type: concept
questions:
    - What editors work with Workspaces?
    - What is the difference between editing in Rapid/iD and editing in AVIV ScoutRoute?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - editing
    - osm-interoperability
    - accessibility-data
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/compatible-tools.md
    - assistant/workspaces/concept/workspace-editing-boundary.md
    - assistant/workspaces/concept/edit-types.md
tags:
    - Assistant
---

<!-- @format -->

# What editors work with Workspaces?

## Short Answer

Workspaces provides a modified Rapid editor for OSW datasets and a different modified Rapid editor for GTFS-Pathways datasets. Rapid is an extended version of the OpenStreetMap iD editor, but standalone iD is not a separate documented Workspaces connection. Workspaces also supports a documented JOSM desktop workflow and AVIV ScoutRoute for configured mobile quest contributions.

## Significance

Editor compatibility determines which users can edit, which fields and workflows are available, and how changes are uploaded and reviewed.

## What This Means

Rapid and iD are related: Rapid extends iD, and Workspaces embeds modified Rapid editors. Use the OSW editor for OSW data; the Pathways editor is a separate modified Rapid experience, and Workspaces routes it with `datatype=pathways&editor=rapid3`. AVIV ScoutRoute presents configured questions about selected features and commits submitted answers to the workspace through changesets. AVIV access and quest definitions must be configured for the workspace.

## What This Does Not Mean

The presence of iD in Rapid's lineage does not establish that standalone iD can connect to Workspaces. Do not send GTFS-Pathways data to the main OSW Rapid editor, assume that every editor supports every dataset type or field, or treat edits as automatically published or validated.

## How To Use This

Choose the Rapid editor that Workspaces launches for the selected dataset type; the GTFS-Pathways editor is distinct from the main OSW Rapid editor. Use AVIV ScoutRoute for configured field questions and JOSM only with its documented connection setup. Do not recommend standalone iD as a separate Workspaces integration.

## Example

A manager edits OSW geometry in the main Workspaces Rapid editor and opens a GTFS-Pathways workspace in its separate Rapid-based editor. Field contributors use AVIV ScoutRoute to answer configured questions about selected features; those submissions can be reviewed in Workspaces.

## Assistant Guidance

Do not promise compatibility for an unverified tool or version. Cite current Workspaces and editor documentation, and abstain when connection or permission details are unknown.

## Related Concepts

- [What tools work with Workspaces?](compatible-tools.md)
- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
- [What kinds of edits can be made in Workspaces?](edit-types.md)
