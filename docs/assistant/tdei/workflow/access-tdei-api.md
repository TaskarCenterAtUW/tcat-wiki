---
uid: 74fe06aa-3fee-40b3-8cb2-42b47b759e1d
title: How do I access the TDEI API?
slug: access-tdei-api
doc_type: workflow
questions:
    - How do I access the TDEI API?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - formats
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed:
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Portal login credentials and API keys are interchangeable.
        - An API key can be safely shared in chat or source control.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How do I access the TDEI API?

## Short Answer

Register for TDEI, obtain the personal API key shown in the portal, and use it in an authorized programmatic request. Keep portal credentials and API keys separate and secret.

## Significance

API access supports automated retrieval and integration without confusing it with interactive portal actions.

## What This Means

Portal credentials authenticate the user interface, while the API key authenticates programmatic TDEI data access. Store the key in approved secret management and update integrations after rotation.

## What This Does Not Mean

An API key does not grant permissions beyond the account and project-group context, and refreshing it invalidates the previous key.

## How To Use This

Check the active project group, use the current key in a secure environment, avoid logging it, and update integrations after rotation.

## Example

A script reads the API key from a secret store to retrieve an authorized dataset and does not place the key in source code.

## Assistant Guidance

Never request a key, password, or token from the user. Ask for the endpoint, status code, and non-secret request details when troubleshooting.

## Related Concepts

- [What happens when an API key is regenerated?](../concept/api-key-rotation.md)
- [What does the dashboard show?](../concept/portal-dashboard.md)
