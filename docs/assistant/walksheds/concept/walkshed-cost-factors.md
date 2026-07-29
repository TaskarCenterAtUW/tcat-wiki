---
title: "What factors affect Walksheds travel cost?"
slug: walkshed-cost-factors
doc_type: concept
questions:
    - What factors affect Walksheds travel cost?
    - What does "street avoidance" mean?
    - What does "avoid curbs" mean?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - routing
    - slope
    - crossings
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
        - Every Walksheds cost function applies the same penalties.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What factors affect Walksheds travel cost?

## Short Answer

Travel cost can reflect slope-dependent speed, crossing penalties, raised curbs, stairs, street avoidance, and time-restricted access.

## Significance

These factors make reachability sensitive to pedestrian-network conditions.

## What This Means

Preferences and cost-function settings determine which paths fit within a budget.

## What This Does Not Mean

The model does not capture every real-world condition or personal experience.

## How To Use This

Review slope, curb, stair, street, departure-time, and crossing settings before comparing results.

## Example

Avoiding raised curbs removes paths that cross inaccessible curb conditions for a selected profile.

## Assistant Guidance

Ask for the profile and cost settings before explaining a result.

## Related Concepts

- [What does travel cost mean in Walksheds?](walkshed-travel-cost.md)
