---
title: "What is the relationship between source and derivative datasets in TDEI?"
slug: source-and-derivative-datasets
doc_type: concept
questions:
    - What is the relationship between source and derivative datasets in TDEI?
    - Can a complete source dataset remain private while a derivative is released?
    - How should external attributes be handled before publication?
    - Does TDEI automatically record a source-to-derivative relationship?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - dataset-lineage
    - releases
    - data-quality
    - interoperability
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: true
    do_not_claim:
        - A dataset stored in TDEI is automatically public.
        - A released derivative must contain every field in its source dataset.
        - TDEI automatically provides a complete source-to-derivative lineage graph.
related_pages:
    - assistant/opensidewalks/concept/external-attributes.md
    - assistant/tdei/workflow/integrate-external-geospatial-data.md
    - assistant/tdei/concept/release-versioning.md
    - assistant/workspaces/concept/dataset-lineage-in-tdei.md
    - assistant/tdei/index.md
tags:
    - Assistant
---

<!-- @format -->

# What is the relationship between source and derivative datasets in TDEI?

## Short Answer

A **source dataset** is the stewarded input. A **derivative dataset** is an output created by transforming, filtering, joining, editing, or validating that source.

A source may remain restricted while a reviewed derivative is released. TDEI storage or processing does not automatically make either dataset public.

## Significance

This distinction preserves detailed source data while allowing purpose-specific releases for routing, planning, editing, or public download.

## What This Means

- Record source and output dataset identifiers.
- Define each derivative's purpose, audience, format, and fields.
- Document transformations, retained or removed fields, validation, and review.
- Review `ext:` fields separately.
- Check current TDEI permissions and release controls.

## What This Does Not Mean

A derivative is not automatically equivalent to its source or ready for release. TDEI does not necessarily provide a complete lineage graph. Removing fields does not remove privacy, licensing, attribution, or data-quality obligations.

## How To Use This

Preserve the source, create a scoped derivative, save the input and output identifiers, validate the result, document omissions, and complete release review before publication.

## Example

A jurisdiction keeps pedestrian geometry and maintenance attributes in a restricted source. A routing derivative retains required fields; a public derivative omits sensitive or unnecessary fields. Each output has documented lineage and review status.

## Assistant Guidance

For operational answers, request the dataset identifier, project group, intended audience, format, and processing operation. Cite current TDEI records or documentation before asserting access, lineage metadata, version behavior, or release status.

## Related Concepts

- [OpenSidewalks external attributes](../../opensidewalks/concept/external-attributes.md)
- [Integrate external geospatial data](../workflow/integrate-external-geospatial-data.md)
- [Release versioning](release-versioning.md)
- [Dataset lineage in TDEI](../../workspaces/concept/dataset-lineage-in-tdei.md)
