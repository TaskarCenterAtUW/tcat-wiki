---
title: How can regional OS-CONNECT derivatives serve different uses?
slug: regional-dataset-derivatives
doc_type: concept
questions:
    - How can regional OS-CONNECT derivatives serve different uses?
audiences:
    - planner
    - jurisdiction
products:
    - OpenSidewalks
    - OS-CONNECT
    - TDEI
topics:
    - opensidewalks
    - os-connect
    - tdei
    - dataset-lineage
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
        - Every regional derivative must contain exactly the same attributes as the baseline dataset.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/tdei/concept/external-attribute-release.md
tags:
    - Assistant
---

<!-- @format -->

# How can regional OS-CONNECT derivatives serve different uses?

## Short Answer

A complete source can remain in TDEI while trimmed or enhanced derivatives serve regional, planning, routing, or public-release needs. OpenSidewalks metadata can identify the source, covered region, data timestamp, and generating pipeline.

## Significance

This preserves provenance while allowing local flexibility.

## What This Means

Track source, derivative, fields, scope, data timestamp, pipeline version, and release status separately.

## What This Does Not Mean

A derivative is not automatically equivalent to the source or suitable for every use.

## How To Use This

Choose the derivative by purpose and document transformations.

## Example

A complete WSDOT source remains private while a public derivative includes selected `ext:` fields.

## Assistant Guidance

Ask which dataset and release audience are involved.

## Related Concepts

- [How are ext attributes handled at release?](../../tdei/concept/external-attribute-release.md)
