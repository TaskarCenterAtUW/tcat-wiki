---
uid: e2515fea-42fe-46dc-9d80-5cd5d7dc9d00
title: Why might a test dataset appear in the portal?
slug: test-dataset-in-portal
doc_type: concept
questions:
    - Why might a test dataset appear in the portal?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - releases
    - testing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A dataset labeled as test is suitable for public planning or production use.
        - A test dataset is automatically an error or a released dataset.
related_pages:
    - assistant/tdei/concept/dataset-visibility.md
    - assistant/tdei/concept/released-dataset.md
    - assistant/tdei/concept/mislabeled-dataset-handling.md
tags:
    - Assistant
---

<!-- @format -->

# Why might a test dataset appear in the portal?

## Short Answer

A test dataset may appear in the TDEI Portal because it supports development, validation, demonstration, or a project workflow. Check its label, project group, release status, scope, and metadata before using it.

## Significance

Distinguishing test data from released data prevents unverified content from entering planning, routing, or public communication.

## What This Means

- Inspect the dataset name, status, project group, version, and scope.
- Confirm whether it is private, test, staged, or released.
- Ask the responsible steward when the label or intended use is unclear.

## What This Does Not Mean

The presence of a test dataset does not prove that the portal is malfunctioning or that the data are suitable for production. A test label alone does not explain its provenance or access rules.

## How To Use This

Do not use the dataset for consequential analysis until its status and intended use are verified. Record the metadata and report a suspected labeling problem through the current support path.

## Example

An analyst sees a dataset marked for testing alongside released data, checks its project group and status, and excludes it from a public map until the steward confirms its purpose.

## Assistant Guidance

Do not infer why a particular test dataset exists. Ask for its identifier and portal context, cite TDEI metadata, and abstain from calling it released or authoritative without verification.

## Related Concepts

- [Dataset visibility](dataset-visibility.md)
- [Released dataset](released-dataset.md)
- [Mislabeled dataset handling](mislabeled-dataset-handling.md)
