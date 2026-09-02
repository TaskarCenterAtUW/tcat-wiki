---
uid: efac73e0-4296-40a3-b923-4b3c5fe998d2
title: Can Walksheds be joined with census, crash data, or internal agency datasets?
slug: external-dataset-joins
doc_type: concept
questions:
    - Can Walksheds be joined with census, crash data, or internal agency datasets?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - gis
    - graph-metrics
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-31
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - External datasets can be joined correctly without checking their source, geography, time, and keys.
    related_pages:
        - assistant/walksheds/concept/os-connect-data-usage.md
tags:
    - Assistant
---

<!-- @format -->

# Can Walksheds be joined with census, crash, or internal agency datasets?

## Short Answer

Yes. Walksheds can be joined with census, crash data, or internal agency layers when the geometries, identifiers, coordinate systems, and analysis units are compatible.

## Significance

Joins add demographic, safety, or operational context to modeled reachability.

## What This Means

Align projections and boundaries, document the join key or spatial relationship, and preserve the Walksheds dataset and profile metadata.

## What This Does Not Mean

The join does not make either source current, authoritative, or causally explanatory.

## How To Use This

Validate a sample and disclose missing, mismatched, or generalized geometries.

## Example

A planner intersects walkshed polygons with census blocks and summarizes reachable population by stop.

## Assistant Guidance

Ask for the source layers and intended join before giving implementation-specific advice.

## Related Concepts

- [OS-CONNECT data usage](os-connect-data-usage.md)
