---
uid: 9fa7a769-08d2-43c6-a40d-00f482049f09
title: What is the imagery JSON configuration?
slug: imagery-json-configuration
doc_type: concept
questions:
    - What is the imagery JSON configuration?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - imagery
    - basemaps
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/asr-imagery-list-repo.md
    - assistant/workspaces/concept/custom-imagery.md
    - assistant/workspaces/concept/imagery-raw-json-requirement.md
tags:
    - Assistant
---

<!-- @format -->

# What is the imagery JSON configuration?

## Short Answer

An imagery JSON configuration describes custom imagery layers and their properties in the structure expected by the current Workspaces or AVIV ScoutRoute workflow. The schema, required fields, and supported sources are version-dependent.

## Significance

A structured configuration lets a workspace load and present imagery consistently while keeping imagery separate from editable data.

## What This Means

Use the current schema and example, provide valid raw URLs and layer properties, confirm access and attribution, validate the JSON, save it in the appropriate workspace setting, and test loading.

## What This Does Not Mean

Valid JSON is not necessarily a valid imagery definition, and a configuration does not grant permission to use a source or prove that imagery is current or authoritative.

## How To Use This

Keep the definition and schema version with project records, check errors in the relevant environment, and do not change data based on imagery without appropriate evidence.

## Example

A manager uses the current ASR imagery-list schema to configure a local imagery source, validates the definition, and tests it with workspace contributors.

## Assistant Guidance

Do not invent fields or promise that a URL will load. Ask for the environment and schema version, cite current configuration guidance, and abstain when permissions are unknown.

## Related Concepts

- [What is the ASR imagery list repo?](asr-imagery-list-repo.md)
- [Can custom imagery be added?](custom-imagery.md)
- [Why must imagery use raw JSON links?](imagery-raw-json-requirement.md)
