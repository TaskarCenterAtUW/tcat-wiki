---
title: How are curb ramps incorporated into routing?
slug: curb-ramp-routing
doc_type: concept
questions:
    - How are curb ramps incorporated into routing?
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
        - A mapped curb ramp guarantees that the crossing is usable.
        - A missing curb-ramp attribute proves that no curb ramp exists.
related_pages:
    - assistant/accessmap/concept/missing-curb-ramps-effect.md
    - assistant/accessmap/concept/avoid-missing-curb-ramps.md
    - assistant/accessmap/concept/combined-crossing-accessibility.md
tags:
    - Assistant
---

<!-- @format -->

# How are curb ramps incorporated into routing?

## Short Answer

AccessMap can use mapped curb-ramp information as part of accessibility-aware route calculation. Depending on the selected profile and data, a known ramp may support a crossing while a missing or unfavorable value may increase route cost or affect route selection.

## Significance

Crossing access is often important to people using wheelchairs or other mobility devices. Representing curb-ramp information can expose route tradeoffs that a general walking route may not show.

## What This Means

- Identify the crossing and curb-ramp information used by the route.
- Check the selected profile and how it treats missing information.
- Verify the current curb condition and crossing environment when needed.

## What This Does Not Mean

A curb-ramp value does not establish ramp condition, clearance, slope, or legal compliance. Missing information does not prove that a ramp is absent in the physical environment.

## How To Use This

Explain curb ramps as one input to the routing model. Cite current feature and profile documentation, and report suspected data gaps through the available feedback path.

## Example

A route avoids a crossing with no mapped curb-ramp information. The user treats that result as a data-dependent preference and checks the crossing locally before deciding.

## Assistant Guidance

Do not promise that a mapped ramp is usable or that an unmapped ramp is absent. Ask for the profile, location, and dataset version, then cite current guidance.

## Related Concepts

- [Missing curb ramps and route selection](missing-curb-ramps-effect.md)
- [Avoid missing curb ramps](avoid-missing-curb-ramps.md)
- [Combined crossing accessibility](combined-crossing-accessibility.md)
