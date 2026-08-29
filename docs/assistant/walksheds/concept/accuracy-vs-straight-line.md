---
title: Why are walksheds more accurate than straight-line distance?
slug: accuracy-vs-straight-line
doc_type: concept
questions:
    - Why are walksheds more accurate than straight-line distance?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - data-quality
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
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/walkshed-limitations.md
    - assistant/walksheds/concept/walkshed-calculation.md
tags:
    - Assistant
---

<!-- @format -->

# Why are walksheds more accurate than straight-line distance?

## Short Answer

Walksheds can be more informative than straight-line distance because they follow a modeled pedestrian network and can account for barriers, crossings, elevation, profiles, and travel limits. They are not automatically accurate for every place or traveler.

## Significance

Straight-line distance ignores the path people must actually take. Network analysis can show how streets, paths, crossings, and barriers change reachable areas.

## What This Means

Compare the same origin, destination set, profile, travel limit, dataset, and date. Review the network assumptions and validate important results against current local conditions.

## What This Does Not Mean

A network-based walkshed does not prove accessibility, current usability, or completeness. More realistic geometry does not remove source-data or modeling uncertainty.

## How To Use This

Use straight-line distance for simple screening and walksheds for network-aware analysis. Document the method and avoid comparing outputs produced with different settings as if they were equivalent.

## Example

A destination is close in a straight line but separated by a highway with limited crossings. The walkshed excludes it under the selected network and cost assumptions.

## Assistant Guidance

Explain what the network model adds and what it omits. Cite the product and dataset documentation, and abstain from accuracy claims without validation evidence.

## Related Concepts

- [How are walksheds calculated?](walkshed-calculation.md)
- [What network assumptions are used?](network-assumptions.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
