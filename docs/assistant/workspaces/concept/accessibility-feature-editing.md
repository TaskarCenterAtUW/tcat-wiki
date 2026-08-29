---
title: How are accessibility features edited?
slug: accessibility-feature-editing
doc_type: concept
questions:
    - How are accessibility features edited?
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
risk_level: medium
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
    - assistant/workspaces/concept/attribute-editing.md
    - assistant/workspaces/concept/edit-types.md
    - assistant/workspaces/workflow/edit-accessibility-features-in-a-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# How are accessibility features edited?

## Short Answer

Accessibility features in Workspaces are edited as geometry and attribute changes using a compatible editor and the workspace's available data model. The exact fields and editor controls depend on the workspace, schema, and current editor version.

## Significance

Careful feature editing helps preserve the meaning and connectivity of pedestrian data and creates changes that reviewers can inspect before export.

## What This Means

Select the feature, edit its geometry or supported attributes using current evidence, preserve unknown values, check nearby connections, and save the changes in a reviewable changeset.

## What This Does Not Mean

Editing a feature does not certify its accessibility, publish it to OpenStreetMap, or automatically update TDEI or downstream products. Editor controls do not replace field verification.

## How To Use This

Use the workspace and schema documentation for the exact field definitions, record sources and uncertainty, and submit edits for review before export or publication.

## Example

A mapper adjusts a curb-ramp location and updates a supported attribute from a field observation, then checks the crossing connection and adds a changeset comment for review.

## Assistant Guidance

Ask which workspace, editor, feature type, and schema are involved. Do not invent fields or imply that an edit is approved, and abstain when current editor support is unknown.

## Related Concepts

- [Can attribute data be edited?](attribute-editing.md)
- [What kinds of edits can be made in Workspaces?](edit-types.md)
- [Edit accessibility features in a workspace](../workflow/edit-accessibility-features-in-a-workspace.md)
