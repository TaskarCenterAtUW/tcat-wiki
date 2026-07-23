---
title: "How do I validate an OpenSidewalks dataset in TDEI?"
slug: validate-osw-dataset
doc_type: workflow
questions:
    - How do I validate an OpenSidewalks dataset in TDEI?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - data-quality
    - testing
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
        - Submitting an OSW Validate job publishes or fixes the dataset.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I validate an OpenSidewalks dataset in TDEI?

## Short Answer

Open the TDEI Jobs area, create an OSW Validate job, attach the dataset file, and review the result. The job checks the file against the OpenSidewalks schema.

## Significance

Validation can identify format or schema problems before later processing or release. It does not replace semantic or geographic review.

## What This Means

Select the current OSW Validate job type and provide its required file. Read the status and messages after processing completes.

## What This Does Not Mean

A validation result is not a guarantee that the data is complete, accurate, or suitable for every use. A failed job does not by itself identify the best correction.

## How To Use This

Keep the input file and job identifier with the result. Correct reported issues and rerun validation as needed.

## Example

A converted GeoJSON file is attached to OSW Validate before it is used in a union or opened in Workspaces.

## Assistant Guidance

Ask for the job status and exact validation message. Do not invent schema corrections without the current error and schema version.

## Related Concepts

- [What are TDEI processing jobs?](../concept/tdei-job-processing.md)
