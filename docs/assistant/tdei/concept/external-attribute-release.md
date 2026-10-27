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
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every external attribute in a source dataset must be released publicly.
        - The OpenSidewalks `ext:` prefix is a TDEI privacy or release control.
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

OpenSidewalks uses the `ext:` prefix for partner-specific fields outside its core schema. The prefix does not make a field private or determine whether TDEI retains it during processing or includes it in a public release. The checked Portal upload and dataset guides do not document a general retention or filtering rule for `ext:` fields.

## Significance

Stewards need to distinguish schema naming from privacy and release controls. Assuming that an external field is automatically hidden or removed could expose information that was not intended for public distribution.

## What This Means

- Review each `ext:` field for its purpose, sensitivity, permissions, and intended audience.
- If some fields should not be distributed, prepare and inspect a filtered copy before using the current TDEI upload and publishing workflow.
- Validate the intended dataset version and confirm its visibility and contents before sharing it.
- Preserve the source separately when project work requires fields that are not approved for public release.

The [OpenSidewalks schema](../../../opensidewalks/schema/index.md) defines the `ext:` naming convention. The [Portal dataset guide](../../../tdei/portal/user-manual/datasets.md) and [member-role guide](../../../tdei/portal/user-manual/members.md) describe dataset and role workflows but do not specify automatic treatment of `ext:` fields.

## What This Does Not Mean

A source dataset's `ext:` fields do not all have to be released publicly. The `ext:` prefix is not a privacy label or release control, and TDEI should not be assumed to hide, remove, or filter external fields automatically. Uploading a dataset also does not by itself make it public; project access and public release are separate.

## How To Use This

Identify the exact dataset version and intended audience. Inspect the actual fields, prepare a filtered copy if needed, and verify the output before following the current Portal workflow to publish or share it. Use the current manuals or ask the project group's Point of Contact when the upload or release behavior is unclear.

## Example

A project dataset contains an `ext:condition` field with local maintenance information. The steward checks whether it is appropriate for the intended audience, creates and validates a filtered copy if necessary, then verifies the released dataset rather than assuming the field was automatically hidden.

## Assistant Guidance

Ask which dataset version, fields, audience, and release state are involved. Cite the OpenSidewalks schema for the `ext:` convention. Do not claim that TDEI retains, removes, or filters these fields without current documentation, and do not say a dataset is safe to release without reviewing its actual contents.

## Related Concepts

- [How can the OpenSidewalks schema support external attributes?](../../opensidewalks/concept/external-attributes.md)
- [OpenSidewalks schema: external attributes](../../../opensidewalks/schema/index.md)
- [Who can see a TDEI dataset?](dataset-visibility.md)
- [How are releases versioned?](release-versioning.md)
- [How are edits uploaded back to TDEI?](../../workspaces/concept/edit-upload-to-tdei.md)
- [TDEI Portal datasets](../../../tdei/portal/user-manual/datasets.md)
- [TDEI Portal members and publishing roles](../../../tdei/portal/user-manual/members.md)
