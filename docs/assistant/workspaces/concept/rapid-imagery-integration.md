---
title: How does imagery configuration differ between AVIV ScoutRoute and Rapid?
slug: rapid-imagery-integration
doc_type: concept
questions:
    - How does imagery configuration differ between AVIV ScoutRoute and Rapid?
audiences:
    - developer
products:
    - Workspaces
    - AVIV ScoutRoute
    - Rapid
topics:
    - workspaces
    - aviv-scoutroute
    - rapid
    - imagery
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A workspace imagery definition is consumed identically by AVIV ScoutRoute and Rapid.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How does imagery configuration differ between AVIV ScoutRoute and Rapid?

## Short Answer

AVIV ScoutRoute and Rapid can use imagery sources differently. A workspace definition may need client-specific processing before a source works in each tool.

## Significance

A layer visible in one editor is not automatically available in another.

## What This Means

Check the target client's supported URL and layer format.

## What This Does Not Mean

Saving a workspace imagery definition guarantees that every editor displays it.

## How To Use This

Test the source in the intended app and document client limitations.

## Example

An imagery URL works in AVIV ScoutRoute but needs separate handling before being passed to Rapid.

## Assistant Guidance

Ask which application and workspace version are involved.

## Related Concepts

- [What is a workspace imagery-layer definition?](imagery-layer-definition.md)
