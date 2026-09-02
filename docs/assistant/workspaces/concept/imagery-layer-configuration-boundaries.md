---
uid: 7588e129-1e1a-41a7-8734-0ae9c6866a39
title: What are imagery-layer configuration boundaries?
slug: imagery-layer-configuration-boundaries
doc_type: concept
questions:
    - What are imagery-layer configuration boundaries?
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
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Saving an imagery definition uploads imagery or configures every client identically.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are imagery-layer configuration boundaries?

## Short Answer

Imagery configuration points supported clients to tile sources; it does not upload imagery and may require separate handling in AVIV ScoutRoute and Rapid.

## Significance

A saved definition can be valid while a particular client still cannot consume it.

## What This Means

Check the target app, source format, URL access, and licensing separately.

## What This Does Not Mean

Saving the definition makes neither the source nor the imagery public.

## How To Use This

Test each target client and use sources the project may redistribute.

## Example

A layer definition works in AVIV ScoutRoute but needs URL extraction before Rapid can use it.

## Assistant Guidance

Ask which client and definition schema are involved.

## Related Concepts

- [How does imagery configuration differ between AVIV ScoutRoute and Rapid?](rapid-imagery-integration.md)
