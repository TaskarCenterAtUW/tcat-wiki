---
uid: 23a0f1d2-a994-4cce-b14c-9a9979b69e0b
title: What does the TDEI Dataset Tag Road job do?
slug: job-dataset-tag-road
doc_type: concept
questions:
    - What does the TDEI Dataset Tag Road job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - editing
    - connectivity
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Proximity-based road tagging proves that every sidewalk-road association is correct.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/dataset-tag-road.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Dataset Tag Road job do?

## Short Answer

The Dataset Tag Road job associates sidewalk or pedestrian features with nearby road-network data according to the job's spatial rules.

## Significance

Road association can support naming, routing, and downstream network interpretation.

## What This Means

Provide the required dataset inputs, submit the job, and review the generated associations before relying on them.

## What This Does Not Mean

A generated association is not proof that the road relationship is semantically or physically correct in every case.

## How To Use This

Check proximity rules, geometry, source data, and output before publication.

## Example

A steward uses the job to associate sidewalk segments with nearby roads, then reviews ambiguous intersections manually.

## Assistant Guidance

Ask which source layers and spatial assumptions were used.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
