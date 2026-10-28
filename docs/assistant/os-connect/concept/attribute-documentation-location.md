---
uid: 8602231a-7020-4aa2-9fed-dcd4725c953e
title: Where are OpenSidewalks attribute definitions documented?
slug: attribute-documentation-location
doc_type: concept
questions:
    - Where are OpenSidewalks attribute definitions documented?
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
    - documentation
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/os-connect/index.md
tags:
    - Assistant
---

<!-- @format -->

# Where are OpenSidewalks attribute definitions documented?

## Short Answer

The OpenSidewalks schema documents field definitions; the OS-CONNECT Data Viewer manual describes attributes shown in feature popups. Consult the applicable schema and dataset version for authoritative meanings.

## Significance

Attribute availability affects what can be interpreted or modeled for a feature.

## What This Means

The viewer may show `highway`, `footway`, `kerb`, `barrier`, `incline`, `width`, `length`, `foot`, `surface`, and `tactile_paving`. Values describe the selected feature and may be absent for other features.

## What This Does Not Mean

An absent attribute is not proof that the real-world condition is absent.

## How To Use This

Check the selected feature, schema version, and dataset metadata before comparing attributes across jurisdictions.

## Example

A sidewalk popup shows `width`, `surface`, and `incline`, while a kerb popup shows `barrier` and `kerb`.

## Assistant Guidance

Do not fill missing values from assumptions. Ask for the dataset and feature type.

## Related Concepts

- [What is OS-CONNECT?](os-connect.md)
- [Where are OpenSidewalks attribute definitions documented?](attribute-documentation-location.md)
