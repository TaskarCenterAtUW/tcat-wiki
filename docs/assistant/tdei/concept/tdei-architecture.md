---
title: "How is TDEI organized?"
slug: tdei-architecture
doc_type: concept
questions:
    - How is TDEI organized?
    - What does TDEI Core do?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - TDEI
topics:
    - tdei
    - tdei-ecosystem
    - interoperability
    - dataset-lineage
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - TDEI Core is the same as any individual data-producing or consuming application.
related_pages:
    - ../index.md
    - tdei.md
    - ../../../tdei/index.md
tags:
    - Assistant
---

<!-- @format -->

# How is TDEI organized?

## Short Answer

TDEI connects data-producing tools, a core exchange layer, and data-consuming applications across the transportation-data lifecycle.

## Significance

The architecture clarifies where collection, editing, validation, publication, APIs, and consumption occur.

## What This Means

Tools such as AVIV ScoutRoute, Rapid, Prophet, and iOSPointMapper feed TDEI Core. Core services include ingestion, validation, schema and metadata handling, versioning and lineage, quality checks, access control, publishing, catalog functions, APIs, and SDKs. Applications such as OS-CONNECT, AccessMap, and Walksheds consume resulting data.

## What This Does Not Mean

A producer, TDEI, and consumer are not interchangeable products. A dataset's presence in one layer does not establish its status in another.

## How To Use This

Identify the layer responsible for the user's problem before troubleshooting. Use portal and API documentation for TDEI operations, editor documentation for data creation, and consumer documentation for visualization or routing.

## Example

A producer edits data in Workspaces, validates and publishes it through TDEI, and a public viewer consumes the released version.

## Assistant Guidance

Ask whether the question concerns data creation, exchange, release, API access, or consumption.

## Related Concepts

- [What is TDEI?](tdei.md)
- [What is a released dataset?](released-dataset.md)
