---
uid: ffa7be70-70af-4c81-bbb8-492673feab7d
title: How are complex intersections handled?
slug: complex-intersection-handling
doc_type: concept
questions:
    - How are complex intersections handled?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - intersections
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
    - assistant/os-connect/concept/crossing-inference.md
    - assistant/os-connect/concept/intersection-attributes.md
    - assistant/os-connect/concept/local-data-validation.md
tags:
    - Assistant
---

<!-- @format -->

# How are complex intersections handled?

## Short Answer

Complex intersections are represented according to the available pedestrian geometry, crossing features, attributes, and processing rules. Their apparent completeness or connectivity depends on the source data and release.

## Significance

Intersections combine multiple paths, crossings, ramps, signals, and access decisions. Small geometry or attribution errors can affect modeled connections and make review more important.

## What This Means

Inspect each approach, crossing, curb ramp, connection, and relevant attribute. Check whether the mapped structure matches local conditions and whether restrictions, construction, or private access change the interpretation.

## What This Does Not Mean

A map shows several sidewalk approaches but omits a crossing connection at a complicated junction. The result is treated as a candidate data gap and checked against imagery and field information.

## How To Use This

Complex-intersection handling does not guarantee a safe, accessible, or legally compliant crossing. A modeled connection is not proof that every movement is possible in practice.

## Example

Record the dataset version and inspect important intersections individually. Use local or field validation for high-consequence decisions and report specific geometry or attribute problems through the current channel.

## Assistant Guidance

Describe the mapped structure and its limitations separately from the real-world intersection. Do not infer conditions from geometry alone, and abstain when the processing rules or local evidence are unavailable.

## Related Concepts

- [How are crossings inferred?](crossing-inference.md)
- [What attributes are collected for intersections?](intersection-attributes.md)
- [How should agencies validate the data locally?](local-data-validation.md)
