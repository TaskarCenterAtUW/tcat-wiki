---
uid: c987db37-06a8-4b20-8cf6-5b55d31ffcd0
title: What are the risks of relying solely on automated data?
slug: automated-data-risks
doc_type: concept
questions:
    - What are the risks of relying solely on automated data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - risk
    - data-quality
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/os-connect/concept/ai-data-risks.md
    - assistant/os-connect/concept/automated-system-limitations.md
    - assistant/os-connect/concept/human-review.md
tags:
    - Assistant
---

<!-- @format -->

# What are the risks of relying solely on automated data?

## Short Answer

Relying solely on automated data can hide errors, miss lived conditions, reproduce uneven source coverage, and create false confidence in a map or metric. Automated data should be combined with documented provenance, human review, and local evidence for consequential uses.

## Significance

Pedestrian accessibility is affected by conditions that may be difficult to infer from imagery, algorithms, or structured records. A missed barrier or incorrect connection can affect routing, planning, and public communication.

## What This Means

Automation may help organize large datasets or identify candidates for review. Its value depends on the source, method, coverage, date, confidence information, and the process used to check and correct results.

## What This Does Not Mean

Automated output is not automatically current, complete, authoritative, accessible, safe, or legally sufficient. A high score or apparently connected network does not replace field validation or community knowledge.

## How To Use This

Use automated data as an input, document its limitations, inspect representative errors, preserve provenance, and require a level of human review appropriate to the decision.

## Example

A model identifies a likely sidewalk connection, but a reviewer finds that the imagery predates construction. The record is marked uncertain and is not treated as a verified current condition.

## Assistant Guidance

Distinguish automated observations from verified features. Cite the source and processing context, avoid guarantees, and abstain from high-stakes conclusions when review evidence is missing.

## Related Concepts

- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [Why can automated systems miss accessibility barriers?](automated-system-limitations.md)
- [How should human review be incorporated?](human-review.md)
