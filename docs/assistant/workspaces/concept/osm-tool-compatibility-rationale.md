---
uid: 27b73b05-5428-4a61-9859-0cc2808ad148
title: Why is Workspaces compatible with OSM tools?
slug: osm-tool-compatibility-rationale
doc_type: concept
questions:
    - Why is Workspaces compatible with OSM tools?
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
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/compatible-tools.md
    - assistant/workspaces/concept/compatible-editors.md
    - assistant/workspaces/concept/osm-api-emulation.md
tags:
    - Assistant
---

<!-- @format -->

# Why is Workspaces compatible with OSM tools?

## Short Answer

Workspaces is compatible with selected OSM tools because it uses familiar data and editing patterns that can connect project-specific workspace data to established editor workflows.

## Significance

Compatibility can lower training and implementation costs and support contributors with existing OSM editing experience.

## What This Means

Check the current tool, API, schema, workspace, version, permissions, supported operations, and upload or review behavior before using a tool.

## What This Does Not Mean

Compatibility does not mean complete parity, public OSM publication, automatic synchronization, or universal support for accessibility fields.

## How To Use This

Use supported tools for bounded tasks, test and review edits, preserve provenance, and confirm the deliberate export or publication path.

## Example

A project uses a compatible editor to edit workspace data, then reviews the resulting changesets before exporting a dataset to TDEI.

## Assistant Guidance

Do not infer compatibility from an OSM-like interface alone. Cite current technical guidance and abstain when the tool or operation is not verified.

## Related Concepts

- [What tools work with Workspaces?](compatible-tools.md)
- [What editors work with Workspaces?](compatible-editors.md)
- [How does Workspaces emulate OSM APIs?](osm-api-emulation.md)
