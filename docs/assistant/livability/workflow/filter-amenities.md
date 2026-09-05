---
uid: a1101b60-cb9d-4108-88bd-4625000e3271
title: How do I filter amenity categories in LivAbility?
slug: filter-amenities
doc_type: workflow
questions:
    - How do I filter amenity categories in LivAbility?
    - How do I show only selected amenity types in LivAbility?
products:
    - LivAbility
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - livability
    - destinations
    - configuration
    - accessibility-metrics
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
        - A filtered LivAbility result is a complete inventory of the selected amenity type.
        - A zero category count proves that no amenity of that type exists.
        - A displayed amenity is necessarily open or accessible to the user.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/amenity-categories.md
    - assistant/livability/workflow/analyze-location.md
tags:
    - Assistant
---

<!-- @format -->

# How do I filter amenity categories in LivAbility?

## Short Answer

After selecting a location, use **All Categories** or the individual category switches in the **Amenity Categories** section. Select **Find Amenities** to run the analysis, then review the category counts and expand a category when details are available.

## Significance

Filtering keeps an analysis focused on the destinations relevant to a planning or community question. It also makes it easier to report which categories were included and which were intentionally excluded.

## What This Means

The observed individual filters are **Grocery Stores**, **Restaurants & Cafes**, **Healthcare**, **Transit Stops**, **Food Banks**, **Schools**, **Libraries**, **Banks & ATMs**, **Community Centers**, **Parks**, and **Gyms**. The **All Categories** switch can enable the full set. Individual switches can then be used to narrow the displayed scope.

## What This Does Not Mean

Filtering changes the categories included in the result; it does not improve the underlying data or make the returned amenities accessible. A missing or zero result can reflect the travel-time budget, profile, route settings, data coverage, or category source rather than the absence of a real-world service.

## How To Use This

1. Select **Location 1** and configure the mobility and routing settings.
2. In **Amenity Categories**, select **All Categories** for an overview or turn on only the relevant individual switches.
3. Check that the intended categories remain enabled before selecting **Find Amenities**.
4. Review the summary after the analysis finishes.
5. Expand a category result when its details control is available.
6. Record the enabled categories, counts, location, profile, travel budget, and date.

## Example

For a food-access question, a user enables **Grocery Stores** and **Food Banks**, disables unrelated categories, runs the analysis, and reports both filters with the resulting counts. The report states that the counts are modeled results under the selected time and routing assumptions.

## Assistant Guidance

Repeat the category names and active settings when explaining a result. Cite the current interface for the available filters. Do not treat category counts as a complete inventory, and ask for local verification when the result supports a consequential planning decision.

## Related Concepts

- [What are amenity categories in LivAbility?](../concept/amenity-categories.md)
- [How do I analyze a location in LivAbility?](analyze-location.md)
