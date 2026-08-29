---
title: 'What does "avoid steep slopes" mean?'
slug: avoid-steep-slopes
doc_type: concept
questions:
    - What does "avoid steep slopes" mean?
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
        - Avoiding steep slopes guarantees a route is comfortable or usable.
        - The setting uses a universally correct slope threshold.
related_pages:
    - assistant/accessmap/concept/slope-routing.md
    - assistant/accessmap/concept/steep-slopes-effect.md
    - assistant/accessmap/concept/accessibility-preference-routing.md
tags:
    - Assistant
---

<!-- @format -->

# What does "avoid steep slopes" mean?

## Short Answer

"Avoid steep slopes" is a routing preference that increases the cost of, or avoids, segments with steep modeled slopes when the current AccessMap implementation and selected profile support it. It does not mean that every steep segment is removed from every route.

## Significance

Slope preferences help users express a route tradeoff that matters for mobility and endurance. They also explain why a route may be longer than a general walking route.

## What This Means

- Select the preference when steep grades are a concern.
- Review the resulting route and the profile used.
- Treat slope information as modeled data and verify important conditions locally.

## What This Does Not Mean

The setting does not guarantee a flat, accessible, or safe route. Missing or inaccurate slope data can affect the result, and the appropriate threshold varies by person and context.

## How To Use This

Explain the preference as a model setting, not a promise. Cite current AccessMap documentation and avoid claiming an exact threshold unless the version-specific source states it.

## Example

A traveler enables the preference and receives a longer route with lower modeled slope exposure, then checks the route for current construction and surface conditions.

## Assistant Guidance

Ask which profile, version, and location are involved. Do not promise a particular route or threshold, and abstain from accessibility or safety conclusions based on the setting alone.

## Related Concepts

- [How slopes are incorporated into routing](slope-routing.md)
- [How steep slopes affect route selection](steep-slopes-effect.md)
- [Accessibility-preference routing](accessibility-preference-routing.md)
