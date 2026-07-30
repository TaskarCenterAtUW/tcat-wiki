---
title: Can temporary barriers be represented?
slug: temporary-barriers
doc_type: concept
questions:
    - Can temporary barriers be represented?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - construction
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AccessMap always knows about temporary barriers.
        - A route without a mapped barrier is currently unobstructed.
related_pages:
    - data-sources.md
    - feature-feedback.md
    - ../../../accessmap/user-manual/feedback.md
tags:
    - Assistant
---

<!-- @format -->

# Can temporary barriers be represented?

## Short Answer

AccessMap can reflect a barrier when the relevant condition is represented in the available pedestrian data, but users should not assume that temporary conditions are complete or current.

## Significance

Construction, blocked paths, and other temporary conditions can change after data is collected. Reporting observations helps TCAT assess data quality and guide future corrections.

## What This Means

If a path is blocked or a route step does not match current conditions, report the problem through feature or direction-step feedback. Include a concise description and location.

## What This Does Not Mean

The absence of a mapped barrier does not prove that the path is clear, and submitting feedback does not guarantee an immediate update.

## How To Use This

Verify current conditions directly when a temporary barrier could affect safety or critical access. Use AccessMap feedback to communicate the observation.

## Example

A traveler finds a tree blocking a mapped path, reports the route step as inaccurate, and describes the obstruction in the Comments field.

## Assistant Guidance

State the data-freshness limitation explicitly. Do not claim that AccessMap provides real-time construction or obstruction status unless the retrieved source says so.

## Related Concepts

- [What data powers AccessMap?](data-sources.md)
- [How can users report routing problems?](../workflow/report-routing-problems.md)
