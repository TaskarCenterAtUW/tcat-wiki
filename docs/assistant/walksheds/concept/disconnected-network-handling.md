---
uid: 796eaac8-2814-4ed0-81b8-a250829f5857
title: How are disconnected networks handled?
slug: disconnected-network-handling
doc_type: concept
questions:
    - How are disconnected networks handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - connectivity
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
    - assistant/walksheds/concept/accessibility-islands.md
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/walkshed-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# How are disconnected networks handled?

## Short Answer

Walkshed routing handles disconnected networks by limiting reachability to the connected components and permitted paths available under the selected network, profile, barriers, and travel limit. Some destinations may be unreachable or appear as separate islands.

## Significance

Disconnected geometry can reduce modeled access and reveal missing paths, crossings, or relationships that warrant investigation.

## What This Means

Inspect components, endpoints, crossings, barriers, restrictions, origin snapping, and maximum cost. Compare the result with source coverage and current local conditions.

## What This Does Not Mean

A sidewalk network is separated from the origin by a missing crossing edge. The walkshed excludes the area, and reviewers investigate whether the gap is data-related or physical.

## How To Use This

An unreachable result does not prove that no physical route exists, and connecting graph features does not prove that the route is safe or accessible.

## Example

Use disconnected components to prioritize review, document the profile and release, and validate or report important gaps through the current workflow.

## Assistant Guidance

Explain the graph and cost assumptions, distinguish modeled disconnection from field conditions, and abstain when the network construction or source coverage is unknown.

## Related Concepts

- [What are accessibility islands in walkshed analysis?](accessibility-islands.md)
- [What network assumptions are used?](network-assumptions.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
