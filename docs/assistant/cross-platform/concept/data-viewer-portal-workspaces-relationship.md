---
title: "How do the TDEI portal, viewer, Workspaces, and AVIV ScoutRoute relate?"
slug: data-viewer-portal-workspaces-relationship
doc_type: concept
questions:
    - What is the relationship between the TDEI portal and Workspaces?
    - How do the data viewer and AVIV ScoutRoute fit together?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - Cross-Platform
    - TDEI
    - Workspaces
    - AVIV ScoutRoute
topics:
    - cross-platform
    - tdei
    - workspaces
    - aviv-scoutroute
    - tdei-ecosystem
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
        - The TDEI portal, viewer, Workspaces, and AVIV ScoutRoute are the same product.
related_pages:
    - assistant/cross-platform/index.md
    - assistant/workspaces/concept/workspace-extract.md
    - assistant/tdei/concept/released-dataset-viewer.md
tags:
    - Assistant
---

<!-- @format -->

# How do the TDEI portal, viewer, Workspaces, and AVIV ScoutRoute relate?

## Short Answer

The TDEI portal manages datasets, services, jobs, and releases. Workspaces supports focused collaborative editing, AVIV ScoutRoute collects targeted mobile answers, and the viewer displays released datasets.

## Significance

Knowing the product boundaries helps users choose the right tool. It also clarifies why an edit or contribution may not appear publicly immediately.

## What This Means

A typical flow is source dataset to a workspace copy, targeted mobile contributions, review and export to TDEI, then release and viewing. Project managers may prepare features in Workspaces for contractors, while source geometry corrections use the OS-CONNECT feedback workflow. Walksheds can model selected attributes in this dataset context, and QA/QC reports analyze a particular dataset and pipeline version. The exact flow depends on project configuration.

## What This Does Not Mean

Signing in to one product does not guarantee access to every product feature. Editing, collecting, exporting, and viewing have separate permissions and states.

## How To Use This

Identify the desired action first: manage, edit, collect, publish, or view. Then check the relevant account, project group, workspace, service, and release status.

## Example

A project edits a city extract in Workspaces, collects curb-ramp answers in AVIV ScoutRoute, exports the result to TDEI, and enables the released dataset for public viewing.

## Assistant Guidance

Ask which product and stage the user is using before troubleshooting. Do not infer publication or visibility from a successful mobile contribution or workspace edit.

## Related Concepts

- [What is a workspace extract?](../../workspaces/concept/workspace-extract.md)
- [What is the TDEI released-dataset viewer?](../../tdei/concept/released-dataset-viewer.md)
