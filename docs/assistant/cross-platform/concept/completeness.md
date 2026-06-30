---
title: Completeness (OS-CONNECT and related datasets)
tags:
    - Assistant
slug: completeness
doc_type: concept
products:
    - OS-CONNECT
audiences:
    - planner
    - jurisdiction
    - advocate
topics:
    - data-quality
    - OS-CONNECT
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Completeness equals ADA compliance or legal sufficiency.
related_pages:
    - assistant/concepts/ada-compliance-boundaries.md
    - assistant/questions/os-connect/what-does-completeness-mean.md
    - assistant/questions/os-connect/is-completeness-ada-compliance.md
---

<!-- @format -->

# Completeness (OS-CONNECT and related datasets)

## Short Answer

Completeness describes how thoroughly pedestrian-relevant features are represented and connected in a dataset for a given area — not whether every real-world condition is captured. It is a data-quality and coverage concept used in reporting and QA/QC, not a legal certification.

## Significance

Jurisdictions use completeness language in snapshots and plans. Misreading it as "we are done" or "we are ADA compliant" creates liability and public trust issues. A shared definition keeps planners, advocates, and residents aligned.

## What This Means

Completeness reflects modeled coverage of the pedestrian network (for example, sidewalks, crossings, and links) relative to expectations for that geography and schema. It can change as mapping improves, imports update, or validation rules evolve.

## What This Does Not Mean

- Not a guarantee that every barrier, temporary closure, or private easement is recorded.
- Not a substitute for facility-by-facility ADA assessments.
- Not a single universal percentage without local methodology context.

## How To Use This

Use completeness to prioritize data improvement and to communicate progress. Pair any completeness statement with the QA/QC or methodology reference from the main OS-CONNECT documentation for that release or report.

## Example

A county shows rising completeness after a mapping campaign. That supports "more of the modeled network is present," not "all sidewalks meet ADA standards."

## Assistant Guidance

Define completeness in plain language first. If the user conflates completeness with compliance, cite [ADA compliance boundaries](ada-compliance-boundaries.md) and stop short of legal conclusions. When methodology is unknown, abstain from numeric comparisons across regions.

## Related Concepts

- [ADA compliance boundaries](ada-compliance-boundaries.md)
- [What does completeness mean?](../../qa-qc/concept/completeness.md)
