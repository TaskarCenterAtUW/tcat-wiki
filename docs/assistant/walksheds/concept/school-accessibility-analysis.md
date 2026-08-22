---
title: How can walksheds support school accessibility analysis?
slug: school-accessibility-analysis
doc_type: concept
questions:
    - How can walksheds support school accessibility analysis?
    - How can I compare school access for different mobility profiles?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - schools
    - mobility-profiles
    - comparison
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
        - A school-centered walkshed represents the access experience of every person or mobility profile.
        - A modeled school walkshed proves that every reachable route is safe or accessible in the real world.
related_pages:
    - assistant/walksheds/index.md
    - assistant/walksheds/concept/accessibility-profiles.md
    - assistant/walksheds/concept/walkshed-scenarios.md
    - assistant/qa-qc/concept/walkshed-profile-comparison.md
    - assistant/walksheds/workflow/run-batch-walksheds.md
tags:
    - Assistant
---

<!-- @format -->

# How can walksheds support school accessibility analysis?

## Short Answer

Walksheds can use schools as origin points of interest (POIs) and model what parts of the surrounding pedestrian network are reachable from each school. Run the analysis from the same school origins with multiple mobility profiles to compare how modeled access differs for different users.

The runs can be performed manually one at a time. When many schools or profiles must be compared, saved scenarios or batch processing can help organize the work; use the related Walksheds guidance for those methods.

## Significance

School access is not experienced in the same way by all pedestrians. Comparing profiles from the same school origins can show how modeled slopes, crossings, curb ramps, surface conditions, or other profile constraints change the reachable network and can help identify questions for further review.

## What This Means

- Treat each school as an origin POI for one or more walkshed runs.
- Keep the school origin and travel budget consistent when comparing profiles, unless the analysis is intentionally testing a different assumption.
- Run the same origin with the relevant mobility profiles and compare the resulting reachable areas and statistics.
- Perform a small comparison manually when only a few schools or profiles are involved. Use [Walksheds scenarios](walkshed-scenarios.md) for saved comparisons and [batch walksheds](../workflow/run-batch-walksheds.md) when many origins or profile runs must be processed.

## What This Does Not Mean

A school-centered walkshed is a modeled result based on the selected network, origin, profile, travel budget, and other settings. It does not represent every student's or traveler's experience, prove that a route is safe or accessible in the field, or establish that areas outside the result are unimportant.

## How To Use This

1. Identify the schools to analyze and use their locations as origin POIs.
2. Choose the travel budget and mobility profiles that represent the comparison question.
3. Run a walkshed for each selected profile from the same school origin.
4. Compare reachable areas and statistics, then record the dataset, profiles, budgets, and other assumptions.
5. Use differences as screening evidence for planning or field review, not as a final accessibility determination.

For a small number of runs, perform the comparisons manually. For repeatable saved alternatives, use [Walksheds scenarios](walkshed-scenarios.md). For many school origins or profile combinations, use [batch walksheds](../workflow/run-batch-walksheds.md).

## Example

An accessibility planner selects three schools as origin POIs and runs a 15-minute walkshed from each one using pedestrian and wheelchair profiles. The planner compares the reachable areas from each school, documents the profile and budget assumptions, and sends locations with large differences to field review. The planner could run the comparisons manually, save them as scenarios, or use batch processing if the number of schools and profiles grows.

## Assistant Guidance

Explain that schools are the origin POIs in this analysis and that the same school should be compared across the selected profiles. Ask for the schools, dataset, travel budget, profiles, and relevant settings before interpreting a result. Link to scenario or batch guidance rather than describing those workflows in detail. Cite this article when explaining the method, and do not claim that a modeled difference proves a real-world accessibility outcome.

## Related Concepts

- [Walksheds](../index.md)
- [What accessibility profiles are supported?](accessibility-profiles.md)
- [What is a Walksheds scenario?](walkshed-scenarios.md)
- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
- [How do QA/QC walksheds compare mobility profiles?](../../qa-qc/concept/walkshed-profile-comparison.md)
