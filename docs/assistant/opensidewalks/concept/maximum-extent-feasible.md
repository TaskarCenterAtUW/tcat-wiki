---
title: "What does maximum extent feasible mean in accessibility data?"
slug: maximum-extent-feasible
doc_type: concept
questions:
    - What does maximum extent feasible mean in sidewalk accessibility work?
    - How can a survey record a measurement that does not meet the target?
audiences:
    - jurisdiction
    - planner
    - developer
products:
    - OpenSidewalks
    - AVIV ScoutRoute
topics:
    - opensidewalks
    - aviv-scoutroute
    - accessibility-data
    - ada
    - legal-boundaries
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A maximum-extent-feasible value by itself establishes legal compliance.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/aviv-scoutroute/concept/quest.md
tags:
    - Assistant
---

<!-- @format -->

# What does maximum extent feasible mean in accessibility data?

## Short Answer

In the discussion, "maximum extent feasible" described an agency-documented allowance when a target accessibility measurement cannot be achieved at a particular site. The transcript did not establish a universal legal definition.

## Significance

Recording the approved practical limit can distinguish a documented constraint from an unexplained deficiency. It should remain tied to the responsible agency's records.

## What This Means

A survey may record whether an approved allowance applies, the allowed minimum, and the actual measurement. The governing form or decision should provide the authority for those values.

## What This Does Not Mean

The term does not automatically excuse a nonconforming condition or prove ADA compliance. Legal and engineering interpretations require the responsible authority.

## How To Use This

Ask for the applicable agency definition and documentation before designing quest logic. Store the approved threshold and observed value as separate fields when appropriate.

## Example

A sidewalk target is four feet, but an agency approval documents a three-foot-ten-inch minimum at one location. A survey can record that allowance and the actual width for later review.

## Assistant Guidance

Use the transcript only as provisional context. Abstain from legal conclusions and request the jurisdiction's governing documentation.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](../../aviv-scoutroute/concept/quest.md)
