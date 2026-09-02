---
uid: 396d6ae7-2c4b-49b9-8f7a-3994d12419a5
title: 'What is the "manual wheelchair" profile?'
slug: manual-wheelchair-profile
doc_type: concept
questions:
    - What is the "manual wheelchair" profile?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
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
    do_not_claim: []
related_pages:
    - assistant/accessmap/concept/manual-wheelchair-support.md
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/os-connect/concept/routing-assumptions.md
tags:
    - Assistant
---

<!-- @format -->

# What is the "manual wheelchair" profile?

## Short Answer

The "manual wheelchair" profile is a documented routing or accessibility-analysis profile intended to model travel considerations associated with manual wheelchair use. Its exact settings and behavior depend on the product, dataset, and current implementation.

## Significance

The profile can help users compare route or reachability results under assumptions that may differ from a general pedestrian profile.

## What This Means

Check the current product documentation for profile controls, slope, surface, crossing, barrier, and cost treatment. Record the profile, data release, and settings when sharing a result.

## What This Does Not Mean

The profile is not a medical classification, universal representation of manual wheelchair users, accessibility certification, or guarantee that a route is usable now.

## How To Use This

Use it as a modeling aid, adjust supported preferences when appropriate, compare alternatives, and verify important conditions locally.

## Example

A user compares a general pedestrian result with the manual-wheelchair profile and investigates a reroute around a modeled slope or missing connection.

## Assistant Guidance

Do not infer personal ability or promise a route's usability. Cite the current product and profile guidance, ask for version and settings, and abstain when behavior is undocumented.

## Related Concepts

- [Manual wheelchair support in AccessMap](../../accessmap/concept/manual-wheelchair-support.md)
- [How do mobility profiles work?](../../accessmap/concept/mobility-profiles.md)
- [What routing assumptions are used?](routing-assumptions.md)
