---
title: "Is app access enabled by default for a new workspace?"
slug: workspace-app-access-default
doc_type: concept
questions:
    - Is app access enabled by default for a new workspace?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - AVIV ScoutRoute
topics:
    - workspaces
    - aviv-scoutroute
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-06-30
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A newly created workspace automatically appears in AVIV ScoutRoute.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Is app access enabled by default for a new workspace?

## Short Answer

A newly created workspace may have external app access disabled by default. It must be enabled before it appears as an AVIV ScoutRoute destination.

## Significance

This explains why a valid workspace may not appear in the mobile app.

## What This Means

Enable app access, configure quests, and confirm project membership before testing.

## What This Does Not Mean

App enablement does not make the workspace public.

## How To Use This

Check the app-access state in workspace settings.

## Example

A project creates a workspace, enables app access, and then makes its quest definition available.

## Assistant Guidance

Ask for workspace settings and project membership before diagnosing missing app access.

## Related Concepts

- [What is an app-enabled workspace?](../../aviv-scoutroute/concept/app-enabled-workspaces.md)
