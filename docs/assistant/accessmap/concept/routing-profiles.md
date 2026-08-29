---
title: What routing profiles are available?
slug: routing-profiles
doc_type: concept
questions:
    - What routing profiles are available?
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
        - A routing profile guarantees that a route is accessible for every user.
        - The available profiles are identical across every AccessMap version.
related_pages:
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/accessibility-preference-routing.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What routing profiles are available?

## Short Answer

AccessMap routing profiles represent different accessibility considerations for route calculation. The current documented profiles include Manual wheelchair, Powered wheelchair, Support cane, BLV, and Custom. Names and settings remain version-sensitive, so users should consult the current AccessMap documentation before relying on a specific option.

## Significance

Profiles let users compare route results under different assumptions instead of treating one walking route as suitable for everyone.

## What This Means

- Select the profile closest to the traveler's mobility consideration. Current documented options include Manual wheelchair, Powered wheelchair, Support cane, BLV, and Custom.
- Review the profile's preferences and route-cost assumptions.
- Record the profile and product version when comparing or sharing results.

## What This Does Not Mean

A profile is not a medical classification, accessibility certification, or guarantee that a route is usable. A profile cannot compensate for missing or outdated network data.

## How To Use This

Use the current AccessMap manual or profile documentation for exact names and controls. Explain differences as modeled tradeoffs and verify current conditions for important trips.

## Example

A planner compares a general pedestrian route with a wheelchair-oriented profile and sees that the selected profile changes the preferred path around a modeled slope.

## Assistant Guidance

Cite the current profile documentation and ask for the product version. Do not invent profile names or capabilities, and abstain when the current profile list is unavailable.

## Related Concepts

- [Mobility profiles](mobility-profiles.md)
- [Accessibility-preference routing](accessibility-preference-routing.md)
- [Routing limitations](routing-limitations.md)
