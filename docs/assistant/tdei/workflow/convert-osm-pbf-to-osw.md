---
title: How do I convert an OSM PBF file to OpenSidewalks format?
slug: convert-osm-pbf-to-osw
doc_type: workflow
questions:
    - How do I convert an OSM PBF file to OpenSidewalks format?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - formats
    - interoperability
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-12
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Converting an OSM PBF file produces complete or validated pedestrian data automatically.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I convert an OSM PBF file to OpenSidewalks format?

## Short Answer

Create a TDEI conversion job with OSM as the source format and OSW as the target format, then download the result for workspace creation.

## Significance

This bridges selected OSM extracts and OpenSidewalks-oriented editing.

## What This Means

Submit the PBF, wait for the job, download the OSW archive, and inspect or validate it.

## What This Does Not Mean

Format conversion does not guarantee complete, correct, or project-ready data.

## How To Use This

Record the source area, job ID, output version, and validation result.

## Example

A SliceOSM area is converted through TDEI and loaded into a new OSW workspace.

## Assistant Guidance

Ask for current supported source and target formats before giving exact steps.

## Related Concepts

- [How can OSM data be imported into Workspaces?](../../workspaces/workflow/import-osm-data-into-workspaces.md)
