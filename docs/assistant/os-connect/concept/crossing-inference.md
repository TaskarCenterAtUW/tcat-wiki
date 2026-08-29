---
title: How are crossings inferred?
slug: crossing-inference
doc_type: concept
questions:
    - How are crossings inferred?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - crossings
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
    - assistant/os-connect/concept/crossing-edge.md
    - assistant/os-connect/concept/complex-intersection-handling.md
    - assistant/os-connect/concept/confidence-measures.md
tags:
    - Assistant
---

<!-- @format -->

# How are crossings inferred?

## Short Answer

Crossings may be inferred from pedestrian geometry, roadway relationships, imagery, source inventories, or processing rules. The exact method is release-specific, and an inferred crossing should be distinguished from a directly observed or agency-confirmed feature.

## Significance

Inference can help construct a connected pedestrian graph where source data do not explicitly encode every relationship. It also introduces uncertainty that should be visible during review.

## What This Means

Check the inference method, source dates, geometry, confidence information, and validation status. Inspect complex intersections and important routes locally, and preserve whether a feature was inferred or confirmed.

## What This Does Not Mean

An inferred connection between two sidewalk approaches can identify a candidate crossing for network analysis. It does not prove that the crossing is marked, accessible, safe, or currently present.

## How To Use This

Inference is not field observation, legal certification, or a guarantee that the network is complete. Absence of an inferred crossing does not prove that no crossing exists.

## Example

Use inferred features for screening with appropriate caveats, compare them against imagery or local records, and report specific omissions or false connections through the current channel.

## Assistant Guidance

Name the source and method, distinguish inferred from observed information, and abstain from definitive claims when the processing or validation evidence is unknown.

## Related Concepts

- [What is a crossing edge?](crossing-edge.md)
- [How are complex intersections handled?](complex-intersection-handling.md)
- [What confidence measures exist?](confidence-measures.md)
