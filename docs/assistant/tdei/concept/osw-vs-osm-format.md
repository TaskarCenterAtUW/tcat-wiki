---
title: What is the difference between downloading OSW format and OSM format?
slug: osw-vs-osm-format
doc_type: concept
questions:
    - What is the difference between downloading OSW format and OSM format?
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
        - Downloading one format automatically creates or updates the other.
        - Converting between OSW and OSM is always lossless.
related_pages:
    - assistant/tdei/concept/osw-download-contents.md
    - assistant/tdei/concept/osw-edges-and-nodes.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between downloading OSW format and OSM format?

## Short Answer

OSW and OSM are different formats used for different data workflows. OSW follows the OpenSidewalks schema for pedestrian-network and accessibility data, while OSM represents geographic objects in the OpenStreetMap data model; a conversion can change structure and available fields.

## Significance

Choosing a format affects which tools can read the data, how network relationships are represented, and what metadata are preserved.

## What This Means

- Choose OSW when the workflow requires the OpenSidewalks schema and its network entities.
- Choose OSM when the target workflow requires OpenStreetMap data structures or OSM-compatible editing.
- Check the release and conversion documentation before transforming files.

## What This Does Not Mean

Downloading one format does not automatically create or update the other. Equivalent-looking geometry does not mean that fields, relationships, provenance, or version information are identical.

## How To Use This

Select the target format based on the receiving tool and required fields, then record the source, target, schema version, and transformations.

## Example

An analyst downloads OSW for schema-aware pedestrian analysis but converts a copy to OSM for an OSM-compatible editing workflow, retaining both source and target metadata.

## Assistant Guidance

Cite the format and schema documentation, do not promise lossless conversion without evidence, and ask which tool and version are involved before recommending a format.

## Related Concepts

- [OSW download contents](osw-download-contents.md)
- [OSW edges and nodes](osw-edges-and-nodes.md)
- [OpenSidewalks schema](../../opensidewalks/concept/opensidewalks-schema.md)
