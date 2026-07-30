---
title: What input does Walksheds batch processing use?
slug: walkshed-batch-input
doc_type: concept
questions:
    - What input does Walksheds batch processing use?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - data-collection
    - formats
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any CSV with coordinates is valid for every Walksheds batch request.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What input does Walksheds batch processing use?

## Short Answer

Batch requests use coordinate-based CSV input with the expected column names.

## Significance

Correct structure prevents avoidable invalid-input failures.

## What This Means

Prepare the file according to the current batch format: `lon`, `lat`, `maxuphill`, `maxdownhill`, `avoidcurbs`, `reversewalkshed`, `maxcost`, and optional `name`. Validate coordinates, booleans, decimal slope values, and cost units.

## What This Does Not Mean

A file that opens in a spreadsheet is not necessarily a valid batch input.

## How To Use This

Check required headers, coordinate order, and location accuracy before uploading.

## Example

A CSV contains the required coordinate columns for multiple parks and senior facilities.

## Assistant Guidance

Ask for the current batch schema and exact error before suggesting corrections.

## Related Concepts

- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
