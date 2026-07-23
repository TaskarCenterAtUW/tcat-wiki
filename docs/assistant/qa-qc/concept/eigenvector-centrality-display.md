---
title: "How are eigenvector centrality values displayed?"
slug: eigenvector-centrality-display
doc_type: concept
questions:
    - How are eigenvector centrality values displayed?
audiences:
    - planner
    - developer
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - graph-metrics
    - interpretation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-14
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Equal-color tile counts mean the underlying eigenvector values are equal.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How are eigenvector centrality values displayed?

## Short Answer

Reports may distribute eigenvector centrality values into more evenly populated display classes and show the underlying values in scientific notation.

## Significance

This can make small, clustered values easier to compare visually.

## What This Means

The color class is a display grouping, while the numeric value provides additional precision.

## What This Does Not Mean

A map class is not the raw metric value or a universal ranking.

## How To Use This

Read the legend and numeric notation together.

## Example

Several tiles share a color class even though their underlying values differ.

## Assistant Guidance

Explain display normalization before interpreting a map concentration.

## Related Concepts

- [How should eigenvector centrality be interpreted?](eigenvector-centrality-interpretation.md)
