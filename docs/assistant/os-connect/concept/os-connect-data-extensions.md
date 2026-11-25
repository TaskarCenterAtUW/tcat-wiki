---
uid: 61db513d-3c76-4860-baf7-a8d5c17b5a48
title: How can OS-CONNECT data be extended?
slug: os-connect-data-extensions
doc_type: concept
questions:
    - Can OS-CONNECT data include attributes beyond its collected fields?
    - How can an OpenSidewalks-format dataset preserve local attributes?
    - Does OS-CONNECT support custom attributes or entities?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OS-CONNECT
    - OpenSidewalks
topics:
    - os-connect
    - opensidewalks
    - interoperability
    - formats
    - standards
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/os-connect/concept/os-connect-entities-and-attributes.md
    - assistant/opensidewalks/concept/external-attributes.md
    - assistant/opensidewalks/concept/custom-entities.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# How can OS-CONNECT data be extended?

## Short Answer

OpenSidewalks-format datasets provide extension mechanisms: additional non-core attributes can use the `ext:` prefix, and Custom Entities can represent feature types that do not fit a predefined entity. These mechanisms do not establish that OS-CONNECT accepts, displays, or publishes a particular extension.

## Significance

Separating the shared feature model from regional additions helps preserve interoperability while allowing a dataset steward to retain useful local information without presenting it as a universally defined OS-CONNECT field.

## What This Means

Use an existing standardized field when it matches the meaning of the information. In an OpenSidewalks-format dataset, a local or partner-specific attribute that has no core equivalent can be represented with an `ext:` key, with its meaning documented for intended consumers.

If the information describes a new kind of feature rather than another attribute on an existing feature, OpenSidewalks Custom Entities may be appropriate. Choose the custom graph entity only when the feature belongs in the traversable network; otherwise use the applicable non-network custom geometry type. Follow the relevant schema version for identifiers, topology, and other required structure.

For OS-CONNECT specifically, confirm support with the applicable ingestion, release, and viewer documentation before claiming that an extension is accepted, retained, displayed, or included in a public dataset.

## What This Does Not Mean

An `ext:` key is not part of the OpenSidewalks core schema, is not guaranteed to be understood by every consumer, and does not by itself make a field an OS-CONNECT attribute. A Custom Entity does not automatically create connectivity or prove that OS-CONNECT supports the type.

## How To Use This

Confirm the data format, schema version, feature meaning, and intended consumer first. Preserve the canonical fields, document each extension's name, meaning, values, units, and source, validate the dataset, and ask the dataset steward whether the relevant pipeline and release retain it.

## Example

A jurisdiction has a local maintenance observation that is not part of the reported OS-CONNECT attribute inventory. It may preserve the observation as a documented `ext:` attribute in an OpenSidewalks-format derivative, then validate consumer support and release handling before describing it as available in OS-CONNECT.

## Assistant Guidance

Present `ext:` attributes and Custom Entities as OpenSidewalks-format extension options, not as confirmed OS-CONNECT ingestion or viewer capabilities. Do not invent extension keys or promise persistence, display, or publication. Cite the schema version and product documentation that establish support; otherwise state that support is unconfirmed.

## Related Concepts

- [What entities and attributes does OS-CONNECT collect?](os-connect-entities-and-attributes.md)
- [How can an OpenSidewalks dataset support external attributes?](../../opensidewalks/concept/external-attributes.md)
- [What are Custom Entities in OpenSidewalks?](../../opensidewalks/concept/custom-entities.md)
- [What is the OpenSidewalks data schema?](../../opensidewalks/concept/opensidewalks-schema.md)
