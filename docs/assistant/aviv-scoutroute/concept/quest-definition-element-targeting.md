---
title: "How do quest definitions target element types?"
slug: quest-definition-element-targeting
doc_type: concept
questions:
    - How do quest definitions target element types?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - editing
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
        - A quest definition targets every feature without a matching element query.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do quest definitions target element types?

## Short Answer

A quest definition can target features by their element type and tags, then present questions for matching features.

## Significance

This connects a field form to the feature it is intended to describe.

## What This Means

Define the matching query and the questions for the selected element. The documented syntax supports tag presence or absence, exact and regular-expression values, numeric or date comparisons, and `and`/`or` expressions with parentheses.

## What This Does Not Mean

A quest does not appear on unrelated features automatically.

## How To Use This

Test the query against the workspace data and review the resulting change set.

## Example

Examples include `ways`, `ways with (footway=sidewalk)`, `ways with (footway=sidewalk and !surface)`, and `nodes with (barrier=kerb and !tactile_paving)`.

## Assistant Guidance

Verify tag names and schema support before deploying the definition.

## Related Concepts

- [How is a quest definition applied?](quest-definition-application.md)
