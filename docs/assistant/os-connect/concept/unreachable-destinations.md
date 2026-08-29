---
title: Why are some destinations unreachable?
slug: unreachable-destinations
doc_type: concept
questions:
    - Why are some destinations unreachable?
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
    - assistant/os-connect/concept/routable-graph.md
    - assistant/os-connect/concept/routing-assumptions.md
    - assistant/os-connect/concept/missing-accessibility-information.md
tags:
    - Assistant
---

<!-- @format -->

# Why are some destinations unreachable?

## Short Answer

Destinations may be unreachable in an OS-CONNECT analysis because the network is disconnected, a crossing or connection is missing, barriers or restrictions apply, the destination is outside the travel limit, or the destination or access point is not represented correctly.

## Significance

Unreachable results can identify data, network, access, or configuration questions for review.

## What This Means

Check the origin, destination point, network, crossings, barriers, profile, maximum cost, source coverage, and release. Compare with local records and current conditions.

## What This Does Not Mean

An unreachable modeled destination is not proof that no physical route exists or that the destination is inaccessible for every traveler.

## How To Use This

Use the result to investigate specific gaps, document assumptions and versions, validate important routes locally, and report confirmed data issues.

## Example

A clinic is near the origin but unreachable because the modeled network lacks a crossing connection. Reviewers check whether the gap is a data issue or a physical condition.

## Assistant Guidance

Name the graph, profile, cost, destination source, and release. Avoid definitive access claims and abstain when the reason for exclusion cannot be determined.

## Related Concepts

- [What is a routable graph?](routable-graph.md)
- [What routing assumptions are used?](routing-assumptions.md)
- [What accessibility information is missing from OS-CONNECT?](missing-accessibility-information.md)
