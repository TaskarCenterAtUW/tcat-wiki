---
title: ADA compliance boundaries for assistant answers
tags:
    - Assistant
slug: ada-compliance-boundaries
doc_type: concept
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
topics:
    - legal-boundaries
    - accessibility
risk_level: high
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-16
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any tool or dataset proves ADA compliance for a facility or program.
        - Routing or walkshed results constitute legal advice.
related_pages:
    - assistant/policies/ada-safety-legal-boundaries.md
    - assistant/concepts/completeness.md
    - assistant/questions/os-connect/is-completeness-ada-compliance.md
---

<!-- @format -->

# ADA compliance boundaries for assistant answers

## Short Answer

TCAT tools and datasets support analysis, planning, and public communication. They do not replace facility assessments, program access reviews, or counsel. Assistants must not state or imply that data outputs alone establish ADA compliance.

## Significance

Accessibility disputes turn on specific facts, standards, and legal tests. Over-claiming from maps or metrics misleads the public and strains institutional relationships. Clear boundaries keep assistants useful without overreaching.

## What This Means

Assistants may describe what a product shows (for example, a route preference or a completeness metric) and point to official definitions in the wiki. They should invite users to consult qualified professionals for compliance determinations.

## What This Does Not Mean

- Not permission to dismiss ADA obligations because "the map looks fine."
- Not a statement that TCAT or the University of Washington certifies sites.
- Not guidance on litigation strategy or enforcement.

## How To Use This

Train retrieval filters to prefer this concept when questions mention "ADA," "legal," "liable," or "compliance proof." Pair answers with [ADA safety and legal boundaries](../policy/ada-safety-legal-boundaries.md) for policy-level wording.

## Example

A user asks, "Does AccessMap prove my city is ADA compliant?" The correct pattern is: "No. AccessMap helps with pedestrian routing preferences; compliance requires professional evaluation of facilities and programs."

## Assistant Guidance

Use firm abstention language for compliance proof questions. Offer adjacent helpful facts (what the tool does) only after the boundary statement. Never cite draft pages as legal authority.

## Related Concepts

- [ADA safety and legal boundaries](../policy/ada-safety-legal-boundaries.md)
- [Completeness](completeness.md)
