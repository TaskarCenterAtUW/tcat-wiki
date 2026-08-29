---
title: What is the OpenSidewalks schema?
slug: opensidewalks-schema
doc_type: concept
questions:
    - What is the OpenSidewalks schema?
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
    - assistant/os-connect/concept/opensidewalks.md
    - assistant/os-connect/concept/opensidewalks-schema-usage.md
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# What is the OpenSidewalks schema?

## Short Answer

The OpenSidewalks schema is a structured model for representing pedestrian-network features, their geometry, relationships, and accessibility-related attributes in a consistent way.

## Significance

Shared definitions help mapping projects, validators, data services, and consumers interpret pedestrian data more consistently.

## What This Means

Read the current schema for feature types, fields, value domains, geometry, required and optional properties, and version changes. Preserve schema and source metadata in derived data.

## What This Does Not Mean

The schema is not a dataset, field survey, accessibility certification, or guarantee that every implementation contains every field or current condition.

## How To Use This

Use the schema version that matches the data, validate before exchange, and document unsupported or transformed fields.

## Example

An agency checks the schema before converting sidewalk and crossing data and records which fields remain unknown or unsupported in the target system.

## Assistant Guidance

Do not invent field meanings or assume schema compatibility from similar names. Cite the current schema and abstain when the relevant version is unavailable.

## Related Concepts

- [What does it mean that OS-CONNECT uses the OpenSidewalks schema?](opensidewalks-schema-usage.md)
- [What is OpenSidewalks?](opensidewalks.md)
- [What attributes are included for pedestrian features?](pedestrian-feature-attributes.md)
