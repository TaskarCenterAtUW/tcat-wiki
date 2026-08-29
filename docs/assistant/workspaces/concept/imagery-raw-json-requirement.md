---
title: Why must imagery use raw JSON links?
slug: imagery-raw-json-requirement
doc_type: concept
questions:
    - Why must imagery use raw JSON links?
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
    - assistant/workspaces/concept/imagery-json-configuration.md
    - assistant/workspaces/concept/asr-imagery-list-repo.md
    - assistant/workspaces/concept/imagery-misconfiguration.md
tags:
    - Assistant
---

<!-- @format -->

# Why must imagery use raw JSON links?

## Short Answer

Raw JSON links may be required when the consuming application needs to fetch and parse the imagery definition itself rather than receive a rendered webpage or an indirect link. The exact requirement depends on the current application and schema.

## Significance

Using the expected machine-readable resource helps the application validate and load configuration consistently.

## What This Means

Use the current raw schema or example URL, check that it returns the expected JSON, validate its structure, and test it in the intended workspace or app.

## What This Does Not Mean

A raw JSON link does not guarantee that the content is valid, accessible, licensed, current, or supported by the application.

## How To Use This

Confirm URL access, content type, schema version, source permissions, and error behavior before saving the configuration.

## Example

A manager enters a raw link to a valid imagery definition, validates it against the current schema, and checks that the configured layer loads for intended users.

## Assistant Guidance

Do not assume every JSON URL meets the requirement. Cite current application guidance and abstain when the expected schema or fetch behavior is unknown.

## Related Concepts

- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [What is the ASR imagery list repo?](asr-imagery-list-repo.md)
- [What happens if imagery is configured incorrectly?](imagery-misconfiguration.md)
