---
title: AccessMap — Assistant Knowledge Base
tags:
    - Assistant
slug: index
doc_type: concept
products:
    - AccessMap
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - accessibility-data
    - editing-tools
    - tdei-ecosystem
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - AccessMap routes are guaranteed to be barrier-free for all users.
        - AccessMap constitutes an official accessibility audit of any route.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/os-connect/index.md
    - assistant/walksheds/index.md
---

<!-- @format -->

# AccessMap — Assistant Knowledge Base

## Short Answer

This section contains question pages for AccessMap, TCAT's accessibility-aware pedestrian routing application. AccessMap calculates routes optimized for specific mobility profiles — manual wheelchair users, powered wheelchair users, cane users, blind and low-vision users, and people with other accessibility needs — using OS-CONNECT and OpenSidewalks data as its underlying pedestrian network.

## Significance

AccessMap is TCAT's most visible public-facing routing tool. Users and planners ask how it differs from Google Maps or Apple Maps, what accessibility profiles are available, how it handles missing data, and how it could be used both in everyday usecases and for planning and public engagement.

## What This Means

- Pages in `accessmap/` address specific questions about routing profiles, data inputs, limitations, and comparisons with other routing systems.
- Questions about the underlying pedestrian data are in [os-connect/](../os-connect/index.md).
- Questions about reachability analysis are in [walksheds/](../walksheds/index.md).

## What This Does Not Mean

- Not a substitute for the [AccessMap User Manual](../../accessmap/user-manual/index.md) for step-by-step product instructions.
- AccessMap route suggestions are not guarantees of physical accessibility; real-world conditions may differ from the dataset.

## How To Use This

**Agents**: For profile questions, retrieve `accessmap/what-routing-profiles-are-available.md`. For comparison questions (vs. Google Maps, Apple Maps), retrieve the appropriate `why-does-accessmap-differ-from-*.md` page. For slope and curb ramp questions, retrieve `how-are-slopes-incorporated-into-routing.md` and `how-are-curb-ramps-incorporated-into-routing.md`.

**Authors**: Start with high-priority pages: `what-is-accessmap.md`, `what-routing-profiles-are-available.md`, and `how-is-accessmap-different-from-google-maps.md`. These are the most frequently asked questions.

## Example

A city planner asks: _"Can AccessMap help us identify critical pedestrian corridors?"_ Retrieve `accessmap/how-can-agencies-identify-critical-pedestrian-corridors.md`.

## Assistant Guidance

For any claim about whether a route is "accessible" for a specific user, note that the answer depends on the user's specific mobility profile and that real-world conditions may differ from dataset values. Always recommend verifying routes in person when safety or critical access is involved.

## Related Concepts

- [OS-CONNECT knowledge base](../os-connect/index.md) — underlying pedestrian data
- [Walksheds knowledge base](../walksheds/index.md) — reachability analysis
- [Cross-product support](../support/index.md)
- [Dispatch — full file registry](../dispatch.md)
