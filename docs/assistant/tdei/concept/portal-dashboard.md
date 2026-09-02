---
uid: 8c844f20-7875-40e4-a212-efe0a43de9fc
title: What does the TDEI portal dashboard show?
slug: portal-dashboard
doc_type: concept
questions:
    - What does the TDEI portal dashboard show?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - overview
    - project-groups
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The dashboard displays every project group or dataset available in TDEI.
        - Refreshing an API key leaves the previous key usable.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI portal dashboard show?

## Short Answer

The dashboard shows the active project group, the user's role, the project-group ID, and an API-key control. A project-group selector provides a shortcut to another group.

## Significance

These values identify the account context used by later portal actions. Checking them can prevent work in the wrong project group.

## What This Means

Confirm the active project group and role before managing data or services. Treat the API key as a credential. Refreshing it invalidates the previous key.

## What This Does Not Mean

The dashboard does not by itself grant permissions or show every dataset. Access depends on the active group and assigned roles.

## How To Use This

Use the project selector to switch context and verify the displayed role. Do not expose or share the API key.

## Example

A user switches to the project group that owns a dataset before opening its services or datasets pages.

## Assistant Guidance

Ask for the active project group and role when troubleshooting portal access. Never request an API key in chat.

## Related Concepts

- [How do TDEI services relate to project groups?](services-and-project-groups.md)
