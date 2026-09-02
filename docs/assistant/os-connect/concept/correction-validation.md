---
uid: e41f2f83-5607-4005-b1a5-6c7946ca9b65
title: "How are agency-submitted corrections validated?"
slug: correction-validation
doc_type: concept
questions:
    - How are agency-submitted corrections validated?
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
    - data-quality
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
        - An agency-submitted correction is accepted without validation.
        - Validation proves that every related dataset is correct.
related_pages:
    - assistant/os-connect/concept/issue-report-follow-up.md
    - assistant/os-connect/concept/correction-tracking.md
    - assistant/os-connect/concept/qa-qc-report.md
tags:
    - Assistant
---

<!-- @format -->

# How are agency-submitted corrections validated?

## Short Answer

Agency-submitted corrections should be checked against the relevant dataset, location, evidence, and mapping or schema requirements before they are incorporated. The exact validation path depends on the submission and release workflow.

## Significance

Validation protects the quality and traceability of released pedestrian data. It helps distinguish a confirmed correction from an observation that still needs local or technical review.

## What This Means

- Confirm the affected feature, location, dataset version, and proposed change.
- Compare the submission with available source data and supporting evidence.
- Record the review outcome and carry accepted changes through the applicable release process.

## What This Does Not Mean

Validation is not a guarantee that the physical condition has been fully surveyed. A reviewed correction does not automatically update OpenStreetMap, TDEI, or downstream products.

## How To Use This

Provide precise locations, source information, and evidence. Separate known facts from assumptions, respond to clarification requests, and retain the dataset version used for comparison.

## Example

An agency submits a corrected curb-ramp location with a field record. Reviewers compare it with the current feature and source data, document the result, and identify the release in which an accepted change may appear.

## Assistant Guidance

Describe validation at a high level unless a current workflow is available. Do not promise acceptance or timing; cite the correction and release guidance and abstain when the dataset or evidence is missing.

## Related Concepts

- [Issue report follow-up](issue-report-follow-up.md)
- [Correction tracking](correction-tracking.md)
- [OS-CONNECT QA/QC report](qa-qc-report.md)
