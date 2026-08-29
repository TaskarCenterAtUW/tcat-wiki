---
title: Why can automated systems miss accessibility barriers?
slug: automated-system-limitations
doc_type: concept
questions:
    - Why can automated systems miss accessibility barriers?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - automation
    - limitations
risk_level: medium
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
    - assistant/os-connect/concept/automated-data-risks.md
    - assistant/os-connect/concept/ai-data-risks.md
    - assistant/os-connect/concept/human-review.md
tags:
    - Assistant
---

<!-- @format -->

# Why can automated systems miss accessibility barriers?

## Short Answer

Automated systems can miss accessibility barriers because source imagery or records may be outdated, conditions may be obscured or ambiguous, and the model may not represent the relevant feature or lived experience. Performance can vary by place, environment, and data quality.

## Significance

Missed barriers can create a misleading impression of access and can direct review resources away from locations that need attention. Understanding failure modes is part of responsible data use.

## What This Means

Common limitations include occlusion, resolution, seasonal conditions, unusual designs, incomplete labels, disconnected geometry, changing construction, and differences between a visible feature and a usable feature.

## What This Does Not Mean

A system's failure to flag a condition does not prove that the condition is absent. Automated limitations do not mean that all automated data are useless; they mean that use must match evidence and risk.

## How To Use This

Check source dates and coverage, sample likely false positives and false negatives, compare results with local or field evidence, and keep uncertain candidates separate from verified records.

## Example

An algorithm misses a temporary obstruction because it is hidden by a vehicle. A community report brings the location to review even though the automated layer shows no barrier.

## Assistant Guidance

Explain the known source and model limitations, do not generalize performance from one area, and abstain when validation evidence or the processing context is unavailable.

## Related Concepts

- [What are the risks of relying solely on automated data?](automated-data-risks.md)
- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [How should human review be incorporated?](human-review.md)
