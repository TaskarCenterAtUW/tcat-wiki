---
uid: f3c427a3-f360-4bfe-a808-981bd74208f4
title: How do I create a workspace from a TDEI dataset?
slug: create-workspace-from-tdei-dataset
doc_type: workflow
questions:
    - How do I create a workspace from a TDEI dataset?
audiences:
    - jurisdiction
    - developer
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - onboarding
    - dataset-lineage
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a workspace changes the source TDEI dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I create a workspace from a TDEI dataset?

## Short Answer

Select the correct TDEI project group and released dataset, choose Open in Workspaces, verify the source version and target group, name the copy, and create it.

## Significance

This creates a sandbox for project-specific editing and collection.

## What This Means

The workspace begins as a copy of the selected dataset version.

## What This Does Not Mean

The source dataset is not modified by creating the copy.

## How To Use This

Confirm dataset name, scope, version, project group, and intended publication path.

## Example

A team opens the latest Olympia City dataset as a test workspace in its WSDOT project group.

## Assistant Guidance

Ask for the exact source dataset and target project group before giving steps.

## Related Concepts

- [How can a workspace diverge from its source dataset?](../concept/workspace-copy-and-divergence.md)
