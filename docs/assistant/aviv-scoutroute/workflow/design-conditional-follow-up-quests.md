---
uid: 31b29431-397c-42c8-af6a-70dae0bbbff8
title: How do I design conditional follow-up quests?
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
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-27
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Conditional follow-up quests can be added without testing the consuming app.
        - A quest_answer_dependency array evaluates its conditions as alternatives to each other.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/conditional-team-questions.md
    - assistant/aviv-scoutroute/concept/quest-answer-dependency-logic.md
    - assistant/aviv-scoutroute/concept/quest-dependency-evaluators.md
tags:
    - Assistant
---

<!-- @format -->

# How do I design conditional follow-up quests?

## Short Answer

Add the opt-in or triggering quest first, add the follow-up quest to the same element, then set the follow-up quest's `quest_answer_dependency` so it shows only when the triggering quest's answer matches the required value or values. Test both the shown and hidden paths on the target app before publishing.

## Significance

Conditional follow-up quests keep survey forms short for most contributors while still collecting deeper detail from those who opt in or whose earlier answers make a follow-up relevant. Getting the dependency logic wrong either hides a needed question from every contributor or shows it to contributors it was never meant for, and neither failure is always obvious from the quest definition alone.

## What This Means

Designing a conditional follow-up quest is a sequence of decisions, not a single field:

1. **Choose the triggering quest(s).** A follow-up can depend on one quest or on several quests at once. Every quest referenced by a dependency must exist in the same element as the follow-up quest.
2. **Decide the accepted answer(s) for each triggering quest.** A dependency condition's `required_value` can be a single value, or an array of values when any one of several answers should trigger the follow-up (an "OR" within that condition). For example, `"required_value": ["example_1", "example_2", "example_3"]` triggers on any one of the three listed answers.
3. **Decide whether more than one triggering quest must all match.** When the follow-up should only show after multiple quests are each answered a certain way, add one dependency condition per triggering quest to the `quest_answer_dependency` array. Every condition in that array must be satisfied at the same time (an "AND" between conditions) for the follow-up to show.
4. **Build the dependency in the Quest Definition Creator.** Select **Single** for one condition or **Multiple (AND)** for more than one, choose the **Dependent Question**, and enter the **Required Value** or values using the dependent quest's stored **Value**, not its display label.
5. **Review the JSON Preview and Validation panel**, then test the flow in the consuming app: confirm the follow-up appears when the triggering answer(s) match, and stays hidden for every other answer.

## What This Does Not Mean

Adding a conditional follow-up quest does not by itself solve role or time-allocation problems, and it is not a substitute for clear question wording. A `quest_answer_dependency` array does not offer a choice between its conditions: if any one condition in the array fails, the follow-up stays hidden, regardless of whether the other conditions match. A conditional design is also not verified until it has been tested on the target app, because the Creator's JSON Preview does not exercise the app's own rendering and evaluation logic.

## How To Use This

- Keep the triggering quest's wording unambiguous, especially when it is an opt-in question ("Are you willing to answer additional questions about access pathways?").
- Use an array in `required_value` whenever more than one answer to the same triggering quest should reveal the follow-up, instead of duplicating the follow-up quest once per accepted answer.
- Use **Multiple (AND)** only when the follow-up genuinely requires every listed condition; a single condition with an array of values is the correct choice for "any one of these answers," not multiple conditions.
- Test both the opt-in/shown path and the opt-out/hidden path with representative users or test data before publishing the quest definition.
- After changing a quest ID, its answer values, or its position, review every dependency elsewhere in the definition that references it.

## Example

A form asks whether a contributor is willing to answer additional access-pathway questions (quest 101). A second quest (quest 102) records the general feature type, with values including `value_a` and `value_b`. A detail quest should show only when the contributor opted in **and** the feature is one of those two types:

```json
"quest_answer_dependency": [
    { "question_id": 101, "required_value": "yes" },
    { "question_id": 102, "required_value": ["value_a", "value_b"] }
]
```

This shows the detail quest only when quest 101 is `yes` **and** quest 102 is `value_a` **or** `value_b`. If quest 101 is `no`, the detail quest stays hidden regardless of quest 102's answer, because every condition in the array must pass.

## Assistant Guidance

Verify schema and app support before promising conditional behavior, and cite the [Quests user manual](../../../aviv-scoutroute/quests/creator/user-manual/quests.md) or [quest_answer_dependency logic](../concept/quest-answer-dependency-logic.md) page rather than asserting dependency behavior from memory. Do not describe a `quest_answer_dependency` array as offering alternative paths between its conditions — clarify that OR logic applies only to multiple values within one condition's `required_value`, while AND logic applies between separate conditions in the array. Ask for the current quest definition and target app version when troubleshooting an unexpected show/hide result.

## Related Concepts

- [How can quests ask about optional team contributions?](../concept/conditional-team-questions.md)
- [How do multiple quest answer dependencies combine?](../concept/quest-answer-dependency-logic.md)
- [Can quest dependencies use numeric comparisons?](../concept/quest-dependency-evaluators.md)
