---
title: How are imagery permissions handled?
slug: imagery-permissions
doc_type: concept
questions:
    - How are imagery permissions handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Workspaces
topics:
    - workspaces
    - imagery
    - basemaps
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/workspaces/concept/custom-imagery.md
    - assistant/workspaces/concept/imagery-json-configuration.md
    - assistant/workspaces/concept/imagery-resource-variation.md
tags:
    - Assistant
---

<!-- @format -->

# How are imagery permissions handled?

## Short Answer

Imagery permissions depend on the source provider's terms, access controls, workspace configuration, user roles, and intended use. Confirm permission and attribution requirements for the exact source and environment.

## Significance

A layer that one user or environment can access may not be available to every contributor. Licensing and access failures can interrupt review and editing.

## What This Means

Check source terms, authentication, audience, URL access, attribution, download or caching rules, and whether the workspace or app may display the imagery.

## What This Does Not Mean

A public-looking URL does not automatically grant reuse permission, and being able to load imagery does not make it authoritative or current.

## How To Use This

Document permissions and attribution, test access for intended users, and replace or remove a source when its terms or availability do not fit the workflow.

## Example

A manager confirms that contributors can view a licensed imagery service and includes the required attribution before enabling it for a workspace.

## Assistant Guidance

Do not provide legal permission advice without source terms. Cite the provider and workspace guidance, ask which users and use are involved, and abstain when access rights are unknown.

## Related Concepts

- [Can custom imagery be added?](custom-imagery.md)
- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [Why do imagery resources differ between workspaces?](imagery-resource-variation.md)
