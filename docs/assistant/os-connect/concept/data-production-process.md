---
uid: d372c83e-127f-4cfb-a919-c07448fff350
title: How was OS-CONNECT data produced?
slug: data-production-process
doc_type: concept
questions:
    - How was OS-CONNECT data produced?
    - How was the OS-CONNECT pedestrian network mapped and prepared for release?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - ai
    - automation
    - data-collection
    - standards
    - releases
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-11-25
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/os-connect/concept/data-collection-history.md
    - assistant/os-connect/concept/machine-learning-role.md
    - assistant/os-connect/concept/opensidewalks-schema-usage.md
tags:
    - Assistant
---

<!-- @format -->

# How was OS-CONNECT data produced?

## Short Answer

The OS-CONNECT data-production process used Prophet, a machine-learning system, to map pedestrian network data from aerial imagery. Human validators then reviewed the mapped data, it was validated against the OpenSidewalks (OSW) schema, and the data was released.

**Process:** Prophet mapping from aerial imagery → human validation → OSW schema validation → release.

## Significance

This sequence distinguishes machine-assisted mapping from the human review and schema checks that followed it. It also explains that schema validation was a step before release, rather than the source of the mapped pedestrian features.

## What This Means

Prophet was used to map pedestrian network data from aerial imagery. Human validators participated after that mapping step. The resulting data then went through OSW schema validation before release.

## What This Does Not Mean

This process description does not establish that every feature was independently field-surveyed, that the data are complete or current, or that schema validation confirms real-world accuracy or accessibility. It also does not specify the imagery dates, detailed validator procedures, model performance, or the validation results for a particular release.

## How To Use This

When explaining how OS-CONNECT data were produced, describe the steps in order and distinguish the machine-learning mapping, human validation, and schema validation stages. For a question about a particular release, use its release-specific documentation for details such as source imagery, dates, coverage, or validation results.

## Example

A user asks whether OS-CONNECT data were generated only by a machine. Explain that Prophet mapped pedestrian network data from aerial imagery, then human validators reviewed the mapped data, and the data underwent OSW schema validation before release. Do not imply that those steps prove every feature is current or field-verified.

## Assistant Guidance

Answer with the documented sequence: Prophet machine-learning mapping from aerial imagery → human validators → OSW schema validation → release. Do not invent imagery dates, validator protocols, model accuracy, field-survey steps, completeness, or release-specific outcomes. Cite this article when used; if asked for details not stated here, request or consult the relevant release documentation.

## Related Concepts

- [How was OS-CONNECT collected?](data-collection-history.md)
- [What role did machine learning play?](machine-learning-role.md)
- [What does it mean that OS-CONNECT uses the OpenSidewalks schema?](opensidewalks-schema-usage.md)
