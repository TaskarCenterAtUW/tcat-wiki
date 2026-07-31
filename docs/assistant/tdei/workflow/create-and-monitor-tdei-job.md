---
title: How do I create and monitor a TDEI job?
slug: create-and-monitor-tdei-job
doc_type: workflow
questions:
    - How do I create and monitor a TDEI job?
products:
    - TDEI
audiences:
    - developer
    - jurisdiction
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
        - Creating a TDEI job means that processing has completed successfully.
related_pages:
    - ../concept/job-processing.md
    - ../../../tdei/portal/user-manual/jobs/index.md
tags:
    - Assistant
---

<!-- @format -->

# How do I create and monitor a TDEI job?

## Short Answer

Open **Jobs**, select **Create Job**, choose a job type, provide its required inputs, create the job, and monitor its job ID and status.

## Significance

Tracking the job separates request submission from processing completion and result review.

## What This Means

Use the job type's guide to prepare inputs. After creation, record the numeric job ID, inspect status such as Completed, Failed, In-Progress, or Abandoned, and download a result when available.

## What This Does Not Mean

A job ID is not a validation result, release, or guarantee that output is correct.

## How To Use This

Record input dataset IDs, files, formats, schema versions, job ID, status, and output. Review errors before using the result.

## Example

A producer creates an OSW conversion job, monitors it to completion, downloads the output, and validates the converted dataset.

## Assistant Guidance

Ask for job type and status before diagnosing an issue. Do not claim success from the creation screen alone.

## Related Concepts

- [How does TDEI job processing work?](../concept/job-processing.md)
- [What does the OSW Convert job do?](../concept/job-osw-convert.md)
