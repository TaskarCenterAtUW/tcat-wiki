---
uid: 95419778-f9cc-45ab-9bdf-d41ee0363844
title: Is the source code for Workspaces publicly available on GitHub?
tags:
    - Assistant
slug: source-code-availability
doc_type: concept
questions:
    - Is the source code for Workspaces publicly available on GitHub?
products:
    - Workspaces
audiences:
    - public
topics:
    - workspaces
    - open-source
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-11-15
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
related_pages:
    - workspaces/index.md
    - assistant/workspaces/index.md
---

<!-- @format -->

# Is the source code for Workspaces publicly available on GitHub?

## Short Answer

Partly. Public repositories include the [frontend](https://github.com/TaskarCenterAtUW/workspaces-frontend), [backend](https://github.com/TaskarCenterAtUW/workspaces-backend), [deployment stack](https://github.com/TaskarCenterAtUW/workspaces-stack), and [Rapid integration](https://github.com/TaskarCenterAtUW/workspaces-rapid). Not every related Workspaces repository is public.

## Significance

Workspaces consists of multiple codebases, so the availability of its source depends on which component is in question.

## What This Means

Source code for the listed Workspaces components can be inspected in their public GitHub repositories.

## What This Does Not Mean

The listed repositories are not a promise that every Workspaces-related service or repository is public or included in those codebases.

## How To Use This

Choose the repository that matches the component you want to inspect, and check its current README, branches, and visibility.

## Example

For the Workspaces user interface, link the [frontend repository](https://github.com/TaskarCenterAtUW/workspaces-frontend); for its deployment setup, link the [deployment stack](https://github.com/TaskarCenterAtUW/workspaces-stack).

## Assistant Guidance

Answer partly, cite the relevant public repository, and do not describe the linked repositories as the complete Workspaces source code.

## Related Concepts

- [Workspaces product page](../../../workspaces/index.md)
- [Workspaces knowledge base](../index.md)
