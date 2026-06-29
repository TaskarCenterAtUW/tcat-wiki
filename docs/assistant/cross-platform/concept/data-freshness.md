---
title: Data freshness and versioning for assistants
tags:
    - Assistant
slug: data-freshness
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
audiences:
    - jurisdiction
    - planner
    - advocate
topics:
    - data-quality
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any map view is real-time without checking product documentation for latency.
related_pages:
    - assistant/cross-platform/concept/assistant-abstention.md
    - assistant/cross-platform/workflow/update-jurisdiction-data.md
---

<!-- @format -->

# Data freshness and versioning for assistants

## Short Answer

Assistants must communicate that pedestrian datasets and derived maps are versioned and can lag real-world construction. When users ask "is this current," answers should describe how to verify version or release notes rather than asserting freshness blindly.

## Significance

Stale answers erode trust and can affect safety decisions. Freshness discipline is part of responsible public deployment.

## What This Means

Cite dataset names, snapshot dates, or release identifiers when available. Encourage feedback channels when discrepancies appear.

## What This Does Not Mean

- Not a guarantee that every assistant integration can read live version metadata.
- Not an instruction to guess publication schedules.

## How To Use This

Require `requires_citation: true` pages to include pointers to manuals that explain update cadence where documented.

## Example

A user sees a new crosswalk on the ground missing from routing. The assistant explains typical staging from field edit to published graph without promising a date.

## Assistant Guidance

Prefer "check the in-app or portal indicator and release notes" patterns. Use abstention if the deployment cannot access version facts.

## Related Concepts

- [Update jurisdiction data](../workflow/update-jurisdiction-data.md)
