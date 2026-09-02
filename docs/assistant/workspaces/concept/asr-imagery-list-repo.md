---
uid: 92cf9b13-6094-4cdb-aadd-5eefc8a3dcaa
title: What is the ASR imagery list repo?
slug: asr-imagery-list-repo
doc_type: concept
questions:
    - What is the ASR imagery list repo?
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
risk_level: low
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
    - assistant/workspaces/concept/imagery-sources.md
    - assistant/workspaces/concept/imagery-raw-json-requirement.md
tags:
    - Assistant
---

<!-- @format -->

# What is the ASR imagery list repo?

## Short Answer

The ASR imagery list repository is the documented source for the schema and examples used to describe custom imagery for AVIV ScoutRoute and related Workspaces configuration. Use the current repository version and examples rather than relying on an older copy.

## Significance

A shared schema helps configuration authors describe imagery consistently and validate JSON before it is used by an app or workspace.

## What This Means

Check the repository's current schema, examples, version or branch, and imagery-provider requirements. Confirm that URLs, attribution, permissions, and layer properties meet the consuming application's needs.

## What This Does Not Mean

The repository is not itself an imagery provider, does not guarantee that a source is available or licensed for a workspace, and does not make a configuration valid merely because it is JSON.

## How To Use This

Use the current raw schema and example links from the documentation, validate the definition, and test the resulting imagery in the intended workspace or app.

## Example

A workspace manager uses the current ASR imagery-list schema to prepare a custom imagery definition, validates it, and checks the source's access and attribution requirements before saving it.

## Assistant Guidance

Do not invent schema fields or claim that every imagery source is supported. Cite the repository and current workspace guidance, and abstain when version or permission details are missing.

## Related Concepts

- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [What imagery sources are available?](imagery-sources.md)
- [Why must imagery use raw JSON links?](imagery-raw-json-requirement.md)
