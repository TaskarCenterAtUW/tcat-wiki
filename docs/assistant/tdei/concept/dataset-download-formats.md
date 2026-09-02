---
uid: b47df565-7d16-4150-9857-39e68e12b46c
title: Which formats can a TDEI dataset download use?
slug: dataset-download-formats
doc_type: concept
questions:
    - Which formats can a TDEI dataset download use?
audiences:
    - developer
    - planner
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - formats
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
        - Every TDEI dataset supports every download format.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Which formats can a TDEI dataset download use?

## Short Answer

For applicable OpenSidewalks datasets, the download dialog may offer OSW and OSM formats. The available choices depend on the dataset and current portal configuration.

## Significance

The selected format affects which tools can consume the downloaded data. It should match the intended editing, analysis, or exchange workflow.

## What This Means

Choose the format from the dataset's download dialog and review the result in the intended tool. Do not assume the same choices appear for every dataset.

## What This Does Not Mean

Choosing OSM or OSW does not change the source dataset in TDEI. It creates a downloaded representation.

## How To Use This

Confirm the dataset type and intended consumer before downloading. Preserve the source and record the selected format.

## Example

A user downloads an OS-CONNECT dataset as OSW for schema-aware processing or as OSM for a compatible editing workflow.

## Assistant Guidance

Ask which dataset and consumer are involved. Verify current format support before giving exact instructions.

## Related Concepts

- [What file formats are available?](file-formats.md)
