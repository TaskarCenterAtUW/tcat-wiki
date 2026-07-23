---
title: "What input types are available in AVIV ScoutRoute quests?"
slug: quest-input-types
doc_type: concept
questions:
    - What input types are available in AVIV ScoutRoute quests?
    - How do I answer different AVIV ScoutRoute question types?
audiences:
    - advocate
    - public
    - planner
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - field-data-collection
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every quest uses the same input type or answer options.
        - A numeric answer is valid when entered in the wrong unit.
related_pages:
    - quest.md
    - ../workflow/answer-quest.md
    - ../../../aviv-scoutroute/user-manual/quest-types.md
tags:
    - Assistant
---

<!-- @format -->

# What input types are available in AVIV ScoutRoute quests?

## Short Answer

AVIV ScoutRoute quests can use exclusive choice, numeric entry, multiple choice, and free-form text inputs. The available type and options depend on the configured quest.

## Significance

Using the correct input method helps preserve accurate observations and measurements.

## What This Means

Exclusive choice selects one answer. Numeric entry records a measurement or count and requires attention to the requested unit. Multiple choice records all applicable options. Free-form text records a concise description; the user manual documents a maximum of 255 characters.

## What This Does Not Mean

Not every quest provides every input type, and an input control does not determine whether the observation itself is accurate.

## How To Use This

Read the complete question, check the requested unit, select all applicable options for multiple-choice questions, and keep text responses specific and concise.

## Example

A sidewalk quest may use numeric entry for width, multiple choice for obstructions, and free-form text when the available options do not describe an unusual condition.

## Assistant Guidance

Ask for the quest type and platform when troubleshooting. Do not infer validation or schema behavior solely from the appearance of an input control.

## Related Concepts

- [What is a quest?](quest.md)
- [What input limitations affect numeric quests?](numeric-quest-input.md)
