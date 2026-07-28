---
title: How are walksheds calculated?
slug: walkshed-calculation
doc_type: concept
questions:
    - How are walksheds calculated?
    - How is a walkshed calculated?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - graph-metrics
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-27
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A walkshed is a field survey or a guarantee that every person can travel throughout the displayed area.
        - A larger walkshed always means better real-world accessibility.
        - A nearby feature is reachable when it is not connected to the pedestrian network.
related_pages:
    - assistant/walksheds/concept/walkshed-cost-factors.md
    - assistant/walksheds/concept/walkshed-default-cost-model.md
    - assistant/walksheds/concept/walkshed-data-connectivity.md
    - assistant/walksheds/concept/travel-profiles.md
    - walksheds/user-manual/datasets.md
    - walksheds/user-manual/preferences.md
tags:
    - Assistant
---

<!-- @format -->

# How are walksheds calculated?

## Short Answer

A walkshed is calculated by traversing a pedestrian network from an origin location under a selected mobility profile and maximum travel cost. Walksheds uses the selected TDEI dataset to build the routing graph, then evaluates connected network edges until the cost limit is reached.

The result shows modeled reachability. It is not a direct measurement of every person's travel experience or a guarantee that every location inside a displayed boundary is accessible.

## Significance

Network traversal accounts for connections, crossings, slopes, barriers, street preferences, and profile assumptions that a straight-line distance buffer ignores. This makes the result useful for comparing modeled access under documented datasets and settings.

## What This Means

### Dataset and routing graph

The calculation begins with a selected TDEI dataset. The tool can also use an optional extension dataset overlay. After the dataset choices are made, Walksheds builds a router that represents the available pedestrian network. Changing the primary or extension dataset requires rebuilding the router and reloading the page before using the new network.

The graph must contain connected geometry near the origin to a feature for that feature to be reachable. A sidewalk, crossing, or other feature can appear close to the origin on a map and still be unreachable if the network has a missing connector or a disconnected segment.

### Origin and travel budget

The user selects an origin on the map and sets **Maximum Cost**. In the documented default interface, maximum cost is measured in seconds of estimated travel time. The traversal includes only edges that can be reached within that budget. Increasing the budget generally allows more of the connected network to be included; decreasing it generally limits the result.

### Profile and edge cost

The selected mobility profile supplies assumptions such as base speed, slope limits, and obstacle avoidance requirements. In the documented default model, edge cost is based on edge length and modeled speed, with a street-cost factor applied. Slope can change modeled speed, crossings can add a time penalty, and street-avoidance settings can add penalties to some street types.

The default guide documents base speeds of 1.3 meters per second for walking, 0.6 meters per second for a manual wheelchair, and 2.0 meters per second for a powered wheelchair. Steps use a fixed speed of 0.5 meters per second in that guide. These are model inputs, not individualized measurements.

### Restrictions and penalties

Depending on the selected profile and preferences, the calculation can exclude or penalize edges with conditions such as:

- uphill or downhill steepness beyond the configured limits;
- raised curbs or stairs when obstacle avoidance is enabled;
- street segments affected by the street-avoidance factor;
- crossings, which receive a default 30-second time penalty; and
- time-restricted paths, when a departure date and time is supplied.

The exact result depends on the active cost function and settings. Advanced users can modify the Python cost function when that experimental feature is available; this article describes the standard documented behavior rather than custom implementations.

## What This Does Not Mean

A walkshed is not a field survey, a legal or engineering determination, a guarantee of access, or an exact prediction of every person's travel. It does not establish that a real-world route is safe, available, or usable when the source dataset is incomplete, outdated, disconnected, or missing relevant conditions.

A larger displayed area is not automatically a better result. It may reflect a larger cost budget, a different profile, different penalties, or a different dataset rather than an improvement in actual accessibility.

## How To Use This

For a reproducible comparison:

1. Record the primary dataset name and version.
2. Record whether an extension dataset was used and identify its version.
3. Record the origin, mobility profile, maximum cost, departure time, and preference values.
4. Confirm that the router was built from those dataset selections before generating the walkshed.
5. Interpret differences as changes in modeled reachability, then check the underlying network and source data before drawing conclusions about conditions on the ground.

Use the [Walksheds Datasets guide](../../../walksheds/user-manual/datasets.md) for dataset and router steps and the [Mobility Profiles and Preferences guide](../../../walksheds/user-manual/preferences.md) for documented settings. For custom implementations, consult the [Custom Cost Function guide](../../../walksheds/user-manual/custom-cost-function.md).

## Example

A planner selects a versioned TDEI dataset, builds the router, and places an origin at a bus stop. The planner generates one result with a walking profile and another with a manual-wheelchair profile using the same maximum cost. The wheelchair-oriented result may exclude edges over its slope limits or edges with raised curbs and stairs when avoidance is enabled. The planner records those settings and describes the comparison as a difference in modeled reachable network, not as proof that one group experiences the exact displayed area.

## Assistant Guidance

Explain that the result is modeled reachability produced by network traversal. Before interpreting a result, ask for the dataset and version, origin, mobility profile, maximum cost, relevant preferences, departure time, and whether a custom cost function was used. Distinguish excluded edges from disconnected geometry: changing an attribute may not resolve a missing network connection.

When those details are missing, do not infer why two walksheds differ. Cite the relevant dataset, preference, cost-model, or connectivity documentation when making a specific claim.

## Related Concepts

- [What factors affect Walksheds travel cost?](walkshed-cost-factors.md)
- [How does the default Walksheds cost model work?](walkshed-default-cost-model.md)
- [Why does network connectivity matter in Walksheds?](walkshed-data-connectivity.md)
- [What travel profiles are available in Walksheds?](travel-profiles.md)
- [Datasets](../../../walksheds/user-manual/datasets.md)
- [Mobility Profiles and Preferences](../../../walksheds/user-manual/preferences.md)
