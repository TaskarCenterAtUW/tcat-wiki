---
uid: 1fffc62a-9d84-491d-bae5-1cc1a151bc84
title: How are campuses handled?
slug: campus-handling
doc_type: concept
questions:
    - How are campuses handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - campus
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
    - assistant/os-connect/concept/private-facilities.md
    - assistant/os-connect/concept/pedestrian-only-facilities.md
    - assistant/os-connect/concept/local-data-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How are campuses handled?

## Short Answer

Campus coverage depends on whether paths, entrances, crossings, and accessibility attributes are included in the source data and within the dataset's scope. Campus conditions should be interpreted with the responsible institution's current information.

## Significance

Campuses often contain internal paths, private areas, controlled entrances, and changing construction conditions that ordinary roadway data may not describe fully.

## What This Means

Review the dataset boundary, ownership, access restrictions, internal paths, buildings, entrances, crossings, and collection date. Combine OS-CONNECT with campus records and local verification when analyzing access to a campus destination.

## What This Does Not Mean

Do not infer that all campus paths are public, accessible, or covered. Campus handling does not establish institutional responsibility or ADA compliance.

## How To Use This

Confirm the campus boundary and intended use, identify the responsible institution, check current conditions, and label private, restricted, or unverified features clearly.

## Example

An analyst studies access to a clinic on a university campus, combines the pedestrian dataset with current campus entrance and construction information, and validates the final approach locally.

## Assistant Guidance

Ask which campus, destination, access restrictions, source, and version are involved. Cite the dataset and local source, distinguish modeled connectivity from entry access, and abstain when the campus data are not documented.

## Related Concepts

- [How are private facilities handled?](private-facilities.md)
- [How are pedestrian-only facilities handled?](pedestrian-only-facilities.md)
- [How should agencies validate the data locally?](local-data-validation.md)
