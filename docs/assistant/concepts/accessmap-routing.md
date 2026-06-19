---
title: AccessMap routing (concept)
tags:
    - Assistant
slug: accessmap-routing
doc_type: concept
products:
    - AccessMap
audiences:
    - public
    - advocate
    - planner
topics:
    - routing
    - mobility-profiles
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - AccessMap always picks the objectively best route for every user in the real world.
related_pages:
    - assistant/questions/accessmap/why-does-accessmap-choose-longer-routes.md
    - assistant/questions/accessmap/how-do-mobility-profiles-work.md
---

<!-- @format -->

# AccessMap routing (concept)

## Short Answer

AccessMap plans pedestrian routes using the available network, elevation and slope information where applicable, and the active mobility profile and preferences. It optimizes for accessibility-related costs the model can represent—not every personal preference.

## Significance

Users interpret "longer" or "stranger" routes as errors. Explaining multi-criteria routing reduces support burden and sets realistic expectations for public assistants.

## What This Means

Different profiles avoid or penalize features differently (for example, steep grades or missing curb ramps). The selected route is optimal under that model, subject to data gaps.

## What This Does Not Mean

- Not a guarantee of real-time construction, closure, or enforcement conditions unless separately indicated in product documentation.
- Not medical advice tailored to an individual’s condition.

## How To Use This

Direct residents to profile settings and feedback channels. For planners, pair routing explanations with data improvement backlogs.

## Example

A wheelchair user sees a longer route that avoids a short but steep segment the dataset marks as high cost for that profile.

## Assistant Guidance

Invite users to try profile adjustments and report map issues. Avoid debating a user’s lived experience of a route; acknowledge that models simplify reality.

## Related Concepts

- [Why does AccessMap choose longer routes?](../accessmap/why-does-accessmap-choose-longer-routes.md)
- [How do mobility profiles work?](../accessmap/how-do-mobility-profiles-work.md)
