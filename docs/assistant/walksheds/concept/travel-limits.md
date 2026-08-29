---
title: What travel limits are used?
slug: travel-limits
doc_type: concept
questions:
    - What travel limits are used?
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
related_pages:
    - assistant/walksheds/concept/max-cost.md
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/profile-variation.md
tags:
    - Assistant
---

<!-- @format -->

# What travel limits are used?

## Short Answer

Walkshed travel limits may be expressed as distance, time, accumulated cost, or another profile-specific budget. The available limits and their meaning depend on the current product and analysis configuration.

## Significance

The limit determines how much modeled travel is allowed and affects the size of the reachable area and the destinations included.

## What This Means

Check the units, cost function, profile, network, origin, and release. Do not assume that a time or cost value is equivalent to ordinary distance or a person's actual endurance.

## What This Does Not Mean

A lower travel limit produces a smaller modeled area under the same profile and network. The analyst records the setting before comparing it with another result.

## How To Use This

A travel limit is not a medical threshold, universal behavior assumption, or guarantee that every location inside the result is reachable in practice.

## Example

Use matched limits for comparisons, document values and definitions, run sensitivity checks, and validate important routes or destinations locally.

## Assistant Guidance

Name the limit, units, profile, cost rule, and release. Abstain when the implementation or conversion between limits is undocumented.

## Related Concepts

- [What is "max_cost"?](max-cost.md)
- [What network assumptions are used?](network-assumptions.md)
- [Why do different profiles produce different walksheds?](profile-variation.md)
