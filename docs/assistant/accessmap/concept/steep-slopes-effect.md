---
uid: 0807e1e4-f16b-4165-96fa-fae2fbe682b2
title: How do steep slopes affect route selection?
slug: steep-slopes-effect
doc_type: concept
questions:
    - How do steep slopes affect route selection?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - slope
    - routing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A steep-slope result proves that a route is unusable.
        - A lower-slope route is automatically safer or accessible.
related_pages:
    - assistant/accessmap/concept/slope-routing.md
    - assistant/accessmap/concept/avoid-steep-slopes.md
    - assistant/accessmap/concept/accessible-routes-appear-longer.md
tags:
    - Assistant
---

<!-- @format -->

# How do steep slopes affect route selection?

## Short Answer

Steep slopes can increase route cost or cause a profile to prefer another path when slope information is available. The effect depends on the profile, settings, and quality of the underlying data.

## Significance

Slope can matter for mobility devices, endurance, and route comfort. It is one reason an accessibility-aware route may be longer than a general walking route.

## What This Means

- Identify the slope source, profile, and preference.
- Compare the modeled route with available local or field information.
- Record missing or uncertain elevation information.

## What This Does Not Mean

Modeled slope does not establish usability, comfort, safety, or compliance. Missing slope information does not prove a segment is level.

## How To Use This

Explain slope as one factor among several and cite the current model documentation.

## Example

A profile avoids a steep modeled segment and selects a longer route; the user checks the actual grade and surface before traveling.

## Assistant Guidance

Do not state that a route is accessible based on slope alone. Ask for profile and version context, and abstain from exact thresholds without a cited source.

## Related Concepts

- [How slopes are incorporated](slope-routing.md)
- [Avoid steep slopes](avoid-steep-slopes.md)
- [Why accessible routes can be longer](accessible-routes-appear-longer.md)
