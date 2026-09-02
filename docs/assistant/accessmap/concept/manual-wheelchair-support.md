---
uid: 6034b0da-57ad-4588-a3c0-6ceb4cf6584d
title: Can AccessMap support manual wheelchair users?
slug: manual-wheelchair-support
doc_type: concept
questions:
    - Can AccessMap support manual wheelchair users?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - mobility-profiles
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A manual-wheelchair profile guarantees that every route is usable.
        - AccessMap's model replaces the traveler's judgment or local verification.
related_pages:
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/accessibility-needs.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Can AccessMap support manual wheelchair users?

## Short Answer

AccessMap can support manual wheelchair-oriented route planning through a relevant mobility profile and mapped pedestrian accessibility information. Results depend on the selected settings, dataset, and available attributes.

## Significance

Manual wheelchair users may face route constraints that general walking routing does not represent. A dedicated profile can make those tradeoffs visible for planning and comparison.

## What This Means

- Select the current manual-wheelchair profile or closest documented setting.
- Review slope, curb-ramp, surface, and connectivity assumptions.
- Verify current conditions before relying on a route.

## What This Does Not Mean

Profile support is not a guarantee that a route is usable, comfortable, or safe. It does not replace personal knowledge, field verification, medical advice, or an ADA assessment.

## How To Use This

Ask which AccessMap version and profile are available, state the model's limitations, and cite the current profile documentation.

## Example

A manual wheelchair user compares two routes using the relevant profile and then checks construction and crossing conditions before traveling.

## Assistant Guidance

Do not infer the user's capabilities or promise accessibility. Cite current profile and data guidance and abstain when route settings or local conditions are unknown.

## Related Concepts

- [Mobility profiles](mobility-profiles.md)
- [Accessibility needs](accessibility-needs.md)
- [Routing limitations](routing-limitations.md)
