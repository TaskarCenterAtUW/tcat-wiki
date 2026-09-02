---
uid: fe02cb42-0751-4abe-b56c-96217e9ae38d
title: What does the TDEI Dataset Union job do?
slug: job-dataset-union
doc_type: concept
questions:
    - What does the TDEI Dataset Union job do?
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
        - A union automatically resolves conflicting features or provenance.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/dataset-union.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Dataset Union job do?

## Short Answer

The Dataset Union job merges spatial data from multiple datasets into a combined output.

## Significance

Union supports composing related geographic inputs for analysis or downstream processing.

## What This Means

Provide the required datasets, submit the job, and inspect the combined result, metadata, IDs, and lineage.

## What This Does Not Mean

Union does not automatically resolve conflicting attributes, duplicate features, topology, or source authority.

## How To Use This

Confirm compatible schemas, coordinate systems, feature meanings, and provenance before combining data.

## Example

A project combines two compatible regional layers into one analysis dataset and records both source versions.

## Assistant Guidance

Ask which datasets and conflict rules apply. Do not imply that union produces a publication-ready dataset without review.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
