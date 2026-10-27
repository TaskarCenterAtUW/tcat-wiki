---
uid: b84cac68-2b22-4e03-b4fb-f23caf74cff7
title: What is the TDEI released-dataset viewer?
slug: released-dataset-viewer
doc_type: concept
questions:
    - What is the TDEI released-dataset viewer?
    - Can I view a released dataset without a portal login?
audiences:
    - public
    - planner
    - jurisdiction
products:
    - TDEI
    - OS-CONNECT
topics:
    - tdei
    - os-connect
    - releases
    - public-vs-private-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The released-dataset viewer exposes unreleased or private project-group data.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is the TDEI released-dataset viewer?

## Short Answer

The TDEI data viewer presents released datasets for viewing without the same login flow used by the portal. It is intended for publicly viewable releases.

## Significance

A viewer makes a released dataset easier to inspect and share. It is distinct from the portal used to manage accounts, jobs, and project data.

## What This Means

Project datasets appear under **My Project Datasets** for their active project group, subject to the user's membership and permissions. Released datasets appear under **All Released Datasets** and in the Data Viewer. Use the Portal for account-based management and processing tasks.

## What This Does Not Mean

The viewer does not expose unreleased or private project-group datasets. Project datasets and released public datasets appear in different Portal views, subject to group membership and permissions.

## How To Use This

Confirm that the dataset is released before looking for it in the viewer. If it is missing, check release status and current viewer configuration.

## Example

A completed workspace is exported to TDEI and released. A public user can inspect the resulting dataset in the viewer without joining the project group.

## Assistant Guidance

Distinguish the viewer from the TDEI portal and Workspaces. Do not promise viewer visibility until release status is confirmed.

## Related Concepts

- [How do TDEI services relate to project groups?](services-and-project-groups.md)
