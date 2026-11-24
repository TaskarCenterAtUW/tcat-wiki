---
uid: 4a67f7be-0bcb-42bb-a559-414137cc6789
title: Which editor should I use?
slug: choose-editor
doc_type: workflow
questions:
    - Which editor should I use?
    - Should I use Rapid, iD, the GTFS-Pathways editor, or AVIV ScoutRoute?
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
    - assistant/workspaces/index.md
    - assistant/workspaces/concept/rapid.md
    - assistant/workspaces/concept/compatible-editors.md
tags:
    - Assistant
---

<!-- @format -->

# Which editor should I use?

## Short Answer

Choose the editor by dataset type and task. Workspaces uses a modified Rapid editor for OSW datasets and a different modified Rapid editor for GTFS-Pathways datasets. Rapid is an extended version of iD; standalone iD is not a separate documented Workspaces option. AVIV ScoutRoute is for configured mobile quest contributions, and JOSM is a supported desktop workflow when set up as documented.

## Significance

The editor choice affects onboarding, precision, field collection, and collaboration, but not the user's authority by itself.

## What This Means

Use the OSW Rapid editor for supported browser-based OSW feature edits and the Pathways-specific Rapid editor for GTFS-Pathways data. Workspaces opens the Pathways editor with a route containing `datatype=pathways&editor=rapid3`; select the editor from the workspace rather than substituting the main OSW editor. Use AVIV ScoutRoute for configured field questions and JOSM only with the documented desktop connection.

## What This Does Not Mean

An editor does not guarantee correct data, review, permissions, or publication. The OSW and GTFS-Pathways Rapid editors are distinct Workspaces editing paths, even though both are modified versions of Rapid.

## How To Use This

Ask whether the task is field collection or map editing, identify the dataset type and workspace environment, and route the user to the corresponding editor launched by Workspaces. Do not direct a GTFS-Pathways dataset to the main OSW editor.

## Example

A contributor uses the OSW Rapid editor for sidewalk feature edits, the Pathways-specific Rapid editor for a GTFS-Pathways workspace, and AVIV ScoutRoute to answer a configured field quest.

## Assistant Guidance

Cite current editor compatibility and workspace role guidance; abstain when the target dataset or workflow is unknown.

## Related Concepts

- [What is Rapid in Workspaces?](../concept/rapid.md)
- [What are compatible editors?](../concept/compatible-editors.md)
