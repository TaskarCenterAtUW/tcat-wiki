---
title: Can quest dependencies use numeric comparisons?
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
last_reviewed: 2026-08-27
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
    - assistant/aviv-scoutroute/concept/quest-answer-dependency-logic.md
tags:
    - Assistant
---

<!-- @format -->

# Can quest dependencies use numeric comparisons?

## Short Answer

`quest_answer_dependency` conditions match exact values only, including exact matches against a list of accepted values. There is no numeric comparison operator such as "greater than" or "less than." A provisional workaround is to ask a yes-or-no threshold question before showing a numeric follow-up.

## Significance

Threshold-based dependencies can reduce unnecessary field questions. Their availability affects how survey logic must be designed.

## What This Means

A `required_value` condition matches when the dependent quest's answer equals the given value, or, when `required_value` is an array, when the answer equals any one of the listed values. Neither form evaluates a numeric range, a greater-than/less-than comparison, or any other operator against the dependent quest's answer. A quest can instead ask whether a measurement exceeds a threshold and condition later questions on that boolean answer. Conditional follow-ups can also ask whether a contributor is willing to answer a topic-specific set rather than infer it from organizational team membership.

## What This Does Not Mean

The workaround is not equivalent to native numeric evaluators, and listing several values in `required_value` is not a numeric range: it only matches the listed exact values, not values between or around them. Confirm the current schema and app implementation before editing JSON directly.

## How To Use This

Use a boolean threshold question only when its wording and follow-up ranges are clear. Do not attempt to approximate a numeric range by listing every individual value in `required_value`; use the boolean threshold workaround instead.

## Example

Ask whether a sidewalk is wider than five feet. If the answer is yes, show one width question; if no, show a constrained question with a maximum of five feet. This differs from combining accepted values in one `required_value`, such as `["value_a", "value_b"]`, which only matches those two exact answers and still is not a numeric comparison.

## Assistant Guidance

Do not claim that the Quest Definition Creator alone can enable an unsupported operator, and do not describe an array in `required_value` as providing range or threshold matching — it only provides exact-match OR logic across the listed values, as described in [How do multiple quest answer dependencies combine?](quest-answer-dependency-logic.md).

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
- [How do multiple quest answer dependencies combine?](quest-answer-dependency-logic.md)
