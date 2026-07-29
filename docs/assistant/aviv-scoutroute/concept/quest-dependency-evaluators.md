---
title: "Can quest dependencies use numeric comparisons?"
slug: quest-dependency-evaluators
doc_type: concept
questions:
    - Can an AVIV ScoutRoute quest dependency use greater-than or less-than logic?
    - Can numeric answers control follow-up quests?
audiences:
    - developer
    - planner
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - automation
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Quest dependencies currently support arbitrary numeric comparison operators.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest.md
tags:
    - Assistant
---

<!-- @format -->

# Can quest dependencies use numeric comparisons?

## Short Answer

Dependencies support exact values, not numeric operators such as "greater than." A provisional workaround is to ask a yes-or-no threshold question before showing a numeric follow-up.

## Significance

Threshold-based dependencies can reduce unnecessary field questions. Their availability affects how survey logic must be designed.

## What This Means

A quest can ask whether a measurement exceeds a threshold and condition later questions on that answer. Conditional follow-ups can also ask whether a contributor is willing to answer a topic-specific set rather than infer it from organizational team membership.

## What This Does Not Mean

The workaround is not equivalent to native numeric evaluators. Confirm the current schema and app implementation before editing JSON directly.

## How To Use This

Use a boolean threshold question only when its wording and follow-up ranges are clear.

## Example

Ask whether a sidewalk is wider than five feet. If the answer is yes, show one width question; if no, show a constrained question with a maximum of five feet.

## Assistant Guidance

Label numeric comparison support as a feature to be supported in the future unless verified in the current schema and apps. Do not claim that the Quest Definition Creator alone can enable an unsupported operator.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
