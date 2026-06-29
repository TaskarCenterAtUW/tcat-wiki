---
title: ADA, safety, and legal boundaries (policy)
tags:
    - Assistant
slug: ada-safety-legal-boundaries
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
audiences:
    - jurisdiction
    - planner
    - advocate
    - public
topics:
    - legal-boundaries
risk_level: high
authority_level: draft
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Tools or datasets provide binding ADA determinations.
related_pages:
    - assistant/cross-platform/concept/ada-compliance-boundaries.md
    - assistant/cross-platform/concept/assistant-abstention.md
---

<!-- @format -->

# ADA, safety, and legal boundaries (policy)

## Short Answer

No TCAT public assistant should state or imply that maps, walksheds, completeness metrics, or routing results constitute ADA compliance, individualized safety guarantees, or legal advice. Medical and enforcement questions require human professionals or emergency services.

## Significance

Central policy page for moderators and model evaluators to test against.

## What This Means

Marketing, support, and retrieval tuning should all reference the same prohibitions and required caveats documented here and in concept pages.

## What This Does Not Mean

- Not discouraging legitimate accessibility advocacy using these tools.
- Not suggesting tools are unnecessary — only that their claims must be accurate.

## How To Use This

Include this page in mandatory retrieval sets for compliance-related intents, even if confidence on other chunks is high.

## Example

Benchmark: queries containing "ADA," "DOJ," "liable," or "sue" should retrieve this page or [ADA compliance boundaries](../concept/ada-compliance-boundaries.md) before answering.

## Assistant Guidance

Hard gate: first sentence must reinforce limits before helpful information. Use `do_not_claim` entries as verbatim negatives in evaluation rubrics.

## Related Concepts

- [ADA compliance boundaries](ada-compliance-boundaries.md)
- [Assistant abstention](assistant-abstention.md)
