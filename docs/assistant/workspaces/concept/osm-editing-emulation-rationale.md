---
uid: 290a0246-bd5f-45f1-980f-071c1c531c65
title: Why does Workspaces emulate OSM editing?
slug: osm-editing-emulation-rationale
doc_type: concept
questions:
    - Why does Workspaces emulate OSM editing?
audiences:
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
    - assistant/workspaces/concept/osm-api-emulation.md
    - assistant/workspaces/concept/osm-editor-benefits.md
    - assistant/workspaces/concept/osm-connection.md
tags:
    - Assistant
---

<!-- @format -->

# Why does Workspaces emulate OSM editing?

## Short Answer

Workspaces emulates OSM editing to reuse familiar map-editing concepts, tools, data structures, and contributor workflows for bounded project data without making the workspace the public OSM database.

## Significance

Familiar patterns can reduce training and implementation effort and let contributors use established editing practices.

## What This Means

The emulation may include nodes, ways, changesets, editor connections, and upload concepts. Check current documentation for which API operations and tools are supported.

## What This Does Not Mean

Emulation does not imply complete API parity, automatic synchronization, public OSM publication, or validation of accessibility conditions.

## How To Use This

Use documented editor and API workflows, preserve source and workspace context, review changes, and keep private project data separate until deliberate export or publication.

## Example

A contributor uses familiar OSM editor controls to modify a private workspace and submits a changeset for project review rather than publishing directly to OSM.

## Assistant Guidance

Do not infer unsupported behavior from visual similarity. Cite the current implementation and abstain when API or editor support is unknown.

## Related Concepts

- [How does Workspaces emulate OSM APIs?](osm-api-emulation.md)
- [What is the benefit of using existing OSM editors?](osm-editor-benefits.md)
- [Is Workspaces connected to the public OSM database?](osm-connection.md)
