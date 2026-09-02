---
uid: 8b10916c-8d15-40df-bb2a-78c07c2f2dd9
title: Can OS-CONNECT support bus stop planning?
slug: bus-stop-planning
doc_type: workflow
questions:
    - Can OS-CONNECT support bus stop planning?
    - How do I use OS-CONNECT to help plan bus stops?
audiences:
    - planner
    - jurisdiction
    - advocate
products:
    - OS-CONNECT
    - Walksheds
topics:
    - os-connect
    - walksheds
    - planning
    - transit
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-24
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: false
    abstain_if_missing_context: false
    do_not_claim:
        - OS-CONNECT always contains up-to-date data reflecting recent changes on the ground.
related_pages:
    - assistant/os-connect/index.md
    - assistant/walksheds/index.md
    - assistant/cross-platform/concept/destination-access-analysis.md
tags:
    - Assistant
---

<!-- @format -->

# Can OS-CONNECT support bus stop planning?

## Short Answer

Yes, OS-CONNECT can be used to support bus stop planning. Use Walksheds to generate pedestrian-access analysis during bus stop planning; Walksheds uses OS-CONNECT data as its data source. OS-CONNECT is therefore relevant as the underlying pedestrian network, while Walksheds is the primary analysis tool for this workflow.

## Significance

This distinction helps planners choose the appropriate tool without treating OS-CONNECT itself as a bus stop planning application. Walkshed results can support comparisons of pedestrian access to proposed or existing stops.

## What This Means

- Use Walksheds to generate walksheds during the planning process.
- The analysis uses OS-CONNECT pedestrian data as its source network.
- Interpret the result as planning support, subject to the coverage and quality of the underlying data.

## What This Does Not Mean

- OS-CONNECT alone is not the primary tool for generating bus stop planning analyses.
- A walkshed does not by itself establish that a stop location is safe, compliant, or suitable.
- The result does not guarantee current field conditions or complete pedestrian access.

## How To Use This

- **Planners and jurisdictions:** Use Walksheds to analyze pedestrian access for bus stop planning, and document the OS-CONNECT data context used for the analysis.
- **Advocates and public users:** Treat the result as evidence for a planning discussion, not as a final determination about a stop location.

## Example

A transit planner compares proposed bus stop locations by generating Walksheds for each location. The planner uses the results to support the comparison and notes that the analysis is based on OS-CONNECT data.

## Assistant Guidance

Emphasize that Walksheds is the primary tool for supporting this workflow and OS-CONNECT provides the underlying data. Do not claim that a walkshed proves safety, legal compliance, or current physical accessibility; recommend local engineering review and field verification for those questions.

## Related Concepts

- [OS-CONNECT knowledge base](../index.md)
- [Walksheds knowledge base](../../walksheds/index.md)
