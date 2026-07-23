---
title: "How is a quest definition applied?"
slug: quest-definition-application
doc_type: concept
questions:
    - Does editing a quest definition automatically change a workspace?
    - How does a quest definition reach AVIV ScoutRoute?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - AVIV ScoutRoute
    - Workspaces
topics:
    - aviv-scoutroute
    - quests
    - workspaces
    - configuration
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Creating a quest definition automatically updates every workspace that uses it.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How is a quest definition applied?

## Short Answer

The Quest Definition Creator produces a definition file; editing it does not automatically change a workspace. The workspace must use an updated definition URL or define its quests through the applicable workspace configuration.

## Significance

This separation can explain why a seemingly correct quest edit has no effect in an app or workspace. It also prevents testing the wrong configuration.

## What This Means

When troubleshooting, inspect the definition source currently configured for the workspace. If using a URL, confirm it directly returns the raw JSON file. Then verify that the mobile app has received or loaded that configuration.

## What This Does Not Mean

A saved definition is not proof that a workspace uses it. Changes in the Creator have no effect until the configuration reference is updated.

## How To Use This

Record the definition URL or workspace setting during testing. Recheck it after changing quest definitions, switch or refresh the app workspace, and test the conditional flow before deployment.

## Example

A project manager updates a quest definition using the Creator and sets a maximum width of 100, but the workspace still points to an older hosted file. The new limit will not affect that workspace until its definition reference changes.

## Assistant Guidance

Ask where the definition is hosted and how the workspace references it. Avoid claiming that a Creator edit was deployed without checking the active configuration.

## Related Concepts

- [What is a quest in AVIV ScoutRoute?](quest.md)
