---
title: What are custom Walksheds cost functions?
slug: walkshed-custom-cost-functions
doc_type: concept
questions:
    - What are custom Walksheds cost functions?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - configuration
    - accessibility-metrics
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A custom cost function can use every collected attribute automatically.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are custom Walksheds cost functions?

## Short Answer

Custom cost functions let users define how available network attributes affect modeled travel cost.

## Significance

They can adapt analysis to project-specific assumptions.

## What This Means

Use the documented `cost_fun_generator` pattern and only attributes exposed by the current Walksheds model and formula interface. The returned edge function must produce a non-negative cost or `None` to exclude an edge.

## What This Does Not Mean

Every attribute collected in source data is necessarily available to formulas.

## How To Use This

Document the formula, fields, units, return values, exclusions, and assumptions before comparing results. This is an experimental feature and may not always be enabled.

## Example

A project gives a higher cost to a surface condition it can access in the formula model.

## Assistant Guidance

Ask which fields are exposed before recommending a formula.

## Related Concepts

- [What factors affect Walksheds travel cost?](walkshed-cost-factors.md)
