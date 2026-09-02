---
uid: 53c458c4-656f-4996-9cb9-8840fb23a5eb
title: 'What is "max_cost"?'
slug: max-cost
doc_type: concept
questions:
    - What is "max_cost"?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - cost
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is "max_cost"?

## Short Answer

`max_cost` is the maximum accumulated travel cost allowed in a walkshed analysis. The cost may combine distance, elevation, barriers, crossing conditions, or profile-specific penalties according to the current implementation.

## Significance

The value determines how far the model may travel under its cost rules and therefore affects the size and shape of the reachable area.

## What This Means

Check the units, cost function, profile, network, origin, and dataset version. Do not assume that the value is ordinary distance or that the same number means the same thing across profiles or releases.

## What This Does Not Mean

`max_cost` is not a universal measure of a person's endurance, a legal accessibility threshold, or a guarantee that every location inside the result is reachable in practice.

## How To Use This

Record the value and its definition with every result. Compare analyses only when their cost rules and other inputs are compatible.

## Example

A lower `max_cost` produces a smaller modeled area for the same profile and network. The analyst explains the change as a travel-budget effect rather than a change in physical accessibility.

## Assistant Guidance

State the implementation and units, cite current documentation, and abstain when the cost definition is unknown.

## Related Concepts

The meaning of `max_cost` is implementation- and profile-dependent.
