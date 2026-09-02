---
uid: adcb3345-4dae-4681-99c5-ddf262e0e7b7
title: What happens when a TDEI API key is regenerated?
slug: api-key-rotation
doc_type: concept
questions:
    - What happens when a TDEI API key is regenerated?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - configuration
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A regenerated TDEI API key leaves the previous key usable.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# What happens when a TDEI API key is regenerated?

## Short Answer

Regenerating a TDEI API key invalidates the previous key immediately. Any integration using the old key must be updated. Confirm the applicable TDEI service and environment before rotating a credential.

## Significance

Key rotation can interrupt automated access if dependent systems are not updated. It should be treated as a credential change.

## What This Means

After regeneration, replace the old key wherever it is securely configured and test the integration. Keep the new key private, and do not paste it into chat, tickets, source control, or public documentation.

## What This Does Not Mean

Refreshing or copying a key is not a harmless display action if it regenerates the credential. Do not assume old clients continue working.

## How To Use This

Identify dependent services before rotating a key. Store the replacement only in approved secret-management locations.

## Example

A script begins failing after the project-group API key is refreshed. Updating the script with the new key restores access.

## Assistant Guidance

Never ask a user to paste an API key. Explain the rotation impact and direct them to their secure configuration process.

## Related Concepts

- [What does the TDEI portal dashboard show?](portal-dashboard.md)
