---
uid: 74738161-a13a-4d27-8b30-fbc9ec4f5889
title: Why do accessibility-aware routes sometimes appear longer?
slug: accessible-routes-appear-longer
doc_type: concept
questions:
    - Why do accessibility-aware routes sometimes appear longer?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
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
        - A longer route is always more accessible.
        - The shortest route is always the best route for every traveler.
related_pages:
    - assistant/accessmap/concept/longer-route-selection.md
    - assistant/accessmap/concept/routing-tradeoffs.md
    - assistant/accessmap/concept/accessibility-preference-routing.md
tags:
    - Assistant
---

<!-- @format -->

# Why do accessibility-aware routes sometimes appear longer?

## Short Answer

An accessibility-aware route may be longer because the selected profile assigns additional cost to conditions such as steep slopes, missing curb-ramp information, or other mapped barriers. Route length is only one part of the tradeoff.

## Significance

Explaining longer routes helps users understand that the model may prioritize a different accessibility objective than shortest-distance routing.

## What This Means

- Compare the same origin, destination, profile, and dataset.
- Review which preferences or penalties changed the route.
- Verify the important conditions locally.

## What This Does Not Mean

Longer does not automatically mean more accessible, safe, or comfortable, and shorter does not automatically mean unsuitable. A route remains dependent on data and model assumptions.

## How To Use This

State the profile and factors affecting cost when explaining the result, and cite current routing guidance.

## Example

A wheelchair-oriented profile avoids a steep segment and missing curb-ramp information, producing a longer route than a general walking profile.

## Assistant Guidance

Do not rank routes by length alone. Ask for the profile and route context, cite the assumptions, and abstain from claiming usability without verification.

## Related Concepts

- [Longer route selection](longer-route-selection.md)
- [Routing tradeoffs](routing-tradeoffs.md)
- [Accessibility-preference routing](accessibility-preference-routing.md)
