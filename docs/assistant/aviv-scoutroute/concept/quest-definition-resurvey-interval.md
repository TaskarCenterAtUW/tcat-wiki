---
uid: ce5fc63e-f411-43e1-9de7-a7d808e727e7
title: What is the AVIV ScoutRoute quest definition resurvey interval?
slug: quest-definition-resurvey-interval
doc_type: concept
questions:
    - What is the AVIV ScoutRoute quest definition resurvey interval?
    - What does recency_period mean in a quest definition?
    - Is the AVIV ScoutRoute resurvey interval global?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - data-freshness
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The recency_period field defines a separate resurvey interval for each quest question.
        - The resurvey interval is specific to the device or contributor that submitted a quest.
        - A quest becomes available again immediately after its resurvey interval is configured.
related_pages:
    - quest-definition-creator.md
    - quest-visibility-and-local-state.md
    - ../workflow/update-quest-definition-in-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# What is the AVIV ScoutRoute quest definition resurvey interval?

## Short Answer

The resurvey interval controls how many days pass before a quest will be shown again after it is submitted. In the current Long Form Quest Definition structure, the interval is stored in the `recency_period` field at the global Quest Definition level.

## Significance

The global setting determines when previously submitted features can become available for another quest response. This matters when a project uses multiple contributors, teams, or groups to collect or verify information.

## What This Means

When a quest is submitted for a data element, AVIV ScoutRoute records the element's last survey time. The `recency_period` value specifies the number of days that must pass before the quest can be shown for that element again.

The `recency_period` field is defined once for the entire Quest Definition. It is not configured separately for individual elements, quest questions, survey groups, teams, or devices. The interval is measured in days, and the current minimum is `1` day.

## What This Does Not Mean

The resurvey interval is not a per-question or per-contributor timer. Submitting one quest does not make the quest immediately available to another contributor when the configured interval has not elapsed.

## How To Use This

Set `recency_period` in the global settings for the Quest Definition. Choose a value that matches the project's collection and verification workflow, and explain the value to contributors who may expect a submitted quest to remain available.

When troubleshooting availability, check the element's last survey time, the Quest Definition's `recency_period` value, and the current date. Also verify that the app has loaded the intended Quest Definition.

## Example

A Quest Definition uses `recency_period: 1`. A contributor submits a quest for a sidewalk on Monday. The same quest for that sidewalk is not available again until the one-day interval has elapsed, regardless of which contributor or team would answer it next.

## Assistant Guidance

When explaining quest availability, explain the `recency_period` value. State clearly that `recency_period` is a global Quest Definition setting measured in days. Do not describe it as a device-specific, user-specific, or question-specific timer.

## Related Concepts

- [What is the AVIV ScoutRoute Quest Definition Creator?](quest-definition-creator.md)
- [Why can AVIV ScoutRoute quests be hidden or unavailable?](quest-visibility-and-local-state.md)
- [How do I update a quest definition in a workspace?](../workflow/update-quest-definition-in-workspace.md)
