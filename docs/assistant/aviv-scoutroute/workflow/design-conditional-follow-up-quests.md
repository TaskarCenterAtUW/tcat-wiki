---
title: "How do I design conditional follow-up quests?"
slug: design-conditional-follow-up-quests
doc_type: workflow
questions:
    - How do I design conditional follow-up quests?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - data-collection
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
        - Conditional follow-up quests can be added without testing the consuming app.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I design conditional follow-up quests?

## Short Answer

Ask an opt-in question, show the relevant follow-up set when selected, and test the flow on the target app.

## Significance

This keeps forms focused while allowing willing contributors to provide additional data.

## What This Means

Define clear conditions, labels, and question ownership before deployment.

## What This Does Not Mean

A conditional form automatically solves role or time-allocation problems.

## How To Use This

Test both the opt-in and opt-out paths with representative users.

## Example

A contributor selects access-pathway questions and receives only that additional set.

## Assistant Guidance

Verify schema and app support before promising conditional behavior.

## Related Concepts

- [How can quests ask about optional team contributions?](../concept/conditional-team-questions.md)
