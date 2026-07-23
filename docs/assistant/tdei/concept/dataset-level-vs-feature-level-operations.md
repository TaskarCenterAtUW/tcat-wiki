---
title: "What is the difference between dataset-level and feature-level operations?"
slug: dataset-level-vs-feature-level-operations
doc_type: concept
questions:
    - What is the difference between dataset-level and feature-level operations?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - Workspaces
topics:
    - tdei
    - workspaces
    - editing
    - automation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-12
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A TDEI whole-dataset operation edits individual features interactively.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between dataset-level and feature-level operations?

## Short Answer

TDEI jobs operate across whole datasets, while Workspaces and editors support inspecting and editing individual features.

## Significance

The distinction helps users select a portal job or editing workspace.

## What This Means

Use TDEI for operations such as adding inferred inclines to a dataset and Workspaces for element-wise changes.

## What This Does Not Mean

A dataset-level result removes the need for feature review when the workflow requires it.

## How To Use This

Define the operation's scope before choosing a tool.

## Example

A TDEI job calculates elevation-derived values across all lines; Rapid adjusts one sidewalk geometry.

## Assistant Guidance

Ask whether the requested change applies to all data or selected features.

## Related Concepts

- [What is the boundary between Workspaces and TDEI?](../../workspaces/concept/workspace-and-tdei-boundary.md)
