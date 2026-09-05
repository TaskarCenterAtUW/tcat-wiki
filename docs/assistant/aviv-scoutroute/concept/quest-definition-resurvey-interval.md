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
last_reviewed: 2026-09-04
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

The resurvey interval controls quest visibility, not answer expiration. In Long Form Quest Definition schema version `3.2.0`, the interval is stored in the global `recency_period` field as a whole number of days. A quest is visible when an applicable question is unanswered or when the elapsed time since the element's `timestampEdited` reaches the configured interval.

## Significance

The global setting determines when previously submitted features can become available for another quest response. This matters when a project uses multiple contributors, teams, or groups to collect or verify information.

## What This Means

When a quest is submitted for a data element, AVIV ScoutRoute records the element's last-edited time. The `recency_period` value specifies how much elapsed time must pass before the quest can be shown for that element again. The check is based on elapsed time, not a calendar-date boundary: with `recency_period: 1`, a survey at 11:59 PM becomes eligible again after 24 hours: at 11:59 PM the following day.

Previously submitted answers are not cleared when the interval elapses. When the quest becomes visible again, those answers can be prefilled so a contributor can review and revalidate them. Submitting the confirmed answers creates a changeset and updates `timestampEdited`.

Quest visibility has two conditions: at least one applicable question remains unanswered, or `(now - element.timestampEdited) >= recency_period`. Questions hidden by answer dependencies do not count as unanswered.

The `recency_period` field is defined once for the entire Quest Definition. It is not configured separately for individual elements, quest questions, survey groups, teams, or devices. Schema version `3.2.0` requires at least `1` whole day and does not support fractional days or hour-based intervals.

Creating a workspace sets imported elements' `timestampEdited` values to the import time. The resurvey interval therefore uses the workspace import time even if the source data was edited earlier. The app does not use `ext:gig_complete` or `ext:gig_last_updated` to determine completion or recency.

## What This Does Not Mean

The resurvey interval is not a per-question or per-contributor timer. It does not delete, invalidate, or replace the existing answers, and it does not make a quest immediately available when the configured elapsed-time interval has not passed.

## How To Use This

Set `recency_period` in the global settings for the Quest Definition. Choose a whole number of days that matches the project's collection and verification workflow, and explain that the value controls visibility rather than retention of answers.

When troubleshooting availability, check the element's last survey time, the Quest Definition's `recency_period` value, and the current date. Also verify that the app has loaded the intended Quest Definition.

## Example

A Quest Definition uses `recency_period: 1`. A workspace is created from source data at 11:59 PM on September 1, so imported elements receive that import time as `timestampEdited`. A contributor submits a sidewalk quest, and the existing answers remain stored. The quest can be shown again after the one-day elapsed-time interval; the next contributor sees the prior answers, reviews them, and can submit a revalidation changeset.

## Assistant Guidance

When explaining quest availability, cite the active Quest Definition and state that `recency_period` is a global setting measured in whole-number days in schema version `3.2.0`. Explain that answers persist and that visibility is based on unanswered applicable questions or the element's `timestampEdited`. Do not describe it as a device-specific, user-specific, or question-specific timer, and do not imply that a recency interval deletes stored answers.

## Related Concepts

- [What is the AVIV ScoutRoute Quest Definition Creator?](quest-definition-creator.md)
- [Why can AVIV ScoutRoute quests be hidden or unavailable?](quest-visibility-and-local-state.md)
- [How do I update a quest definition in a workspace?](../workflow/update-quest-definition-in-workspace.md)
