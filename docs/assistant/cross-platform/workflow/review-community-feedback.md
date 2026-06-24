---
title: Review community feedback (cross-product workflow)
tags:
    - Assistant
slug: workflow-review-community-feedback
doc_type: workflow
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
audiences:
    - jurisdiction
    - planner
topics:
    - feedback
    - governance
risk_level: medium
authority_level: explanatory
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - All feedback items are verified bugs in the core dataset.
related_pages:
    - assistant/policies/data-freshness.md
    - assistant/workflows/update-jurisdiction-data.md
---

# Review community feedback (cross-product workflow)

## Short Answer

Route feedback from each surface — AccessMap, Walksheds, OS-CONNECT viewers, or TDEI tickets — into a triage queue that distinguishes data defects, policy questions, and out-of-scope requests. Respond with transparent timelines where possible.

## Significance

Feedback is a sensor for both quality and communication gaps. Consistent handling prevents duplicate work and protects trust.

## What This Means

1. Tag tickets by product, geography, and suspected layer (graph vs basemap vs policy).
2. Reproduce in the appropriate tool with the same profile or scenario when applicable.
3. Escalate to data maintainers or software teams per internal runbooks.
4. Close the loop publicly when your process allows.

## What This Does Not Mean

- Not a commitment to accept every suggested geometry edit without validation.
- Not real-time incident response for emergencies — direct users to emergency services.

## How To Use This

Align labels with your CRM or GIS ticketing system; mirror language used in public privacy notices.

## Example

Several AccessMap reports cluster near a construction detour; staff confirm a temporary closure missing from OS-CONNECT staging and schedule an import fix.

## Assistant Guidance

Describe triage categories only at a high level; abstain from internal SLAs or team names unless documented publicly.

## Related Concepts

- [Update jurisdiction data](update-jurisdiction-data.md)
