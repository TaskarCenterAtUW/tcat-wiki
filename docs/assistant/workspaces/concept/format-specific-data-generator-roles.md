---
uid: c891d6dc-7c7b-419d-98e9-f9a3c0914907
title: What are format-specific data-generator roles?
slug: format-specific-data-generator-roles
doc_type: concept
questions:
    - What are format-specific data-generator roles in TDEI?
audiences:
    - developer
    - jurisdiction
products:
    - Workspaces
    - TDEI
topics:
    - workspaces
    - tdei
    - roles
    - formats
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A format-specific data-generator role grants unrestricted access to every TDEI format.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What are format-specific data-generator roles?

## Short Answer

TDEI can assign data-generator roles for formats such as OpenSidewalks, GTFS Pathways, and GTFS-Flex. These roles support work with the corresponding service type.

## Significance

Format-specific roles help separate responsibilities across different data products. They also limit publishing or generation privileges more precisely than a generic membership role.

## What This Means

Assign the role that matches the service or format a member maintains. A user may hold multiple roles when their work spans formats.

## What This Does Not Mean

A format-specific role does not automatically grant every project-group permission. Exact capabilities depend on current TDEI configuration.

## How To Use This

Review the service type and required action before assigning a role. Avoid granting broader roles when a narrower one is sufficient.

## Example

A member receives an OpenSidewalks data-generator role for sidewalk data and a separate Pathways role for station-navigation data.

## Assistant Guidance

Ask which format and operation are involved. Verify current role permissions before recommending assignment.

## Related Concepts

- [What roles can members have in a TDEI project group?](../../tdei/concept/project-group-roles.md)
