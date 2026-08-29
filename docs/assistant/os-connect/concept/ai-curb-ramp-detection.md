---
title: Can AI automatically detect curb ramps?
slug: ai-curb-ramp-detection
doc_type: concept
questions:
    - Can AI automatically detect curb ramps?
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
    - curb-ramps
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
    - assistant/os-connect/concept/ai-data-risks.md
    - assistant/os-connect/concept/curb-ramp-identification.md
tags:
    - Assistant
---

<!-- @format -->

# Can AI automatically detect curb ramps?

## Short Answer

AI may assist with finding possible curb ramps in imagery or other sources, but detection is not automatically authoritative. Whether a current system provides this capability, and how well it performs, must be verified for the dataset and location.

## Significance

Automated screening may help identify candidate curb ramps for inventory or review. Curb-ramp presence, condition, orientation, detectable warnings, slope, and connection often require more information than an image or model can establish.

## What This Means

Treat detections as candidates. Record the source date, image or data context, model or processing information when available, confidence, and human-review outcome before accepting a feature into an inventory or released dataset.

## What This Does Not Mean

A detected curb ramp is not proof that it meets a design standard or is usable. A missing detection is not proof that no curb ramp exists, and AI output does not establish ADA compliance.

## How To Use This

Check the current documented capability, sample results in different environments, verify priority locations in the field or with authoritative local evidence, and preserve uncertainty and provenance.

## Example

An automated process flags a possible ramp at an intersection. A reviewer compares the image date with current conditions and checks the ramp's connections and attributes before recording a verified observation.

## Assistant Guidance

Do not state that AI automatically detects all curb ramps. Cite current technical documentation, name the review boundary, and abstain when the system, source, or validation method is not documented.

## Related Concepts

- [Can AI automatically identify pedestrian barriers?](ai-barrier-identification.md)
- [What risks exist in AI-generated accessibility data?](ai-data-risks.md)
- [How are curb ramps identified?](curb-ramp-identification.md)
