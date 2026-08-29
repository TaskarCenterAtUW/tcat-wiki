---
title: What accessibility information is missing from OS-CONNECT?
slug: missing-accessibility-information
doc_type: concept
questions:
    - What accessibility information is missing from OS-CONNECT?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - ada
    - completeness
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
    - assistant/os-connect/concept/accessibility-data-gaps.md
    - assistant/os-connect/concept/missing-attribute-values.md
    - assistant/os-connect/concept/ada-transition-data-requirements.md
tags:
    - Assistant
---

<!-- @format -->

# What accessibility information is missing from OS-CONNECT?

## Short Answer

OS-CONNECT may not contain every accessibility detail needed for a particular trip, inventory, planning decision, or compliance process. Missing information can include condition, dimensions, surface quality, slope, crossing operation, temporary barriers, entrances, ownership, inspection history, or lived experience.

## Significance

Knowing what is not represented prevents users from treating pedestrian geometry or a limited set of attributes as a complete accessibility assessment.

## What This Means

Check the release scope, feature and attribute definitions, source dates, coverage, confidence, and known limitations. Identify which fields are absent or unknown and supplement them with appropriate local, field, agency, or community evidence.

## What This Does Not Mean

Missing information does not prove that a condition is absent or inaccessible. OS-CONNECT does not certify accessibility, replace an inspection, or establish ADA compliance.

## How To Use This

Document the missing field or feature, preserve its unknown status, validate high-consequence locations locally, and report specific data gaps through the current channel.

## Example

A sidewalk is mapped, but its surface condition and curb-ramp details are not present in the release. A planner treats those facts as unknown and schedules additional review rather than assigning favorable values.

## Assistant Guidance

Name the dataset, release, feature, and missing information. Distinguish a missing attribute from a negative observation, cite the schema, and abstain from definitive accessibility claims.

## Related Concepts

- [What gaps still exist in accessibility data?](accessibility-data-gaps.md)
- [Why do some features have missing values?](missing-attribute-values.md)
- [What additional data is needed for ADA transition plans?](ada-transition-data-requirements.md)
