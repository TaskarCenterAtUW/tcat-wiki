---
title: Can custom imagery be added?
slug: custom-imagery
doc_type: concept
questions:
    - Can custom imagery be added?
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
    - assistant/workspaces/concept/asr-imagery-list-repo.md
    - assistant/workspaces/concept/imagery-json-configuration.md
    - assistant/workspaces/concept/imagery-permissions.md
tags:
    - Assistant
---

<!-- @format -->

# Can custom imagery be added?

## Short Answer

Custom imagery can be added to a workspace when the current configuration supports it and the source meets the required schema, URL, access, attribution, and licensing conditions.

## Significance

Custom imagery can provide useful local visual context for editing when the default layers are insufficient.

## What This Means

Prepare a valid imagery definition using the current schema, confirm the source is accessible to intended users, verify attribution and permissions, save the configuration, and test the layer in the workspace.

## What This Does Not Mean

Adding imagery does not make the source authoritative, current, or suitable for every accessibility judgment. It does not change editable data or bypass source licensing and workspace permissions.

## How To Use This

Use the workspace settings and current ASR imagery-list documentation, keep raw configuration and version records, and report failures with the source and environment.

## Example

A manager adds an approved local imagery source using a validated JSON definition, checks that contributors can load it, and records its date and attribution.

## Assistant Guidance

Do not promise that a custom source will load or be permitted. Ask for the workspace, definition, URL, and access requirements, and abstain when current configuration rules are unknown.

## Related Concepts

- [What is the ASR imagery list repo?](asr-imagery-list-repo.md)
- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [How are imagery permissions handled?](imagery-permissions.md)
