---
title: How are numeric quest values validated?
slug: numeric-quest-validation
doc_type: concept
questions:
    - How are numeric quest values validated?
    - Do minimum and maximum values block invalid quest answers?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - testing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: false
    abstain_if_missing_context: true
    do_not_claim:
        - A displayed range error always prevents quest form submission.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest.md
tags:
    - Assistant
---

<!-- @format -->

# How are numeric quest values validated?

## Short Answer

Numeric quests may define minimum and maximum values. As of July 21, 2026, tested app versions displayed out-of-range errors but could still submit the value; behavior may vary by platform and version.

## Significance

A visible validation message is not equivalent to blocked submission. This distinction matters when interpreting collected measurements.

## What This Means

The user manual explains how to enter and submit numeric values, but does not establish that every displayed range error blocks submission. Validation behavior may vary by platform and app version. Test both the displayed error and whether submission is actually prevented.

## What This Does Not Mean

The observed behavior does not establish that all versions or platforms permit invalid values. Confirm behavior in the deployed app before relying on it.

## How To Use This

Record the platform, app version, quest definition, entered value, displayed message, and submission result. Report reproducible discrepancies with screenshots or changeset details.

## Example

A quest allows widths from 0 to 100. Entering 501 may show an error message while still allowing submission on an affected app version.

## Assistant Guidance

Describe this as a reported, version-sensitive behavior unless current testing confirms it. Do not promise that a range will block submission.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
