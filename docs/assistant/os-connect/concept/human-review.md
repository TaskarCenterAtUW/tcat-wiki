---
uid: 8eb9cfce-2b54-4169-93d1-ad14818d26f2
title: How should human review be incorporated?
slug: human-review
doc_type: concept
questions:
    - How should human review be incorporated?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - data-quality
    - ai
risk_level: high
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
    - assistant/os-connect/concept/ai-data-risks.md
    - assistant/os-connect/concept/field-validation.md
    - assistant/os-connect/concept/community-validation-role.md
tags:
    - Assistant
---

<!-- @format -->

# How should human review be incorporated?

## Short Answer

Human review should be incorporated wherever automated, inferred, community-submitted, or otherwise uncertain data may affect routing, planning, accessibility interpretation, or release decisions. The depth of review should match the consequence and uncertainty.

## Significance

Human reviewers can identify context, ambiguity, source errors, and lived conditions that automated processing may miss. Review also creates accountability for acceptance and correction decisions.

## What This Means

Define review roles, evidence, sampling, criteria, version, date, decision, and escalation. Keep generated candidates and observations separate from accepted or released records until an authorized review is complete.

## What This Does Not Mean

Human review is not automatically exhaustive or unbiased, and reviewer approval does not prove that a condition is current or accessible for every traveler.

## How To Use This

Prioritize high-risk or low-confidence records, include local and community knowledge where appropriate, record disagreements, and audit decisions over time.

## Example

A reviewer checks an automated curb-ramp candidate against imagery and field evidence, marks it as confirmed or unresolved, and preserves the reason for the decision.

## Assistant Guidance

State who reviewed what, when, and using which criteria. Do not imply that review covered the whole dataset, and abstain when the review process or status is unknown.

## Related Concepts

- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [How should field validation be incorporated?](field-validation.md)
- [What role did community validation play?](community-validation-role.md)
