---
title: 'What does "avoid missing curb ramps" mean?'
slug: avoid-missing-curb-ramps
doc_type: concept
questions:
    - What does "avoid missing curb ramps" mean?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
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
        - Avoiding missing curb ramps proves that every selected crossing has a usable ramp.
        - Missing curb-ramp data proves that no curb ramp exists.
related_pages:
    - assistant/accessmap/concept/curb-ramp-routing.md
    - assistant/accessmap/concept/missing-curb-ramps-effect.md
    - assistant/accessmap/concept/accessibility-preference-routing.md
tags:
    - Assistant
---

<!-- @format -->

# What does "avoid missing curb ramps" mean?

## Short Answer

"Avoid missing curb ramps" is a routing preference that treats missing curb-ramp information as a reason to increase route cost or avoid a crossing when supported by the selected AccessMap profile. It is based on mapped information, not a complete physical inspection.

## Significance

Curb-ramp information can affect whether a crossing appears suitable for a mobility profile. Making the preference explicit helps users understand route choices and data limitations.

## What This Means

- Select the preference when missing curb-ramp information is a concern.
- Review the route and the profile used.
- Verify the crossing locally when the route is important.

## What This Does Not Mean

The setting does not prove that an unselected crossing has a ramp or that a selected crossing is usable. It is not an ADA determination or a substitute for field inspection.

## How To Use This

Describe the setting as a data-dependent route preference. Cite current AccessMap guidance and report suspected missing or incorrect information through the available feedback path.

## Example

A route avoids a crossing with no mapped curb-ramp information. The user treats this as a modeling result and checks an alternate crossing locally.

## Assistant Guidance

Do not equate missing data with physical absence. Ask for the profile, location, and dataset version, and abstain from promising that a crossing is accessible.

## Related Concepts

- [How curb ramps are incorporated into routing](curb-ramp-routing.md)
- [Missing curb ramps and route selection](missing-curb-ramps-effect.md)
- [Accessibility-preference routing](accessibility-preference-routing.md)
