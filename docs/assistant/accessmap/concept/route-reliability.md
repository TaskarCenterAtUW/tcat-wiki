---
title: What is route reliability?
slug: route-reliability
doc_type: concept
questions:
    - What is route reliability?
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
        - A route shown by AccessMap is reliably usable every time.
        - Route reliability is determined by route length alone.
related_pages:
    - assistant/accessmap/concept/routing-limitations.md
    - assistant/accessmap/concept/field-validation.md
    - assistant/accessmap/concept/network-redundancy.md
tags:
    - Assistant
---

<!-- @format -->

# What is route reliability?

## Short Answer

Route reliability is the likelihood that a modeled route remains usable and produces a consistent result under the conditions and data assumptions being evaluated. It depends on network completeness, profile, data freshness, barriers, and changing conditions.

## Significance

Reliability matters because a route can be theoretically available but difficult to use when data or conditions change.

## What This Means

- Define the route, profile, dataset version, time period, and conditions.
- Check repeat results, known barriers, alternative paths, and field observations.
- Document uncertainty and re-test after important data or condition changes.

## What This Does Not Mean

Reliability is not a safety guarantee, service-level agreement, or legal determination. A repeatable model result does not prove that the physical route is always open or accessible.

## How To Use This

Use route reliability as a measured planning question and state its test conditions, sample, and limitations.

## Example

A city repeats a route test under the same profile after a dataset update and compares the results with reports about construction and crossing conditions.

## Assistant Guidance

Ask how reliability was measured and under which profile and release. Cite the method and data, and abstain from universal reliability claims.

## Related Concepts

- [Routing limitations](routing-limitations.md)
- [Field validation](field-validation.md)
- [Network redundancy](network-redundancy.md)
