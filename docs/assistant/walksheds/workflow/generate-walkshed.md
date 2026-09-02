---
uid: 84f2c082-c041-4203-a960-24c971f45630
title: How do I generate a walkshed?
slug: generate-walkshed
doc_type: workflow
questions:
    - How do I generate a walkshed?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - routing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-02
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Generating a walkshed proves that the result is physically accessible or legally compliant.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I generate a walkshed analysis?

## Short Answer

Sign in to Walksheds, select an OpenSidewalks dataset, build the router, configure a profile or preferences, set an origin, and choose a maximum travel cost.

## Significance

The result models which network edges are reachable under stated assumptions.

## What This Means

Open the Datasets tab, select a TDEI dataset, choose **Build Router**, reload when requested, configure the Walkshed Preferences tab, click the map or search an address, and set the cost budget. Reachable paths are highlighted in blue.

## What This Does Not Mean

A result depends on the dataset, router, origin, budget, profile, preferences, and time-dependent access.

## How To Use This

Record the dataset version and settings, then inspect gaps and statistics rather than treating the blue area as a guarantee.

A user builds a router from a city dataset, selects Manual wheelchair, sets a ten-minute budget, and reviews reachable paths.

## Example

A user builds a router from a city dataset, selects Manual wheelchair, sets a ten-minute budget, and reviews reachable paths.

## Assistant Guidance

Ask which dataset, version, profile, cost, origin, and departure time are involved.

## Related Concepts

- [How do I select and build a walkshed dataset?](select-walkshed-dataset.md)
- [What is a walkshed?](../concept/walkshed.md)
