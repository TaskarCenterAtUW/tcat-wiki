---
title: "How should Assistant Knowledge Base article stubs be reviewed?"
slug: review-assistant-article-stubs
doc_type: workflow
questions:
    - How should Assistant Knowledge Base article stubs be reviewed?
audiences:
    - developer
products:
    - Cross-Platform
topics:
    - cross-platform
    - documentation
    - assistant-behavior
    - review
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AI expansion is a substitute for human subject-matter review.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How should Assistant Knowledge Base article stubs be reviewed?

## Short Answer

Choose a stub, establish a grounded short answer, define boundaries, let AI expand only from that answer, and perform human review before saving.

## Significance

This reduces hallucination and keeps articles evidence-based.

## What This Means

Human knowledge comes first; domain-expert input helps resolve ambiguity, AI expands it second, and human review follows.

## What This Does Not Mean

AI output is not authoritative without review.

## How To Use This

Check facts, scope, metadata, links, and non-claims before committing.

## Example

A subject-matter expert answers a stub question in bullets, then reviews the generated nine-section article.

## Assistant Guidance

Abstain when the grounded answer is missing or disputed.

## Related Concepts

- [What is topic-based Assistant Knowledge Base content?](../concept/topic-based-assistant-content.md)
