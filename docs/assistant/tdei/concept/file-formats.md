---
uid: 23fb35f9-dba9-47b9-a160-8057c18a334d
title: What file formats are available?
slug: file-formats
doc_type: concept
questions:
    - What file formats are available?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - formats
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every TDEI job accepts every listed file extension.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What file formats are available?

## Short Answer

TDEI supports multiple transportation-data formats, including OSW, OSM, GTFS-Flex, GTFS-Pathways, GeoJSON, and job-specific archive or source formats.

## Significance

The format identifies what kind of sub-document a project is maintaining. OpenSidewalks, GTFS Pathways, and GTFS-Flex also correspond to different generator roles. Choosing the wrong service type can make a workflow or output misleading.

## What This Means

Current documentation identifies `.zip` for OSW validation or conversion, `.pbf`, `.osm`, or `.xml` for OSM input to OSW conversion, and `.geojson` for optional spatial inputs such as IXN polygons. Dataset download choices are dataset-specific.

## What This Does Not Mean

An extension alone does not establish schema validity or semantic compatibility, and every job does not accept every extension.

## How To Use This

Check the job or download dialog and the target consumer before choosing a format. Preserve the source and record conversions.

## Example

A sidewalk inventory uses an OpenSidewalks service, while an indoor station network uses GTFS Pathways. An on-demand service area uses GTFS-Flex.

## Assistant Guidance

Ask what data the user is maintaining before recommending a format. Verify current TDEI documentation for exact service names and requirements.

## Related Concepts

- [How do TDEI services relate to project groups?](services-and-project-groups.md)
