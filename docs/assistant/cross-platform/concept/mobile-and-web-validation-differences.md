---
uid: 1783d183-b377-4c17-a303-f83701312400
title: How can validation differ between mobile apps and Workspaces?
slug: mobile-and-web-validation-differences
doc_type: concept
questions:
    - Does Workspaces enforce the same numeric limits as AVIV ScoutRoute?
    - Why might mobile and web editing accept different values?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
    - Workspaces
topics:
    - cross-platform
    - aviv-scoutroute
    - workspaces
    - editing
    - testing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A limit configured for a mobile quest automatically constrains Workspaces editing.
related_pages:
    - assistant/cross-platform/index.md
    - assistant/aviv-scoutroute/concept/numeric-quest-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How can validation differ between mobile apps and Workspaces?

## Short Answer

Limits set in a quest definition do not apply to values submitted to a workspace using editors other than AVIV ScoutRoute.

## Significance

A value collected through one interface may be handled differently in another. Cross-platform testing is necessary when a data rule matters.

## What This Means

Values submitted in an editor such as Rapid may not match the conventions set by a quest definition.

## What This Does Not Mean

A mobile quest limit is not automatically a workspace-wide constraint. The survey via app does not establish the behavior of every field or version.

## How To Use This

Include platform, app version, workspace, quest definition, value, warning, and submission result in a test report. Review edits before relying on them.

## Example

A mobile quest is configured for widths entered as numbers up to 100, while a Workspaces editor accepts any string.

## Assistant Guidance

Do not generalize one interface's validation behavior to another. Ask which product and editing path the user is using.

## Related Concepts

- [How are numeric quest values validated?](../../aviv-scoutroute/concept/numeric-quest-validation.md)
