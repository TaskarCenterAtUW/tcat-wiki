---
title: "What are current Walksheds editing limitations?"
slug: walkshed-edit-limitations
doc_type: concept
questions:
    - What are current Walksheds editing limitations?
audiences:
    - planner
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - editing
    - limitations
    - connectivity
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
        - Walksheds can create missing network geometry or report source-data issues directly.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are current Walksheds editing limitations?

## Short Answer

Walksheds can change attributes on existing features, but cannot currently create missing geometry, expose every source attribute, or directly report source-data issues. Edit deletion may also fail in some versions.

## Significance

A scenario may remain disconnected even after an attribute is changed.

## What This Means

Use the OS-CONNECT viewer or source workflow to report missing geometry.

## What This Does Not Mean

Walksheds is not a complete geometry editor or data-feedback system.

## How To Use This

Verify topology before modeling and record any source-data correction separately.

## Example

A missing sidewalk connector must be corrected in the source dataset before a Walksheds scenario can use it.

## Assistant Guidance

Explain the limitation and route the user to the appropriate source-data feedback process.

## Related Concepts

- [Why does network connectivity matter in Walksheds?](walkshed-data-connectivity.md)
