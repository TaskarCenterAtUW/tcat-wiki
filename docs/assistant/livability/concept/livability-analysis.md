---
uid: 06e48701-4a6f-4c81-a77c-f3d277c64bb0
title: What does LivAbility analyze?
slug: livability-analysis
doc_type: concept
questions:
    - What does LivAbility analyze?
    - What is a LivAbility accessibility analysis?
products:
    - LivAbility
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - livability
    - accessibility-metrics
    - routing
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - LivAbility measures every real-world accessibility condition at a location.
        - A LivAbility result is a legal, engineering, or ADA compliance determination.
        - A location is accessible simply because LivAbility returns reachable amenities.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/mobility-profiles.md
    - assistant/livability/concept/amenity-categories.md
    - assistant/livability/workflow/analyze-location.md
tags:
    - Assistant
---

<!-- @format -->

# What does LivAbility analyze?

## Short Answer

LivAbility analyzes pedestrian access from one or two selected locations using a mobility profile, route preferences, and a travel-time budget. It displays the modeled accessibility result on a map and can identify nearby amenities in selected categories.

The analysis depends on the sidewalk data available around the selected location. The interface can report that an analysis failed when it cannot find sidewalk data near a location.

## Significance

The analysis helps people explore how modeled pedestrian conditions and travel constraints affect access to everyday services. It can support community conversations and early planning questions without treating a map result as a complete field assessment.

## What This Means

The LivAbility interface provides controls for:

- selecting a primary location and an optional second location;
- choosing a **Manual wheelchair**, **Powered wheelchair**, **Cane**, **Walk**, or **Custom** mobility profile;
- setting maximum uphill and downhill steepness for the active profile;
- choosing whether to route through **sidewalks only**, **sidewalks whenever possible**, or **the shortest path**;
- optionally avoiding raised curbs and stairs or primary streets;
- setting a travel-time budget from 1 to 30 minutes; and
- showing or hiding amenity categories such as grocery stores, restaurants and cafes, healthcare, transit stops, food banks, schools, libraries, banks and ATMs, community centers, parks, and gyms.

These settings describe the conditions used for a particular modeled analysis. They do not describe every condition that a person may encounter outside the model.

## What This Does Not Mean

LivAbility does not establish that a route, building, service, or neighborhood is accessible for every person. It cannot replace current field verification, local knowledge, or professional review. A failed result can indicate missing sidewalk data near the selected location; it is not proof that no accessible route or amenity exists in the real world.

## How To Use This

Use LivAbility to compare a clearly documented set of locations and assumptions. Record the selected locations, profile, steepness settings, routing preference, avoidance options, travel-time budget, amenity filters, and date of the result. Investigate unexpected or high-impact results against current local data and field conditions.

## Example

An advocate selects a location, chooses **Manual wheelchair**, keeps **Avoid raised curbs and stairs** enabled, sets a 10-minute travel budget, and displays **Transit Stops** and **Healthcare**. The resulting map is an accessibility analysis under those settings, not a certification that every displayed destination is usable.

## Assistant Guidance

Cite the current LivAbility interface or product documentation when describing controls. Ask for the selected location, profile, travel budget, and relevant options before interpreting a result. If the interface reports that no sidewalk data was found, explain that the analysis could not run for that location and avoid converting the message into a claim about real-world accessibility.

## Related Concepts

- [LivAbility knowledge base](../index.md)
- [What is a mobility profile in LivAbility?](mobility-profiles.md)
- [What are amenity categories in LivAbility?](amenity-categories.md)
- [How do I analyze a location in LivAbility?](../workflow/analyze-location.md)
