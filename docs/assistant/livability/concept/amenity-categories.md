---
uid: 533fabeb-00a6-464e-884a-957fd220ff8d
title: What are amenity categories in LivAbility?
slug: amenity-categories
doc_type: concept
questions:
    - What are amenity categories in LivAbility?
    - Which amenities can LivAbility find?
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
    - accessibility-metrics
    - community
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
        - LivAbility's amenity categories contain every destination in the selected area.
        - A displayed amenity is open, available, or accessible to every user.
        - An empty category proves that no amenity of that type exists nearby.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/livability-analysis.md
    - assistant/livability/workflow/filter-amenities.md
tags:
    - Assistant
---

<!-- @format -->

# What are amenity categories in LivAbility?

## Short Answer

Amenity categories are filters that control which types of nearby services LivAbility displays during an analysis. The observed categories include **Grocery Stores**, **Restaurants & Cafes**, **Healthcare**, **Transit Stops**, **Food Banks**, **Schools**, **Libraries**, **Banks & ATMs**, **Community Centers**, **Parks**, and **Gyms**.

The interface includes **All Categories** and individual switches. After a location is analyzed, the summary can show a count for each category and allow a category to be expanded for details.

## Significance

Grouping destinations by type helps users ask practical access questions, such as whether modeled travel reaches healthcare or transit within a selected time budget. It also makes the scope of a result visible instead of mixing every destination into one undifferentiated list.

## What This Means

Amenity filters affect the categories LivAbility seeks and summarizes for the selected location or locations. A category count is meaningful only together with the location, mobility profile, route settings, travel-time budget, underlying data, and date of the analysis.

The category list is not a complete inventory of all possible community destinations. The interface's **Find Amenities** action is available after a location has been selected; without a selected location it is disabled.

## What This Does Not Mean

An amenity count does not establish that a service is open, affordable, available to a particular person, or accessible in every relevant respect. A zero count does not by itself prove that no such service exists. It may reflect the selected travel budget, route assumptions, category data, or the coverage available to LivAbility.

## How To Use This

Select only the categories relevant to the question, or use **All Categories** for an initial overview. After the analysis, expand the categories that matter and record their counts with the active profile, travel-time budget, route preference, and location. Verify important destinations with current local information.

## Example

A planner wants to explore access to food and transit. The planner selects a location, enables **Grocery Stores**, **Food Banks**, and **Transit Stops**, and runs the analysis with a documented travel-time budget. The resulting counts identify modeled nearby services for those filters; they do not constitute a complete food-security or transit-access assessment.

## Assistant Guidance

When explaining a category result, repeat the category, location, travel budget, profile, and relevant route settings. Cite the current LivAbility interface or documentation for the available category names. Do not infer completeness, service availability, or accessibility from a count alone.

## Related Concepts

- [What does LivAbility analyze?](livability-analysis.md)
- [How do I filter amenity categories in LivAbility?](../workflow/filter-amenities.md)
- [How do I analyze a location in LivAbility?](../workflow/analyze-location.md)
