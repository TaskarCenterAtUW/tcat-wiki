---
uid: c079a4b4-c8a8-4bca-acfc-ccc144208c6c
title: What are QA/QC report question sections?
slug: report-question-sections
doc_type: concept
questions:
    - What are QA/QC report question sections?
audiences:
    - public
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - documentation
risk_level: low
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: medium
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/report-purpose-and-limitations.md
    - assistant/qa-qc/concept/report-provenance.md
    - assistant/qa-qc/concept/report-data-sources.md
    - assistant/qa-qc/workflow/interpret-report-sections.md
tags:
    - Assistant
---

<!-- @format -->

# What are QA/QC report question sections?

## Short Answer

Question sections organize a QA/QC report around inventory, attribute coverage, accessibility islands, intersection traversability, network importance, and bottleneck hotspots.

## Significance

They help non-technical readers find the evidence relevant to a decision or review task.

## What This Means

The question navigation groups report content into six practical tasks:

1. **What is in this dataset and how complete is the inventory for this jurisdiction?** Section 2 summarizes sources, area, and mapped objects.
2. **Which attributes are strong vs missing?** Section 3 compares feature completeness with the project's required, graph, and additional fields.
3. **Where are accessibility islands and disconnected destinations?** Section 4 presents islands, walksheds, and POI density.
4. **How easy are intersections to cross (traversability)?** Section 5.2 presents the intersection-quality metric.
5. **Which places matter most for network flow (traversability and centrality)?** Section 5 presents citywide connectivity metrics, including degree and centrality.
6. **Where are the highest-priority bottleneck hotspots?** Section 6 combines route dependence and traversability into a ranked review list.

The report's opening, glossary, and provenance appear before these analysis sections. Use the questions as navigation, then read the applicable metric definitions, inputs, and limitations.

## What This Does Not Mean

Question wording and section numbering vary by report. A section title alone does not define the calculation, denominator, or comparison set, and it does not establish a conclusion.

## How To Use This

Start with the question that matches the task, then check the report's provenance and glossary. Verify the section's method, data scope, metric scale, and map or table before drawing a conclusion.

## Example

A reader starts with the accessibility analysis to locate possible network breaks, checks the relevant profile and POI coverage, then treats any ranked bottleneck list as candidates for local review.

## Assistant Guidance

Use report-specific question labels when naming sections. Summarize the section's actual evidence and comparison set; do not assume every report has identical sections or methods.

## Related Concepts

- [How do I interpret QA/QC report sections?](../workflow/interpret-report-sections.md)
- [What is QA/QC report provenance?](report-provenance.md)
