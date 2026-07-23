---
title: "What are TDEI processing jobs?"
slug: tdei-job-processing
doc_type: concept
questions:
    - What are TDEI processing jobs?
    - What can a TDEI job do?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - automation
    - data-quality
    - formats
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
        - A successful TDEI job proves that the output is ready for public release.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are TDEI processing jobs?

## Short Answer

TDEI jobs are submitted operations that process datasets. Examples include validation, format conversion, quality metrics, union, and spatial join.

## Significance

Jobs provide repeatable processing through the portal and expose status, messages, and results. They separate data operations from manual editing.

## What This Means

Choose a job type, provide its required inputs, submit it, and review the result or errors. Different jobs have different parameters and permissions.

## What This Does Not Mean

A completed job does not automatically prove that the data is accurate, complete, or ready for release. Output review remains necessary.

## How To Use This

Record the job type, input dataset IDs, parameters, status, and result. Use the current job documentation for exact fields.

## Example

A user runs OSW Validate on an uploaded file, then reviews the validation messages before attempting another processing step.

## Assistant Guidance

Ask for the job type and current status before troubleshooting. Do not infer success from job creation alone.

## Related Concepts

- [How do I validate an OpenSidewalks dataset?](../workflow/validate-osw-dataset.md)
