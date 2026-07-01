---
title: Update jurisdiction data through TDEI and OS-CONNECT pipelines
tags:
    - Assistant
slug: update-jurisdiction-data
doc_type: workflow
products:
    - OS-CONNECT
    - TDEI
audiences:
    - jurisdiction
    - planner
topics:
    - data-stewardship
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A specific turnaround time for publication without citing active policy.
related_pages:
    - assistant/tdei/how-do-i-use-the-tdei-portal.md
    - assistant/cross-platform/index.md
    - tdei/portal/user-manual/datasets.md
---

<!-- @format -->

# Update jurisdiction data through TDEI and OS-CONNECT pipelines

## Short Answer

Jurisdictions stage corrections and contributions through agreed TDEI workflows — datasets, validation jobs, and publication steps — so OS-CONNECT consumers see consistent, versioned updates rather than ad hoc files.

## Significance

Public assistants should not invent upload URLs or credential flows; this workflow anchors them to portal documentation.

## What This Means

1. Confirm project group membership and roles.
2. Prepare data to documented schemas and validation expectations.
3. Upload or register datasets, run validation jobs, resolve findings.
4. Publish or request publication per service rules; communicate release notes locally.

## What This Does Not Mean

- Not a tutorial replacement for the portal manual's click-level detail.
- Not permission to bypass access controls.

## How To Use This

Keep an internal changelog mapping local releases to OS-CONNECT versions referenced in planning products.

## Example

A county imports corrected curb ramp geometries, passes validation, and notifies internal GIS teams when the downstream OS-CONNECT snapshot refresh occurs.

## Assistant Guidance

Stay at the conceptual level; deep links should target the datasets and jobs manuals. Abstain on "when will my edit be live" without version context.

## Related Concepts

- [Where do I download OS-CONNECT data?](../../tdei/workflow/download-os-connect-data.md)
