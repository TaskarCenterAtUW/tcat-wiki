---
title: "How do I follow an AccessMap route using my location?"
slug: follow-a-route-with-location
doc_type: workflow
questions:
    - How do I follow an AccessMap route using my current location?
    - How do I use screen-reader alerts while following a route?
audiences:
    - public
    - advocate
products:
    - AccessMap
topics:
    - accessmap
    - routing
    - mobility-profiles
    - device-compatibility
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
        - AccessMap can follow a route without location permission or an available device location.
related_pages:
    - assistant/accessmap/index.md
    - assistant/accessmap/workflow/plan-and-share-a-route.md
tags:
    - Assistant
---

<!-- @format -->

# How do I follow an AccessMap route using my location?

## Short Answer

Enable device location services and browser permission, choose **Start route from your location**, and open the **Directions** panel. AccessMap can then show your position, highlight the selected direction and associated route segment, and provide configured alerts as you travel.

## Significance

Following a route differs from previewing it at home. The workflow supports turn-by-turn use and optional screen-reader alerts.

## What This Means

Set or select a destination, start from your location, and use the direction cards. Configure surface, incline, building, or landmark alerts according to your preferences, and enable the device screen reader when using spoken alerts.

## What This Does Not Mean

Location following does not guarantee accurate positioning or complete instructions. Alerts that are disabled may still be available for manual inspection.

## How To Use This

Grant location permission when prompted and verify that location access is enabled both for the device or browser and for `https://accessmap.app/`. Choose the desired alerts in the preferences before starting route-following mode.

## Example

A user opens a route on a phone, starts from their current location, and enables incline and surface alerts for screen-reader guidance.

## Assistant Guidance

Ask about device permissions, route mode, and alert settings when troubleshooting. Do not assume that a missing alert means the underlying feature is absent.

## Related Concepts

- [How do I plan and share an AccessMap route?](plan-and-share-a-route.md)
