---
title: Can AI automatically identify pedestrian barriers?
slug: ai-barrier-identification
doc_type: concept
questions:
    - Can AI automatically identify pedestrian barriers?
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

# Can AI automatically identify pedestrian barriers?

## Short Answer

AI can assist with identifying possible pedestrian barriers in imagery or other data, but a system's current capability, coverage, and accuracy must be verified. Potential detections should be treated as review candidates rather than authoritative findings.

## Significance

Automated screening can help focus limited review capacity on locations that warrant attention. It can also miss barriers, confuse objects, or reproduce gaps in its source data.

## What This Means

An AI workflow may flag a blocked path, missing connection, or unusual feature for human review. The workflow should preserve the source, model or processing context, confidence information when available, and review outcome.

## What This Does Not Mean

An AI flag does not prove that a barrier exists, and a lack of a flag does not prove that a path is clear. AI output does not establish accessibility, safety, ownership, or legal compliance.

## How To Use This

Confirm whether the capability is current or only a possible future use, inspect representative false positives and false negatives, validate important locations locally, and keep machine-generated candidates separate from accepted data.

## Example

An image model flags a possible obstruction near a sidewalk. A reviewer checks the image date and current site condition before recording an observation or submitting a correction.

## Assistant Guidance

Do not claim automatic barrier detection unless a current source documents it. Cite the source and version, identify human-review requirements, and abstain when the model, coverage, or validation evidence is unknown.

## Related Concepts

- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [Why can automated systems miss accessibility barriers?](automated-system-limitations.md)
- [How should human review be incorporated?](human-review.md)
