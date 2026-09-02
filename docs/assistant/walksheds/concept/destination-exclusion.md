---
uid: 5489d6d2-92bd-46e8-97d4-9e1b091876f8
title: Why are some destinations excluded?
slug: destination-exclusion
doc_type: concept
questions:
    - Why are some destinations excluded?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
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
    - assistant/walksheds/concept/walkshed-result-statistics.md
    - assistant/walksheds/concept/hospital-access-analysis.md
    - assistant/walksheds/concept/walkshed-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Why are some destinations excluded?

## Short Answer

A destination may be excluded from a walkshed because it is outside the selected travel limit, unreachable in the modeled network, outside the analysis scope, filtered by destination rules, or missing from the source data.

## Significance

Exclusion explains why a nearby or expected place may not appear in the result and can identify a data, network, or configuration question for review.

## What This Means

Check the destination source, coordinates, filters, origin, profile, maximum cost, network connections, barriers, and dataset version. Determine whether the destination is excluded by data, analysis settings, or modeled reachability.

## What This Does Not Mean

A clinic lies close to the origin in a straight line but is outside the wheelchair profile's modeled cost limit. The analyst checks the network and destination filters before interpreting the result.

## How To Use This

Exclusion does not prove that the destination is physically inaccessible, unimportant, or absent from the real world. It does not establish an agency's responsibility.

## Example

Document excluded destinations and reasons, review important omissions locally, and rerun the analysis only after recording any changed data or settings.

## Assistant Guidance

Name the exclusion rule and source. Avoid treating absence from a result as a physical finding, and abstain when the destination data or analysis configuration is unknown.

## Related Concepts

- [What do walkshed result statistics represent?](walkshed-result-statistics.md)
- [Hospital access analysis](hospital-access-analysis.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
