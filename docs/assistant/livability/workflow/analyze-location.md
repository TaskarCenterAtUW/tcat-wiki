---
uid: bdf10e29-ec71-4d65-abfa-1ca11e2a8af4
title: How do I analyze a location in LivAbility?
slug: analyze-location
doc_type: workflow
questions:
    - How do I analyze a location in LivAbility?
    - How do I find amenities from a location in LivAbility?
products:
    - LivAbility
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - livability
    - routing
    - accessibility-metrics
    - destinations
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
        - Running a LivAbility analysis certifies that the selected location or route is accessible.
        - A failed LivAbility analysis proves that no accessible sidewalk or amenity exists.
        - LivAbility results remain valid when the location, settings, or source data changes.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/livability-analysis.md
    - assistant/livability/concept/mobility-profiles.md
    - assistant/livability/concept/amenity-categories.md
tags:
    - Assistant
---

<!-- @format -->

# How do I analyze a location in LivAbility?

## Short Answer

Select a location in LivAbility, choose the mobility and routing settings, set a travel-time budget, select amenity categories, and activate **Find Amenities**. LivAbility then shows a summary of the modeled result and category counts when the required sidewalk data is available.

## Significance

Using the controls in a repeatable order makes comparisons easier to interpret. Recording the settings is important because changing the profile, route preference, avoidance options, or time budget changes the question the analysis answers.

## What This Means

The workflow produces an analysis for a selected location under the current controls. It may also support an optional second location, but this procedure focuses on one primary location and its nearby amenities.

## What This Does Not Mean

The result is a model-based accessibility assessment, not a guarantee of real-world access or a legal compliance finding. If LivAbility reports **No sidewalk data found near this location**, the requested analysis did not run for that location; the message does not prove that the area has no sidewalk or accessible destination.

## How To Use This

1. Open LivAbility.
2. In **Location 1**, search for an address or select a location on the map. Choose a suggestion when the search presents one, or use the map interaction described by the current interface.
3. Select a **Mobility profile**: **Manual wheelchair**, **Powered wheelchair**, **Cane**, **Walk**, or **Custom**.
4. Review the maximum uphill and downhill steepness values and adjust them when the analysis requires different assumptions.
5. Under **Route me through**, choose **sidewalks only**, **sidewalks whenever possible**, or **the shortest path**.
6. Review **Options** and enable or disable **Avoid raised curbs and stairs** and **Avoid primary streets** as appropriate.
7. Set the **Travel time** budget using the control provided by the interface.
8. Select the amenity categories to include, or use **All Categories**.
9. Select **Find Amenities**.
10. Review the summary, any error message, and the category counts. Record the location, settings, result date, and any data-coverage limitation before sharing the result.

## Example

A user selects a street address, chooses **Walk**, sets a 15-minute budget, keeps **sidewalks whenever possible**, enables **Transit Stops**, and selects **Find Amenities**. The user reports the transit count together with the profile and settings, rather than saying that all transit stops within 15 minutes are accessible.

## Assistant Guidance

Give these steps only when the user is working in the current LivAbility interface. Ask for the interface version or a screenshot if labels differ. If the result reports missing sidewalk data or another error, preserve that limitation and do not fabricate category results. Cite the current product source when interpreting output.

## Related Concepts

- [What does LivAbility analyze?](../concept/livability-analysis.md)
- [What is a mobility profile in LivAbility?](../concept/mobility-profiles.md)
- [What are amenity categories in LivAbility?](../concept/amenity-categories.md)
