---
title: "How do TDEI services relate to project groups?"
slug: services-and-project-groups
doc_type: concept
questions:
    - What does a TDEI service define?
    - Can a project group contain multiple services?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - project-groups
    - formats
    - dataset-lineage
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
        - A TDEI project group can define only one service.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do TDEI services relate to project groups?

## Short Answer

A TDEI service describes the type and scope of a shared data sub-document. A project group can contain multiple services when partners maintain different datasets or service areas together.

## Significance

The distinction separates collaboration membership from the data being maintained. It helps partners organize related but different outputs.

## What This Means

A service can identify a format and scope, such as OpenSidewalks for a city area or GTFS Pathways for a station. The project group provides the shared organizational context.

## What This Does Not Mean

A service is not necessarily a project group, and one project group does not necessarily have only one service. Current product configuration controls the available options.

## How To Use This

Points of contact generally manage services for the project group. Define the service scope before publishing or exporting a workspace, and confirm the format, geographic area, and responsible partners.

## Example

One project group maintains city sidewalk data as OpenSidewalks and several transit-station pathway datasets as separate services.

## Assistant Guidance

Ask whether the user means a membership group, dataset scope, or file type. Verify current service terminology before giving configuration steps.

## Related Concepts

- [How do project-group referrals provide workspace access?](../../workspaces/concept/project-group-referral-access.md)
