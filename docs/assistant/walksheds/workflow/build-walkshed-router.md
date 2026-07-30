---
title: How do I build a Walksheds router?
slug: build-walkshed-router
doc_type: workflow
questions:
    - How do I build a Walksheds router?
    - Why must I reload after building a Walksheds router?
audiences:
    - planner
    - developer
products:
    - Walksheds
    - TDEI
topics:
    - walksheds
    - tdei
    - connectivity
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
        - Changing the selected dataset changes the active router without rebuilding and reloading.
related_pages:
    - select-walkshed-dataset.md
    - ../concept/walkshed-application-architecture.md
    - ../../../walksheds/user-manual/datasets.md
tags:
    - Assistant
---

<!-- @format -->

# How do I build a Walksheds router?

## Short Answer

Select a primary TDEI dataset, optionally select an extension dataset, choose **Build Router**, and reload the page when the tool reports that the request is fulfilled.

## Significance

The router is the graph used by later walkshed calculations; a dataset selection is not active until the graph is built and loaded.

## What This Means

Open **Datasets**, select the intended version, optionally choose an overlay, and build the router. Rebuild whenever the primary or extension dataset changes.

## What This Does Not Mean

Refreshing the dataset list alone does not activate a newly built router.

## How To Use This

Record dataset IDs and versions, wait for the build, fully reload when prompted, and verify the active data before analysis.

## Example

A planner switches from version 1.3 to 1.4, builds the router, reloads the page, and regenerates the walkshed.

## Assistant Guidance

Ask which datasets were selected and whether the page was reloaded after the build.

## Related Concepts

- [How do I select a walkshed dataset?](select-walkshed-dataset.md)
- [What is a walkshed?](../concept/walkshed.md)
