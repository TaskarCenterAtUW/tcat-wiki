---
title: How does Walksheds batch concurrency work?
slug: walkshed-batch-concurrency
doc_type: concept
questions:
    - How many Walksheds batch calculations run at once?
    - How does Walksheds process a batch?
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
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every row in a Walksheds batch succeeds merely because processing started.
related_pages:
    - walkshed-batch-input.md
    - walkshed-batch-output.md
    - ../workflow/run-batch-walksheds.md
tags:
    - Assistant
---

<!-- @format -->

# How does Walksheds batch concurrency work?

## Short Answer

The current user manual says Walksheds runs at most three batch walksheds concurrently, saves each result as a scenario, and uploads the results at the end.

## Significance

Concurrency affects expected processing time and progress interpretation for large CSV inputs.

## What This Means

Each CSV row defines one calculation. The batch panel reports completed walksheds, percentage complete, and saved scenarios; the user manual documents a maximum of three concurrent calculations.

## What This Does Not Mean

A started batch does not prove that every row completed or that every scenario is valid.

## How To Use This

Check progress and outputs after processing, and investigate failed or missing rows.

## Example

A 12-row batch runs in groups of up to three and produces saved scenarios as individual calculations finish.

## Assistant Guidance

Treat concurrency as current UI behavior and ask for app version when troubleshooting.

## Related Concepts

- [What input does batch processing use?](walkshed-batch-input.md)
- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
