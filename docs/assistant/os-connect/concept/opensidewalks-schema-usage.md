---
title: What does it mean that OS-CONNECT uses the OpenSidewalks schema?
slug: opensidewalks-schema-usage
doc_type: concept
questions:
    - What does it mean that OS-CONNECT uses the OpenSidewalks schema?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - opensidewalks
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
    - assistant/os-connect/concept/opensidewalks-schema.md
    - assistant/os-connect/concept/opensidewalks.md
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# What does it mean that OS-CONNECT uses the OpenSidewalks schema?

## Short Answer

Saying that OS-CONNECT uses the OpenSidewalks schema means that its data are structured according to the documented OpenSidewalks model for representing pedestrian features and attributes, subject to the specific release and implementation.

## Significance

Using a shared schema improves consistency and makes compatible conversion, validation, and interpretation more practical.

## What This Means

Check the schema version, feature definitions, required and optional fields, value domains, geometry rules, and release metadata. Preserve provenance when converting or consuming the data.

## What This Does Not Mean

Schema use does not mean that OS-CONNECT and every OpenSidewalks dataset are identical, complete, synchronized, or authoritative. It does not guarantee that every consumer supports every field.

## How To Use This

Use the exact schema documentation for the release, validate data before exchange, and document any fields or semantics that a consumer does not support.

## Example

An analyst converts OS-CONNECT data to another compatible format, checks the schema and required fields, and retains the source release and identifier.

## Assistant Guidance

Do not infer compatibility or equivalence from the schema name alone. Cite the current schema and release, and abstain when the version or conversion behavior is unknown.

## Related Concepts

- [What is the OpenSidewalks schema?](opensidewalks-schema.md)
- [What is OpenSidewalks?](opensidewalks.md)
- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
