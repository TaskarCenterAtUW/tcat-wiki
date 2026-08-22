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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any CSV with coordinates is valid for every Walksheds batch request.
related_pages:
    - ../workflow/run-batch-walksheds.md
    - walkshed-batch-output.md
tags:
    - Assistant
---

<!-- @format -->

# What input does Walksheds batch processing use?

## Short Answer

Batch requests use coordinate-based CSV input with the expected column names, but batch processing does not support every mobility-profile setting available in the Walksheds interface or URL parameters.

## Significance

Correct structure prevents avoidable invalid-input failures.

## What This Means

Prepare the file according to the current batch format: `lon`, `lat`, `maxuphill`, `maxdownhill`, `avoidcurbs`, `reversewalkshed`, `maxcost`, and optional `name`. These fields represent the batch settings currently identified for maximum uphill, maximum downhill, avoiding curbs, reverse walksheds, and maximum cost. Validate coordinates, booleans, decimal slope values, and cost units.

Do not assume that a mobility-profile setting exposed in the regular Walksheds UI interface or URL is available in batch processing. For example, the **Avoid street** slider in the interface and the corresponding street-avoidance factor in the URL are not supported in Walksheds batch processing.

## What This Does Not Mean

A file that opens in a spreadsheet is not necessarily a valid batch input. Likewise, a setting that works in an individual Walksheds request is not necessarily available as a batch column.

## How To Use This

Check required headers, coordinate order, location accuracy, and the current list of supported batch settings before uploading. If street avoidance is required, do not represent it as a batch parameter; use an individual Walksheds request configured through the UI instead.

## Example

A CSV contains the required coordinate columns for multiple parks and senior facilities.

## Assistant Guidance

Clarify that the input format for running batch walksheds is a CSV file with a defined ordered list of values. Distinguish settings exposed in the individual-request UI or URL from settings supported by the batch format.

## Related Concepts

- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
