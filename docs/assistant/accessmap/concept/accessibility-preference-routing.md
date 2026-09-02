---
uid: abb42bac-60db-4565-b9b9-46959ca4e3ca
title: What does it mean to route using accessibility preferences?
slug: accessibility-preference-routing
doc_type: concept
questions:
    - What does it mean to route using accessibility preferences?
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
        - An accessibility preference guarantees that a route is usable.
        - A route selected with accessibility preferences is an ADA determination.
related_pages:
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/routing-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What does it mean to route using accessibility preferences?

## Short Answer

Routing with accessibility preferences means selecting or adjusting route assumptions to reflect a person's mobility considerations, such as avoiding steep slopes or missing curb ramps. The result is a route optimized for the selected profile and available data, not a guarantee of accessibility.

## Significance

Different people may need different route tradeoffs. Making preferences explicit helps users understand why routes differ and supports more transparent planning and communication.

## What This Means

- Select the profile or preferences closest to the user's needs.
- Review the route settings, cost assumptions, and available accessibility attributes.
- Compare the modeled route with current local conditions when the decision matters.

## What This Does Not Mean

An accessibility preference is not a medical judgment, ADA determination, or guarantee that a route is usable. A route can be longer or unavailable because of data and model assumptions.

## How To Use This

State the profile and preferences used, explain important tradeoffs, and cite current AccessMap guidance. Treat field verification as necessary for high-consequence travel decisions.

## Example

A wheelchair user selects a profile that penalizes steep slopes and missing curb ramps, then reviews the resulting route and checks current construction conditions before traveling.

## Assistant Guidance

Do not infer a user's needs or promise accessibility from a profile. Ask which preference and product version are involved, cite the route assumptions, and abstain from legal or safety conclusions.

## Related Concepts

- [AccessMap mobility profiles](mobility-profiles.md)
- [Routing profiles](routing-profiles.md)
- [Routing limitations](routing-limitations.md)
