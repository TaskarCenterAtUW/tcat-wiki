---
uid: 7fb805f0-385d-49e0-8db2-26917817853f
title: What operational workflows still need improvement?
slug: workflow-improvement-areas
doc_type: concept
questions:
    - What operational workflows still need improvement?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - operational-workflows
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-09-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - OS-CONNECT has fully automated correction, review, and release workflows.
        - Reporting an issue immediately changes the published dataset.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/data-maintenance-challenges.md
    - assistant/os-connect/concept/correction-tracking.md
    - assistant/os-connect/concept/correction-release-lag.md
tags:
    - Assistant
---

<!-- @format -->

# What operational workflows still need improvement?

## Short Answer

Documented improvement areas include making maintenance, correction tracking, validation, follow-up, and release propagation more explicit and dependable. Exact priorities depend on the current OS-CONNECT operating process.

## Significance

Users need to know what happens after an issue is reported and when a corrected value can be expected in a released dataset. Clear handoffs reduce repeated reports and prevent users from mistaking an open issue for a completed correction.

## What This Means

 - Record the issue, evidence, owner, review state, and affected release.
 - Distinguish intake, validation, correction, publication, and viewer refresh.
 - Monitor unresolved items and communicate release lag or scope limitations.

## What This Does Not Mean

An issue-reporting workflow is not proof that a correction has been accepted, applied, or published. A process may still have manual steps or unresolved ownership.

## How To Use This

Ask for the issue's current state and the dataset release being viewed. Do not promise a correction date without evidence.

## Example

A reviewer confirms that a submitted correction was validated and included in a later release before telling an analyst that the map has changed.

## Assistant Guidance

This article describes improvement themes, not a complete service-level commitment. Cite relevant workflow evidence and abstain when ownership, status, or release timing is unknown.

## Related Concepts

 - [OS-CONNECT — Assistant Knowledge Base](../index.md)
 - [How are corrections tracked?](correction-tracking.md)
 - [What is correction release lag?](correction-release-lag.md)
