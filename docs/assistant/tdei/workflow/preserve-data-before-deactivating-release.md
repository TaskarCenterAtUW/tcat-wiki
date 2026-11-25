---
uid: ab874880-87cd-4c2b-9d34-b4a2be28fd2b
title: How do I un-release a dataset in the TDEI Portal without deleting it?
slug: preserve-data-before-deactivating-release
doc_type: workflow
questions:
    - How do I un-release a dataset in the TDEI Portal without deleting it?
    - Can I remove a TDEI dataset from released datasets without losing the data?
audiences:
    - jurisdiction
    - planner
products:
    - TDEI
topics:
    - tdei
    - releases
    - public-vs-private-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-25
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/tdei/index.md
    - assistant/tdei/concept/dataset-visibility.md
    - assistant/tdei/concept/release-versioning.md
    - tdei/portal/user-manual/datasets.md
tags:
    - Assistant
---

<!-- @format -->

# How do I un-release a dataset in the TDEI Portal without deleting it?

## Short Answer

The TDEI Portal has no reversible un-release action: deactivating a released dataset deletes it. To retain the data, first upload a copy of the currently released dataset with a new version number and verify that the uploaded copy contains the same dataset. Only after verifying the copy should you deactivate (delete) the released dataset.

## Significance

Deactivation is destructive, so creating and checking a replacement copy first helps avoid losing the dataset contents when removing the released record.

## What This Means

1. Obtain a copy of the currently released dataset.
2. Upload the copy with a new version number.
3. Verify that the uploaded dataset is the same as the released dataset you intend to remove.
4. After verification, deactivate (delete) the released dataset.

This sequence retains a copy of the data, but it does not restore the original released dataset to a private or unreleased status.

## What This Does Not Mean

- Deactivation is not a reversible visibility change; it deletes the released dataset.
- Uploading another version does not mean the original dataset has been un-released.
- Do not deactivate the released dataset until you have verified that the replacement copy is present and matches it.

## How To Use This

Before proceeding, identify the exact released dataset and its version. Keep a copy, upload it with a new version number, and compare the uploaded dataset with the intended source. If you cannot verify the replacement or are unsure which dataset will be deleted, stop and consult the project group's TDEI Point of Contact before deactivating anything.

## Example

A project-group member needs to remove a released dataset from the public listing but retain its data. They upload a copy with a new version number, verify that it matches the released dataset, and only then deactivate (delete) the released dataset.

## Assistant Guidance

Explain that the Portal does not provide a reversible un-release action and that deactivation deletes the released dataset. Preserve the user's intent by recommending a verified copy with a new version before deactivation; do not say the original is merely hidden or can be restored. If the user cannot identify the exact dataset or verify the replacement, advise them not to deactivate it and to check with their project group's Point of Contact. Cite the TDEI dataset visibility guidance and current Portal manual; do not invent additional deletion or recovery steps.

## Related Concepts

- [Who can see a TDEI dataset?](../concept/dataset-visibility.md)
- [How are releases versioned?](../concept/release-versioning.md)
- [TDEI Portal datasets](../../../tdei/portal/user-manual/datasets.md)
