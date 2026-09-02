---
uid: 4e468dc8-b2d6-48b9-be4b-1b6adbcdc8ab
title: What role did machine learning play?
slug: machine-learning-role
doc_type: concept
questions:
    - What role did machine learning play?
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
    - assistant/os-connect/concept/data-collection-history.md
    - assistant/os-connect/concept/ai-data-risks.md
    - assistant/os-connect/concept/human-review.md
tags:
    - Assistant
---

<!-- @format -->

# What role did machine learning play?

## Short Answer

Machine learning may support pedestrian-data collection or processing by identifying candidate features, classifying imagery, finding patterns, or prioritizing records for review. Its actual role must be established from the relevant dataset or release documentation.

## Significance

Machine learning can help process large areas, but it introduces model, source-data, coverage, and validation dependencies.

## What This Means

Check the training or source context, task, processing version, coverage, confidence, errors, and human-review process. Preserve whether a feature was predicted, inferred, observed, or confirmed.

## What This Does Not Mean

Machine learning does not automatically identify every feature, establish accessibility, or make output authoritative, current, unbiased, or legally sufficient.

## How To Use This

Use model output as a candidate or processing aid, test representative locations and failure modes, validate consequential results, and retain provenance.

## Example

A model identifies possible sidewalk geometry from imagery. Reviewers compare the result with source dates and local evidence before accepting or correcting it.

## Assistant Guidance

Do not claim a specific model or performance without evidence. Cite the collection history and validation guidance, and abstain when the processing role is not documented.

## Related Concepts

- [How was OS-CONNECT collected?](data-collection-history.md)
- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [How should human review be incorporated?](human-review.md)
