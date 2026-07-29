---
title: "How can quests ask about optional team contributions?"
slug: conditional-team-questions
doc_type: concept
questions:
    - How can a quest ask whether someone will answer another team's questions?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - teams
    - data-collection
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-05-26
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A contributor's organizational team determines every question they can answer.
related_pages:
    - assistant/aviv-scoutroute/index.md
    - assistant/aviv-scoutroute/concept/quest-dependency-evaluators.md
tags:
    - Assistant
---

<!-- @format -->

# How can quests ask about optional team contributions?

## Short Answer

A form can ask whether a contributor is willing to answer an additional topic-specific question set, then show those questions conditionally.

## Significance

This supports cross-team contributions without assuming that people have unlimited time.

## What This Means

Condition follow-up questions on the contributor's stated willingness or selection.

## What This Does Not Mean

The flow does not require the contributor's organizational team to determine the form.

## How To Use This

Keep the opt-in question clear and label the purpose of each follow-up set.

## Example

A contributor can opt into speed-and-reliability questions even when they belong to another project team.

## Assistant Guidance

Ask for the intended conditional flow and current quest schema support.

## Related Concepts

- [Can quest dependencies use numeric comparisons?](quest-dependency-evaluators.md)
