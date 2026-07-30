---
title: What should I do when Walksheds reveals a data issue?
slug: walkshed-data-issue-workflow
doc_type: concept
questions:
    - What should I do when Walksheds reveals a data issue?
audiences:
    - planner
    - jurisdiction
products:
    - Walksheds
    - OS-CONNECT
topics:
    - walksheds
    - os-connect
    - feedback
    - issue-reporting
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A Walksheds anomaly is necessarily a Walksheds calculation error.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What should I do when Walksheds reveals a data issue?

## Short Answer

Check the same location in OS-CONNECT or imagery, identify whether the problem is geometry or attributes, and report source-data errors through OS-CONNECT.

## Significance

A walkshed result may expose an upstream network problem rather than a model problem.

## What This Means

Use the OS-CONNECT viewer to verify and document the issue because Walksheds does not currently provide a direct source-data reporting workflow.

## What This Does Not Mean

An unexpected walkshed alone does not identify the responsible component.

## How To Use This

Record the location, dataset version, observed condition, and evidence.

## Example

A missing connector is confirmed in imagery and reported in the OS-CONNECT viewer.

## Assistant Guidance

Help separate model settings, source attributes, and source geometry.

## Related Concepts

- [How do I report a connectivity error in OS-CONNECT?](../../os-connect/workflow/report-connectivity-data-error.md)
