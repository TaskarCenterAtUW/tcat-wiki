---
title: How do missing curb ramps affect route selection?
slug: missing-curb-ramps-effect
doc_type: concept
questions:
    - How do missing curb ramps affect route selection?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - curb-ramps
    - routing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Missing curb-ramp data proves that no curb ramp exists.
        - Avoiding a missing curb ramp guarantees that the alternative is usable.
related_pages:
    - assistant/accessmap/concept/curb-ramp-routing.md
    - assistant/accessmap/concept/avoid-missing-curb-ramps.md
    - assistant/accessmap/concept/missing-accessibility-data.md
tags:
    - Assistant
---

<!-- @format -->

# How do missing curb ramps affect route selection?

## Short Answer

Missing curb-ramp information can cause an accessibility-aware route to increase the cost of, avoid, or fail to use a crossing, depending on the selected profile and current model. The result reflects missing data as well as the physical network.

## Significance

Because crossings are important to many mobility-device users, missing ramp data can change route choices and reveal a data-quality gap.

## What This Means

- Identify the crossing, profile, dataset, and missing attribute.
- Compare the route with available imagery, local records, or field observations.
- Report a confirmed or suspected data gap through the current process.

## What This Does Not Mean

Missing information does not prove that a ramp is absent, and a mapped ramp does not prove that it is usable or compliant.

## How To Use This

Explain the difference between data absence and physical absence, and verify priority crossings locally.

## Example

A route avoids a crossing with no curb-ramp record, but a field check finds a ramp. The agency reports the missing attribute and treats the original route as data-dependent.

## Assistant Guidance

Do not make definitive accessibility claims from missing data. Cite the profile and dataset, ask for location and version, and abstain when the crossing context is incomplete.

## Related Concepts

- [Curb ramps in routing](curb-ramp-routing.md)
- [Avoid missing curb ramps](avoid-missing-curb-ramps.md)
- [Missing accessibility data](missing-accessibility-data.md)
