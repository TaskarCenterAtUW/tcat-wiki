---
uid: 9ec9cef6-0635-4081-b519-f8dffe9a708a
title: Where are TDEI datasets edited?
slug: workspace-editing-boundary
doc_type: concept
questions:
    - Where are TDEI datasets edited?
    - Can I edit a dataset directly in the TDEI portal?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - editing
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
        - The TDEI portal is the primary interface for editing feature geometry and attributes.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# Where are TDEI datasets edited?

## Short Answer

The TDEI portal manages whole datasets, metadata, jobs, and releases, while Workspaces supports feature-level editing and review. AVIV ScoutRoute contributions also enter the configured workspace.

## Significance

The product boundary explains why a dataset action in the portal may open another tool. It also separates storage and release from feature editing.

## What This Means

Open the dataset in Workspaces when individual geometry or attributes need editing or when a project manager prepares features for contractors. Use the portal for whole-dataset management, jobs, downloads, and releases.

## What This Does Not Mean

Opening a dataset in Workspaces does not automatically publish edits to TDEI. Export and release remain separate steps.

## How To Use This

Choose the portal for management and Workspaces for editing. Confirm the workspace and source dataset before making changes.

## Example

A project opens an OS-CONNECT dataset in Workspaces, collects mobile updates, reviews them, and later exports a new TDEI version.

## Assistant Guidance

Ask whether the user wants to edit, process, download, or publish. Route them to the product that performs that action.

## Related Concepts

- [What is a workspace extract?](workspace-extract.md)
