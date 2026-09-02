---
uid: 342f1749-8884-4cbe-ae38-8eabbc15fec0
title: Can routing systems personalize accessibility preferences?
slug: routing-personalization
doc_type: concept
questions:
    - Can routing systems personalize accessibility preferences?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
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
    do_not_claim: []
related_pages:
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/os-connect/concept/routing-assumptions.md
    - assistant/os-connect/concept/missing-accessibility-information.md
tags:
    - Assistant
---

<!-- @format -->

# Can routing systems personalize accessibility preferences?

## Short Answer

Routing systems can personalize modeled accessibility preferences when the current product supports profiles or user-configurable settings for factors such as slope, surface, crossings, barriers, or distance. The available controls and their effects are implementation-specific.

## Significance

Different people may need different route tradeoffs. Profiles and preferences allow a model to reflect selected considerations instead of applying one route rule to everyone.

## What This Means

Check the current product's profiles, controls, cost rules, and data requirements. Record settings and release, compare alternatives, and verify important conditions locally.

## What This Does Not Mean

Personalization does not capture every need, infer a medical condition, guarantee accessibility, or replace lived experience and current local information.

## How To Use This

Use supported preferences as modeling aids, explain tradeoffs, preserve uncertainty, and avoid filling missing attributes with favorable or unfavorable assumptions.

## Example

A user changes the slope preference and receives a longer modeled route. The result is explained as a preference-based tradeoff, not a universal recommendation.

## Assistant Guidance

Do not promise a control or claim that a profile represents every user. Cite current product documentation, ask for version and settings, and abstain when behavior is unknown.

## Related Concepts

- [How do mobility profiles work?](../../accessmap/concept/mobility-profiles.md)
- [What routing assumptions are used?](routing-assumptions.md)
- [What accessibility information is missing from OS-CONNECT?](missing-accessibility-information.md)
