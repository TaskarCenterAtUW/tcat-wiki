---
uid: 1a48c315-7a74-43ce-8fd3-17850f22d886
title: How do I configure a mobility profile in LivAbility?
slug: configure-profile
doc_type: workflow
questions:
    - How do I configure a mobility profile in LivAbility?
    - How do I change steepness and routing options in LivAbility?
products:
    - LivAbility
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - livability
    - mobility-profiles
    - routing
    - configuration
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
        - LivAbility's preset values apply to every person represented by a profile name.
        - Changing a LivAbility setting changes the underlying sidewalk data.
        - A configured profile guarantees that a route is usable by a specific person.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/mobility-profiles.md
    - assistant/livability/workflow/analyze-location.md
tags:
    - Assistant
---

<!-- @format -->

# How do I configure a mobility profile in LivAbility?

## Short Answer

Use the **Mobility profile** choices and the related controls in LivAbility to define the assumptions for an analysis. You can choose a named profile or **Custom**, adjust maximum uphill and downhill steepness, choose a route preference, set avoidance options, and set a travel-time budget.

## Significance

The configuration determines how LivAbility interprets the available pedestrian network. Keeping a record of these settings makes results reproducible and helps users explain why two analyses differ.

## What This Means

Named profiles provide starting values. The interface observed for **Manual wheelchair** displayed 8.5% maximum uphill and 10% maximum downhill steepness with **Avoid raised curbs and stairs** enabled. The observed **Cane** profile displayed 10% uphill and 12% downhill with that avoidance option disabled. Values may change with future product releases, so verify the current display before documenting them.

## What This Does Not Mean

The controls do not edit the sidewalk network or confirm conditions in the field. A named profile is not a clinical or legal classification, and a custom configuration is not proof that the selected assumptions describe a particular person's full travel needs.

## How To Use This

1. Select a mobility profile from **Manual wheelchair**, **Powered wheelchair**, **Cane**, **Walk**, or **Custom**.
2. Read the displayed **Maximum uphill steepness** and **Maximum downhill steepness** values.
3. Adjust each steepness slider when the analysis requires values different from the preset.
4. Under **Route me through**, select **sidewalks only**, **sidewalks whenever possible**, or **the shortest path**.
5. Review **Options** and set **Avoid raised curbs and stairs** or **Avoid primary streets** according to the question being analyzed.
6. Set the **Travel time** budget.
7. Record the profile, steepness values, route preference, avoidance options, and time budget before selecting **Find Amenities**.

## Example

A planner compares two scenarios using the same location and a 10-minute budget. In the first scenario, the planner selects **Manual wheelchair** and records its displayed settings. In the second, the planner selects **Custom**, lowers the maximum uphill steepness, and keeps the same category filters. The planner labels the outputs with their different assumptions before comparing them.

## Assistant Guidance

Ask the user to report the displayed values instead of relying on an old preset description. Explain that settings are model inputs and cite the current LivAbility source. Do not prescribe a profile for an individual or infer that a profile is medically appropriate.

## Related Concepts

- [What is a mobility profile in LivAbility?](../concept/mobility-profiles.md)
- [How do I analyze a location in LivAbility?](analyze-location.md)
