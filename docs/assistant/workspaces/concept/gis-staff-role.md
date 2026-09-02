---
uid: 11a74018-2359-4be9-87dd-278e35482312
title: How do technical GIS staff interact with Workspaces?
slug: gis-staff-role
doc_type: concept
questions:
    - How do technical GIS staff interact with Workspaces?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - stewardship
    - operational-workflows
    - public-support
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
    - assistant/workspaces/concept/gis-tool-decision.md
    - assistant/workspaces/concept/workspace-editing-boundary.md
    - assistant/workspaces/concept/local-data-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How do technical GIS staff interact with Workspaces?

## Short Answer

Technical GIS staff can use Workspaces to inspect and edit supported pedestrian data, coordinate source and schema information, review changesets, validate imports or exports, and manage the boundary between local GIS and shared datasets.

## Significance

GIS staff often connect operational records with collaborative editing and release workflows. Their role helps preserve quality, lineage, and appropriate use.

## What This Means

Define the source, workspace, schema, coordinate system, permissions, review criteria, export target, and local authoritative records. Document transformations and unresolved conflicts.

## What This Does Not Mean

Workspaces does not replace an agency GIS, asset-management system, inspection process, or legal authority. A GIS user's access does not make a workspace edit approved.

## How To Use This

Use Workspaces for supported collaborative feature editing and review, and external GIS tools for agency-specific analysis or records when those tools better fit the need.

## Example

A GIS analyst imports or reviews a pedestrian dataset in Workspaces, checks geometry and attributes against local records, and preserves lineage before export.

## Assistant Guidance

Ask what task, source, workspace, role, and output are involved. Cite current documentation, avoid inventing permissions, and abstain when the workflow is not verified.

## Related Concepts

- [When should a city use external GIS tools?](gis-tool-decision.md)
- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
- [How should agencies validate the data locally?](../../os-connect/concept/local-data-validation.md)
