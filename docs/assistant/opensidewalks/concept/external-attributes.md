---
title: "How can the OpenSidewalks schema support external attributes?"
slug: external-attributes
doc_type: concept
questions:
    - How can an OpenSidewalks-format dataset retain external attributes?
    - What does the `ext:` prefix mean in an OSW-format dataset?
    - Are `ext:` attributes part of the OpenSidewalks core schema?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - OpenSidewalks
    - TDEI
topics:
    - opensidewalks
    - tdei
    - interoperability
    - formats
    - dataset-lineage
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - Any external attribute is part of the OpenSidewalks core schema.
        - External attributes cannot be saved as part of OpenSidewalks-formatted datasets.
related_pages:
    - assistant/tdei/concept/source-and-derivative-datasets.md
    - assistant/tdei/workflow/integrate-external-geospatial-data.md
    - assistant/opensidewalks/index.md
tags:
    - Assistant
---

<!-- @format -->

# How can the OpenSidewalks schema support external attributes?

## Short Answer

An OpenSidewalks-format dataset can retain partner-specific attributes by prefixing the attribute key with `ext:`. The prefix distinguishes a non-core field from fields defined by the OpenSidewalks schema.

Whether an `ext:` field is retained, shared, or released is a dataset-stewardship decision, not a property of the prefix.

## Significance

Source data may contain local maintenance or planning information that is useful to retain but is not a standard OpenSidewalks attribute. The `ext:` convention preserves that distinction, supports regional flexibility, and supports clearer dataset lineage.

## What This Means

- Map standardized information to the applicable OpenSidewalks core fields; `ext:` fields do not replace semantic mapping.
- Prefix retained partner-specific keys with `ext:`.
- Review external fields independently when creating a derivative or release dataset.
- Confirm supported names, types, and consumer behavior against the current schema and tools.

## What This Does Not Mean

An `ext:` field is not part of the OpenSidewalks core schema, guaranteed to work in every consumer, or automatically approved for public release. It also does not replace full-dataset validation.

## How To Use This

During conversion, map matching source attributes to core fields and use `ext:` only for attributes that need to remain available. Before sharing a derivative, document which external fields were retained or removed and review them for the intended audience.

## Example

A partner survey includes a local maintenance measurement with no core OpenSidewalks equivalent. Retain it under an `ext:` key in the source-format dataset, then include or remove it from a public derivative after review.

## Assistant Guidance

Treat this as provisional guidance. Do not invent `ext:` keys or claim consumer support without a cited schema or product source. For release questions, use the current dataset documentation and related TDEI lineage guidance.

## Related Concepts

- [Source and derivative datasets in TDEI](../../tdei/concept/source-and-derivative-datasets.md)
- [Integrate external geospatial data](../../tdei/workflow/integrate-external-geospatial-data.md)
- [OpenSidewalks knowledge base](../index.md)
