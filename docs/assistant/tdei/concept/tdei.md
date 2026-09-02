---
uid: 08caed9b-c4f5-4693-b7a8-b7ea5373b764
title: What is the TDEI?
slug: tdei
doc_type: concept
questions:
    - What is the TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - tdei-overview
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-02
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - TDEI is the same product as OS-CONNECT or Workspaces.
        - TDEI publication proves that transportation data is complete or current.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is TDEI?

## Short Answer

TDEI is the Transportation Data Exchange Initiative: shared infrastructure and standards for collecting, validating, managing, publishing, and consuming transportation datasets.

## Significance

TDEI connects data producers, stewards, and consumers through common metadata, formats, versioning, access controls, quality checks, APIs, and publication workflows.

## What This Means

Tools such as Workspaces, Rapid, AVIV ScoutRoute, JOSM, and iOSPointMapper can produce or edit data. TDEI Core handles ingestion, validation, metadata, lineage, quality checks, access control, publishing, and APIs. Applications such as OS-CONNECT, AccessMap, and Walksheds consume resulting data.

## What This Does Not Mean

TDEI is not one dataset, one editor, or a guarantee that every dataset is public, complete, current, or suitable for a particular decision.

## How To Use This

Identify whether the question concerns the portal, API, project group, dataset, job, release, or consumer application. Record the dataset ID, version, source, and intended use.

## Example

A data producer validates an OpenSidewalks file in TDEI, publishes a release, and a consumer downloads an appropriate representation for analysis.

## Assistant Guidance

Distinguish TDEI from OS-CONNECT and Workspaces in every answer. Ask for the relevant role, dataset state, and portal environment.

## Related Concepts

- [TDEI architecture](tdei-architecture.md)
- [What is a released dataset?](released-dataset.md)
- [What is a project group?](project-group.md)
