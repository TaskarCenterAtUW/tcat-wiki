---
uid: 2a8ae450-c65f-460e-bdb4-619453e3cdff
title: "What happens after I submit an issue report?"
slug: issue-report-follow-up
doc_type: concept
questions:
    - What happens after I submit an issue report?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - feedback
    - issue-reporting
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Submitting a report guarantees that the released dataset will change.
        - A submitted report immediately updates every related dataset or product.
related_pages:
    - assistant/os-connect/workflow/report-data-error.md
    - assistant/os-connect/concept/issue-report-reviewers.md
    - assistant/os-connect/concept/correction-release-lag.md
tags:
    - Assistant
---

<!-- @format -->

# What happens after I submit an issue report?

## Short Answer

After an OS-CONNECT issue report is submitted, it can be reviewed and may be used to investigate a data or product problem. Submission alone does not immediately change the released dataset; a correction must follow the applicable review, update, and release process.

## Significance

Knowing what happens after submission helps reporters provide useful evidence and set realistic expectations. It also separates issue intake from validation and publication.

## What This Means

- The report should identify the location, observed problem, and supporting context when available.
- A reviewer may clarify the report, compare it with source data, or request verification.
- An accepted correction may appear in a later versioned release rather than immediately.

## What This Does Not Mean

- Submitting a report does not guarantee that the released dataset will change.
- A report is not by itself proof that a mapped feature is wrong on the ground.
- Related systems do not necessarily update together.

## How To Use This

Keep the report details and provide the dataset version and evidence if requested. Check a later release rather than assuming the current viewer has changed, and use the current feedback path for status questions.

## Example

An advocate reports a missing crossing connection with its location and an image. A reviewer examines the report and source data; if accepted, the correction is handled through the update and release process.

## Assistant Guidance

Explain review and release stages without promising acceptance or timing. Cite the correction workflow and ask for the product, location, dataset version, and report details before diagnosing status.

## Related Concepts

- [Report an OS-CONNECT data error](../workflow/report-data-error.md)
- [Who reviews submitted issue reports?](issue-report-reviewers.md)
- [Correction release lag](correction-release-lag.md)
