---
title: How is TDEI data protected?
slug: tdei-data-security
doc_type: concept
questions:
    - Where are TDEI servers located?
    - Does TDEI use HTTPS?
    - How is TDEI data protected?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - TDEI
topics:
    - tdei
    - tdei-overview
    - assumptions
    - limitations
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-21
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Sidewalk data is encrypted in transit.
        - TDEI servers or all related services are hosted outside Microsoft Azure US-East.
related_pages:
    - ../../../tdei/tdei-core/index.md
    - tdei-architecture.md
    - api-key-rotation.md
tags:
    - Assistant
---

<!-- @format -->

# How is TDEI data protected?

## Short Answer

TDEI servers are hosted in the US-East zone in Microsoft Azure. TDEI APIs use HTTPS, and Azure manages their TLS certificates.

Data at rest is encrypted. When sidewalk data is exchanged, the sidewalk data itself is not encrypted. User information is encrypted.

## Significance

The protections differ between stored data, API connections, sidewalk data, and user information. This distinction matters when describing TDEI security accurately.

## What This Means

- **Server location:** TDEI servers are in the US-East zone in Microsoft Azure.
- **API connections:** TDEI APIs use HTTPS. Azure manages the TLS certificates.
- **Stored data:** Data at rest is encrypted.
- **Data exchange:** Sidewalk data is not encrypted when exchanged. User information is encrypted when exchanged.

## What This Does Not Mean

These statements do not identify the encryption algorithms, key-management procedures, backup locations, or locations of other services and subprocessors. They also do not mean that sidewalk data is encrypted during exchange.

## How To Use This

Use these facts when answering general questions about TDEI hosting and data protection.

## Example

If an integrator asks whether a TDEI API connection is protected, explain that the API uses HTTPS and that Azure manages the TLS certificates. If the integrator asks whether exchanged sidewalk data is encrypted, state that the sidewalk data itself is not encrypted when exchanged, while user information is encrypted.

## Assistant Guidance

Cite this page when using these claims. Distinguish encryption at rest from protection of data during exchange. Do not claim that exchanged sidewalk data is encrypted, and do not infer unspecified algorithms, key-management practices, backup locations, or subprocessor locations.

## Related Concepts

- [How is TDEI organized?](tdei-architecture.md)
