---
uid: d0ab91b6-e1a1-4cff-93e0-280a250ad81f
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
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
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
    - assistant/os-connect/concept/destination-access-analysis.md
    - assistant/cross-platform/concept/ada-compliance-boundaries.md
tags:
    - Assistant
---

<!-- @format -->

# Can OS-CONNECT support pedestrian access analysis around destinations?

## Short Answer

Yes. Select an appropriate TDEI pedestrian-network dataset in Walksheds; use OS-CONNECT when its geographic scope and data are suitable for the question. Walksheds estimates areas reachable from destinations such as schools, clinics, grocery stores, parks, and transit stops.

## Significance

Straight-line buffers show proximity, not whether a connected pedestrian route exists. Network-based analysis can reveal differences caused by disconnected sidewalks, crossings, slopes, stairs, curb conditions, and other mapped barriers. This supports transportation-equity, public-health, and infrastructure-planning decisions.

## What This Means

The Walksheds tool calculates the area reachable from an origin or destination within a selected travel-time or cost budget, using the TDEI dataset selected in the tool.

## What This Does Not Mean

An analysis based on a TDEI dataset does not establish that a destination or route is necessarily accessible, safe, ADA compliant, or current. A straight-line buffer represents proximity, not whether a connected pedestrian route exists. Missing attributes do not prove that barriers are absent. Construction, surface conditions, weather, debris, signal timing, lighting, and other local conditions may not be represented. Use field verification, engineering review, local inventories, and community input before making operational or legal conclusions.

## How To Use This

1. Identify destinations and select a relevant TDEI pedestrian-network dataset; use OS-CONNECT if its coverage fits the analysis area.
2. Generate Walksheds for each destination or origin using appropriate travel budgets and mobility profiles.
3. Compare destinations, neighborhoods, or populations and note possible gaps in connectivity or mapped accessibility features.
4. Inspect priority routes with AccessMap.
5. Validate important findings with local knowledge, field review, or community input before using them to prioritize investments or support planning applications.

## Example

A jurisdiction selects an OS-CONNECT dataset that covers its analysis area and compares modeled access to clinics and grocery stores for different profiles. The team uses AccessMap to inspect priority routes, then validates findings in the field before proposing improvements. The analysis informs planning; it does not certify ADA compliance.

## Assistant Guidance

Say that a suitable TDEI pedestrian-network dataset, including OS-CONNECT when appropriate, can support destination-based analysis, with Walksheds for reachability and AccessMap for route inspection. Explain that results depend on the selected dataset, update date, destinations, profile, and field validation. Cite this article when used, qualify answers when context is missing, and avoid definitive claims about accessibility, safety, compliance, completeness, or currency.

## Related Concepts

- [Walksheds knowledge base](../../walksheds/index.md)
- [AccessMap knowledge base](../../accessmap/index.md)
- [OS-CONNECT knowledge base](../index.md)
- [ADA compliance boundaries](../../cross-platform/concept/ada-compliance-boundaries.md)
