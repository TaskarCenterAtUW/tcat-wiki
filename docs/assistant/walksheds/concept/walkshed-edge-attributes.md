---
uid: 3c4dae86-476e-4d51-9a6d-a119b09efa91
title: What edge attributes can Walksheds cost functions use?
slug: walkshed-edge-attributes
doc_type: concept
questions:
    - What edge attributes can Walksheds cost functions use?
    - What does the Walksheds edge attribute dictionary contain?
audiences:
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - configuration
    - formats
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every source dataset attribute is available to a Walksheds custom cost function.
related_pages:
    - walkshed-custom-cost-function-contract.md
    - walkshed-custom-cost-functions.md
    - ../../../walksheds/user-manual/custom-cost-function.md
tags:
    - Assistant
---

<!-- @format -->

# What edge attributes can Walksheds cost functions use?

## Short Answer

The documented edge dictionary may include length, highway, incline, footway, curb ramps, indoor status, opening hours, adjacent street type, closure status, step count, and pathway mode.

## Significance

Available attributes determine what a custom cost function can model or exclude.

## What This Means

The documented keys include `length`, `highway`, `incline`, `footway`, `curbramps`, `indoor`, `opening_hours`, `street_highway`, `is_closed`, `step_count`, and `pathway_mode`.

## What This Does Not Mean

A field's presence in an input dataset does not prove that it is exposed, typed, or populated in the cost function's dictionary.

## How To Use This

Inspect the current function interface, check units and null behavior, and test on representative edges.

## Example

A function checks `is_closed` to exclude a closed edge and uses `incline` to adjust cost.

## Assistant Guidance

Ask for the current Walksheds version and edge sample when a field is unavailable.

## Related Concepts

- [What is the custom cost-function contract?](walkshed-custom-cost-function-contract.md)
