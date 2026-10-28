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
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
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

Project datasets appear in the Portal's **My Project Datasets** view for the active project group, subject to the user's membership and permissions. Released datasets appear in the public **All Released Datasets** listing.

## Significance

Visibility determines who can inspect, download, or use a dataset. It should be checked before sharing a dataset link.

## What This Means

Use **My Project Datasets** for data within the active project group and **All Released Datasets** for public releases. A source or baseline dataset can remain within the project group while completed or derived versions are prepared. The Portal manual describes the first view as datasets belonging to the active project group and the second as public releases across TDEI.

## What This Does Not Mean

Being stored in TDEI does not make a dataset public. Access to project datasets is also subject to the user's membership and permissions in the active project group.

## How To Use This

Check the active project group and release status before troubleshooting missing data. Do not share private dataset contents without authorization.

## Example

A user opens **My Project Datasets** while their project group is active to find a project dataset. They use **All Released Datasets** to browse public releases.

## Assistant Guidance

Ask whether the user is looking for a private project dataset or a public release. Do not infer visibility from storage alone. For current Portal labels and dataset-list behavior, refer to the [TDEI Portal dataset guide](../../../tdei/portal/user-manual/datasets.md).

## Related Concepts

- [What is the TDEI released-dataset viewer?](released-dataset-viewer.md)
- [TDEI Portal datasets](../../../tdei/portal/user-manual/datasets.md)
