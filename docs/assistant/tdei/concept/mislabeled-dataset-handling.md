---
title: What should I do if a dataset appears mislabeled or downloads the wrong file?
slug: mislabeled-dataset-handling
doc_type: concept
questions:
    - What should I do if a dataset appears mislabeled or downloads the wrong file?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - support
    - export
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
        - A mislabeled download is safe to use without checking its contents.
        - Reporting a mislabeled dataset immediately replaces the incorrect file.
related_pages:
    - assistant/tdei/workflow/check-dataset-currency.md
    - assistant/tdei/concept/released-dataset.md
    - assistant/tdei/workflow/download-data.md
tags:
    - Assistant
---

<!-- @format -->

# What should I do if a dataset appears mislabeled or downloads the wrong file?

## Short Answer

If a dataset appears mislabeled or the download is not the expected file, stop using it for analysis, preserve the file and metadata, compare its contents with the portal listing, and report the discrepancy through the current TDEI support path.

## Significance

Checking a questionable download prevents incorrect geography, format, or version information from entering an agency workflow.

## What This Means

- Record the dataset name, identifier, version, download date, and expected format.
- Inspect the archive contents and metadata without modifying the original.
- Compare the file with the portal listing and report the discrepancy with evidence.

## What This Does Not Mean

An unexpected file does not prove that the portal record is wrong; the download, listing, and local handling may each need checking. Do not infer that a report has already corrected the dataset.

## How To Use This

Keep the original file, screenshots or identifiers, and the exact steps that produced it. Do not publish results based on the questionable file until the source is verified.

## Example

An analyst expects an OSW release for one jurisdiction but receives a file with a different scope. The analyst preserves the download, checks its metadata, and reports the mismatch before analysis.

## Assistant Guidance

Ask for the dataset identifier, expected result, actual contents, and release context. Cite current TDEI guidance, do not invent a replacement download, and abstain from deciding which file is authoritative without verification.

## Related Concepts

- [Check dataset currency](../workflow/check-dataset-currency.md)
- [Released dataset](released-dataset.md)
- [Download TDEI data](../workflow/download-data.md)
