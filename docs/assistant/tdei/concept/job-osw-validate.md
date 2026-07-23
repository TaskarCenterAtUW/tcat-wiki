---
title: "What does the TDEI OSW Validate job do?"
slug: job-osw-validate
doc_type: concept
questions:
    - What does the TDEI OSW Validate job do?
products:
    - TDEI
    - OpenSidewalks
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - opensidewalks
    - data-quality
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - OSW validation proves accessibility or ADA compliance.
related_pages:
    - job-processing.md
    - ../workflow/validate-osw-dataset-in-tdei.md
    - ../../../tdei/portal/user-manual/jobs/osw-validate.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI OSW Validate job do?

## Short Answer

The OSW Validate job checks an attached OSW dataset against the applicable validation rules. The documented upload format is `.zip`.

## Significance

Validation identifies schema or data problems before downstream use or publication.

## What This Means

Create the job with the OSW `.zip` file, record the returned job ID, and monitor its status or result.

## What This Does Not Mean

A successful validation does not prove complete coverage, current conditions, physical accessibility, or legal compliance.

## How To Use This

Confirm the schema version and review validation output before using or releasing the dataset.

## Example

A producer submits an OSW archive, waits for completion, and corrects reported errors before a release.

## Assistant Guidance

Ask for the schema version, job ID, and result. Do not treat validation as certification.

## Related Concepts

- [How does TDEI job processing work?](job-processing.md)
