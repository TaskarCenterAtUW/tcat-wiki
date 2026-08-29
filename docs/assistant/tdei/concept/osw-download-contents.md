---
title: What files are included in an OSW download?
slug: osw-download-contents
doc_type: concept
questions:
    - What files are included in an OSW download?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - export
    - formats
    - opensidewalks
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every OSW release contains exactly the same files.
        - An OSW download is automatically an OpenStreetMap database export.
related_pages:
    - assistant/tdei/concept/osw-edges-and-nodes.md
    - assistant/tdei/concept/osw-vs-osm-format.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# What files are included in an OSW download?

## Short Answer

An OSW download contains the files and metadata defined by the applicable OpenSidewalks dataset release. It commonly represents pedestrian-network entities and their relationships, but the exact file set depends on the release and format documentation.

## Significance

Knowing the contents helps users choose the right file for GIS, routing, or validation and prevents assumptions based on a different OSW version.

## What This Means

- Check the archive and release metadata first.
- Use the schema to identify network, attribute, and metadata files.
- Preserve the original archive and version when extracting or converting it.

## What This Does Not Mean

Every OSW download does not necessarily contain the same files, and file presence does not prove that a layer is complete or populated. An OSW download is not automatically an OSM database export.

## How To Use This

List the files in the downloaded archive, compare them with the current schema, and document any conversion or filtering before analysis.

## Example

A GIS analyst receives an OSW archive, inspects its files and metadata, identifies the network entities needed for a map, and records the release before converting selected layers.

## Assistant Guidance

Cite the OSW release and schema version. Do not provide an exhaustive file list without a version, and ask for the archive metadata when the contents differ from expectations.

## Related Concepts

- [OSW edges and nodes](osw-edges-and-nodes.md)
- [OSW versus OSM format](osw-vs-osm-format.md)
- [OpenSidewalks schema](../../opensidewalks/concept/opensidewalks-schema.md)
