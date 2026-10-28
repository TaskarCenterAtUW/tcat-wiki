---
uid: c3b02f8d-955d-4d16-9107-826eb20a5176
title: What is a project group in TDEI?
slug: project-group
doc_type: concept
questions:
    - What is a project group in TDEI?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - project-groups
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What is a project group in TDEI?

## Short Answer

A TDEI project group is a managed context for members, roles, services, datasets, and related workflows.

## Significance

The active project group determines which portal resources and permissions the user sees.

## What This Means

Users can belong to multiple groups, switch the active group, and copy its unique Project Group ID. Group members and Points of Contact have different permissions. The Portal's [Members guide](../../../tdei/portal/user-manual/members.md) specifies that a `poc` can view and manage the member list and that data-generator roles can publish datasets for their format.

## What This Does Not Mean

Belonging to one project group does not imply membership in every other group. A project group does not automatically make its datasets public or grant every member publishing rights.

## How To Use This

Confirm the active group before managing members, services, datasets, or jobs. The Portal's [Project Groups guide](../../../tdei/portal/user-manual/project-groups.md) documents group switching and the current-group indicator.

## Example

A user switches from one project group to another before opening its datasets page.

## Assistant Guidance

Ask for group name, ID, active context, and role when diagnosing access.

## Related Concepts

- [What roles can members have?](project-group-roles.md)
- [How do services relate to project groups?](tdei-services.md)
- [TDEI Portal Project Groups](../../../tdei/portal/user-manual/project-groups.md)
