---
title: "Why does AKB content need domain-expert review?"
slug: knowledge-base-domain-review
doc_type: concept
questions:
    - Why does Assistant Knowledge Base content need domain-expert review?
audiences:
    - developer
products:
    - Cross-Platform
topics:
    - cross-platform
    - assistant-behavior
    - documentation
    - review
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-23
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - AI expansion can replace domain-expert review of ambiguous answers.
related_pages:
    - assistant/cross-platform/index.md
    - assistant/cross-platform/workflow/review-assistant-article-stubs.md
tags:
    - Assistant
---

<!-- @format -->

# Why does AKB content need domain-expert review?

## Short Answer

Domain experts provide the grounded answer and clarify edge cases before AI expands an AKB article.

## Significance

This reduces hallucination and prevents similar concepts from being conflated.

## What This Means

Use expert input for the short answer, boundaries, and related concepts, then review the expanded article.

## What This Does Not Mean

An AI-generated explanation is not authoritative by itself.

## How To Use This

Bring difficult or ambiguous stubs to the relevant expert and record the final interpretation.

## Example

A QA/QC specialist distinguishes node betweenness from eigenvector centrality before article expansion.

## Assistant Guidance

Abstain when expert evidence is missing or disputed.

## Related Concepts

- [How should Assistant Knowledge Base article stubs be reviewed?](../workflow/review-assistant-article-stubs.md)
