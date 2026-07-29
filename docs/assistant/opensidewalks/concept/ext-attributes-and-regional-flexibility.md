---
title: "How do ext attributes support regional flexibility?"
slug: ext-attributes-and-regional-flexibility
doc_type: concept
questions:
    - How do ext attributes support regional flexibility?
audiences:
    - developer
    - jurisdiction
products:
    - OpenSidewalks
    - Workspaces
topics:
    - opensidewalks
    - workspaces
    - interoperability
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - An ext attribute is part of the OpenSidewalks baseline schema.
related_pages:
    - assistant/opensidewalks/index.md
    - assistant/opensidewalks/concept/external-attributes.md
tags:
    - Assistant
---

<!-- @format -->

# How do ext attributes support regional flexibility?

## Short Answer

The `ext:` convention lets a regional dataset add local attributes on top of the baseline OpenSidewalks schema.

## Significance

It supports local data collection without requiring every region to adopt every national field.

## What This Means

Keep core fields compatible and document local extension names, meanings, and consumers.

## What This Does Not Mean

An extension is not universally standardized or guaranteed to work in every tool.

## How To Use This

Review, validate, and decide whether extensions belong in a released derivative.

## Example

A region adds an `ext:` field for a local ADA-planning observation.

## Assistant Guidance

Do not invent extension names or imply legal meaning from a local tag.

## Related Concepts

- [How can the OpenSidewalks schema support external attributes?](external-attributes.md)
