---
title: How should AI outputs be validated?
slug: how-should-ai-outputs-be-validated
doc_type: concept
questions:
    - How should AI outputs be validated?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - ai
    - data-quality
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/cross-platform/concept/what-are-the-risks-of-automated-accessibility-analysis.md
    - assistant/os-connect/concept/human-review.md
    - assistant/os-connect/concept/ai-data-risks.md
tags:
    - Assistant
---

<!-- @format -->

# How should AI outputs be validated?

## Short Answer

Validate AI outputs against representative, current, and appropriately authoritative evidence before using them for accessibility, routing, planning, or release decisions. Document the source, model or process, version, test sample, errors, reviewer, and decision.

## Significance

AI outputs can contain false positives, false negatives, uneven performance, and hidden assumptions. Validation helps users understand whether an output is useful for a specific decision.

## What This Means

Define the intended use and acceptance criteria, sample different locations and conditions, compare outputs with field or trusted local evidence, inspect errors by context, and keep generated candidates separate from accepted records until reviewed.

## What This Does Not Mean

Validation does not prove that an AI system is universally accurate, unbiased, current, accessible, or legally sufficient. A confidence score is not field verification.

## How To Use This

Use risk-based review, preserve provenance and privacy, record disagreements, test for coverage gaps, and provide a correction or appeal path where outputs affect people or public decisions.

## Example

A model flags a possible curb ramp. Reviewers compare it with dated imagery and a local inspection record, document the result, and retain the model output as evidence rather than silently replacing the source data.

## Assistant Guidance

State what was tested and what was not. Cite the method and evidence, avoid claiming validation beyond the sample, and abstain when the output's source or review status is unknown.

## Related Concepts

- [What are the risks of automated accessibility analysis?](what-are-the-risks-of-automated-accessibility-analysis.md)
- [How should human review be incorporated?](../../os-connect/concept/human-review.md)
- [What risks exist in AI-generated accessibility data?](../../os-connect/concept/ai-data-risks.md)
