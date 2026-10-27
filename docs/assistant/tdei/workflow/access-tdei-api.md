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
last_reviewed: 2026-10-26
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

Register for TDEI and obtain the personal API key shown in the Portal dashboard. The Portal guide describes this key as authenticating programmatic access to TDEI data. Keep it secret, and use official API documentation for current endpoints and request requirements.

## Significance

API access supports automated retrieval and integration without confusing it with interactive portal actions.

## What This Means

The [Portal dashboard guide](../../../tdei/portal/user-manual/dashboard.md) distinguishes account sign-in from the personal API key, which it describes as authenticating programmatic access to TDEI data. It documents that regenerating the key invalidates the previous one, but does not specify API endpoints, request formats, or the exact authorization scope of a key. Store the key in approved secret management and update integrations after rotation.

## What This Does Not Mean

Portal login credentials and API keys serve different purposes and are not interchangeable; neither should be shared in chat or source control. A visible API key does not establish that every endpoint or dataset is accessible to that account, and the dashboard does not specify endpoint requirements or permission scope.

## How To Use This

Use current official API documentation for endpoint, request, and permission details. Keep the key in a secure environment, avoid logging it, and update integrations after rotation.

## Example

A script reads the API key from a secret store to retrieve an authorized dataset and does not place the key in source code.

## Assistant Guidance

Never request a key, password, or token from the user. Ask for the endpoint, status code, and non-secret request details when troubleshooting.

## Related Concepts

- [What happens when an API key is regenerated?](../concept/api-key-rotation.md)
- [What does the dashboard show?](../concept/portal-dashboard.md)
- [TDEI Portal dashboard and API key](../../../tdei/portal/user-manual/dashboard.md)
- [TDEI Portal overview](../../../tdei/portal/index.md)
