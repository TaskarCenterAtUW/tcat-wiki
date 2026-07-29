---
title: "How do point and line feature workflows differ?"
slug: point-and-line-feature-workflows
doc_type: concept
questions:
    - How do point and line feature workflows differ in OpenSidewalks editing?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
    - Workspaces
    - AVIV ScoutRoute
topics:
    - opensidewalks
    - workspaces
    - aviv-scoutroute
    - editing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Mobile point creation and desktop line editing have identical accuracy and workflow requirements.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/workspaces/concept/mobile-point-feature-creation.md
tags:
    - Assistant
---

<!-- @format -->

# How do point and line feature workflows differ?

## Short Answer

Mobile apps are well suited to targeted point observations, while desktop editors are better for precise sidewalk, crossing, and connector geometry.

## Significance

The geometry type affects accuracy and the appropriate contributor interface.

## What This Means

Use mobile points or notes to signal field conditions and use desktop or Workspaces editors for line construction and connectivity. A Custom Point can preserve a non-routable feature such as a bus stop, while a sidewalk or crossing requires network-aware line geometry.

## What This Does Not Mean

A point observation does not create the line network around it, and a point dataset should not be treated as a substitute for connected Edges.

## How To Use This

Choose the editor based on geometry, GPS accuracy, and review requirements.

## Example

A contractor reports a missing sidewalk by note, and a desktop editor draws the line and connects it.

## Assistant Guidance

Ask whether the intended change is a point, line, or connector.

## Related Concepts

- [What can AVIV ScoutRoute create on mobile?](../../workspaces/concept/mobile-point-feature-creation.md)
