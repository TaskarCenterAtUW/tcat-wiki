---
title: How do multiple quest answer dependencies combine?
slug: quest-answer-dependency-logic
doc_type: concept
questions:
    - Can a quest dependency show a question in an "OR" fashion when a parent quest has one of several answers?
    - What happens when a quest has more than one dependency condition?
    - Does a quest_answer_dependency list use AND or OR logic between conditions?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
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
        - A quest_answer_dependency list evaluates any condition as an "or" against another condition in the same list.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest-dependency-evaluators.md
    - assistant/aviv-scoutroute/workflow/design-conditional-follow-up-quests.md
tags:
    - Assistant
---

<!-- @format -->

# How do multiple quest answer dependencies combine?

## Short Answer

A quest's `quest_answer_dependency` field can hold one dependency condition or an array of them. When it is an array, **every** condition must be satisfied ("AND" between conditions) for the quest to show. Within a single condition, `required_value` can list more than one accepted answer, and the quest shows if the dependent quest's answer matches **any one** of them ("OR" within that condition).

## Significance

Getting this combination logic wrong produces a quest definition that never shows a follow-up question, or shows it under the wrong conditions, without an obvious error at edit time.

## What This Means

A single dependency object such as `{ "question_id": 101, "required_value": ["value_a", "value_b"] }` matches when quest 101's answer is `value_a` or `value_b`. An array of dependency objects, one per referenced question, requires every object in the array to match at the same time. These two behaviors combine: a dependency list can express `(condition 1) AND (condition 2)`, where each condition can itself be `(value A OR value B)`.

## What This Does Not Mean

Multiple conditions in one `quest_answer_dependency` array are not evaluated as alternatives to each other. If any one condition in the array fails, the quest does not show, regardless of whether other conditions in the array are satisfied.

## How To Use This

List every accepted answer inside a single condition's `required_value` to get "OR" behavior for that dependent question. Add a separate condition object to the array, referencing a different `question_id`, to require an additional answer at the same time ("AND" behavior). Verify the resulting visibility against the intended survey logic before publishing the quest definition.

## Example

```json
"quest_answer_dependency": [
    { "question_id": 101, "required_value": ["value_a", "value_b"] },
    { "question_id": 102, "required_value": "value_x" }
]
```

This means: `Visible only if: (Q101 == "value_a" OR Q101 == "value_b") AND (Q102 == "value_x")`

- Q101 = `value_a`, Q102 = `value_x` -> visible
- Q101 = `value_b`, Q102 = `value_x` -> visible
- Q101 = `value_c`, Q102 = `value_x` -> hidden (fails Q101's OR condition)
- Q101 = anything, Q102 = anything other than `value_x` -> hidden (fails the AND between conditions)

## Assistant Guidance

Distinguish the two levels of combination clearly: OR only applies to multiple values within one condition's `required_value`; AND applies between separate conditions in a `quest_answer_dependency` array. Do not describe an array of conditions as offering an "either/or" choice between conditions. Point to the [Quests user manual](../../../aviv-scoutroute/quests/creator/user-manual/quests.md) for the Quest Definition Creator UI steps that produce this JSON.

## Related Concepts

- [Can quest dependencies use numeric comparisons?](quest-dependency-evaluators.md)
- [How do I design conditional follow-up quests?](../workflow/design-conditional-follow-up-quests.md)
