---
title: "What does the TDEI Flex Validate job do?"
slug: job-flex-validate
doc_type: concept
questions:
    - What does the TDEI Flex Validate job do?
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
        - GTFS-Flex validation proves service quality or operational compliance.
related_pages:
    - job-processing.md
    - ../../../tdei/portal/user-manual/jobs/flex-validate.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI Flex Validate job do?

## Short Answer

The Flex Validate job checks a GTFS-Flex dataset using the TDEI processing system.

## Significance

Validation can identify format or data problems before a Flex dataset is published or consumed.

## What This Means

Select the Flex validation job, provide its required dataset input, submit it, and review the resulting job status and output.

## What This Does Not Mean

Validation does not prove that transit service is available, accessible, or operated as described in the data.

## How To Use This

Record the dataset version, job ID, validator result, and corrections made.

## Example

A producer validates a GTFS-Flex dataset before releasing it to consumers.

## Assistant Guidance

Ask for the job ID, dataset version, and validation result.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
