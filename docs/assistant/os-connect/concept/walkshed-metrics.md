---
title: "What do walkshed metrics represent?"
slug: walkshed-metrics
doc_type: concept
questions:
    - What do walkshed metrics represent?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - walksheds
    - accessibility-metrics
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A smaller modeled walkshed proves that a person cannot travel in the jurisdiction.
        - A walkshed result measures physical accessibility independently of the dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What do walkshed metrics represent?

## Short Answer

OS-CONNECT QA/QC walkshed metrics estimate reachable pedestrian-network extent from selected points of interest for an unconstrained pedestrian and a manual-wheelchair profile.

## Significance

Reachability comparisons help identify possible barriers, missing curb ramps, steep segments, and disconnected or incomplete network data.

## What This Means

The analysis generates network-based walksheds around POIs such as schools, libraries, community centers, and transit stops. Reports can include reachable path length, counts of crossings and curbs, marked and lowered curbs, maps, and disconnected accessibility islands.

## What This Does Not Mean

The results depend on the selected POIs, profile assumptions, routing rules, dataset version, and mapped attributes. They do not represent every traveler or prove real-world access.

## How To Use This

Compare profiles and inspect the underlying map and data quality indicators. Use differences to prioritize investigation, not to make unqualified claims about residents.

## Example

A manual-wheelchair walkshed is smaller than an unconstrained walkshed near a transit stop; the difference may reflect steep slopes, missing ramps, or graph discontinuities that require review.

## Assistant Guidance

State the profile and POI context. Cite the report and explain the result as modeled reachability.

## Related Concepts

- [How should completeness scores be interpreted?](completeness-score-interpretation.md)
- [What is an OS-CONNECT QA/QC report?](qa-qc-report.md)
