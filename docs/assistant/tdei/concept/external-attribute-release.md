---
uid: 2fa3f991-fa78-4c2a-9ed1-0ffaf2d53496
title: How are external attributes handled at release?
slug: external-attribute-release
doc_type: concept
questions:
    - How are external attributes handled at release?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
    - OpenSidewalks
topics:
    - tdei
    - opensidewalks
    - public-vs-private-data
    - publication-workflow
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every external attribute in a source dataset must be released publicly.
related_pages:
    - assistant/opensidewalks/concept/external-attributes.md
    - assistant/tdei/concept/dataset-visibility.md
    - assistant/tdei/concept/release-versioning.md
    - assistant/workspaces/concept/edit-upload-to-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# How are external attributes handled at release?

## Short Answer

A release of a dataset on the TDEI may retain all `ext:` fields, remove them all, or manually filter selected fields before publishing.

## Significance

This lets a steward preserve a complete private source while sharing only appropriate attributes.

## What This Means

Review extension names, sensitivity, usefulness, and intended audience before release. When internal attributes must be retained for project work but excluded from a public release, keep a complete version in the private project dataset and prepare a filtered derivative:

1. Upload the complete workspace export to TDEI without releasing it, so it remains available to the relevant project group.
2. Download that project dataset and remove the attributes that should not appear in the public version, using an appropriate script or data-editing tool.
3. Review the filtered result, then upload it to TDEI as a new dataset version.
4. Verify the dataset identity, version, contents, and visibility before releasing the filtered version.

Keep the complete project dataset private if it contains attributes that are not intended for external distribution. Check current project-group permissions and release controls before sharing either dataset.

## What This Does Not Mean

The `ext:` prefix itself does not decide whether an attribute is public.

Uploading a complete dataset to the TDEI platform does not make it suitable for public release. Filtering selected attributes creates a separate derivative; it does not remove the internal attributes from the preserved private copy.

## How To Use This

Decide which attributes the intended audience may receive before release. Preserve the complete project version where needed, create a filtered derivative, inspect the derivative for excluded fields, and confirm its version and release state. Do not assume that an upload is public or that TDEI will automatically remove selected fields during export.

## Example

A project team keeps the complete survey dataset unreleased in its project group, removes internal-only attributes from a downloaded copy, uploads the cleaned copy as a later dataset version, and releases only that filtered version.

## Assistant Guidance

Ask which audience, project group, dataset version, and release state are involved before recommending filtering. Distinguish the retained private dataset from the filtered derivative. Do not claim a filtered dataset is safe to release until its contents and visibility have been reviewed.

## Related Concepts

- [How can the OpenSidewalks schema support external attributes?](../../opensidewalks/concept/external-attributes.md)
- [Who can see a TDEI dataset?](dataset-visibility.md)
- [How are releases versioned?](release-versioning.md)
- [How are edits uploaded back to TDEI?](../../workspaces/concept/edit-upload-to-tdei.md)
