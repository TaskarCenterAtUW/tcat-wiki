---
title: "How do I select a Walksheds dataset?"
slug: select-walkshed-dataset
doc_type: workflow
questions:
    - How do I select a dataset in Walksheds?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
    - TDEI
topics:
    - walksheds
    - tdei
    - configuration
    - data-freshness
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Typing a dataset name selects it automatically in Walksheds.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I select a Walksheds dataset?

## Short Answer

Open dataset settings, filter or search for the desired dataset, select the result, and build the router.

## Significance

A router must use the intended geography and dataset version.

## What This Means

Typing filters the list; clicking the result selects it before building the router.

## What This Does Not Mean

A typed name without an active selection does not necessarily change the dataset.

## How To Use This

Confirm the selected dataset and wait for the router request to finish.

## Example

A planner searches for a city dataset, selects the highlighted result, and builds its router.

## Assistant Guidance

Ask for the exact dataset name, version, and region.

## Related Concepts

- [How should I choose a TDEI dataset version?](../../tdei/concept/dataset-version-selection.md)
