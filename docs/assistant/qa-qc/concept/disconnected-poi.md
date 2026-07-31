---
title: What does a disconnected point of interest mean?
slug: disconnected-poi
doc_type: concept
questions:
    - What does a disconnected point of interest mean in a QA/QC report?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - connectivity
    - destinations
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A disconnected POI is necessarily inaccessible in the real world.
related_pages:
    - assistant/qa-qc/concept/accessibility-island.md
    - assistant/qa-qc/concept/point-of-interest-sources.md
tags:
    - Assistant
---

<!-- @format -->

# What does a disconnected point of interest mean?

## Short Answer

A disconnected point of interest is a mapped destination that does not connect to the report's identified pedestrian-network islands.

## Significance

It highlights destinations that may be isolated in the mapped network.

## What This Means

The result depends on the network, POI inventory, and connectivity rules used in that report.

## What This Does Not Mean

It does not prove that people cannot reach the destination by any route.

## How To Use This

Check the POI source, network version, and map before investigating a result.

## Example

A mapped clinic outside the connected network may be listed as a disconnected POI.

## Assistant Guidance

Use "disconnected in the modeled network" unless field evidence supports a stronger claim.

## Related Concepts

- [What is an accessibility island?](accessibility-island.md)
