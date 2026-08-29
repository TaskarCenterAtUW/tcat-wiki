---
title: Can attribute data be edited?
slug: attribute-editing
doc_type: concept
questions:
    - Can attribute data be edited?
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
    - assistant/workspaces/concept/accessibility-feature-editing.md
    - assistant/workspaces/concept/edit-types.md
    - assistant/workspaces/concept/workspace-editing-boundary.md
tags:
    - Assistant
---

<!-- @format -->

# Can attribute data be edited?

## Short Answer

Supported attribute data can be edited in Workspaces through a compatible editor and workspace schema. Which fields are editable depends on the dataset, editor, permissions, and current product configuration.

## Significance

Attribute edits can add important context to pedestrian geometry, but they also affect routing, analysis, and downstream interpretation, so they need review and provenance.

## What This Means

Open the feature in the workspace editor, change only supported fields using evidence, preserve unknown values, review the before-and-after state, and upload the edit with a clear changeset comment.

## What This Does Not Mean

An editable field is not automatically authoritative, and changing an attribute does not prove the physical condition or publish the change to TDEI, OpenStreetMap, or another product.

## How To Use This

Check the schema and editor documentation, record the source and date, avoid guessing values, and follow the workspace review and export process.

## Example

A reviewer updates a sidewalk surface field from a dated local observation, checks that the value is allowed by the schema, and leaves the edit pending review.

## Assistant Guidance

Ask for the workspace, field, schema, and editor version. Do not promise that a field is editable or accepted without current documentation.

## Related Concepts

- [How are accessibility features edited?](accessibility-feature-editing.md)
- [What kinds of edits can be made in Workspaces?](edit-types.md)
- [Where are TDEI datasets edited?](workspace-editing-boundary.md)
