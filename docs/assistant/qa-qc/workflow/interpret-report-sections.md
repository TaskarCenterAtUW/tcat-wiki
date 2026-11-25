---
uid: 76d768a3-0d9d-40aa-adb2-715e6791971d
title: How do I interpret QA/QC report sections?
slug: interpret-report-sections
doc_type: workflow
questions:
    - How do I interpret QA/QC report sections?
audiences:
    - planner
    - jurisdiction
products:
    - QA-QC Reports
    - OS-CONNECT
topics:
    - qa-qc
    - os-connect
    - documentation
    - interpretation
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/qa-qc/concept/report-provenance.md
    - assistant/qa-qc/concept/report-question-sections.md
    - assistant/qa-qc/concept/report-data-sources.md
    - assistant/qa-qc/concept/walkshed-profile-assumptions.md
    - assistant/qa-qc/concept/report-map-interpretation.md
    - assistant/qa-qc/concept/bottleneck-hotspots.md
tags:
    - Assistant
---

<!-- @format -->

# How do I interpret QA/QC report sections?

## Short Answer

Start with the report's introduction, glossary, and provenance, then review inventory, attribute completeness, walksheds, connectivity, and bottlenecks with their definitions and limits.

## Significance

Different sections answer different questions and use different denominators or units.

## What This Means

Move from data context to metrics, distinguish raw values from transformed displays, then validate candidate findings locally.

## What This Does Not Mean

A single map or score is not the whole report.

## How To Use This

1. Read the introduction for the report's purpose and stated limits, then check the glossary and provenance.
2. Use the inventory section to identify the jurisdiction, dataset version, pipeline, area, and mapped feature counts.
3. Read the attribute section to distinguish project-required fields, baseline graph fields, and additional reported attributes.
4. Review the walkshed profiles, travel budget and units, POI coverage, islands, and per-profile counts before interpreting reach.
5. In connectivity sections, identify the metric, tile aggregation, comparison set, and whether the summary or map uses raw, normalized, log-normalized, or z-scored values.
6. Treat bottleneck rankings as candidates for local review; check their inputs, exclusions, tile location, and field context.

## Example

A planner checks the report's provenance, confirms which profile and threshold define its accessibility islands, and checks whether a connectivity map shows raw or transformed values before using a hotspot for local review.

## Assistant Guidance

Ask which report, section, metric, and decision the user is working with. Do not assume section numbering, travel budgets, or displayed scales are identical across reports; abstain from a specific interpretation when the relevant method or comparison set is missing.

## Related Concepts

- [What is QA/QC report provenance?](../concept/report-provenance.md)
- [What are QA/QC report question sections?](../concept/report-question-sections.md)
