---
title: "How do I conflate jurisdiction datasets in TDEI?"
slug: conflate-jurisdiction-datasets
doc_type: workflow
questions:
    - How do I conflate jurisdiction datasets in TDEI?
    - When should I use union or spatial join?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
    - OS-CONNECT
topics:
    - tdei
    - opensidewalks
    - os-connect
    - interoperability
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A union or spatial join automatically resolves every duplicate feature or attribute conflict.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I conflate jurisdiction datasets in TDEI?

## Short Answer

Upload compatible datasets, then use a union for simpler best-effort merging or a spatial join when selecting geometry and attributes requires more control.

## Significance

Conflation combines partner data while preserving an intentional choice of source geometry and attributes.

## What This Means

Validate inputs, choose the job, inspect the output, and review duplicate or conflicting features.

## What This Does Not Mean

A completed job does not prove that the merged dataset is correct or ready for release.

## How To Use This

Test by jurisdiction first and document the selected source, geometry, attributes, and scope.

## Example

A partner OpenSidewalks dataset is merged with OS-CONNECT using a spatial join to control which attributes survive.

## Assistant Guidance

Ask whether the need is simple combination or controlled attribute and geometry selection.

## Related Concepts

- [What are TDEI processing jobs?](../concept/tdei-job-processing.md)
