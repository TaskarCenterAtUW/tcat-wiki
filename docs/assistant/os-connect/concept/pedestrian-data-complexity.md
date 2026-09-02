---
uid: f9b4d35c-e819-49a4-8706-cc3b6cb8ad90
title: What makes pedestrian data uniquely complex?
slug: pedestrian-data-complexity
doc_type: concept
questions:
    - What makes pedestrian data uniquely complex?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - complexity
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
    - assistant/os-connect/concept/data-maintenance-challenges.md
    - assistant/os-connect/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# What makes pedestrian data uniquely complex?

## Short Answer

Pedestrian data are complex because access depends on connected geometry, crossings, surfaces, slopes, barriers, entrances, changing conditions, different users, and distributed ownership. These details must be represented across compatible schemas and releases.

## Significance

Small geometry or attribute differences can change routing and reachability. Static data also cannot capture every temporal or lived condition.

## What This Means

Consider feature definitions, relationships, attributes, source dates, uncertainty, coverage, licensing, local authority, and the intended analysis. Combine structured data with field and community evidence.

## What This Does Not Mean

Complexity does not mean that a dataset is unusable, and a simple-looking map does not prove complete or accessible conditions.

## How To Use This

Use documented schemas, preserve provenance, validate consequential features, and communicate what is known and missing.

## Example

A crossing's geometry, curb ramps, surface, signal, and connection to sidewalks all affect how a route should be interpreted.

## Assistant Guidance

Avoid reducing pedestrian data to one completeness score or feature type. Cite the schema and release and abstain when the relevant context is missing.

## Related Concepts

- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
- [What makes accessibility data difficult to maintain?](data-maintenance-challenges.md)
- [What is the OpenSidewalks schema?](opensidewalks-schema.md)
