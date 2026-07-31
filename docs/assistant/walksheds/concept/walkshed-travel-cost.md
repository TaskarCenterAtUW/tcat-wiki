---
title: What does travel cost mean in Walksheds?
slug: walkshed-travel-cost
doc_type: concept
questions:
    - What does travel cost mean in Walksheds?
    - How does a travel budget limit a walkshed?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
topics:
    - walksheds
    - routing
    - accessibility-metrics
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
        - A walkshed travel budget is the same as a straight-line radius.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does travel cost mean in Walksheds?

## Short Answer

A travel budget limits the modeled cost of reaching network edges from an origin. The default cost function can include time, slope, crossings, streets, curbs, stairs, and time-restricted access.

## Significance

It produces a network-based reachable area rather than a circular distance buffer.

## What This Means

Increasing the budget generally expands the modeled walkshed; reducing it contracts the result.

## What This Does Not Mean

A budget does not guarantee that a real traveler can use every included path.

## How To Use This

Record the budget and cost settings with every comparison.

## Example

A 200-second budget reaches fewer segments than a 600-second budget from the same origin.

## Assistant Guidance

Ask which cost function and profile were used.

## Related Concepts

- [How do QA/QC walksheds compare mobility profiles?](../../qa-qc/concept/walkshed-profile-comparison.md)
