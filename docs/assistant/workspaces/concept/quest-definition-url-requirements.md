---
uid: 7622fde6-19c3-4a11-8e4a-850a32f66a51
title: What URL can a workspace use for a quest definition?
slug: quest-definition-url-requirements
doc_type: concept
questions:
    - What URL can a workspace use for a quest definition?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - quests
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A normal GitHub repository page is a valid quest-definition URL.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What URL can a workspace use for a quest definition?

## Short Answer

The URL should point directly to the raw JSON quest-definition file, not to a repository page or HTML view.

## Significance

Using the wrong URL can make workspace settings or app configuration fail; current versions should fail clearly rather than become inaccessible.

## What This Means

Test that the URL returns JSON content directly.

## What This Does Not Mean

A link that displays JSON in a browser is not necessarily a direct raw-file URL.

## How To Use This

Use the raw-file URL and validate it in a test workspace before wider deployment.

## Example

A GitHub repository's raw JSON URL is used instead of the repository's normal file page.

## Assistant Guidance

Ask for the URL type and current error before diagnosing configuration.

## Related Concepts

- [How is a quest definition applied?](../../aviv-scoutroute/concept/quest-definition-application.md)
