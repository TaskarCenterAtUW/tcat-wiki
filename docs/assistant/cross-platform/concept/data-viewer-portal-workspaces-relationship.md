---
uid: d1f34cff-a68b-4671-9f2a-3ef5f66c126e
title: How do the TDEI portal, viewer, Workspaces, and AVIV ScoutRoute relate?
slug: data-viewer-portal-workspaces-relationship
doc_type: concept
questions:
    - What is the relationship between the TDEI portal and Workspaces?
    - Do I need to sign in separately to the TDEI Portal and Workspaces?
    - What happens when I log out of the TDEI Portal or Workspaces?
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
last_reviewed: 2026-11-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/cross-platform/index.md
    - assistant/workspaces/concept/workspace-extract.md
    - assistant/tdei/concept/released-dataset-viewer.md
    - tdei/portal/user-manual/account-registration.md
    - workspaces/user-manual/getting-started.md
tags:
    - Assistant
---

<!-- @format -->

# How do the TDEI portal, viewer, Workspaces, and AVIV ScoutRoute relate?

## Short Answer

The TDEI Portal manages datasets, services, jobs, and releases. Workspaces supports focused collaborative editing, AVIV ScoutRoute collects targeted mobile answers, and the viewer displays released datasets. In production, the Portal and Workspaces share a single sign-on (SSO) session, while each application creates its own local session.

## Significance

Knowing the product boundaries helps users choose the right tool. It also clarifies why an edit or contribution may not appear publicly immediately.

## What This Means

A typical data flow is source dataset to a workspace copy, targeted mobile contributions, review and export to TDEI, then release and viewing. For production sign-in, select **TDEI Login** in the application you want to open. It redirects to the shared TDEI accounts page and returns you to the application that started sign-in. If you already signed in to the other application, SSO normally avoids another credential prompt. Project managers may prepare features in Workspaces for contractors, while source geometry corrections use the OS-CONNECT feedback workflow. Walksheds can model selected attributes in this dataset context, and QA/QC reports analyze a particular dataset and pipeline version. The exact flow depends on project configuration.

## What This Does Not Mean

The shared SSO session does not automatically open the other application or guarantee access to every product feature. Each application creates its own local session, and roles and permissions still determine what you can access. Logging out of either application ends the central SSO session and returns you to that application's login page. An already-open tab in the other application may remain active briefly until it refreshes or validates its token; refresh its open tabs for an immediate logout across both applications.

## How To Use This

Identify the desired action first: manage, edit, collect, publish, or view. Then check the relevant account, project group, workspace, service, and release status.

## Example

A project manager signs in to the Portal, opens Workspaces, and selects **TDEI Login**; the shared session normally avoids another credential prompt. The manager then edits a city extract in Workspaces, collects curb-ramp answers in AVIV ScoutRoute, exports the result to TDEI, and enables the released dataset for public viewing.

## Assistant Guidance

Ask which product and stage the user is using before troubleshooting. For production authentication, distinguish the shared SSO session from each application's local session and permissions. Do not claim that signing in opens the other application or infer publication or visibility from a successful mobile contribution or workspace edit.

## Related Concepts

- [What is a workspace extract?](../../workspaces/concept/workspace-extract.md)
- [What is the TDEI released-dataset viewer?](../../tdei/concept/released-dataset-viewer.md)
