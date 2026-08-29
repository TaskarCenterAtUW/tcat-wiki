---
title: What attributes are required vs recommended?
slug: required-vs-recommended-attributes
doc_type: concept
questions:
    - What attributes are required vs recommended?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - formats
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
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
    - assistant/os-connect/concept/opensidewalks-schema.md
    - assistant/os-connect/concept/missing-attribute-values.md
tags:
    - Assistant
---

<!-- @format -->

# What attributes are required vs recommended?

## Short Answer

Required attributes are fields a schema, validator, or workflow needs for a feature or file to be valid. Recommended attributes provide useful additional context but may be optional. The exact distinction depends on the schema version and use.

## Significance

Knowing the distinction helps contributors validate data without treating an optional unknown as an error or assuming that required fields guarantee accessibility.

## What This Means

Check the exact schema and validator, feature type, version, and intended consumer. Preserve missing optional information, satisfy required structural fields, and document fields that a workflow cannot provide.

## What This Does Not Mean

Required does not mean accurate, current, complete, or sufficient for a planning or accessibility decision. Recommended does not mean irrelevant or safe to invent.

## How To Use This

Use the release-specific schema and validation results, do not fill unknown values by assumption, and supplement required fields with local evidence when the decision needs more detail.

## Example

A sidewalk file passes structural validation because required geometry fields are present, but its optional surface and condition fields remain unknown and require separate review.

## Assistant Guidance

Name the schema, version, feature, and validator. Do not provide a universal field list without evidence and abstain when the requirement is release-specific.

## Related Concepts

- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [What is the OpenSidewalks schema?](opensidewalks-schema.md)
- [Why do some features have missing values?](missing-attribute-values.md)
