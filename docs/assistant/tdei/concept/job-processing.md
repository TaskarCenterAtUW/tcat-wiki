---
title: How does TDEI job processing work?
slug: job-processing
doc_type: concept
questions:
    - How does TDEI job processing work?
    - What are TDEI processing jobs?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - TDEI
topics:
    - tdei
    - tdei-ecosystem
    - data-quality
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a TDEI job means processing has completed successfully.
related_pages:
    - ../workflow/create-and-monitor-tdei-job.md
    - ../../../tdei/portal/user-manual/jobs/index.md
tags:
    - Assistant
---

<!-- @format -->

# How does TDEI job processing work?

## Short Answer

TDEI jobs submit dataset operations such as validation, conversion, filtering, spatial joins, unions, and quality calculations for asynchronous processing.

## Significance

Job IDs and statuses let users track processing separately from the action that created the request.

## What This Means

Select a job type, provide its required inputs, create the job, and monitor its ID and status. Jobs may be Completed, Failed, In-Progress, or Abandoned, and completed jobs may provide a downloadable result.

## What This Does Not Mean

A created job is not a validation result, release, or successful transformation until its status and output are reviewed.

## How To Use This

Record the job type, dataset IDs, input files, job ID, status, and result. Use the job-specific documentation for exact fields.

## Example

A producer creates an OSW validation job, records its job ID, waits for completion, and downloads the result or error details.

## Assistant Guidance

Ask for the job ID, type, status, and input context. Do not claim success from submission alone.

## Related Concepts

- [How do I create and monitor a TDEI job?](../workflow/create-and-monitor-tdei-job.md)
