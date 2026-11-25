---
uid: 86053952-7794-44d1-b4b8-8c6c24d8ac94
title: What entities and attributes does OS-CONNECT collect?
slug: os-connect-entities-and-attributes
doc_type: concept
questions:
    - What data does OS-CONNECT collect?
    - Which feature entities does OS-CONNECT include?
    - Which attributes are collected for OS-CONNECT sidewalks, crossings, connecting links, and curb points?
    - Which OS-CONNECT attributes are required?
audiences:
    - developer
    - jurisdiction
    - planner
    - advocate
products:
    - OS-CONNECT
topics:
    - os-connect
    - formats
    - connectivity
    - standards
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-11-24
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
related_pages:
    - assistant/os-connect/concept/required-vs-recommended-attributes.md
    - assistant/os-connect/concept/sidewalk-attributes.md
    - assistant/os-connect/concept/crossing-attributes.md
    - assistant/opensidewalks/concept/opensidewalks-schema.md
    - assistant/qa-qc/concept/project-completeness-standard.md
    - assistant/qa-qc/concept/attribute-completeness.md
    - assistant/qa-qc/concept/attribute-presence-vs-feature-completeness.md
    - assistant/qa-qc/concept/report-question-sections.md
tags:
    - Assistant
---

<!-- @format -->

# What entities and attributes does OS-CONNECT collect?

## Short Answer

- **Edge entities**
    - **Sidewalks** (centerline): `highway=footway`, `footway=sidewalk`, `incline`, `width`, `length`, `surface`
    - **Crossings** (curb point to curb point): `highway=footway`, `footway=crossing`, `crossing:markings` (`yes`, `no`), `length`, `surface`, `incline`
    - **Connecting links** (sidewalk centerline to curb point): `highway=footway`, `length`, `surface`, `incline`
- **Node entities**
    - **Curb points:** `kerb` (`raised`, `flush`, `lowered`), `tactile_paving` (`yes`, `no`)
- **Units**
    - `length`: meters.
    - `incline`: percentage.

## Significance

Knowing which geometry and attributes belong to each feature helps users interpret the pedestrian network, check connectivity, and avoid treating a collected field as proof of accessibility or data completeness.

## What This Means

OS-CONNECT data uses the following entities and attributes:

- **Edge entities**
    - **Sidewalks** (centerline):
        - `highway=footway`: type of way
        - `footway=sidewalk`: subclassification of the footway
        - `incline`: slope grade as a percentage (for example, `5%` or `-3%`)
        - `width`: width in meters (for example, `1.5`)
        - `length`: length in meters (for example, `42.3`)
        - `surface`: surface material (for example, `concrete` or `asphalt`)
    - **Crossings** (curb point to curb point):
        - `highway=footway`: type of way
        - `footway=crossing`: subclassification of the footway
        - `crossing:markings`: `yes` for marked or `no` for unmarked
        - `length`: length in meters (for example, `42.3`)
        - `surface`: information about the crossing surface
        - `incline`: slope grade as a percentage (for example, `5%` or `-3%`)
    - **Connecting links** (sidewalk centerline to curb point):
        - `highway=footway`: type of way
        - `length`: length in meters (for example, `42.3`)
        - `surface`: information about the link surface
        - `incline`: slope grade as a percentage (for example, `5%` or `-3%`)
- **Node entities**
    - **Curb points** have:
        - `kerb`: `raised`, `flush`, or `lowered`
        - `tactile_paving`: `yes` or `no`

## What This Does Not Mean

The collected-attribute inventory is not itself a universal required-field list. QA/QC reports identify project-required fields as **Required for OS-CONNECT**; that category defines the project's feature-completeness baseline, not every useful attribute or ADA compliance. A missing value does not mean “no,” and a recorded value does not certify accessibility.

## How To Use This

Match each attribute to its feature type and preserve the stated units and values. To find the fields counted as required for a specific QA/QC project, review the report's feature-completeness section, where required, graph, and additional fields are distinguished. Consult the applicable OpenSidewalks schema version and OS-CONNECT release documentation for schema-specific requirements and exact key definitions.

## Example

A sidewalk line is tagged with `highway=footway`, `footway=sidewalk`, `width=1.5`, and `surface=concrete`; a separate curb-to-curb crossing line records its geometry and crossing information, and a connecting link joins the sidewalk centerline to a curb-point node.

## Assistant Guidance

Answer direct inventory questions with the feature-by-feature list in Short Answer. Use its entity types and tag keys as authoritative. For project-required fields, distinguish the QA/QC report's **Required for OS-CONNECT** category from a universal schema requirement and from attribute presence or completeness. Do not infer fields beyond the listed inventory. Cite the applicable report, schema, and release when answering version-specific questions, and distinguish missing data from a negative value.

## Related Concepts

- [What attributes are required versus recommended?](required-vs-recommended-attributes.md)
- [What attributes are collected for sidewalks?](sidewalk-attributes.md)
- [What attributes are collected for crossings?](crossing-attributes.md)
- [What is the OpenSidewalks data schema?](../../opensidewalks/concept/opensidewalks-schema.md)
- [What is the QA/QC project completeness standard?](../../qa-qc/concept/project-completeness-standard.md)
- [What does attribute completeness mean in QA/QC reports?](../../qa-qc/concept/attribute-completeness.md)
- [How does attribute presence differ from feature completeness?](../../qa-qc/concept/attribute-presence-vs-feature-completeness.md)
- [What are QA/QC report question sections?](../../qa-qc/concept/report-question-sections.md)
