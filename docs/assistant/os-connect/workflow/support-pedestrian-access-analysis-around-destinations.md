---
title: Can OS-CONNECT support pedestrian access analysis around destinations?
slug: support-pedestrian-access-analysis-around-destinations
doc_type: workflow
questions:
    - Can OS-CONNECT support pedestrian access analysis around destinations?
    - How can I use OS-CONNECT to analyze access around destinations?
products:
    - OS-CONNECT
    - Walksheds
    - AccessMap
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - os-connect
    - walksheds
    - accessmap
    - destinations
    - mobility-profiles
    - planning
    - connectivity
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-24
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - OS-CONNECT proves that a destination is accessible.
        - OS-CONNECT data guarantees current field conditions.
        - A walkshed result is equivalent to an ADA compliance determination.
        - Straight-line distance is sufficient for pedestrian access analysis.
related_pages:
    - assistant/os-connect/index.md
    - assistant/walksheds/index.md
    - assistant/accessmap/index.md
    - assistant/cross-platform/concept/destination-access-analysis.md
    - assistant/cross-platform/concept/ada-compliance-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# Can OS-CONNECT support pedestrian access analysis around destinations?

## Short Answer

Yes. Use OS-CONNECT as the pedestrian network dataset and Walksheds to estimate areas reachable from destinations such as schools, clinics, grocery stores, parks, and transit stops.

## Significance

Straight-line buffers show proximity, not whether a connected pedestrian route exists. Network-based analysis can reveal differences caused by disconnected sidewalks, crossings, slopes, stairs, curb conditions, and other mapped barriers. This supports transportation-equity, public-health, and infrastructure-planning decisions.

## What This Means

The Walksheds tool calculates the area reachable from an origin or destination within a selected travel-time or cost budget, using OS-CONNECT as the underlying source dataset.

## What This Does Not Mean

An analysis based on OS-CONNECT data does not establish that a destination or route is necessarily accessible, safe, ADA compliant, or current. Missing attributes do not prove that barriers are absent. Construction, surface conditions, weather, debris, signal timing, lighting, and other local conditions may not be represented. Use field verification, engineering review, local inventories, and community input before making operational or legal conclusions.

## How To Use This

1. Identify destinations and select the relevant OS-CONNECT subset dataset from the TDEI.
2. Generate Walksheds for each destination or origin using appropriate travel budgets and mobility profiles.
3. Compare destinations, neighborhoods, or populations and note possible gaps in connectivity or mapped accessibility features.
4. Inspect priority routes with AccessMap.
5. Validate important findings with local knowledge, field review, or community input before using them to prioritize investments or support planning applications.

## Example

A jurisdiction uses OS-CONNECT data to compare access to clinics and grocery stores for walking and wheelchair profiles. Walksheds show that some nearby neighborhoods have limited network reach because of gaps in the pedestrian network, such as missing sidewalks and crossings. The team uses AccessMap to inspect priority routes, then validates the findings in the field before proposing improvements. The analysis informs planning; it does not certify ADA compliance.

## Assistant Guidance

Say that OS-CONNECT can provide the network dataset for destination-based analysis, with the Walksheds tool for reachability and AccessMap for route inspection. Explain that results depend on the dataset, update date, destination choices, mobility profile, and field validation. Cite this article when used, qualify answers when that context is missing, and avoid definitive claims about accessibility, safety, compliance, completeness, or currency.

## Related Concepts

- [Walksheds knowledge base](../../walksheds/index.md)
- [AccessMap knowledge base](../../accessmap/index.md)
- [OS-CONNECT knowledge base](../index.md)
- [ADA compliance boundaries](../../cross-platform/concept/ada-compliance-boundaries.md)
