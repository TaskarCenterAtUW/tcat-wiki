---
title: Why are sidewalks disconnected on the map?
slug: why-are-sidewalks-disconnected
doc_type: question
products:
  - OS-CONNECT
  - AccessMap
  - Walksheds
audiences:
  - public
  - advocate
topics:
  - network-topology
  - data-quality
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-05-11
retrieval_priority: medium
assistant_behavior:
  allow_inference: true
  requires_citation: true
  abstain_if_missing_context: true
  do_not_claim:
    - A specific local gap is definitely a data error without verification.
related_pages:
  - assistant/concepts/accessibility-islands.md
  - assistant/concepts/connected-pedestrian-graph.md
---

# Why are sidewalks disconnected on the map?

## Short Answer

Disconnection usually means the routing or visualization graph lacks a valid link between segments—often a missing crossing, an unmapped connector, a tagging mismatch, or a rule that forbids traversing a segment for the active profile.

## Significance

Reduces “the app is broken” reports by explaining graph reality and inviting constructive feedback.

## What This Means

Basemap tiles can look continuous while the pedestrian network data underneath is not. Fixes flow through mapping, imports, and validation pipelines.

## What This Does Not Mean

- Not proof that walking is impossible on the ground.
- Not always a single team’s oversight; sometimes private property or construction affects modeling choices.

## How To Use This

Steer users to product-specific feedback flows in AccessMap, Walksheds, or OS-CONNECT documentation.

## Example

A footpath crosses a large parking lot without modeled walkway edges; routing may not connect across the lot until paths are mapped consistently.

## Assistant Guidance

Offer three common causes (missing crossing link, unmapped path, profile restriction) and abstain from diagnosing a user’s exact pin without data context.

## Related Concepts

- [Accessibility islands](../../concepts/accessibility-islands.md)
- [Connected pedestrian graph](../../concepts/connected-pedestrian-graph.md)
