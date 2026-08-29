---
title: What are accessibility islands in walkshed analysis?
slug: accessibility-islands
doc_type: concept
questions:
    - What are accessibility islands in walkshed analysis?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - accessibility-data
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
    - assistant/walksheds/concept/disconnected-network-handling.md
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/walkshed-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What are accessibility islands in walkshed analysis?

## Short Answer

An accessibility island is an area reachable within a walkshed's selected profile and travel limit but separated from other reachable areas or the broader network by modeled barriers, missing connections, or cost thresholds.

## Significance

Islands can reveal places where network structure or accessibility assumptions limit modeled reachability and where additional data review or infrastructure investigation may be useful.

## What This Means

Interpret an island using the walkshed's origin, profile, maximum cost, network, barriers, and dataset version. Inspect nearby crossings, endpoints, and missing or restricted connections.

## What This Does Not Mean

An island does not prove that a real-world area is inaccessible, isolated, or underserved. It may reflect missing data, a modeling threshold, or a temporary condition.

## How To Use This

Use islands as screening indicators, compare profiles and scenarios, validate important locations locally, and state the assumptions next to any map or conclusion.

## Example

A walkshed shows a small reachable component across a roadway. Reviewers inspect the crossing data and field conditions before describing it as a network gap.

## Assistant Guidance

Name the profile, travel limit, network, and release. Avoid treating an island as a judgment about residents or places, and abstain when the analysis assumptions are missing.

## Related Concepts

- [How are disconnected networks handled?](disconnected-network-handling.md)
- [What network assumptions are used?](network-assumptions.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
