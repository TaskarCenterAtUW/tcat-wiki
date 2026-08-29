---
title: What is an interoperable accessibility ecosystem?
slug: interoperable-accessibility-ecosystem
doc_type: concept
questions:
    - What is an interoperable accessibility ecosystem?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - interoperability
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
    - assistant/os-connect/concept/os-connect-tdei-relationship.md
    - assistant/os-connect/concept/gtfs-pathways-generation.md
tags:
    - Assistant
---

<!-- @format -->

# What is an interoperable accessibility ecosystem?

## Short Answer

An interoperable accessibility ecosystem is a set of data, schemas, tools, and organizations that can exchange accessibility-related information while preserving meaning, provenance, versions, and appropriate responsibilities.

## Significance

Interoperability can reduce duplicated work and help pedestrian, transit, planning, and community systems use compatible information without making them one system.

## What This Means

Use documented schemas and formats, preserve identifiers and source metadata, validate conversions, define ownership and review, and distinguish pedestrian, transit, routing, and analysis layers.

## What This Does Not Mean

Interoperability does not mean that datasets are interchangeable, synchronized, complete, or authoritative for every use. A shared format does not guarantee shared quality or semantics.

## How To Use This

Check the source and target schema, version, licensing, required fields, conversion behavior, and downstream consumer before integrating data.

## Example

An agency combines a pedestrian dataset with transit pathway data after validating identifiers, geometry, field meanings, and release dates, while retaining each source's provenance.

## Assistant Guidance

Explain the boundary between compatibility and equivalence. Cite the relevant schema or release, and abstain when the integration path or semantics are undocumented.

## Related Concepts

- [What is the OpenSidewalks schema?](opensidewalks-schema.md)
- [How is OS-CONNECT related to TDEI?](os-connect-tdei-relationship.md)
- [Can OS-CONNECT generate GTFS Pathways data?](gtfs-pathways-generation.md)
