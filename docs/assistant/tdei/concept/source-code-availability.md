---
uid: daacdf1c-571a-4475-89a1-78cb5dde4fee
title: Is the source code for TDEI publicly available on GitHub?
tags:
    - Assistant
slug: source-code-availability
doc_type: concept
questions:
    - Is the source code for TDEI publicly available on GitHub?
products:
    - TDEI
audiences:
    - public
topics:
    - tdei
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
    - tdei/index.md
    - assistant/tdei/index.md
---

<!-- @format -->

# Is the source code for TDEI publicly available on GitHub?

## Short Answer

Partly. Public components include [TDEI Tools](https://github.com/TaskarCenterAtUW/tdei-tools), the [TDEI Backend Service](https://github.com/TaskarCenterAtUW/TDEI-backend-service), [TDEI Gateway](https://github.com/TaskarCenterAtUW/TDEI-gateway), and [TDEI OSW Data Service](https://github.com/TaskarCenterAtUW/TDEI-osw-datasvc-ts). Not every TDEI component is public.

## Significance

TDEI is a collection of services and tools, so source availability can differ by component.

## What This Means

The listed repositories are public sources for specific TDEI components; they do not represent the complete TDEI platform.

## What This Does Not Mean

Public source for some components does not mean all TDEI services, deployments, or internal tools are publicly available.

## How To Use This

Use the repository that matches the component in question, and check its README and current visibility for details.

## Example

For TDEI backend processing code, link the [TDEI Backend Service repository](https://github.com/TaskarCenterAtUW/TDEI-backend-service); for the API gateway, link [TDEI Gateway](https://github.com/TaskarCenterAtUW/TDEI-gateway).

## Assistant Guidance

Answer partly and link only repositories verified as public. Do not claim the complete TDEI source code is publicly available.

## Related Concepts

- [TDEI product page](../../../tdei/index.md)
- [TDEI knowledge base](../index.md)
