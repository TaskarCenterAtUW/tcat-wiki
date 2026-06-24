---
title: TDEI — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-tdei
doc_type: concept
products:
    - TDEI
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - tdei-ecosystem
    - dataset-lineage
    - publication-workflow
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - TDEI and OS-CONNECT are the same platform.
        - Downloading data from TDEI gives access to unreleased or private datasets.
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/index.md
    - assistant/os-connect/index.md
---

# TDEI — Assistant Knowledge Base

## Short Answer

This section contains question pages for the Transportation Data Exchange Initiative (TDEI), the data portal and API that publishes released pedestrian datasets — including OS-CONNECT — and manages dataset versioning, project groups, and data downloads. TDEI is the publication layer that connects Workspaces (editing) to OS-CONNECT (public viewer).

## Significance

TDEI is frequently misunderstood as synonymous with OS-CONNECT or with the Workspaces editing platform. Clarifying the roles of TDEI (portal and API), OS-CONNECT (viewer and released dataset), and Workspaces (editing environment) is essential for partners working in the TCAT data ecosystem.

## What This Means

- Pages in `tdei/` address the TDEI portal UI, data downloads, file formats, API access, dataset versioning, and project groups.
- For questions about how data moves from Workspaces into TDEI, see [workspaces/workflows/](../workspaces/workflows/index.md).
- For questions about the published viewer experience, see [os-connect/](../os-connect/index.md).

## What This Does Not Mean

- Not a substitute for official TDEI API documentation for developers integrating directly with TDEI endpoints.
- TDEI does not publicly host private or pre-release data; only `released` datasets are publicly accessible.

## How To Use This

**Agents**: For ecosystem-positioning questions, start with `tdei/what-is-tdei.md`. For download questions, use `tdei/where-can-i-download-the-data.md` and `tdei/what-file-formats-are-available.md`. For dataset versioning, use `tdei/how-are-releases-versioned.md`.

**Authors**: Key pages to author first: `what-is-tdei.md`, `what-is-a-project-group-in-tdei.md`, `where-can-i-download-the-data.md`, and `what-file-formats-are-available.md`. These answer the most common onboarding questions.

## Example

A GIS analyst asks: _"What is the difference between downloading OSW format and OSM format from TDEI?"_ Retrieve `tdei/what-is-the-difference-between-downloading-osw-format-and-osm-format.md`.

## Assistant Guidance

Always distinguish TDEI (the data exchange infrastructure and portal) from OS-CONNECT (the specific pedestrian dataset published via TDEI) and from Workspaces (the editing environment that feeds TDEI). Conflating these three is a common source of confusion.

## Related Concepts

- [Workspaces knowledge base](../workspaces/index.md)
- [OS-CONNECT knowledge base](../os-connect/index.md)
- [Cross-product support](../support/index.md)
- [Dispatch — full file registry](../dispatch.md)
