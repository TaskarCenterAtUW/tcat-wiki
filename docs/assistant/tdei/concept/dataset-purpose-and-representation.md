---
title: Why can one area have multiple TDEI datasets?
slug: dataset-purpose-and-representation
doc_type: concept
questions:
    - Why can one area have multiple TDEI datasets?
audiences:
    - planner
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - dataset-lineage
    - comparison
    - publication-workflow
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - One dataset must serve every routing, inventory, analysis, and maintenance use case.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Why can one area have multiple TDEI datasets?

## Short Answer

Different datasets can serve routing, inventory, analysis, or maintenance purposes. A source dataset can support separate derivatives optimized for those uses.

## Significance

One representation may create noise or lose useful detail when forced to serve every workflow.

## What This Means

Keep source and derivative purposes explicit and preserve their lineage.

## What This Does Not Mean

Multiple datasets do not necessarily indicate contradictory data or poor stewardship.

## How To Use This

Choose the dataset that matches the task and record its source and transformations.

## Example

Survey points remain separate for maintenance while a segmented derivative supports routing.

## Assistant Guidance

Ask the intended use before recommending a dataset.

## Related Concepts

- [What does a TDEI derived dataset ID show?](derived-dataset-lineage.md)
