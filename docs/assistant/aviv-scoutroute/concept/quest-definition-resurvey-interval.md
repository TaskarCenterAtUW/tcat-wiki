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
last_reviewed: 2026-10-12
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

The resurvey interval controls quest visibility, not answer expiration. Long Form Quest Definition schema version `3.2.1` stores the interval in the global `recency_period` field as a whole number of days from `0` upward; Quest Definition Creator version `0.12.0` supports this schema. A quest is visible when an applicable question is unanswered or when the elapsed time since the element's `timestampEdited` reaches the configured interval. A value of `0` makes quests immediately eligible for resurvey, even when all applicable questions have answers.

## Significance

The global setting determines when previously submitted features can become available for another quest response. This matters when a project uses multiple contributors, teams, or groups to collect or verify information.

## What This Means

When a quest is submitted for a data element, AVIV ScoutRoute records the element's last-edited time. The `recency_period` value specifies how much elapsed time in days must pass before the quest can be shown for that element again. The check is based on elapsed time, not a calendar-date boundary: with `recency_period: 1`, a survey at 11:59 PM becomes eligible again after 24 hours: at 11:59 PM the following day. With `recency_period: 0`, the recency condition is satisfied immediately, so the quest can be resurveyed without a waiting period.

Previously submitted answers are not cleared when the interval elapses. When the quest becomes visible again, those answers can be prefilled so a contributor can review and revalidate them. Submitting the confirmed answers creates a changeset and updates `timestampEdited`.

Quest visibility has two conditions: at least one applicable question remains unanswered, or `(now - element.timestampEdited) >= recency_period`. Questions hidden by answer dependencies do not count as unanswered.

The `recency_period` field is defined once for the entire Quest Definition. It is not configured separately for individual elements, quest questions, survey groups, teams, or devices. Schema version `3.2.1` accepts `0` or greater and does not support fractional days or hour-based intervals; schema version `3.2.0` required at least `1` whole day.

Creating a workspace sets imported elements' `timestampEdited` values to the import time. The resurvey interval therefore uses the workspace import time even if the source data was edited earlier. The app does not use `ext:gig_complete` or `ext:gig_last_updated` to determine completion or recency.

## What This Does Not Mean

The resurvey interval is not a per-question or per-contributor timer. It does not delete, invalidate, or replace existing answers. A zero-day interval removes the recency wait but does not override workspace configuration, enabled quest types, map visibility, or other app visibility controls.

## How To Use This

Set `recency_period` in the global settings for the Quest Definition. Choose a whole number of days from `0` upward that matches the project's collection and verification workflow. Use `0` only when quests should be eligible for resurvey without a waiting period, and explain that the value controls visibility rather than retention of answers.

When troubleshooting availability, check the element's last survey time, the Quest Definition's `recency_period` value, and the current date. Also verify that the app has loaded the intended Quest Definition.

## Example

A Quest Definition uses `recency_period: 1`. A workspace is created from source data at 11:59 PM on September 1, so imported elements receive that import time as `timestampEdited`. A contributor submits a sidewalk quest, and the existing answers remain stored. The quest can be shown again after the one-day elapsed-time interval; the next contributor sees the prior answers, reviews them, and can submit a revalidation changeset.

With `recency_period: 0`, a completed quest is immediately eligible for resurvey, and its existing answers remain available for review.

## Assistant Guidance

When explaining quest availability, cite the active Quest Definition and state that `recency_period` is a global whole-number-of-days setting. Schema version `3.2.1` permits `0`; Creator version `0.12.0` supports that schema. Explain that `0` makes completed quests eligible for immediate resurvey without deleting prior answers, while other app and workspace visibility conditions still apply. Do not describe the interval as device-specific, user-specific, or question-specific.

## Related Concepts

- [What is the AVIV ScoutRoute Quest Definition Creator?](quest-definition-creator.md)
- [Why can AVIV ScoutRoute quests be hidden or unavailable?](quest-visibility-and-local-state.md)
- [How do I update a quest definition in a workspace?](../workflow/update-quest-definition-in-workspace.md)
