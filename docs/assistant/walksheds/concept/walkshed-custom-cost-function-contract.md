---
uid: 68f1ff89-3732-4fd3-8a1e-cb56a63f8cbf
title: What is the Walksheds custom cost-function contract?
slug: walkshed-custom-cost-function-contract
doc_type: concept
questions:
    - What is the Walksheds custom cost-function contract?
    - What must a Walksheds cost function return?
audiences:
    - developer
products:
    - Walksheds
topics:
    - walksheds
    - configuration
    - accessibility-metrics
risk_level: high
authority_level: provisional
publication_status: draft
last_reviewed: 2026-07-22
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A custom cost function can safely execute arbitrary code without review.
related_pages:
    - walkshed-custom-cost-functions.md
    - walkshed-edge-attributes.md
    - ../workflow/model-infrastructure-change.md
tags:
    - Assistant
---

<!-- @format -->

# What is the Walksheds custom cost-function contract?

## Short Answer

The custom editor expects a `cost_fun_generator` that returns a `cost_fun(u, v, d)` function. The returned function must produce a non-negative cost or `None` for each edge.

## Significance

The contract determines whether a custom analysis can calculate, penalize, or exclude network edges.

## What This Means

The generator receives the graph and UI preference parameters. The edge function receives incoming node `u`, outgoing node `v`, and an attribute dictionary `d`. A non-negative float is a traversal cost; `None` excludes the edge.

## What This Does Not Mean

The custom function is not a general-purpose editor and cannot assume every source attribute is exposed or correctly typed.

## How To Use This

Document inputs, units, assumptions, exclusion rules, and output interpretation. Test on a controlled dataset before relying on results.

## Example

A function returns `None` for edges tagged `ext:construction=yes` and a time cost for other edges.

## Assistant Guidance

Ask for the current function signature and exposed fields. Treat custom code as experimental and high-risk analysis configuration.

## Related Concepts

- [What are custom cost functions?](walkshed-custom-cost-functions.md)
- [What edge attributes are exposed?](walkshed-edge-attributes.md)
