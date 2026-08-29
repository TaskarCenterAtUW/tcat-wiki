---
title: How is OS-CONNECT related to TDEI?
slug: os-connect-tdei-relationship
doc_type: concept
questions:
    - How is OS-CONNECT related to TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - tdei
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
    - assistant/os-connect/concept/os-connect.md
    - assistant/tdei/concept/tdei.md
    - assistant/os-connect/concept/opensidewalks-schema-usage.md
tags:
    - Assistant
---

<!-- @format -->

# How is OS-CONNECT related to TDEI?

## Short Answer

OS-CONNECT is a pedestrian-network data product or release, while TDEI provides services for datasets, metadata, processing, downloads, and releases. An OS-CONNECT dataset may be distributed or managed through TDEI workflows when the current release documentation says so.

## Significance

The relationship helps users distinguish the data from the platform or service used to store, process, identify, or publish it.

## What This Means

Check the exact dataset identifier, source, schema, release, TDEI service, and download or processing workflow. Preserve lineage when moving between OS-CONNECT and TDEI.

## What This Does Not Mean

The products are not interchangeable, and an OS-CONNECT change does not automatically update every TDEI record or downstream tool.

## How To Use This

Use OS-CONNECT documentation for data meaning and TDEI documentation for portal, job, download, and release behavior. Cite both when explaining an integrated workflow.

## Example

An analyst selects an OS-CONNECT release in TDEI, records its identifier and version, downloads a supported format, and retains the source metadata for analysis.

## Assistant Guidance

Do not claim automatic synchronization or a universal publication path. Ask for the release and environment, cite current metadata, and abstain when the relationship is not documented.

## Related Concepts

- [What is OS-CONNECT?](os-connect.md)
- [What is the TDEI?](../../tdei/concept/tdei.md)
- [What does it mean that OS-CONNECT uses the OpenSidewalks schema?](opensidewalks-schema-usage.md)
