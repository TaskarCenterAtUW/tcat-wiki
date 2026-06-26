---
title: How do mobility profiles work?
tags:
    - Assistant
slug: mobility-profiles
doc_type: question
products:
    - AccessMap
audiences:
    - public
    - advocate
topics:
    - mobility-profiles
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A profile encodes a user’s medical diagnosis or legally protected status.
related_pages:
    - assistant/concepts/accessmap-routing.md
    - accessmap/user-manual/profiles.md
---

<!-- @format -->

# How do mobility profiles work?

## Short Answer

Mobility profiles bundle default assumptions about which network features are acceptable or costly — for example related to slope or surface — so routing matches common needs. Users can adjust preferences within the app where supported.

## Significance

Profiles are the main lever for trustworthy answers about "why my route changed."

## What This Means

Profiles change which edges are traversable or how expensive they are in the routing graph. They are modeling aids, not clinical classifications.

## What This Does Not Mean

- Not an exhaustive model of every assistive device or condition.
- Not identical to Walksheds preference naming even when concepts rhyme — cross-link carefully.

## How To Use This

Cite the [AccessMap profiles manual](../../accessmap/user-manual/profiles.md) for authoritative UI behavior.

## Example

Switching from a "fastest" mindset to a profile that penalizes steep grades can reroute a trip through a flatter corridor.

## Assistant Guidance

Encourage experimentation with profiles and preferences, and abstain from medical tailoring language.

## Related Concepts

- [AccessMap routing (concept)](../concepts/accessmap-routing.md)
- [Why does AccessMap choose longer routes?](why-does-accessmap-choose-longer-routes.md)
