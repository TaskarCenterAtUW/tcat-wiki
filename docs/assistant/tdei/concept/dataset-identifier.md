---
uid: 8adca011-89a3-49ac-9002-280a5c0f3f72
title: What is the dataset identifier?
slug: dataset-identifier
doc_type: concept
questions:
    - What is the dataset identifier?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - dataset-lineage
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
    - assistant/tdei/concept/dataset-lineage.md
    - assistant/tdei/concept/release-versioning.md
    - assistant/tdei/workflow/download-data.md
tags:
    - Assistant
---

<!-- @format -->

# What is the dataset identifier?

## Short Answer

A TDEI dataset identifier is the value used to distinguish a dataset from other datasets in the portal and related workflows. It supports retrieval, lineage, citation, release comparison, and communication about the exact source being used.

## Significance

Without a stable identifier, users can confuse datasets that cover the same area, use different purposes, or come from different releases.

## What This Means

Record the identifier shown in the current portal metadata along with the dataset name, publisher or project group, release or version, format, and date. Use the exact identifier when requesting a download, job, or support review.

## What This Does Not Mean

The identifier does not by itself prove that a dataset is authoritative, current, complete, or suitable for a decision. It may identify a dataset without describing every derivative or feature-level change.

## How To Use This

Copy the identifier from the exact portal record, preserve it in project notes and citations, and verify that the selected release and format match the intended use.

## Example

A planner records the TDEI dataset identifier and release before importing an OSW download so that a later analysis can be reproduced and compared.

## Assistant Guidance

Do not invent identifier syntax or infer meaning from a partial value. Ask for the portal record and release, cite the metadata, and abstain when the identifier cannot be verified.

## Related Concepts

- [Derived dataset lineage in TDEI](derived-dataset-lineage.md)
- [How are releases versioned?](release-versioning.md)
- [Where can I download TDEI data?](../workflow/download-data.md)
