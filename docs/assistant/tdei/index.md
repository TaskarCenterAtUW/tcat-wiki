---
uid: 15c65282-0552-4aac-a7ac-9957cac9db20
title: TDEI — Assistant Knowledge Base
slug: tdei-index
doc_type: policy
questions:
    - What assistant-facing information and policies are covered in the TDEI knowledge base?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - tdei-ecosystem
    - dataset-lineage
    - publication-workflow
risk_level: low
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - TDEI and OS-CONNECT are the same platform.
        - The public released-dataset listings expose unreleased or private project-group datasets.
        - Accessing project datasets under **My Project Datasets** makes them public.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/index.md
    - assistant/os-connect/index.md
tags:
    - Assistant
---

<!-- @format -->

# TDEI — Assistant Knowledge Base

## Short Answer

This section contains question pages for the Transportation Data Exchange Initiative (TDEI), its data portal and API, project groups, services, datasets, and processing jobs. The Portal supports OSW, Flex, and Pathways dataset types; OS-CONNECT is a public viewer for released pedestrian data, and Workspaces is a separate editing platform that can connect to TDEI. See the [Portal dataset guide](../../tdei/portal/user-manual/datasets.md) for the documented dataset types.

## Significance

TDEI is frequently misunderstood as synonymous with OS-CONNECT or with the Workspaces editing platform. Clarifying the roles of TDEI (portal and API), OS-CONNECT (viewer and released dataset), and Workspaces (editing environment) is essential for partners working in the TCAT data ecosystem.

## What This Means

- Pages in `tdei/` address the TDEI portal UI, data downloads, file formats, API access, dataset versioning, and project groups.
- For questions about how data moves from Workspaces into TDEI, see [workspaces/](../workspaces/index.md).
- For questions about the published viewer experience, see [os-connect/](../os-connect/index.md).

## What This Does Not Mean

- This knowledge base is not a substitute for official TDEI API documentation for developers integrating directly with TDEI endpoints.
- The public **All Released Datasets** listing does not expose unreleased or private project-group datasets; access to a project dataset through **My Project Datasets** does not make it public.
- TDEI, OS-CONNECT, and Workspaces have distinct roles and are not the same platform or application.

## How To Use This

**Agents**: For ecosystem-positioning questions, start with [What is TDEI?](concept/tdei.md). For download questions, use [Where can I download the data?](workflow/download-data.md) and [What file formats are available?](concept/file-formats.md). For dataset versioning, use [How are releases versioned?](concept/release-versioning.md).

**Authors**: Key onboarding pages include [What is TDEI?](concept/tdei.md), [What is a project group in TDEI?](concept/project-group.md), [Where can I download the data?](workflow/download-data.md), and [What file formats are available?](concept/file-formats.md).

## Example

A GIS analyst asks: _"What is the difference between downloading OSW format and OSM format from TDEI?"_ Retrieve [What is the difference between downloading OSW and OSM format?](concept/osw-vs-osm-format.md).

## Assistant Guidance

Always distinguish TDEI (the data exchange infrastructure and portal) from OS-CONNECT (the specific pedestrian dataset published via TDEI) and from Workspaces (the editing environment that feeds TDEI). Conflating these three is a common source of confusion.

## Related Concepts

- [Workspaces knowledge base](../workspaces/index.md)
- [OS-CONNECT knowledge base](../os-connect/index.md)
- [Cross-product support](../support/index.md)
- [Dispatch — full file registry](../dispatch.md)
