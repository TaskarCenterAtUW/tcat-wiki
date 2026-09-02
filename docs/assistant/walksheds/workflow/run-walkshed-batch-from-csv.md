---
uid: 94429e21-4442-46ef-8725-ffe376c1809e
title: How do I run a Walksheds batch from CSV?
slug: run-walkshed-batch-from-csv
doc_type: workflow
questions:
    - How do I run a Walksheds batch from CSV?
    - What columns does a Walksheds batch CSV need?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - walksheds
    - formats
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
        - A batch run guarantees that every CSV row produces a valid scenario.
related_pages:
    - ../concept/walkshed-batch-input.md
    - ../concept/walkshed-batch-output.md
    - ../concept/walkshed-batch-concurrency.md
    - ../../../walksheds/user-manual/batches.md
tags:
    - Assistant
---

<!-- @format -->

# How do I run a Walksheds batch from CSV?

## Short Answer

Prepare a CSV with the required origin, slope, obstacle, reverse, cost, and optional name columns, upload it in the Batch tab, and select **Run batch**.

## Significance

Batch processing applies consistent assumptions to multiple origins or scenarios.

## What This Means

Use `lon`, `lat`, `maxuphill`, `maxdownhill`, `avoidcurbs`, `reversewalkshed`, and `maxcost`; `name` is optional. Slope values use decimals such as `0.08` for 8%, and cost is in seconds. The current guide documents up to three concurrent calculations.

## What This Does Not Mean

A spreadsheet that opens successfully is not necessarily valid, and completed processing does not prove that every output is correct.

## How To Use This

Validate headers, longitude/latitude order, booleans, decimal slope values, budgets, and names before upload. Monitor progress and inspect saved scenarios.

## Example

A CSV contains three origins with different slope and cost assumptions, and the batch creates three named scenarios.

## Assistant Guidance

Ask for the exact CSV headers, row error, dataset version, and app behavior. Do not request sensitive data unnecessarily.

## Related Concepts

- [What input does batch processing use?](../concept/walkshed-batch-input.md)
- [How does batch concurrency work?](../concept/walkshed-batch-concurrency.md)
