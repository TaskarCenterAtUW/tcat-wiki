---
title: "How does centrality sampling affect repeatability?"
slug: centrality-sampling-and-repeatability
doc_type: concept
questions:
    - How does centrality sampling affect repeatability?
    - What does the K value mean in centrality analysis?
audiences:
    - developer
    - planner
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - graph-metrics
    - testing
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-23
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Centrality results from different dataset IDs are automatically identical.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How does centrality sampling affect repeatability?

## Short Answer

A K value controls how many graph nodes are sampled for some centrality calculations. The current workflow uses repeatable sampling settings, but dataset changes or IDs can affect comparability.

## Significance

Sampling balances computation time and representativeness.

## What This Means

Record K, dataset ID, version, and sampling settings with a result.

## What This Does Not Mean

A result from a different dataset or sampling configuration is not automatically equivalent.

## How To Use This

Keep analysis parameters consistent when comparing versions.

## Example

A K value of 1,000 samples up to that many nodes and caps when the graph is smaller.

## Assistant Guidance

Verify implementation details before making claims about the seed or exact repeatability.

## Related Concepts

- [How do QA/QC centrality metrics differ?](centrality-metric-selection.md)
