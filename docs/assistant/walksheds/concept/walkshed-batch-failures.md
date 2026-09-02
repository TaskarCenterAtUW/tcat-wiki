---
uid: b0df384a-bf0c-4518-897f-e69a1e87ee0f
title: How should Walksheds batch failures be interpreted?
slug: walkshed-batch-failures
doc_type: concept
questions:
    - How should Walksheds batch failures be interpreted?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - testing
    - data-quality
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A failed batch item always indicates a calculation defect.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should Walksheds batch failures be interpreted?

## Short Answer

A batch failure can indicate an invalid waypoint, unsupported input, or a processing problem.

## Significance

Failure labels and partial results need careful review.

## What This Means

Inspect the failed location, profile, message, and input record.

## What This Does Not Mean

A valid location for one profile necessarily succeeds for every profile.

## How To Use This

Keep the input and result identifiers when reporting a failure.

## Example

A park waypoint fails because it is too far from the mapped pedestrian network.

## Assistant Guidance

Ask for the exact failure message and affected profile.

## Related Concepts

- [How do I run batch walksheds?](../workflow/run-batch-walksheds.md)
