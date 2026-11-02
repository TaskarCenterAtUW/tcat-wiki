---
uid: 298fc015-dc9c-41f6-a4ad-438c01f375ed
title: What are Workspaces teams?
slug: workspace-teams
doc_type: concept
questions:
    - What are Workspaces teams?
    - How can Workspaces teams organize contributors?
audiences:
    - jurisdiction
    - planner
products:
    - Workspaces
topics:
    - workspaces
    - teams
    - onboarding
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-10-30
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/workspaces/concept/teams.md
    - assistant/workspaces/concept/workspaces-api.md
tags:
    - Assistant
---

<!-- @format -->

# What are Workspaces teams?

## Short Answer

Workspaces teams organize contributors within a project and may provide team-specific QR-code onboarding.

## Significance

Teams can support event grouping and contribution reporting.

## What This Means

The API reference documents workspace-scoped team creation, retrieval, update, and deletion, plus member-list and membership operations. Its team schema includes an ID, name, and member count; this contract does not establish user-interface availability or permission effects.

## What This Does Not Mean

A team is not the same as a TDEI project group or its permissions.

## How To Use This

Confirm whether a QR code joins a team or a project group.

## Example

An event creates separate teams for contributors assigned to different cities.

## Assistant Guidance

Treat this feature as version-sensitive. Verify current user-interface availability and use the API reference only for documented endpoint and schema details.

## Related Concepts

- [How do teams differ from project groups?](teams-vs-project-groups.md)
- [What are teams in Workspaces?](teams.md)
- [What APIs does Workspaces provide?](workspaces-api.md)
- [Workspaces API Swagger documentation](https://api.workspaces.sidewalks.washington.edu/docs)
