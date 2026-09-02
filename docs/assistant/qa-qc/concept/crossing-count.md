---
uid: e1199eaf-c060-41f3-bed8-259828b12cd3
title: What does crossing count mean in QA/QC reports?
slug: crossing-count
doc_type: concept
questions:
    - What does crossing count mean in QA/QC reports?
    - What does crossing count mean?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - walksheds
    - crossings
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does "crossing count" mean in QA/QC reports?

## Short Answer

Crossing count is the number of deduplicated crossings reachable within merged POI-origin walksheds for a profile.

## Significance

It describes reachable crossing infrastructure rather than the complete crossing inventory.

## What This Means

Interpret the value with the profile, origins, budget, and dataset version.

## What This Does Not Mean

Overlapping walksheds do not multiply-count the same crossing, and the value is not the citywide crossing total.

## How To Use This

Compare crossing counts only when the walkshed inputs are comparable.

## Example

A crossing reachable from several nearby POIs contributes once after the walksheds are merged.

## Assistant Guidance

Distinguish reachable crossing count from total crossing count.

## Related Concepts

- [What does path count mean in QA/QC reports?](path-count.md)
