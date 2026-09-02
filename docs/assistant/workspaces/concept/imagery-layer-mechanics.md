---
uid: 53210438-96ab-4a05-bf4a-65b1bbbc41b2
title: How do imagery layers work in Workspaces?
slug: imagery-layer-mechanics
doc_type: concept
questions:
    - How do imagery layers work in Workspaces?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - imagery
    - basemaps
    - configuration
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
    - assistant/workspaces/concept/imagery-layer-overview.md
    - assistant/workspaces/concept/imagery-json-configuration.md
    - assistant/workspaces/concept/imagery-permissions.md
tags:
    - Assistant
---

<!-- @format -->

# How do imagery layers work in Workspaces?

## Short Answer

Imagery layers in Workspaces are reference layers loaded from configured imagery sources and displayed alongside editable workspace data. Their availability and behavior depend on configuration, source permissions, network access, and the current application.

## Significance

Imagery provides visual context for tracing, checking geometry, and reviewing conditions without becoming part of the editable dataset automatically.

## What This Means

Check the active layer, source date, resolution, coordinate alignment, access, attribution, and configuration. Compare imagery with other evidence and preserve uncertainty.

## What This Does Not Mean

An imagery layer is not an authoritative survey, current-condition guarantee, or accessibility certification. Its visual appearance does not automatically change workspace data.

## How To Use This

Use imagery as one source, report loading or alignment problems, and validate consequential edits with appropriate local or field evidence.

## Example

A contributor uses an imagery layer to trace a sidewalk but leaves a curb-ramp attribute unknown because the image does not show the feature clearly.

## Assistant Guidance

Name the source and date, distinguish reference imagery from editable data, and abstain when the layer or configuration cannot be verified.

## Related Concepts

- [What are imagery layers?](imagery-layer-overview.md)
- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [How are imagery permissions handled?](imagery-permissions.md)
