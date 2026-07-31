---
title: How should QA/QC report maps support visual accessibility?
slug: qa-qc-visual-accessibility
doc_type: concept
questions:
    - How should QA/QC report maps support visual accessibility?
audiences:
    - developer
    - planner
products:
    - QA-QC Reports
topics:
    - qa-qc
    - accessibility-data
    - documentation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Distinct colors alone make a QA/QC map accessible.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should QA/QC report maps support visual accessibility?

## Short Answer

Report maps should distinguish layers through color, contrast, shape, line width, and a clear legend.

## Significance

Users may not distinguish similar hues or may view maps at different zoom levels.

## What This Means

Test the rendered map in context, including overlays and background layers.

## What This Does Not Mean

A color palette checker alone validates the complete map experience.

## How To Use This

Use redundant visual cues and maintain a readable legend.

## Example

A wheelchair layer uses a dark, high-contrast line while the full network uses a distinct width and tone.

## Assistant Guidance

Ask about contrast, color vision, zoom, and non-color cues.

## Related Concepts

- [How should QA/QC report maps be interpreted?](report-map-interpretation.md)
