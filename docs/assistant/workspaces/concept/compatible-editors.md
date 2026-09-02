---
uid: d86313df-89c4-4ebd-91b3-300e7ebca9dc
title: What editors work with Workspaces?
slug: compatible-editors
doc_type: concept
questions:
    - What editors work with Workspaces?
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
    - assistant/workspaces/concept/workspace-editing-boundary.md
    - assistant/workspaces/concept/edit-types.md
tags:
    - Assistant
---

<!-- @format -->

# What editors work with Workspaces?

## Short Answer

Workspaces can work with the editors documented for the current product and workspace configuration. The repository's human documentation identifies embedded Rapid and support for tools such as JOSM; AVIV ScoutRoute provides a mobile contribution path when external-app access is configured.

## Significance

Editor compatibility determines which users can edit, which fields and workflows are available, and how changes are uploaded and reviewed.

## What This Means

Check the current Workspaces documentation, workspace permissions, editor version, API or connection settings, and dataset schema before choosing a tool.

## What This Does Not Mean

An editor named in general documentation is not guaranteed to support every workspace or field. Compatibility does not mean that edits are published automatically or that the editor validates accessibility.

## How To Use This

Choose an editor based on the task, platform, user role, and required fields. Test a small change, review its metadata, and confirm the upload and review path before scaling work.

## Example

A manager uses embedded Rapid for map editing, JOSM for a supported desktop workflow, and AVIV ScoutRoute for configured mobile observations, then reviews the resulting changes in Workspaces.

## Assistant Guidance

Do not promise compatibility for an unverified tool or version. Cite current Workspaces and editor documentation, and abstain when connection or permission details are unknown.

## Related Concepts

- [What tools work with Workspaces?](compatible-tools.md)
- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
- [What kinds of edits can be made in Workspaces?](edit-types.md)
