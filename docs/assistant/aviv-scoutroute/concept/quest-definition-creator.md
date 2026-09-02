---
uid: 779b1905-fca1-4d28-a561-d849c6dcc66e
title: What is the AVIV ScoutRoute Quest Definition Creator?
slug: quest-definition-creator
doc_type: concept
questions:
    - What does the AVIV ScoutRoute Quest Definition Creator do?
    - Can the Quest Definition Creator edit an existing definition?
    - How can I resume a Quest Definition Creator draft?
audiences:
    - developer
    - jurisdiction
products:
    - AVIV ScoutRoute
topics:
    - aviv-scoutroute
    - quests
    - configuration
    - documentation
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The Quest Definition Creator automatically deploys changes to a workspace.
        - The Quest Definition Creator supports every version of the Long Form Quest Definition schema.
        - A locally resumed draft is stored outside the user's device.
related_pages:
    - quest-definition-application.md
    - quest-definition-element-icons.md
    - ../workflow/update-quest-definition-in-workspace.md
tags:
    - Assistant
---

<!-- @format -->

# What is the AVIV ScoutRoute Quest Definition Creator?

## Short Answer

The Quest Definition Creator is a browser-based utility for creating, loading, editing, validating, previewing, upgrading, and exporting AVIV ScoutRoute Long Form Quest Definitions. The interface identifies its own version and the Long Form Quest Definition schema version it supports; check those values before relying on version-specific behavior.

## Significance

The Creator reduces the need to edit quest-definition JSON directly. It also makes the active Creator and schema versions visible, which helps users interpret validation results and compatibility behavior.

## What This Means

The welcome screen provides three modes when applicable:

- **Create new** starts a definition from a blank supported version with available presets.
- **Load existing** imports a Quest Definition file for editing.
- **Resume** reopens an in-progress draft saved in the browser's local storage on that device.

While editing, the utility provides section information, live preview, validation feedback, a JSON preview, and export controls. When a compatible older definition is loaded, the interface can offer a one-click schema upgrade.

## What This Does Not Mean

The Creator is an authoring and validation utility, not a deployment mechanism. Saving or exporting a definition does not change a workspace until the workspace configuration uses the updated definition and the app loads that configuration. Local draft persistence also does not imply that the draft is available on another device or stored centrally.

## How To Use This

Use the Creator to make or revise a definition, check the validation result, inspect the generated JSON, and export the file. Record the Creator version and supported schema version shown in the interface. If loading an older definition, use the upgrade control only when the interface identifies the version as compatible, then test the resulting definition in the intended workspace.

## Example

A project manager loads an existing version `3.1.0` definition into the Creator that supports `3.2.0`. The interface offers an upgrade, changes the definition version, and continues to show the live preview and validation panels. The manager still must update the workspace configuration before testing the new definition in AVIV ScoutRoute.

## Assistant Guidance

Treat the recorded Creator and schema versions as time-bound observations, not permanent current-version claims. Ask which definition version, Creator version, workspace, and configuration source are involved. Explain that a local resumed draft is browser- and device-specific unless other evidence establishes different storage behavior. Cite the current Quest Definition Creator documentation when available.

## Related Concepts

- [How is a quest definition applied?](quest-definition-application.md)
- [How are AVIV ScoutRoute quest element icons selected?](quest-definition-element-icons.md)
- [How do I update a quest definition in a workspace?](../workflow/update-quest-definition-in-workspace.md)
