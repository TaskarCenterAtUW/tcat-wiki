---
title: Why does AccessMap choose longer routes?
tags:
    - Assistant
slug: why-accessmap-longer-routes
doc_type: question
products:
    - AccessMap
audiences:
    - public
    - advocate
topics:
    - routing
risk_level: low
authority_level: explanatory
review_status: draft
last_reviewed: 2026-06-19
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: false
    do_not_claim:
        - The shortest car route is always the correct comparison baseline.
related_pages:
    - assistant/concepts/accessmap-routing.md
    - assistant/accessmap/how-do-mobility-profiles-work.md
---

# Why does AccessMap choose longer routes?

## Short Answer

AccessMap trades raw shortest distance for lower modeled cost under your mobility profile — often avoiding steep slopes, missing ramps, or other penalized features. A longer path can be "better" under those criteria.

## Significance

Preempts support tickets and social posts framed as routing "bugs."

## What This Means

The optimizer minimizes a cost function, not only meters. Costs come from network attributes and profile settings documented in the user manual.

## What This Does Not Mean

- Not proof that the shorter path is illegal or impassable for everyone.
- Not an error solely because another map shows a different line.

## How To Use This

Suggest checking active profile, preferences, and elevation-related settings before reporting data issues.

## Example

Two routes differ by two blocks, but the shorter one crosses a segment tagged with a high slope penalty for manual wheelchair profiles.

## Assistant Guidance

Explain multi-criteria optimization in plain language. Avoid telling users their preferred route is "wrong"; explain tradeoffs instead.

## Related Concepts

- [AccessMap routing (concept)](../concepts/accessmap-routing.md)
- [How do mobility profiles work?](how-do-mobility-profiles-work.md)
