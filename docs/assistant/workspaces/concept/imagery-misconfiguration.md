---
title: What happens if imagery is configured incorrectly?
slug: imagery-misconfiguration
doc_type: concept
questions:
    - What happens if imagery is configured incorrectly?
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
    - assistant/workspaces/concept/imagery-layer-mechanics.md
    - assistant/workspaces/concept/imagery-permissions.md
tags:
    - Assistant
---

<!-- @format -->

# What happens if imagery is configured incorrectly?

## Short Answer

Incorrect imagery configuration can cause a layer to fail to load, display in the wrong place or style, show incomplete tiles, produce errors, or be unavailable to intended users.

## Significance

Misconfiguration can mislead editing and review if users mistake a failed or misaligned layer for a missing or changed feature.

## What This Means

Check JSON syntax and schema, raw URLs, layer properties, coordinate alignment, access, attribution, source status, and browser or environment errors. Test with a known location.

## What This Does Not Mean

An imagery error does not prove that the workspace data are wrong or that the source is unavailable everywhere. Correct configuration does not prove that imagery is current.

## How To Use This

Restore or revise configuration using current guidance, document the source and version, and pause consequential edits until the reference layer is understood.

## Example

A layer appears blank because its URL is not accessible from the workspace environment. The manager checks permissions and configuration before changing mapped geometry.

## Assistant Guidance

Do not invent error causes or promise a fix. Ask for the workspace, URL, environment, and error, cite current configuration guidance, and abstain when live behavior cannot be verified.

## Related Concepts

- [What is the imagery JSON configuration?](imagery-json-configuration.md)
- [How do imagery layers work in Workspaces?](imagery-layer-mechanics.md)
- [How are imagery permissions handled?](imagery-permissions.md)
