---
uid: e0fd2c85-f94d-4b70-8611-8fcd5f57c385
title: How do mobility profiles work?
slug: mobility-profiles
doc_type: concept
questions:
    - How do mobility profiles work?
audiences:
    - public
    - advocate
products:
    - AccessMap
topics:
    - accessmap
    - mobility-profiles
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-06-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A profile encodes a user's medical diagnosis or legally protected status.
related_pages:
    - assistant/cross-platform/concept/accessmap-routing.md
    - accessmap/user-manual/profiles.md
tags:
    - Assistant
---

<!-- @format -->

# How do mobility profiles work?

## Short Answer

Mobility profiles bundle default assumptions about which network features are acceptable or costly — for example related to slope or surface — so routing matches common needs. Users can adjust preferences within the app where supported.

## Significance

Profiles are the main lever for trustworthy answers about "why my route changed."

## What This Means

Profiles change which edges are traversable or how expensive they are in the routing graph. Documented profiles include Manual wheelchair, Powered wheelchair, Support cane, BLV, and Custom. The Custom profile exposes controls for uphill and downhill steepness, street avoidance, barrier avoidance, noise avoidance, landmark distance, and screen-reader alerts. Profiles are modeling aids, not clinical classifications.

## What This Does Not Mean

- Not an exhaustive model of every assistive device or condition.
- Not identical to Walksheds preference naming even when concepts rhyme — cross-link carefully.

## How To Use This

Select the profile closest to the user's primary mobility consideration, then customize settings when needed. Cite the [AccessMap User Manual's profiles section](../../../accessmap/user-manual/profiles.md) for authoritative UI behavior.

## Example

Switching to the Manual wheelchair profile, or lowering the maximum uphill grade in Custom, can exclude steeper segments and reroute a trip through a flatter corridor.

## Assistant Guidance

Encourage experimentation with profiles and preferences, and abstain from medical tailoring language.

## Related Concepts

- [Accessibility preference routing](accessibility-preference-routing.md)
- [Why does AccessMap choose longer routes?](accessible-routes-appear-longer.md)
