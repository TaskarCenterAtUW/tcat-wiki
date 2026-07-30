---
title: How do I generate OpenSidewalks Tasking Manager polygons?
slug: generate-task-polygons
doc_type: workflow
questions:
    - How do I generate OpenSidewalks task polygons?
    - How does the OSW task polygon workflow work?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
topics:
    - opensidewalks
    - editing-tools
    - automation
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The task-polygon command syntax is unchanged across OSW tool versions.
        - Generated polygons are ready for publication without inspection.
related_pages:
    - ../concept/tasking-manager-roles.md
    - ../../../opensidewalks/tasking-manager/task-polygon-automation.md
tags:
    - Assistant
---

<!-- @format -->

# How do I generate OpenSidewalks Tasking Manager polygons?

## Short Answer

The documented internal workflow stages state, county, and community data, extracts OSM PBF data with `osmium`, runs `osw task` against a community target GeoJSON, and prepares crossing and sidewalk task-polygon outputs.

## Significance

Automation can produce repeatable task boundaries for organized pedestrian-infrastructure mapping projects.

## What This Means

Prepare a staging directory with `data_sources`, `intermediate_data`, and `output` folders. Store state PBF data and community target GeoJSON, extract the community PBF, run `osw task`, and rename the resulting crossing and sidewalk GeoJSON files for upload.

## What This Does Not Mean

Generated polygons do not verify the source data, task coverage, or output quality. The workflow depends on installed tools and current command behavior.

## How To Use This

Confirm the `osw` and `osmium` versions, preserve the staging structure, inspect outputs, and follow the current Tasking Manager upload requirements.

## Example

A community folder contains a source PBF, target GeoJSON, extracted community PBF, and separately named crossing and sidewalk task-polygon files.

## Assistant Guidance

Ask for tool versions, paths, target geometry, and intended Tasking Manager format. Treat this as an internal, version-sensitive workflow.

## Related Concepts

- [What roles exist in the Tasking Manager?](../concept/tasking-manager-roles.md)
- [How do I map OSW features?](map-osw-features-in-tasking-manager.md)
