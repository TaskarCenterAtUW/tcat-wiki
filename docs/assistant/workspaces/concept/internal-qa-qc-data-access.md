---
title: "How is internal QA/QC supporting data accessed?"
slug: internal-qa-qc-data-access
doc_type: concept
questions:
    - How is internal QA/QC supporting data accessed?
audiences:
    - developer
products:
    - Workspaces
    - QA-QC Reports
topics:
    - workspaces
    - qa-qc
    - configuration
    - data-quality
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: low
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - QA/QC supporting data is available through an unauthenticated public download.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How is internal QA/QC supporting data accessed?

## Short Answer

Some report-supporting data is stored in internal Azure storage and may require an internal access key.

## Significance

This supporting data is distinct from public report pages and released datasets.

## What This Means

Use the approved internal process and protect credentials when accessing it.

## What This Does Not Mean

Do not assume that a report's supporting archive is a public download.

## How To Use This

Ask the responsible team for authorized access and current commands.

## Example

A report generator retrieves a dataset-specific archive for internal analysis.

## Assistant Guidance

Never request or disclose a blob key. Redirect unauthorized users to public report or dataset channels.

## Related Concepts

- [What is QA/QC report provenance?](../../qa-qc/concept/report-provenance.md)
