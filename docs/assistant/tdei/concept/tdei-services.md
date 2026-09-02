---
uid: 6c3e53f6-6b7b-46f8-ab45-c164b8e5b29d
title: How do TDEI services relate to project groups?
slug: tdei-services
doc_type: concept
questions:
    - What is a TDEI service?
    - How do TDEI services relate to project groups?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - project-groups
    - configuration
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
        - Every project-group member can create or edit TDEI services.
related_pages:
    - project-group.md
    - project-group-roles.md
    - ../../../tdei/portal/user-manual/services.md
tags:
    - Assistant
---

<!-- @format -->

# How do TDEI services relate to project groups?

## Short Answer

A TDEI service belongs to a project group and identifies a data service type such as OSW, Flex, or Pathways. Points of Contact can create, edit, or deactivate services.

## Significance

Services connect project-group configuration to the datasets and workflows the group manages.

## What This Means

Services have a name, type, ID, and optional GeoJSON boundaries. Members can view services, while a `poc` can create, edit, and deactivate them. Active/inactive filters and service search help manage the list.

## What This Does Not Mean

A service is not itself a dataset, and service access does not automatically grant publishing permissions.

## How To Use This

Confirm the active project group, service type, ID, boundaries, and role before changing a service.

## Example

A Point of Contact creates an OSW service with a GeoJSON boundary for a project group's jurisdiction.

## Assistant Guidance

Ask for the project group, role, service type, and intended change. Do not infer permission from read-only visibility.

## Related Concepts

- [What roles can members have?](project-group-roles.md)
- [What is a project group?](project-group.md)
