---
uid: 180a0bc8-9236-4053-b66d-ba22601b6fad
title: How should municipalities validate routing results?
slug: validate-routing-results
doc_type: workflow
questions:
    - How should municipalities validate routing results?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - data-quality
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
        - A small routing test proves that all AccessMap routes are accurate.
        - A route validation result is an accessibility or ADA certification.
related_pages:
    - assistant/accessmap/concept/field-validation.md
    - assistant/accessmap/concept/routing-limitations.md
    - assistant/accessmap/workflow/report-routing-problems.md
tags:
    - Assistant
---

<!-- @format -->

# How should municipalities validate routing results?

## Short Answer

Municipalities should validate AccessMap routes by testing representative origins, destinations, profiles, and conditions against current local knowledge or field observations. They should document the dataset, settings, date, expected result, observed result, and unresolved limitations.

## Significance

Validation helps agencies distinguish a model or data problem from a route that simply reflects a different accessibility objective.

## What This Means

- Select representative, high-consequence, and known-problem locations.
- Record origin, destination, profile, preferences, dataset version, and route result.
- Compare with imagery, agency records, community reports, or field observations.
- Report reproducible problems with supporting evidence.

## What This Does Not Mean

Validation does not prove that every route is usable, current, safe, or legally compliant. A sample cannot establish universal accuracy.

## How To Use This

Use a repeatable test set, include affected users where appropriate, and repeat tests when the product or source data change.

## Example

A municipality tests routes to a clinic under two profiles, compares crossing and slope conditions with field observations, and reports a reproducible discrepancy with the dataset version.

## Assistant Guidance

Ask what route, profile, date, and condition were tested. Cite the result and source data, avoid overgeneralization, and recommend professional review for legal or safety decisions.

## Related Concepts

- [Field validation](../concept/field-validation.md)
- [Routing limitations](../concept/routing-limitations.md)
- [Report routing problems](report-routing-problems.md)
