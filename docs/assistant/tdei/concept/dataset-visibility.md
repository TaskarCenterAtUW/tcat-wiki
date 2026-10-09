---
uid: 86d1356e-dcdf-4bbf-bd0e-a5e40b791e4b
title: Who can see a TDEI dataset?
slug: dataset-visibility
doc_type: concept
questions:
    - Who can see a TDEI dataset?
    - What is the difference between project datasets and released datasets?
audiences:
    - public
    - jurisdiction
    - planner
products:
    - TDEI
topics:
    - tdei
    - public-vs-private-data
    - releases
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-29
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every TDEI project dataset is publicly downloadable.
        - Deactivating a dataset is a reversible way to unrelease it.
related_pages:
    - assistant/tdei/concept/released-dataset.md
    - assistant/tdei/concept/release-versioning.md
    - assistant/workspaces/concept/keeping-edits-private.md
tags:
    - Assistant
---

<!-- @format -->

# Who can see a TDEI dataset?

## Short Answer

Project datasets are available to the relevant project-group members, while released datasets are available through the public released-dataset listings. Release status controls the boundary.

## Significance

Visibility determines who can inspect, download, or use a dataset. It should be checked before sharing a dataset link.

## What This Means

Use the project-dataset view for group work and the released-dataset view for public data. A source or baseline dataset can remain private while completed or derived versions are prepared.

Treat dataset deactivation as removal, not as a temporary visibility change: the interface warns that deactivation removes the dataset from the system. Confirm the dataset and version before deactivating it, and preserve any data that must be retained. Do not use deactivation as a substitute for controlling release status.

## What This Does Not Mean

Being stored in TDEI does not make a dataset public. Membership and release settings still apply. Deactivation is not an ordinary unrelease or hide action, and should be treated as irreversible.

## How To Use This

Check the active project group and release status before troubleshooting missing data. Before deactivation, verify the dataset identity and version and confirm that needed copies are preserved. Do not share private dataset contents without authorization, or deactivate a dataset merely to remove it from public view.

## Example

A draft dataset appears to project members but not in the all-released list until a point of contact publishes it.

## Assistant Guidance

Ask whether the user is looking for a private project dataset or a public release. Do not infer visibility from storage alone or suggest deactivation as a reversible release control. Treat deactivation as permanent removal.

## Related Concepts

- [What is the TDEI released-dataset viewer?](released-dataset-viewer.md)
