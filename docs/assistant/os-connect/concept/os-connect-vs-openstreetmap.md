---
title: How is OS-CONNECT different from OpenStreetMap?
slug: os-connect-vs-openstreetmap
doc_type: concept
questions:
    - How is OS-CONNECT different from OpenStreetMap?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - osm-interoperability
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
    - assistant/os-connect/concept/os-connect.md
    - assistant/os-connect/concept/opensidewalks-schema-usage.md
    - assistant/support/concept/tdei-os-connect-osm-differences.md
tags:
    - Assistant
---

<!-- @format -->

# How is OS-CONNECT different from OpenStreetMap?

## Short Answer

OpenStreetMap is a broad collaborative geographic database, while OS-CONNECT is a connected pedestrian-data product or release with its own scope, schema, processing, and publication context. OS-CONNECT may use or relate to OSM data, but the two should not be treated as the same dataset.

## Significance

The distinction helps users understand source, authority, update path, schema, coverage, and licensing before comparing or combining data.

## What This Means

Check the source, release, identifiers, schema, date, licensing, and processing history. Treat an OSM edit, an OS-CONNECT correction, and a TDEI release as separate workflow events unless documented otherwise.

## What This Does Not Mean

OS-CONNECT is not automatically a live mirror of OSM, and an OSM feature or edit does not automatically appear in an OS-CONNECT or TDEI release.

## How To Use This

Use each source for its documented purpose, preserve provenance when converting data, and validate geometry and attributes before combining them.

## Example

An analyst compares an OSM feature with an OS-CONNECT release, notices different dates and attributes, and records both sources rather than treating the difference as an error automatically.

## Assistant Guidance

Do not claim synchronization, ownership, or authority without evidence. Cite the relevant source and release, and abstain when lineage or update behavior is unknown.

## Related Concepts

- [What is OS-CONNECT?](os-connect.md)
- [What does it mean that OS-CONNECT uses the OpenSidewalks schema?](opensidewalks-schema-usage.md)
- [TDEI, OS-CONNECT, and OSM differences](../../support/concept/tdei-os-connect-osm-differences.md)
