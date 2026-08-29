---
title: What is an accessibility attribute?
slug: accessibility-attribute
doc_type: concept
questions:
    - What is an accessibility attribute?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
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
    - assistant/os-connect/concept/pedestrian-feature-attributes.md
    - assistant/os-connect/concept/required-vs-recommended-attributes.md
    - assistant/os-connect/concept/missing-attribute-values.md
tags:
    - Assistant
---

<!-- @format -->

# What is an accessibility attribute?

## Short Answer

An accessibility attribute is a data field that describes a condition relevant to how a person may use a pedestrian feature. Examples may describe surface, width, slope, curb ramps, crossings, barriers, or other feature characteristics, depending on the dataset schema.

## Significance

Accessibility attributes add context to pedestrian geometry. They help people interpret a mapped feature, support quality review, and allow a routing or analysis system to apply documented preferences when the relevant fields are present.

## What This Means

The meaning of an attribute depends on its schema, value definitions, source, and dataset version. A value should be interpreted as a description of mapped or observed information, not as a complete statement about a person's experience.

## What This Does Not Mean

An accessibility attribute is not a legal determination, an accessibility certification, or a guarantee that a feature is usable now. A missing value does not necessarily mean that the condition is absent.

## How To Use This

Check the field definition, allowed values, source, collection date, and version before using an attribute. Preserve null or unknown values, and validate important locations with current local or field evidence.

## Example

A sidewalk record may include a width value and a surface value. An analyst can use those fields to screen locations for review, but should not conclude that the sidewalk is accessible for every person without additional context.

## Assistant Guidance

Name the schema and dataset version when explaining an attribute. Do not infer a physical condition from an undocumented value, and abstain when the field definition or source is unavailable.

## Related Concepts

- [Pedestrian feature attributes](pedestrian-feature-attributes.md)
- [Required and recommended attributes](required-vs-recommended-attributes.md)
- [Missing attribute values](missing-attribute-values.md)
