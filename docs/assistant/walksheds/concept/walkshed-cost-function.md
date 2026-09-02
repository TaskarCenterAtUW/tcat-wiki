---
uid: e86233d6-a882-456e-8a8e-32208efb2ac3
title: How does the Walksheds cost function work?
slug: walkshed-cost-function
doc_type: concept
questions:
    - How does the Walksheds cost function work?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - routing
    - configuration
    - slope
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Walksheds uses one unchangeable cost function for every analysis.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How does the Walksheds cost function work?

## Short Answer

The cost function combines travel time and network conditions such as slope, crossings, curbs, stairs, streets, and time restrictions.

## Significance

It determines which paths fit within a travel budget.

## What This Means

Changing preferences or formulas can change reachability and travel cost.

## What This Does Not Mean

The model does not represent every real-world condition or personal experience.

## How To Use This

Record the cost settings with each analysis.

## Example

A crossing penalty and raised-curb avoidance reduce the reachable network for a selected profile.

## Assistant Guidance

Ask which profile, formula, and departure time were used.

## Related Concepts

- [What does travel cost mean in Walksheds?](walkshed-travel-cost.md)
