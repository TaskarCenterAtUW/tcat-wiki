---
uid: 2fa3f991-fa78-4c2a-9ed1-0ffaf2d53496
title: How are ext attributes handled at release?
slug: external-attribute-release
doc_type: concept
questions:
    - How are ext attributes handled at release?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - public-vs-private-data
    - publication-workflow
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every ext attribute in a source dataset must be released publicly.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How are ext attributes handled at release?

## Short Answer

A release can retain all `ext:` fields, remove them all, or manually filter selected fields before publishing a derivative.

## Significance

This lets a steward preserve a complete private source while sharing only appropriate attributes.

## What This Means

Review extension names, sensitivity, usefulness, and intended audience before release.

## What This Does Not Mean

The `ext:` prefix itself does not decide whether an attribute is public.

## How To Use This

Use a script or GIS tool to create and review a cleaned derivative when needed.

## Example

A complete source remains private while a public derivative removes internal maintenance fields.

## Assistant Guidance

Ask about release status, audience, and stewardship authority before recommending filtering.

## Related Concepts

- [How can the OpenSidewalks schema support external attributes?](../../opensidewalks/concept/external-attributes.md)
