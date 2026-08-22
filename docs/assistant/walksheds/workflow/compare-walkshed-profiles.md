---
title: How do I compare Walksheds profiles?
slug: compare-walkshed-profiles
doc_type: workflow
questions:
    - How do I compare Walksheds profiles?
    - How can Walksheds visualize the difference between mobility profiles?
    - How do I compare pedestrian and powered-wheelchair walksheds?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
topics:
    - walksheds
    - mobility-profiles
    - comparison
    - planning
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Differences between profiles directly identify the infrastructure project to build.
related_pages:
    - ../concept/walkshed-scenarios.md
    - ../concept/pedestrian-vs-wheelchair-walkshed.md
    - save-and-compare-walkshed-scenarios.md
tags:
    - Assistant
---

<!-- @format -->

# How do I compare Walksheds profiles?

## Short Answer

Run walkshed requests from the same origin using different mobility profiles, save the results as scenarios, and enable the scenarios together in the **Scenarios** tab. The map displays the overlapping walksheds in different colors, making profile-specific differences in modeled accessibility visible.

## Significance

The differences can suggest what infrastructure would expand access for a more constrained profile.

## What This Means

To compare an unconstrained pedestrian profile with a powered-wheelchair profile:

1. Run a walkshed request for an origin with the pedestrian profile.
2. Save the result as a scenario.
3. Run a second request for that same origin with the powered-wheelchair profile.
4. Save the result as another scenario, using a name that identifies the mobility profile.
5. Open the **Scenarios** tab.
6. Check the pedestrian scenario first, which is typically the wider walkshed.
7. Check the powered-wheelchair scenario second.

Both walkshed highlights then appear on the map. The more constrained profile's result can be compared with the larger pedestrian result to show which areas are reachable under one profile but not the other.

Walkshed highlights are stacked in the order in which their scenarios are checked. The scenario checked last is displayed on top of the earlier selection. Check the wider pedestrian walkshed first so the powered-wheelchair walkshed is visible above it. If the wheelchair scenario is checked first and the pedestrian scenario second, the wider pedestrian highlight can cover the wheelchair result.

## What This Does Not Mean

The comparison is not a final design or funding recommendation. A visible difference between profiles is a difference in modeled results under the selected settings, not a complete description of a person's experience.

## How To Use This

Keep the origin, dataset, travel budget, and other relevant settings consistent. Record which mobility profiles produced each scenario, then use the map and supporting statistics to identify differences in reachable network, crossings, slopes, or curb-ramp constraints. Validate important findings against current local data and field knowledge.

## Example

An unconstrained pedestrian walkshed extends beyond a powered-wheelchair walkshed from the same origin. Checking the pedestrian scenario first and the powered-wheelchair scenario second leaves the constrained result visible on top, highlighting areas reached by the pedestrian profile but not by the powered-wheelchair profile.

## Assistant Guidance

Ask which profiles, origin, dataset, travel budget, scenario order, and other network settings were compared. Explain that the last checked scenario is displayed on top and that the result represents modeled accessibility under those settings.

## Related Concepts

- [What assumptions do QA/QC walkshed profiles use?](../../qa-qc/concept/walkshed-profile-assumptions.md)
