---
uid: 57386715-0bd4-4e6a-a200-d57f4c8941ae
title: Where is a Walksheds router built?
slug: walkshed-router-processing
doc_type: concept
questions:
    - Where is a Walksheds router built?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - routing
    - automation
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: low
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Router-building time depends only on the user's device.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Where is a Walksheds router built?

## Short Answer

Router construction runs on TCAT infrastructure rather than solely on the user's device.

## Significance

Processing time depends on the selected network and service conditions.

## What This Means

A larger or denser dataset may take longer to prepare.

## What This Does Not Mean

A slow request does not necessarily indicate a problem with the user's device.

## How To Use This

Wait for the router request to complete before retrying or diagnosing results.

## Example

A small town router builds quickly while a dense city network takes longer.

## Assistant Guidance

Ask for the dataset and request status before recommending local troubleshooting.

## Related Concepts

- [What does building a Walksheds router do?](walkshed-router-building.md)
