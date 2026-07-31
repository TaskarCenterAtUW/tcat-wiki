---
title: How does the default Walksheds cost model work?
slug: walkshed-default-cost-model
doc_type: concept
questions:
    - How does the default Walksheds cost model work?
    - How does Walksheds estimate travel cost?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - accessibility-metrics
    - assumptions
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds estimated cost is a guaranteed travel time for a person.
related_pages:
    - walkshed-cost-function.md
    - walkshed-cost-factors.md
    - ../../../walksheds/user-manual/preferences.md
tags:
    - Assistant
---

<!-- @format -->

# How does the default Walksheds cost model work?

## Short Answer

The documented default model calculates edge cost as a street-cost factor multiplied by length divided by modeled speed. Speed changes with slope and profile assumptions.

## Significance

The model explains why equal-distance routes can have different modeled costs and why profiles change reachable area.

## What This Means

Base speeds documented for Walking, Manual wheelchair, and Powered wheelchair are 1.3, 0.6, and 2.0 meters per second. Steps use a fixed 0.5 meters per second in the current guide. Slope modifies speed, while crossing and street penalties can add cost.

## What This Does Not Mean

These values are model assumptions, not individual travel measurements or guarantees.

## How To Use This

Record profile, slope limits, penalties, dataset version, and custom function when comparing results.

## Example

A steep edge may cost more than a flat edge of the same length because modeled speed is reduced.

## Assistant Guidance

State that the result is an estimated model and cite the current implementation documentation.

## Related Concepts

- [What is the walkshed travel cost?](walkshed-travel-cost.md)
- [How do accessibility profiles work?](accessibility-profiles.md)
