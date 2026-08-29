---
title: How are barriers incorporated?
slug: barrier-incorporation
doc_type: concept
questions:
    - How are barriers incorporated?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - Walksheds
topics:
    - walksheds
    - accessibility-data
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim: []
related_pages:
    - assistant/walksheds/concept/network-assumptions.md
    - assistant/walksheds/concept/disconnected-network-handling.md
    - assistant/walksheds/concept/walkshed-limitations.md
tags:
    - Assistant
---

<!-- @format -->

# How are barriers incorporated?

## Short Answer

Walkshed barriers are incorporated according to the dataset, routing implementation, profile, and scenario settings. A barrier may block a connection, increase travel cost, restrict a feature, or be absent if it is not represented in the source data.

## Significance

Barriers can materially change the area reachable within a fixed travel limit and can reveal why two profiles or scenarios produce different results.

## What This Means

Identify the barrier type, location, source, date, profile behavior, and cost rule. Check whether it is permanent, temporary, inferred, or missing and validate important barriers locally.

## What This Does Not Mean

A modeled barrier does not prove a physical barrier exists now, and an unmodeled barrier does not prove that a route is clear or accessible.

## How To Use This

Document barriers and assumptions, compare alternatives, preserve the dataset version, and report important data gaps or changed conditions through the current channel.

## Example

A closed crossing causes a modeled detour that places a nearby destination outside the selected cost limit. The result is explained as a scenario outcome, not proof that the destination is always unreachable.

## Assistant Guidance

Name the barrier source and routing rule. Distinguish physical observations from modeled restrictions and abstain when the implementation or current condition is unknown.

## Related Concepts

- [What network assumptions are used?](network-assumptions.md)
- [How are disconnected networks handled?](disconnected-network-handling.md)
- [What are the limitations of walkshed analysis?](walkshed-limitations.md)
