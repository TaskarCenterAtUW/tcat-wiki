---
uid: dba68e63-4e82-41fe-96d9-167bf339fc15
title: How do I know whether a dataset is current?
slug: check-dataset-currency
doc_type: workflow
questions:
    - How do I know whether a dataset is current?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - TDEI
topics:
    - tdei
    - data-freshness
    - releases
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-10-26
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A dataset is current without release metadata and relevant geographic context.
related_pages:
    - assistant/tdei/concept/released-dataset.md
tags:
    - Assistant
---

<!-- @format -->

# How do I know whether a dataset is current?

## Short Answer

Check the dataset's ID, name, version, upload timestamp, project group, service, derived dataset ID, and validity dates in TDEI. Compare its geographic scope and intended use with the decision area, and verify known local changes with the data steward or field checks.

## Significance

Currency is part of fitness for use, especially when conditions change quickly.

## What This Means

Compare the dataset timestamp with the decision date and verify known changes locally.

## What This Does Not Mean

An older release may still have data that matches the conditions on the ground. Conversely, metadata alone does not prove that a dataset is current for a particular place and decision.

## How To Use This

Record the dataset ID, version, upload timestamp, validity dates, and geographic scope used in the analysis. The Portal dataset guide documents these metadata fields but does not present a complete change history. Verify current conditions with the data steward or locally before relying on the dataset for a time-sensitive decision.

## Example

An agency chooses a recent release but field-checks a construction corridor before relying on it.

## Assistant Guidance

Do not claim that a dataset is current without release metadata and relevant geographic context.

## Related Concepts

- [Released dataset](../concept/released-dataset.md)
- [TDEI Portal datasets](../../../tdei/portal/user-manual/datasets.md)
- [TDEI Data Viewer project groups and datasets](../../../tdei/data-viewer/user-manual/project-groups.md)
