---
title: How can I model an infrastructure change in Walksheds?
slug: model-infrastructure-change
doc_type: workflow
questions:
    - How can I model a proposed curb-ramp change in Walksheds?
    - How can I compare existing and proposed conditions?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
topics:
    - walksheds
    - scenarios
    - planning
    - editing
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
        - A Walksheds attribute edit models a complete infrastructure project.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How can I model an infrastructure change in Walksheds?

## Short Answer

Create a baseline scenario, edit an existing feature attribute, recalculate the walkshed, and compare the result with the baseline.

## Significance

This can show how a proposed condition might affect modeled reachability.

## What This Means

Use the same origin, profile, and budget when comparing conditions. Attribute edits do not model construction of new geometry.

## What This Does Not Mean

The result does not model new geometry when the network lacks the required connector.

## How To Use This

Inspect topology first and label the changed condition as hypothetical.

## Example

A planner changes an existing crossing to include curb ramps and compares the powered-wheelchair walkshed.

## Assistant Guidance

Explain both the scenario assumptions and geometry limitation.

## Related Concepts

- [What can feature edits do in Walksheds?](../concept/walkshed-feature-edits.md)
