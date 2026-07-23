---
title: "How does AccessMap represent crossing accessibility?"
slug: combined-crossing-accessibility
doc_type: concept
questions:
    - Why can AccessMap mark an entire crossing as inaccessible?
    - How does AccessMap differ from OS-CONNECT for curb ramps?
audiences:
    - public
    - advocate
    - planner
products:
    - AccessMap
    - OS-CONNECT
topics:
    - accessmap
    - os-connect
    - crossings
    - accessibility-data
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
        - AccessMap identifies which individual curb ramp is inaccessible in its route display.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How does AccessMap represent crossing accessibility?

## Short Answer

AccessMap may represent a crossing as inaccessible when a required curb ramp is missing on either side. OS-CONNECT provides more detailed inspection of individual curb-ramp features.

## Significance

The combined display prioritizes a travel decision: whether the crossing can serve the selected traveler. It avoids adding detailed feature symbols that may complicate route planning.

## What This Means

Use AccessMap for route-level interpretation and OS-CONNECT for feature-level inspection. A crossing-level result may combine multiple curb-ramp conditions.

## What This Does Not Mean

An inaccessible crossing display does not identify which side caused the result. It is not a replacement for inspecting the underlying curb-ramp data.

## How To Use This

If a crossing appears wrong, inspect the corresponding curb ramps in OS-CONNECT and submit feature feedback where available. Consider the selected mobility profile.

## Example

One side of a crossing lacks a usable curb ramp, so AccessMap marks the whole crossing as inaccessible for a profile that avoids raised curbs.

## Assistant Guidance

Explain the product-level difference before interpreting a crossing. Do not infer the individual curb-ramp condition from the AccessMap color alone.

## Related Concepts

- [What are crossing links in pedestrian data?](crossing-links.md)
