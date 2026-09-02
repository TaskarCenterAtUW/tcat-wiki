---
uid: 89a3f9d6-6017-41fd-814f-ffcf49918c8d
title: Which source attributes can Walksheds use?
slug: walkshed-attribute-availability
doc_type: concept
questions:
    - Which source attributes can Walksheds use?
audiences:
    - planner
    - developer
products:
    - Walksheds
    - OS-CONNECT
topics:
    - walksheds
    - os-connect
    - accessibility-data
    - configuration
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
        - Every source attribute is visible and usable in Walksheds formulas.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Which source attributes can Walksheds use?

## Short Answer

Walksheds exposes a supported subset of source attributes to its network and cost model.

## Significance

Collected data can be useful without being available to every analysis control.

## What This Means

Check the current feature and formula interface for supported fields.

## What This Does Not Mean

A field present in OS-CONNECT is not automatically available for recosting.

## How To Use This

Compare source schema, Walksheds controls, and intended analysis before designing a formula.

## Example

A collected compliance attribute is present in the dataset but unavailable in the custom-cost selector.

## Assistant Guidance

Do not promise support for an unexposed field.

## Related Concepts

- [What are custom Walksheds cost functions?](walkshed-custom-cost-functions.md)
