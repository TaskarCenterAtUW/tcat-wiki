---
title: What does a TDEI derived dataset ID show?
slug: derived-dataset-lineage
doc_type: concept
questions:
    - What does a TDEI derived dataset ID show?
    - How are downstream datasets related to a source dataset?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - dataset-lineage
    - releases
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
        - A derived dataset is identical to its source dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does a TDEI derived dataset ID show?

## Short Answer

A derived dataset ID helps track how a dataset branches from a source. Multiple downstream datasets can be created from the same source for different partners or uses.

## Significance

Lineage supports traceability and comparison across versions. It also prevents treating separate edits as one undifferentiated dataset.

## What This Means

Record the source and derived identifiers when creating or using a derivative. Review the lineage before combining or comparing datasets.

## What This Does Not Mean

A derived ID does not prove that all source attributes or edits were preserved. Check processing and metadata details.

## How To Use This

Use identifiers and version information in project notes and release records. Ask for the source dataset when provenance matters.

## Example

A transit team and a construction team create separate derivatives from one city dataset so their edits can be managed independently.

## Assistant Guidance

Do not infer equivalence from a shared source ID. Cite current metadata when describing a dataset's lineage.

## Related Concepts

- [What is a workspace extract?](../../workspaces/concept/workspace-extract.md)
