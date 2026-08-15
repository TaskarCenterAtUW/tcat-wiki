---
title: What is eigenvector centrality?
slug: eigenvector-centrality
doc_type: concept
questions:
    - What is eigenvector centrality?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - graph-metrics
    - os-connect
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-16
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Eigenvector centrality measures the number of direction choices at an intersection.
        - A high eigenvector centrality value by itself identifies the most important location for investment.
        - Eigenvector centrality identifies real-world travel demand or the destinations people want to reach.
related_pages:
    - assistant/qa-qc/concept/degree-centrality.md
    - assistant/qa-qc/concept/eigenvector-centrality-interpretation.md
tags:
    - Assistant
---

<!-- @format -->

# What is eigenvector centrality?

## Short Answer

Eigenvector centrality describes how strongly an intersection connects to other important intersections in the modeled pedestrian network. A higher value means the intersection is more closely connected to the network's core.

## Significance

This metric helps identify important intersections for accessing locations of interest through the network. It describes the intersection's position within the network structure, not a condition observed in the field.

## What This Means

Read a higher value as indicating that an intersection connects to other intersections that are themselves well-connected or important in the graph. This can highlight intersections near the core of the modeled network.

## What This Does Not Mean

Eigenvector centrality does not measure how many walking paths meet at an intersection or how many direction choices are available there. Degree centrality is the metric used to describe direct connections. Eigenvector centrality also does not by itself measure real-world travel demand, safety, physical condition, or project priority.

## How To Use This

Use eigenvector centrality to compare an intersection's network position with other intersections in the same report. Interpret it alongside degree centrality, other graph metrics, mapped destinations, and local knowledge rather than treating it as a standalone decision rule.

## Example

An intersection connected to several well-connected intersections can have a higher eigenvector centrality value than an intersection with the same number of direct links to less-connected parts of the network.

## Assistant Guidance

Explain higher values as stronger connection to important parts of the modeled network. Do not describe the metric as a count of direction choices, a measure of observed trips, or proof that a location should receive priority. Cite the relevant QA/QC Report when answering from this page.

## Related Concepts

- [What does degree centrality mean in pedestrian-network reports?](degree-centrality.md)
- [How should eigenvector centrality be interpreted?](eigenvector-centrality-interpretation.md)
