---
title: What is completeness?
slug: completeness
doc_type: concept
questions: What is completeness?
    - What does completeness mean?
    - What does completeness measure in a dataset?
    - Does completeness measure how many real-world features have an attribute?
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
    - completeness
    - os-connect
risk_level: high
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-10
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Completeness measures how many real-world features have a given attribute.
        - Completeness measures the accuracy or correctness of an attribute.
        - A high completeness value proves that the mapped features meet accessibility standards or ADA requirements.
        - A low completeness value proves that the corresponding real-world features are absent or deficient.
related_pages:
    - assistant/qa-qc/concept/attribute-completeness.md
    - assistant/qa-qc/concept/attribute-presence-vs-feature-completeness.md
    - assistant/qa-qc/concept/presence-percent.md
    - assistant/qa-qc/concept/completeness-vs-ada-compliance.md
    - assistant/qa-qc/concept/completeness-vs-accessibility-gaps.md
tags:
    - Assistant
---

<!-- @format -->

# What does "completeness" mean?

## Short Answer

Completeness refers to the percentage of elements in a dataset that have a given attribute. It describes whether information is present for the dataset elements being measured.

## Significance

Completeness helps identify missing attribute values that may limit analysis or accessibility planning. It describes the coverage of information in the dataset, not the condition or availability of the corresponding real-world features.

## What This Means

To calculate completeness, a count of the dataset elements with the specified attribute is divided by the total count of that element.

## What This Does Not Mean

Completeness is not a measure of how many corresponding features in a city or other real-world area have that attribute. For example, it can show how many curbs in the dataset have a `type` attribute; it does not show how many curbs in the city are lowered. Completeness also does not establish that an attribute value is accurate, current, or compliant with an accessibility standard.

## How To Use This

Check which attribute is being measured, which elements are included in the denominator, and what geographic or project scope the dataset covers. Use the result to identify data gaps, and do not use it to infer real-world feature prevalence or condition.

## Example

Suppose 80 of 100 mapped curb elements have a `type` attribute. The dataset's completeness for that attribute is 80 percent. This does not mean that 80 percent of all curbs in the city are lowered, or that the 80 recorded values are correct.

## Assistant Guidance

Explain completeness as dataset attribute coverage. State the attribute and denominator when they are known. Distinguish attribute presence from real-world prevalence, accuracy, physical condition, and ADA compliance. If the report does not identify the attribute or denominator, ask for that context before interpreting the percentage.

## Related Concepts

- [What does attribute completeness mean in QA/QC reports?](attribute-completeness.md)
- [How does attribute presence differ from feature completeness?](attribute-presence-vs-feature-completeness.md)
- [What does presence percent mean in QA/QC reports?](presence-percent.md)
- [Is completeness ADA compliance?](completeness-vs-ada-compliance.md)
- [How does completeness differ from accessibility gaps?](completeness-vs-accessibility-gaps.md)
