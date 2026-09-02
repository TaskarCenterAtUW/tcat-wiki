---
uid: 377a2e5f-06e9-4713-8d2d-a34aeb056b0b
title: What sources were used for an edit?
slug: edit-source-tracking
doc_type: concept
questions:
    - What sources were used for an edit?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - review
    - changesets
    - qa-qc
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/edit-metadata.md
    - assistant/workspaces/concept/changeset-tracking.md
    - assistant/workspaces/concept/workspace-review-interface.md
tags:
    - Assistant
---

<!-- @format -->

# What sources were used for an edit?

## Short Answer

Edit source tracking records the imagery, field observation, local dataset, quest, or other evidence associated with an edit when that information is supplied and retained by the workspace or editor.

## Significance

Source context helps reviewers assess whether an edit is reproducible, appropriate to the feature, and consistent with the dataset's intended use.

## What This Means

Inspect changeset comments and metadata, record source names, URLs or identifiers, dates, licenses, and versions where available, and compare the source with the changed geometry or attributes.

## What This Does Not Mean

Source metadata does not prove that the source is current, authoritative, or correctly interpreted. An edit without a visible source is not automatically false, but it may require clarification.

## How To Use This

Require source notes for consequential edits according to project policy, preserve provenance during export, and ask contributors for clarification when evidence is incomplete.

## Example

A mapper cites current imagery and a field note for a sidewalk edit. The reviewer checks the dates and confirms that the source supports the changed geometry before further review.

## Assistant Guidance

Do not infer sources from editor appearance or location alone. Cite the actual record and abstain when source provenance cannot be verified.

## Related Concepts

- [What metadata is stored for edits?](edit-metadata.md)
- [How are changesets tracked?](changeset-tracking.md)
- [What can the Workspaces review interface show?](workspace-review-interface.md)
