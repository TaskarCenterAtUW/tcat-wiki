---
uid: 8ff15f9e-ed6e-42a1-9a0d-63eb33bf1aa0
title: What risks exist in AI-generated accessibility data?
slug: ai-data-risks
doc_type: concept
questions:
    - What risks exist in AI-generated accessibility data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - ai
    - risk
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
    - assistant/os-connect/concept/ai-barrier-identification.md
    - assistant/os-connect/concept/automated-data-risks.md
    - assistant/os-connect/concept/human-review.md
tags:
    - Assistant
---

<!-- @format -->

# What risks exist in AI-generated accessibility data?

## Short Answer

AI-generated accessibility data can be incomplete, inaccurate, out of date, biased toward well-observed places, difficult to explain, or mistaken for verified fact. The risks depend on the source, model, task, population, and decision.

## Significance

Accessibility decisions can have serious consequences when a false positive hides a barrier or a false negative leads someone to expect access that is not available. Transparent review and provenance help limit those risks.

## What This Means

Risks include uneven imagery coverage, outdated observations, mislabeled training data, false positives and negatives, opaque confidence scores, privacy concerns, schema errors, and automation bias. Human review should be scaled to the consequence of the use.

## What This Does Not Mean

AI assistance does not make data authoritative, current, complete, or legally sufficient. A high confidence score is not the same as field verification or accessibility for every traveler.

## How To Use This

Document the source and processing version, test representative locations, inspect errors by setting and population, keep generated candidates distinct from accepted records, and establish correction and appeal paths.

## Example

An image model performs well on clear urban photographs but misses ramps obscured by vehicles and performs poorly in rural areas. The team reports those limitations and requires local review before operational use.

## Assistant Guidance

Name the model or workflow only when verified. Explain uncertainty, avoid high-stakes automated determinations, protect sensitive information, and abstain when validation or provenance is unavailable.

## Related Concepts

- [Can AI automatically identify pedestrian barriers?](ai-barrier-identification.md)
- [What are the risks of relying solely on automated data?](automated-data-risks.md)
- [How should human review be incorporated?](human-review.md)
