---
title: "What input limitations affect numeric quests?"
slug: numeric-quest-input
doc_type: concept
questions:
    - Can AVIV ScoutRoute numeric quests accept negative values?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - device-compatibility
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - Every mobile numeric keyboard supports negative values.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest.md
tags:
    - Assistant
---

<!-- @format -->

# What input limitations affect numeric quests?

## Short Answer

As of July 21, 2026, tested AVIV ScoutRoute iOS and Android keyboards did not provide a negative-sign key for numeric quests. This does not establish that the quest schema rejects negative values.

## Significance

Some measurements, such as slope, may require negative values. Keyboard limitations can prevent a valid value from being entered even when the data model permits it.

## What This Means

Treat numeric input as platform- and version-sensitive. Follow the unit named in the quest, verify the entered value, and check whether the app provides a negative key, alternate control, or another supported entry method.

## What This Does Not Mean

The test does not prove that negative values are unsupported by the quest schema. It only documents the tested mobile input behavior as of the current version.

## How To Use This

Record the device, operating system, app version, quest type, and available keyboard controls when testing. Report missing input controls separately from range-validation failures.

## Example

A slope quest requires a negative number, but the displayed decimal keypad has no minus sign. The user cannot enter the measurement without an alternate control or app change.

## Assistant Guidance

Do not infer schema support from keyboard behavior. Ask for platform and version details before giving troubleshooting guidance.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
