---
uid: 22d1cd80-e62e-4a6a-9325-3accbdbf0fe2
title: What assumptions do QA/QC walkshed profiles use?
slug: walkshed-profile-assumptions
doc_type: concept
questions:
    - What assumptions do QA/QC walkshed profiles use?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - Walksheds
topics:
    - qa-qc
    - walksheds
    - mobility-profiles
    - slope
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - QA/QC walkshed profiles represent every pedestrian or wheelchair user's needs.
        - A 600-cost budget represents exactly ten minutes of travel for every profile.
        - A street-avoidance value guarantees a particular increase in walkshed size.
related_pages:
    - assistant/qa-qc/concept/walkshed-profile-comparison.md
    - assistant/qa-qc/concept/report-purpose-and-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# What assumptions do QA/QC walkshed profiles use?

## Short Answer

QA/QC reports compare modeled walksheds using different network and mobility assumptions. The sidewalk-only pedestrian profile stays on mapped sidewalks and crossings. Pedestrian using sidewalks whenever possible prefers sidewalks but can use street segments when sidewalks are missing. Fan-out applies the pedestrian walkshed costing to road segments too, generally producing the broadest reach.

## Significance

Profile assumptions explain differences in reachable network area and help planners distinguish sidewalk access from reach that includes streets. The resulting maps and metrics describe modeled network reach, not a route guarantee for an individual traveler.

## What This Means

The report's profiles differ in which network edges they can use and how those edges are costed:

- **Sidewalk-only pedestrian** uses mapped sidewalks and crossings, with 100% street avoidance.
- **Pedestrian using sidewalks whenever possible** prefers sidewalks and crossings but can use street segments where sidewalks are missing. It ignores curbs as barriers and has a 0.9 (90%) street-avoidance setting in the report interface.
- **Fan-out** applies the pedestrian walkshed costing to road segments rather than the higher road-segment costing used without fan-out. It is a separate parameter, not another street-avoidance value.
- The modeled manual-wheelchair profile uses more restrictive assumptions, including tighter grade limits than the pedestrian profiles.

Reports use the same 600-cost budget across profiles. That value should not automatically be read as 600 seconds or ten minutes for a profile that includes road segments: edge types and profile settings affect the accumulated cost. Lowering street avoidance generally permits more street use and can increase modeled reach, but the value does not specify an exact increase.

## What This Does Not Mean

These profiles do not represent every person's mobility or guarantee that a route is safe or usable. A shared cost budget does not guarantee equal elapsed travel time, and a street-avoidance value is not a probability or a direct measure of distance.

## How To Use This

When comparing walksheds, record the profile names, street-avoidance settings, road/fan-out treatment, slope and curb assumptions, travel-cost budget, and dataset version. Use the profile descriptions and map together; do not infer an exact travel time or reach difference from the street-avoidance number alone.

## Example

At a site with a large parking lot and missing sidewalk connections, pedestrian using sidewalks whenever possible may reach across parking-lot or street segments that sidewalk-only pedestrian excludes. Fan-out may extend farther because road segments receive the pedestrian walkshed costing. These are modeled differences, not confirmation that a particular traveler can enter a building or safely use every segment.

## Assistant Guidance

Ask which report profiles, cost budget, and dataset version are being compared. Explain that the 0.9 setting expresses street avoidance in the report configuration, not a percentage chance of choosing a sidewalk. Do not convert the 600-cost budget to elapsed time for road-inclusive profiles without a documented conversion.

## Related Concepts

- [How do QA/QC walksheds compare mobility profiles?](walkshed-profile-comparison.md)
