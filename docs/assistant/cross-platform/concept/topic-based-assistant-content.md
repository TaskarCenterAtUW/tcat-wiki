---
title: "What is topic-based Assistant Knowledge Base content?"
slug: topic-based-assistant-content
doc_type: concept
questions:
    - What is topic-based Assistant Knowledge Base content?
    - Why should Assistant Knowledge Base articles be concise?
audiences:
    - developer
products:
    - Cross-Platform
topics:
    - cross-platform
    - documentation
    - assistant-behavior
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-02
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A broad page is always a better retrieval source than an atomic answer.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is topic-based Assistant Knowledge Base content?

## Short Answer

Topic-based articles answer one focused question with concise evidence, boundaries, and assistant guidance.

## Significance

Atomic pages improve retrieval and reduce unrelated context in answers.

## What This Means

Each page should have a clear scope and avoid duplicating unrelated workflows.

## What This Does Not Mean

Concise content does not permit unsupported inference or omitted caveats.

## How To Use This

Split broad manuals into question-oriented concepts and workflows where useful.

## Example

A page about batch input should not also explain every interactive profile control.

## Assistant Guidance

Prefer the smallest supported article that answers the user's question.

## Related Concepts

- [What types of documentation guide TCAT users?](documentation-guide-types.md)
