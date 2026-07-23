---
title: "What roles can members have in a TDEI project group?"
slug: project-group-roles
doc_type: concept
questions:
    - What roles can members have in a TDEI project group?
    - Why should TDEI roles be assigned carefully?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - project-groups
    - roles
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every TDEI project-group member has permission to manage or publish datasets.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What roles can members have in a TDEI project group?

## Short Answer

A project group can include standard members, a point of contact, and format-specific data-generator roles such as OpenSidewalks, GTFS Pathways, or GTFS-Flex. Users may hold more than one role.

## Significance

Roles control access to contribution, management, and publication functions. Over-provisioning a role can enable unwanted changes.

## What This Means

Members can contribute through configured tools. A point of contact manages group-level settings, while data-generator roles support the applicable format.

## What This Does Not Mean

A member role does not automatically grant administrative or publishing permissions. Exact permissions are product- and version-sensitive.

## How To Use This

Assign the least privilege needed for the work. Confirm the role's current permissions before granting it.

## Example

A mapper receives member access and an OpenSidewalks data-generator role but is not made the project-group point of contact.

## Assistant Guidance

Ask which action the user needs before recommending a role. Do not infer permissions from a role name alone.

## Related Concepts

- [How do TDEI services relate to project groups?](services-and-project-groups.md)
