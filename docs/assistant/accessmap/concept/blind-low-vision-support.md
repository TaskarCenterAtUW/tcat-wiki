---
title: Can AccessMap support blind or low-vision users?
slug: blind-low-vision-support
doc_type: concept
questions:
    - Can AccessMap support blind or low-vision users?
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
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AccessMap's BLV profile replaces a person's own orientation and mobility judgment.
        - Screen-reader alerts guarantee complete non-visual navigation.
related_pages:
    - mobility-profiles.md
    - ../../../accessmap/user-manual/navigation.md
tags:
    - Assistant
---

<!-- @format -->

# Can AccessMap support blind or low-vision users?

## Short Answer

AccessMap supports blind and low-vision users through a BLV profile, screen-reader-compatible directions, and optional alerts for surfaces, inclines, buildings, and landmarks.

## Significance

Non-visual alerts can provide information about route changes and nearby orientation cues without requiring the traveler to continuously inspect the map.

## What This Means

Enable the device screen reader, select the BLV profile or configure Custom preferences, and enable relevant alerts. Landmark alerts can announce nearby landmarks such as benches, waste bins, signals, and buildings within the configured landmark distance.

## What This Does Not Mean

The BLV profile and alerts do not guarantee complete instructions, accurate positioning, or safe conditions. Their usefulness depends on available mapped data, settings, device support, and the traveler's judgment.

## How To Use This

Confirm the alert settings before beginning route following and verify location permissions when using current-location navigation.

## Example

A traveler enables surface and incline alerts, sets a landmark distance, and follows the direction cards while the device announces configured alerts.

## Assistant Guidance

Ask which screen reader, profile, and alert settings are enabled when troubleshooting. Do not infer that an unannounced feature is absent from the route or environment.

## Related Concepts

- [How do mobility profiles work?](mobility-profiles.md)
- [How do I follow an AccessMap route using my location?](../workflow/follow-a-route-with-location.md)
