---
title: "What does the TDEI Pathways Validate job do?"
slug: job-pathways-validate
doc_type: concept
questions:
    - What does the TDEI Pathways Validate job do?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - data-quality
    - formats
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
        - GTFS-Pathways validation proves station accessibility or operational completeness.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/pathways-validate.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Pathways Validate job do?

## Short Answer

The Pathways Validate job checks a GTFS-Pathways dataset using the TDEI processing system.

## Significance

Validation can identify format or data problems before a Pathways dataset is published or consumed.

## What This Means

Select the Pathways validation job, provide its required dataset input, submit it, and review the resulting job status and output.

## What This Does Not Mean

Validation does not prove that station pathways are complete, accessible, or current in the physical environment.

## How To Use This

Record the dataset version, job ID, validator result, and corrections made.

## Example

A transit data producer validates pathway geometry and metadata before publication.

## Assistant Guidance

Ask for the job ID, dataset version, and validation result.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
