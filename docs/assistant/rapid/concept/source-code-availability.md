---
uid: 920ad5af-7956-4f71-906d-0af465e98bfd
title: Is the source code for Rapid publicly available on GitHub?
tags:
    - Assistant
slug: source-code-availability
doc_type: concept
questions:
    - Is the source code for Rapid publicly available on GitHub?
products:
    - Rapid
audiences:
    - public
topics:
    - rapid
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
    - rapid/index.md
    - assistant/rapid/index.md
---

<!-- @format -->

# Is the source code for Rapid publicly available on GitHub?

## Short Answer

Yes. The upstream [Rapid editor](https://github.com/meta/Rapid) and [Workspaces Rapid integration](https://github.com/TaskarCenterAtUW/workspaces-rapid) are public.

## Significance

The public repositories let developers inspect Rapid and the TCAT Workspaces integration separately.

## What This Means

The upstream editor code and TCAT's integration code are available in separate public GitHub repositories.

## What This Does Not Mean

The upstream Rapid project and the Workspaces integration are distinct codebases; the integration repository is not the full upstream editor source.

## How To Use This

Use the [Rapid repository](https://github.com/meta/Rapid) for the upstream editor and the [Workspaces integration repository](https://github.com/TaskarCenterAtUW/workspaces-rapid) for its integration.

## Example

For a question about Rapid itself, link the upstream repository; for questions about Rapid in Workspaces, link the TCAT integration repository as well.

## Assistant Guidance

Answer yes and distinguish the upstream project from TCAT's integration. Do not imply the integration repository contains all upstream code.

## Related Concepts

- [Rapid product page](../../../rapid/index.md)
- [Rapid knowledge base](../index.md)
