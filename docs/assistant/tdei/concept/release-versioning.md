---
uid: 22bff919-f050-43c0-9437-934d1ead9b49
title: How are releases versioned?
slug: release-versioning
doc_type: concept
questions:
    - How are releases versioned?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - releases
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/tdei/concept/dataset-identifier.md
    - assistant/tdei/concept/released-dataset.md
    - assistant/tdei/workflow/check-dataset-currency.md
tags:
    - Assistant
---

<!-- @format -->

# How are releases versioned?

## Short Answer

TDEI release versioning distinguishes one published state of a dataset from another so users can identify the source used for download, analysis, citation, or comparison. The exact naming and version fields must be read from the current portal metadata.

## Significance

Version records support reproducibility, change tracking, currency checks, and communication about whether a correction or update is present.

## What This Means

Record the dataset identifier, release or version value, publication date, source, format, and any relevant processing or derivative relationship. Compare exact versions rather than relying on a dataset name alone.

## What This Does Not Mean

A newer release does not automatically mean every feature is corrected, and an older release is not necessarily invalid for historical analysis. Versioning does not certify accuracy or accessibility.

## How To Use This

Select the release that matches the decision, check its metadata and currency, retain the version in analysis records, and revisit conclusions when the source changes.

## Example

A planner compares two releases and identifies a newly added crossing while noting that other attributes and local conditions still require separate review.

## Assistant Guidance

Do not invent a numbering scheme or claim that versions imply semantic-version guarantees. Cite the exact portal record and abstain when release metadata are missing.

## Related Concepts

- [What is the dataset identifier?](dataset-identifier.md)
- [What is a released dataset in TDEI?](released-dataset.md)
- [How do I know whether a dataset is current?](../workflow/check-dataset-currency.md)
