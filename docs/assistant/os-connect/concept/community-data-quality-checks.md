---
title: What quality checks are needed before community-mapped data can support planning or routing?
slug: community-data-quality-checks
doc_type: concept
questions:
    - What quality checks are needed before community-mapped data can support planning or routing?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - community
    - data-quality
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
        - Passing quality checks proves that every community-mapped feature is accurate.
        - Quality checks automatically authorize publication or routing use.
related_pages:
    - assistant/os-connect/concept/community-data-usability.md
    - assistant/os-connect/concept/correction-validation.md
    - assistant/os-connect/concept/planner-data-validation.md
tags:
    - Assistant
---

<!-- @format -->

# What quality checks are needed before community-mapped data can support planning or routing?

## Short Answer

Before community-mapped data support planning or routing, check its coverage, geometry, connectivity, attributes, provenance, consistency, licensing, and review status. The checks should match the consequences of the intended use.

## Significance

Quality checks help agencies distinguish a useful contribution from a dataset that still needs correction or field verification.

## What This Means

- Check for missing or duplicated features and invalid geometry.
- Test network connections, crossings, and relevant accessibility attributes.
- Compare representative features with imagery, local records, or field observations.
- Record findings, unresolved issues, source version, and reviewer.

## What This Does Not Mean

Passing a quality check does not prove that every feature is accurate or that the data satisfy legal or safety requirements. A check does not automatically authorize publication or routing use.

## How To Use This

Define acceptance criteria before review, sample both ordinary and complex locations, and keep unverified data separate from accepted data.

## Example

A reviewer checks a volunteer-mapped corridor for gaps, geometry errors, missing crossing attributes, and alignment with local observations before allowing it into a planning analysis.

## Assistant Guidance

Do not claim quality without naming the checks and dataset version. Cite the validation guidance and abstain from routing or legal conclusions when critical checks are incomplete.

## Related Concepts

- [Community data usability](community-data-usability.md)
- [Correction validation](correction-validation.md)
- [Planner data validation](planner-data-validation.md)
