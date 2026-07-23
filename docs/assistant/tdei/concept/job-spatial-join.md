---
title: "What does the TDEI Spatial Join job do?"
slug: job-spatial-join
doc_type: concept
questions:
    - What does the TDEI Spatial Join job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - vector-data
    - interoperability
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A spatial join proves that joined features have the same real-world meaning.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/spatial-join.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Spatial Join job do?

## Short Answer

The Spatial Join job combines information from datasets based on spatial relationships.

## Significance

Spatial joins support enrichment and analysis across compatible geographic datasets.

## What This Means

Provide the required source datasets and spatial relationship inputs, submit the job, and inspect the output and lineage.

## What This Does Not Mean

Spatial proximity alone does not establish semantic equivalence or a correct operational relationship.

## How To Use This

Check coordinate systems, geometry validity, join rules, source versions, and output attributes.

## Example

A pedestrian network is joined with a jurisdiction boundary layer so features can be analyzed by area.

## Assistant Guidance

Ask which layers, CRS, join predicate, and intended output are involved.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
