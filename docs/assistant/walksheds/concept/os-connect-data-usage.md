---
uid: 1c1aa0d5-0d74-425f-80de-058df7743e63
title: How does Walksheds use OS-CONNECT data?
slug: os-connect-data-usage
doc_type: concept
questions:
    - How does Walksheds use OS-CONNECT data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - os-connect
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-31
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every OS-CONNECT release or feature is available in every Walksheds workflow.
    related_pages:
        - assistant/walksheds/concept/external-dataset-joins.md
tags:
    - Assistant
---

<!-- @format -->

# How does Walksheds use OS-CONNECT data?

## Short Answer

Walksheds can use an appropriate OS-CONNECT pedestrian-network release as a routing or reachability input.

## Significance

OS-CONNECT supplies network features; Walksheds applies travel profiles and cost rules to model reachable areas.

## What This Means

Check the dataset boundary, version, connectivity, and attributes before generating a walkshed.

## What This Does Not Mean

Using OS-CONNECT does not make a walkshed a field survey, ADA certification, or guarantee of current access.

## How To Use This

Record dataset, profile, cost, and assumptions in outputs.

## Example

A city uses a versioned OS-CONNECT release to compare pedestrian and wheelchair-oriented access to clinics.

## Assistant Guidance

Do not claim that every OS-CONNECT release or feature is available in every Walksheds workflow without verification.

## Related Concepts

- [External dataset joins](external-dataset-joins.md)
