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
last_reviewed: 2026-10-26
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

The Portal lists `OSW`, `Flex`, and `Pathways` as dataset types, while individual jobs accept specific file formats. The current job guides list `.zip` for OSW, GTFS-Flex, and GTFS-Pathways validation; OSW-to-OSM conversion also uses `.zip`, while OSM-to-OSW conversion accepts `.pbf`, `.osm`, or `.xml`. Accepted formats depend on the job and selected options.

## Significance

A dataset or service type is not the same as a file extension. Matching the job's documented input format prevents upload and processing errors.

## What This Means

The current Portal job guides document `.zip` for OSW, GTFS-Flex, and GTFS-Pathways validation and OSW conversion; `.pbf`, `.osm`, or `.xml` for OSM input to OSW conversion; and `.geojson` for an optional intersection-polygon input to the IXN quality-metric job. The Portal's OSW dataset example shows a download-format dropdown that defaults to OSW; inspect the selected dataset's dialog for the choices available to that dataset.

## What This Does Not Mean

A file extension alone does not establish schema validity or semantic compatibility. A listed extension is not necessarily accepted by every job or service.

## How To Use This

Identify the dataset type and target job first. Check the corresponding job guide and the current form's allowed inputs, then preserve the source and record any conversion.

## Example

For OSW - Convert, select `.zip` when the source format is OSW and `.pbf`, `.osm`, or `.xml` when the source format is OSM. The documented Flex and Pathways validation jobs accept `.zip` archives.

## Assistant Guidance

Ask which dataset type, job, and intended output are involved. Cite the relevant current job guide for exact extensions and do not infer an input format from a service name.

## Related Concepts

- [How do TDEI services relate to project groups?](services-and-project-groups.md)
- [TDEI Portal job types and inputs](../../../tdei/portal/user-manual/jobs/index.md)
- [OSW - Validate input format](../../../tdei/portal/user-manual/jobs/osw-validate.md)
- [Flex - Validate input format](../../../tdei/portal/user-manual/jobs/flex-validate.md)
- [Pathways - Validate input format](../../../tdei/portal/user-manual/jobs/pathways-validate.md)
- [OSW - Convert input and output formats](../../../tdei/portal/user-manual/jobs/osw-convert.md)
- [IXN quality-metric polygon input](../../../tdei/portal/user-manual/jobs/quality-metric-ixn-calculation.md)
- [TDEI Portal service types](../../../tdei/portal/user-manual/services.md)
