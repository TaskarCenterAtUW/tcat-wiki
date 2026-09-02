---
uid: 7bb47f06-a390-4389-8837-c4712bd76514
title: How do I open a TDEI dataset for inspection?
slug: open-dataset-for-inspection
doc_type: workflow
questions:
    - How do I open a TDEI dataset for inspection?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
    - Rapid
topics:
    - workspaces
    - rapid
    - tdei
    - editing
    - gis
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Opening a dataset for inspection commits an edit.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I open a TDEI dataset for inspection?

## Short Answer

Use the dataset action menu to open it in Workspaces, then inspect features in the map or Rapid editor as appropriate.

## Significance

This separates viewing and inspection from downloading or publishing.

## What This Means

Select the exact dataset, open it in Workspaces, and review its geometry and attributes.

## What This Does Not Mean

Opening a dataset does not commit an edit or publish a new version.

## How To Use This

Confirm the dataset ID, version, and project group before opening it. Use the map inspector for feature-level attributes.

## Example

A project opens a completed city dataset and inspects an `ext:` curb-ramp attribute in Rapid.

## Assistant Guidance

Ask whether the user wants inspection or editing. Preserve the source version when reporting an observation.

## Related Concepts

- [Where are TDEI datasets edited?](../concept/workspace-editing-boundary.md)
