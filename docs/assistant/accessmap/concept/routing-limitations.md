---
uid: c7896de9-9fac-422e-a7f2-e8bc15e4d5f0
title: What are the limitations of AccessMap routing?
slug: routing-limitations
doc_type: concept
questions:
    - What are the limitations of AccessMap routing?
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
    - limitations
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
        - AccessMap guarantees that a route is accessible or safe.
        - A route result reflects all current physical conditions.
related_pages:
    - assistant/accessmap/concept/accessibility-assumptions.md
    - assistant/accessmap/concept/missing-accessibility-data.md
    - assistant/accessmap/concept/route-calculation.md
tags:
    - Assistant
---

<!-- @format -->

# What are the limitations of AccessMap routing?

## Short Answer

AccessMap routing is limited by the quality, completeness, freshness, and interpretation of pedestrian-network data, as well as by the selected profile and routing model. A route is a modeled result, not a guarantee of current access.

## Significance

Understanding limits helps users make responsible decisions and helps agencies identify where better data or field validation is needed.

## What This Means

- Check the source dataset, date, profile, and preferences.
- Look for missing attributes, disconnected segments, construction, and local conditions.
- Verify important routes and report suspected data or product problems.

## What This Does Not Mean

The presence of a route does not prove accessibility, safety, ADA compliance, or current physical availability. No route does not prove that walking is impossible.

## How To Use This

State the relevant limitation next to the route result and cite current product and dataset guidance. Recommend local or professional verification for high-consequence decisions.

## Example

A route avoids a crossing because curb-ramp data are missing, but a field check finds a temporary condition not in the dataset. The user treats both the model and field observation as necessary context.

## Assistant Guidance

Do not overstate route confidence. Ask for the location, profile, dataset version, and observed condition, and abstain from safety or legal conclusions.

## Related Concepts

- [Accessibility assumptions](accessibility-assumptions.md)
- [Missing accessibility data](missing-accessibility-data.md)
- [How AccessMap calculates routes](route-calculation.md)
