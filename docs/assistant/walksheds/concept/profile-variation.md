---
uid: f847a412-fc69-4c8b-b120-47249db9e589
title: Why do different profiles produce different walksheds?
slug: profile-variation
doc_type: concept
questions:
    - Why do different profiles produce different walksheds?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
    - OS-CONNECT
topics:
    - walksheds
    - mobility-profiles
    - os-connect
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
    - assistant/walksheds/concept/accessibility-profiles.md
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/walkshed-edit-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why do different profiles produce different walksheds?

## Short Answer

Different profiles produce different walksheds because they apply different assumptions or costs to slopes, surfaces, barriers, crossings, distance, and other network conditions.

## Significance

Profile comparison can show how reachability changes under different mobility considerations and can identify locations for review.

## What This Means

Hold the origin, network, destinations, release, and travel limit constant when comparing profiles. Record each profile's settings and interpret differences through its documented cost rules.

## What This Does Not Mean

A profile is not a medical diagnosis, universal representation of a group, or guarantee that the result is usable for a particular person.

## How To Use This

Use profiles as modeling aids, compare results carefully, validate important routes locally, and ask affected users how the result relates to lived experience.

## Example

A wheelchair profile excludes or increases the cost of a steep segment that a general pedestrian profile includes, producing a smaller or differently shaped result.

## Assistant Guidance

Name the profiles, settings, network, and release. Avoid inferring a person's abilities from a profile result and abstain when definitions are unknown.

## Related Concepts

- [What accessibility profiles are supported?](accessibility-profiles.md)
- [What network assumptions are used?](network-assumptions.md)
- [Walkshed editing limitations](walkshed-edit-limitations.md)
