---
uid: aebbd76a-d493-4672-b4cc-28713e669e0a
title: What can feature edits do in Walksheds?
slug: walkshed-feature-edits
doc_type: concept
questions:
    - What can feature edits do in Walksheds?
    - Can Walksheds model a proposed curb-ramp change?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
topics:
    - walksheds
    - editing
    - scenarios
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds feature edits can create any missing geometry.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What can feature edits do in Walksheds?

## Short Answer

Walksheds can edit attributes on existing network features and recalculate reachability. It cannot currently create missing geometry connections.

## Significance

This distinction limits which infrastructure scenarios the tool can model.

## What This Means

Use attribute edits to test conditions such as curb-ramp availability, slope, or surface. Saving an edit recalculates reachability, but collected source attributes may not all be exposed to the Walksheds model.

## What This Does Not Mean

Changing an attribute cannot connect two otherwise disconnected features.

## How To Use This

Check the underlying network before interpreting an edited scenario.

## Example

Marking an existing crossing as having curb ramps does not help if no connector links it to the sidewalk.

## Assistant Guidance

Explain geometry limitations and direct data errors to the appropriate source-data feedback workflow.

## Related Concepts

- [What is the boundary between an external overlay and workspace data?](../../opensidewalks/concept/external-data-overlay-boundary.md)
