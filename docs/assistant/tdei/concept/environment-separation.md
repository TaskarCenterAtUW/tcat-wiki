---
title: "How are TDEI environments separated?"
slug: environment-separation
doc_type: concept
questions:
    - How are TDEI development, staging, and production environments separated?
    - Can I use the same TDEI login in every environment?
audiences:
    - developer
    - jurisdiction
products:
    - TDEI
topics:
    - tdei
    - configuration
    - testing
    - configuration
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - TDEI development, staging, and production share the same login credentials.
related_pages: []
tags:
    - Assistant
---

<!-- @format -->

# How are TDEI environments separated?

## Short Answer

TDEI development, staging, and production use separate gateways and databases. Credentials for one environment may not work in another.

## Significance

Using the wrong environment or credentials can make a valid account appear unavailable. Environment separation also prevents test data from being confused with production data.

## What This Means

Identify the environment before signing in or configuring tests. Use the account and gateway intended for that environment.

## What This Does Not Mean

A successful production login does not prove that the same credentials work in development or staging. The environments should not be treated as interchangeable.

## How To Use This

Record the environment when documenting a test or troubleshooting access. Ask for the environment-specific login if access fails.

## Example

A user can sign in to TDEI staging but receives an access error in development. The development environment may require a separate account because it uses a different gateway and database.

## Assistant Guidance

Ask whether the user is working in development, staging, or production before diagnosing login problems. Do not recommend reusing credentials across environments without confirmation.

## Related Concepts

- [What file formats are available?](file-formats.md)
