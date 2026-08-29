---
title: How are private facilities handled?
slug: private-facilities
doc_type: concept
questions:
    - How are private facilities handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - private-property
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/excluded-infrastructure-types.md
    - assistant/os-connect/concept/campus-handling.md
    - assistant/os-connect/concept/pedestrian-only-facilities.md
tags:
    - Assistant
---

<!-- @format -->

# How are private facilities handled?

## Short Answer

Private facilities are represented or excluded according to the dataset's scope, source permissions, access conditions, and release rules. A feature may be mapped without implying public access.

## Significance

Private paths, campuses, developments, and facilities can affect pedestrian connectivity and destinations but may have restrictions or different maintenance responsibilities.

## What This Means

Check ownership, access rules, dataset scope, source license, entrances, hours, restrictions, and current conditions. Label private or restricted features clearly in analysis.

## What This Does Not Mean

Private-facility data does not establish permission to enter, accessibility, ownership of every feature, or legal responsibility. Absence from a release does not prove that the facility or path is absent.

## How To Use This

Use current owner or facility information for access decisions, preserve privacy and licensing, validate important routes, and distinguish public right-of-way from private access.

## Example

A campus path appears to connect to a public sidewalk, but the facility requires authorization. The analyst treats it as a restricted connection and checks the current campus access rules.

## Assistant Guidance

Ask which facility, access status, release, and use are involved. Do not infer public access from geometry and abstain when ownership or access rules are unknown.

## Related Concepts

- [What kinds of infrastructure are not included?](excluded-infrastructure-types.md)
- [How are campuses handled?](campus-handling.md)
- [How are pedestrian-only facilities handled?](pedestrian-only-facilities.md)
