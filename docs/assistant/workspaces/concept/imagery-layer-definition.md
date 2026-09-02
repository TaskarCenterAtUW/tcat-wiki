---
uid: 11cec0d3-3211-4e32-b0d4-08ce0b47a2cd
title: What is a workspace imagery-layer definition?
slug: imagery-layer-definition
doc_type: concept
questions:
    - What is a workspace imagery-layer definition?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - imagery
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - An imagery-layer definition uploads imagery into TDEI or OS-CONNECT.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is a workspace imagery-layer definition?

## Short Answer

An imagery-layer definition is configuration describing background tile sources for a workspace or app.

## Significance

It tells supported clients which imagery layers they may display.

## What This Means

The definition contains source URLs and layer settings rather than the imagery files themselves.

## What This Does Not Mean

Saving a definition does not upload or publish imagery.

## How To Use This

Use a supported schema and sources the project may redistribute.

## Example

A workspace definition points to a public raster tile service for field orientation.

## Assistant Guidance

Ask which client and schema version are involved.

## Related Concepts

- [How is custom imagery configured in a workspace?](custom-imagery-configuration.md)
