---
uid: 6f4ba36c-3827-4b8f-8f0c-38939834768a
title: Can agencies customize routing profiles?
slug: agency-routing-customization
doc_type: concept
questions:
    - Can agencies customize routing profiles?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - mobility-profiles
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Every agency can customize every AccessMap routing setting.
        - Customizing a profile guarantees suitable routes for every user.
related_pages:
    - assistant/accessmap/concept/routing-profiles.md
    - assistant/accessmap/concept/mobility-profiles.md
    - assistant/accessmap/concept/routing-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# Can agencies customize routing profiles?

## Short Answer

An agency may be able to configure routing profiles or preferences when the current AccessMap deployment supports that capability. Customization should be documented, reviewed, and tested against the agency's intended use.

## Significance

Local agencies may need settings that reflect local priorities or a defined planning scenario, but undocumented customization can make results difficult to interpret or reproduce.

## What This Means

- Define the users, purpose, geography, and accessibility assumptions.
- Confirm which settings the current deployment supports.
- Test and document the profile, data, and resulting tradeoffs.

## What This Does Not Mean

Customization is not a guarantee of accessibility, compliance, or universal suitability. An agency preference does not represent every person's needs.

## How To Use This

Use current product documentation and obtain responsible review before publishing a custom profile or using it for decisions.

## Example

An agency creates a profile that gives more weight to missing curb-ramp data, tests it on representative routes, and documents that it is a planning configuration rather than a universal standard.

## Assistant Guidance

Do not invent controls or claim a customization is available. Ask for the deployment, profile, and purpose, cite current documentation, and abstain when support is not confirmed.

## Related Concepts

- [Routing profiles](routing-profiles.md)
- [Mobility profiles](mobility-profiles.md)
- [Routing limitations](routing-limitations.md)
