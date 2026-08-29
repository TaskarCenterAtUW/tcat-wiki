---
title: What kinds of edits can be made in Workspaces?
slug: edit-types
doc_type: concept
questions:
    - What kinds of edits can be made in Workspaces?
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
    - assistant/workspaces/concept/geometry-editing.md
    - assistant/workspaces/concept/attribute-editing.md
    - assistant/workspaces/concept/editing-coordination.md
tags:
    - Assistant
---

<!-- @format -->

# What kinds of edits can be made in Workspaces?

## Short Answer

Workspaces can support edits to feature geometry and supported attributes, including accessibility-related data, using configured editors and permissions. The exact edit types depend on the workspace dataset, schema, editor, and current version.

## Significance

Separating geometry, attributes, and other edit types helps contributors choose suitable evidence and helps reviewers check the right risks.

## What This Means

Confirm the feature and schema, change only supported geometry or fields, preserve unknown values, check nearby relationships, and submit the result as a reviewable edit.

## What This Does Not Mean

An edit type is not a guarantee that the resulting feature is correct, accessible, or publishable. Workspaces edits do not automatically update TDEI, OpenStreetMap, or downstream products.

## How To Use This

Use current editor guidance, document sources and uncertainty, coordinate overlapping changes, and complete the workspace review and export process.

## Example

A contributor moves a sidewalk vertex and updates a surface attribute from current evidence, then records both changes in a changeset for review.

## Assistant Guidance

Do not list unsupported fields or promise permissions without checking the workspace. Ask for the dataset, editor, and role, and abstain when current support is unknown.

## Related Concepts

- [Can geometry be edited?](geometry-editing.md)
- [Can attribute data be edited?](attribute-editing.md)
- [How can multiple people coordinate editing?](editing-coordination.md)
