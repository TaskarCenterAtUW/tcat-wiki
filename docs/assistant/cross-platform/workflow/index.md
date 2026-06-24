---
title: Workflows — Assistant Knowledge Base
tags:
    - Assistant
slug: assistant-workflows
doc_type: workflow
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
    - Workspaces
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - assistant-layer
    - publication-workflow
    - collaboration
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-09
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim: []
related_pages:
    - assistant/index.md
    - assistant/dispatch.md
    - assistant/workspaces/workflows/index.md
---

<!-- @format -->

# Workflows — Assistant Knowledge Base

## Short Answer

This section contains cross-product workflow pages describing common operational tasks that involve multiple TCAT tools — such as reviewing community feedback, updating jurisdiction data, using AccessMap for public engagement, and using OS-CONNECT for ADA transition planning. Workspaces-specific workflows are in [workspaces/workflows/](../workspaces/workflows/index.md).

## Significance

Workflow pages answer "how do I do X?" questions that span more than one product or that describe a multi-step process involving external stakeholders. They help assistants provide actionable, sequential guidance rather than abstract explanations.

## What This Means

- Pages in `workflows/` describe task sequences, actor roles, and tool involvement for common cross-product workflows.
- Product-specific workflows (e.g., creating a workspace from TDEI, exporting workspace edits) are in the relevant product section.
- Staff communication workflows (e.g., how to respond to a support email) are in `workflows/support-answer-patterns.md`.

## What This Does Not Mean

- Workflow pages do not replace official procedural manuals; they provide assistant-layer summaries with links to authoritative sources.
- These workflows reflect the state of tools at the time of authoring; verify against current product documentation before using in high-stakes contexts.

## How To Use This

**Agents**: Match user queries to the closest workflow page. For OS-CONNECT ADA planning questions, retrieve `workflows/use-os-connect-for-ada-transition-planning.md`. For public engagement, retrieve `workflows/use-accessmap-for-public-engagement.md`.

**Authors**: Six workflow pages are planned at the cross-product level. Additional Workspaces-specific workflows are in [workspaces/workflows/](../workspaces/workflows/index.md).

## Example

A Safe Routes to School coordinator asks: _"How can I use Walksheds to support our SRTS program?"_ Retrieve `workflows/use-walksheds-for-safe-routes-to-school.md`.

## Assistant Guidance

Workflow pages often involve external stakeholder coordination (jurisdiction staff, advocacy groups, school districts). When presenting a workflow, note which steps require human judgment or external approval, and which are tool-assisted.

## Related Concepts

- [Workspaces workflows](../workspaces/workflows/index.md)
- [Policies](../policies/index.md)
- [Dispatch — full file registry](../dispatch.md)

## Planned Pages

| File                                                      | Workflow                                                                  |
| :-------------------------------------------------------- | :------------------------------------------------------------------------ |
| `workflows/review-community-feedback.md`                  | How to review and act on community-submitted data corrections             |
| `workflows/support-answer-patterns.md`                    | Communication patterns for staff responding to external partner questions |
| `workflows/update-jurisdiction-data.md`                   | How jurisdictions submit and track data updates                           |
| `workflows/use-accessmap-for-public-engagement.md`        | Using AccessMap in community meetings and public-facing planning          |
| `workflows/use-os-connect-for-ada-transition-planning.md` | Integrating OS-CONNECT data into ADA transition plan workflows            |
| `workflows/use-walksheds-for-safe-routes-to-school.md`    | Using Walksheds for SRTS analysis and grant applications                  |
