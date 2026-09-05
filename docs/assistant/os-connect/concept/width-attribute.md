---
uid: 07b716b4-105a-4db8-ac21-63d4f938cb4c
title: 'What does "width" mean in the dataset?'
slug: width-attribute
doc_type: concept
questions:
    - What does "width" mean in the dataset?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - editing
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-09-04
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A missing width value means the feature has no usable width.
        - A recorded width proves ADA compliance or usability for every traveler.
related_pages:
    - assistant/os-connect/index.md
    - assistant/os-connect/concept/attribute-documentation-location.md
    - assistant/os-connect/concept/accessibility-attribute.md
tags:
    - Assistant
---

<!-- @format -->

# What does "width" mean in the dataset?

## Short Answer

In the OS-CONNECT Data Viewer, `width` describes the width of the selected feature in meters when that attribute is present. It is a dataset value for that feature, not a universal measurement for every nearby path or location.

## Significance

Width can affect how planners, analysts, and routing or accessibility tools interpret a pedestrian feature. Missing or inconsistent values limit comparisons and should be treated as data gaps rather than silently filled assumptions.

## What This Means

The Data Viewer documents `width` as the width of the selected feature, expressed in meters; an example value is `1.5`. The popup shows the field only when it is present in the dataset for that feature.

## What This Does Not Mean

An absent `width` value does not prove that the feature has no width or fails an accessibility requirement. A recorded width does not by itself establish ADA compliance, usability for every person, or the width of an adjacent feature.

## How To Use This

Select the feature in the Data Viewer and inspect its available attributes and dataset context. Record the unit as meters when using the documented OS-CONNECT viewer field, preserve the dataset version, and consult the applicable OpenSidewalks schema before comparing or transforming values.

## Example

A selected sidewalk displays `width: 1.5`. Report it as a 1.5-meter dataset value for that sidewalk, not as a measurement of the entire block or a guarantee that every traveler can use it.

## Assistant Guidance

State the feature, dataset or schema version, and unit when discussing `width`. Do not infer missing values or convert the field into a compliance conclusion without the applicable standard and additional context.

## Related Concepts

- [OS-CONNECT knowledge base](../index.md)
- [Where are OpenSidewalks attribute definitions documented?](attribute-documentation-location.md)
- [What is an accessibility attribute?](accessibility-attribute.md)
