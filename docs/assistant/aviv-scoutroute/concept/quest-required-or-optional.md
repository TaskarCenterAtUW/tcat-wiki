---
title: Can quests in AVIV ScoutRoute be marked as required or optional?
slug: quest-required-or-optional
doc_type: concept
questions:
    - Can quests in AVIV ScoutRoute be marked as required or optional?
    - Can an AVIV ScoutRoute question be required?
    - How can a quest communicate that a question is optional or required?
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
    - limitations
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-14
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AVIV ScoutRoute currently enforces required or optional question status in the app.
        - Adding the words required or optional to a quest title enforces completion behavior.
related_pages:
    - quest.md
    - quest-definition-application.md
    - ../workflow/design-conditional-follow-up-quests.md
tags:
    - Assistant
---

<!-- @format -->

# Can quests in AVIV ScoutRoute be marked as required or optional?

## Short Answer

AVIV ScoutRoute and the long form quest definition schema currently do not provide a way to enforce required or optional questions. A quest title can communicate that a question is optional or required, but that wording is not enforced by the app or the schema.

## Significance

Confusing a label with enforcement can produce incomplete field data or lead contributors to believe that the app will prevent them from continuing.

## What This Means

Use clear wording such as `(Optional)` or `(Required)` in the question or quest title only as a communication aid.

## What This Does Not Mean

A label that says required does not force a contributor to answer the question, and a label that says optional does not configure a special validation rule.

## How To Use This

When designing a quest, decide which answers the project needs and label the question clearly if that helps contributors. For operationally necessary data, use project review and quality-control procedures rather than assuming the label provides validation.

## Example

A quest title includes `What is the surface material type of this sidewalk? (Required)` to tell contributors that the project expects an answer. The contributor can still continue if the current app version does not enforce required questions, so the project must identify missing answers during review.

## Assistant Guidance

Describe title labels as communicative only and describe native enforcement as planned but not yet implemented. Do not state that a contributor will be blocked from submitting an unanswered question.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
- [How is a quest definition applied?](quest-definition-application.md)
- [How do I design conditional follow-up quests?](../workflow/design-conditional-follow-up-quests.md)
