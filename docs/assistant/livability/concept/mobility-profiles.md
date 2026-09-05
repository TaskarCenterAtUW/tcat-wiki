---
uid: ae864769-1e4c-4b2b-8169-7a690a84f4d3
title: What is a mobility profile in LivAbility?
slug: mobility-profiles
doc_type: concept
questions:
    - What is a mobility profile in LivAbility?
    - Which mobility profiles does LivAbility provide?
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
        - A LivAbility mobility profile represents every person in the named mobility group.
        - LivAbility mobility profiles are identical to profiles in AccessMap or Walksheds.
        - Selecting a LivAbility profile proves that a route is safe or accessible for an individual.
related_pages:
    - assistant/livability/index.md
    - assistant/livability/concept/livability-analysis.md
    - assistant/livability/workflow/configure-profile.md
tags:
    - Assistant
---

<!-- @format -->

# What is a mobility profile in LivAbility?

## Short Answer

A LivAbility mobility profile is a set of routing assumptions used to model access from a selected location. The available profile choices are **Manual wheelchair**, **Powered wheelchair**, **Cane**, **Walk**, and **Custom**.

The active profile sets default steepness limits and avoidance behavior that can be adjusted through the interface. The profile is a model input, not a diagnosis or a complete description of a person's mobility.

## Significance

Different people can experience the same pedestrian network differently. Making the profile explicit helps users compare modeled results under stated assumptions instead of presenting one route as universally accessible.

## What This Means

When a user selects a named profile, LivAbility applies profile-specific values for maximum uphill and downhill steepness and may set an avoidance option. For example, the observed **Manual wheelchair** profile displayed 8.5% maximum uphill steepness, 10% maximum downhill steepness, and **Avoid raised curbs and stairs** enabled. The observed **Cane** profile displayed 10% uphill, 12% downhill, and that avoidance option disabled.

The **Custom** choice allows the user to work with adjustable settings rather than relying only on a named preset. Users can also choose routing behavior, avoidance options, and a travel-time budget for the analysis.

## What This Does Not Mean

A profile name is not a clinical classification and does not represent every person who uses a wheelchair, cane, or walking route. LivAbility profiles are not established here as equivalent to profiles in other TCAT products. A route modeled under a profile still depends on data coverage, model assumptions, and current local conditions.

## How To Use This

Choose the profile that best matches the question being explored, then review its active steepness and avoidance settings before running the analysis. Use **Custom** when the preset does not express the assumptions needed for the question. Record the profile and settings when sharing or comparing results.

## Example

To explore a route for a person who wants to avoid raised curbs and stairs, a user selects **Manual wheelchair**, confirms the displayed steepness limits, keeps the relevant avoidance switch enabled, and records the travel-time budget. The output should be described as a result for those settings, not as a guarantee for all manual wheelchair users.

## Assistant Guidance

Ask which profile and adjustable settings were active before interpreting a result. Cite the current LivAbility interface for observed preset values because product settings can change. Do not import profile definitions from AccessMap or Walksheds, and do not infer a person's capability from a profile label.

## Related Concepts

- [What does LivAbility analyze?](livability-analysis.md)
- [How do I configure a LivAbility mobility profile?](../workflow/configure-profile.md)
- [How do I analyze a location in LivAbility?](../workflow/analyze-location.md)
