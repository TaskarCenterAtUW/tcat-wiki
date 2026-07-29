---
title: "Which help-desk questions belong in the Assistant Knowledge Base?"
slug: help-desk-questions-as-knowledge-sources
doc_type: concept
questions:
    - Which help-desk questions belong in the Assistant Knowledge Base?
audiences:
    - developer
    - planner
products:
    - Cross-Platform
topics:
    - cross-platform
    - support
    - documentation
    - issue-reporting
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
        - Every help-desk ticket is suitable for public Assistant Knowledge Base content.
related_pages:
    - assistant/cross-platform/index.md
    - assistant/cross-platform/workflow/review-assistant-article-stubs.md
tags:
    - Assistant
---

<!-- @format -->

# Which help-desk questions belong in the Assistant Knowledge Base?

## Short Answer

Resolved user questions about reusable product behavior can become AKB candidates; vendor infrastructure and private operational matters generally should not.

## Significance

Help-desk traffic can reveal real information needs that planned documentation missed.

## What This Means

Triage questions for reusable scope, privacy, authority, and user relevance.

## What This Does Not Mean

A ticket is not automatically a publishable article.

## How To Use This

Remove private details and verify the answer before authoring.

## Example

A repeated question about finding a workspace becomes a workflow article, while an Azure incident remains internal.

## Assistant Guidance

Abstain or route to support for private, vendor-specific, or unresolved issues.

## Related Concepts

- [How should Assistant Knowledge Base article stubs be reviewed?](../workflow/review-assistant-article-stubs.md)
