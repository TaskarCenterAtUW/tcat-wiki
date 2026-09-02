---
uid: 090dc77d-f4ac-43f7-bb3c-24225857d960
title: Can an agency submit a batch of known corrections instead of reporting one issue at a time?
slug: batch-correction-alternatives
doc_type: concept
questions:
    - Can an agency submit a batch of known corrections instead of reporting one issue at a time?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - feedback
    - agencies
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A batch submission guarantees acceptance or publication of every correction.
        - A batch submission bypasses validation or release controls.
related_pages:
    - assistant/os-connect/concept/bulk-correction-submission.md
    - assistant/os-connect/concept/agency-data-integration.md
    - assistant/os-connect/workflow/report-data-error.md
tags:
    - Assistant
---

<!-- @format -->

# Can an agency submit a batch of known corrections instead of reporting one issue at a time?

## Short Answer

An agency can ask whether several known corrections may be submitted together instead of reported one at a time. The appropriate method depends on the current OS-CONNECT intake process, the evidence, and the structure of the proposed changes.

## Significance

Batching can reduce repetitive reporting for a coordinated set of known issues while preserving review and traceability. It is different from asking that an entire priority area receive special attention.

## What This Means

- Group corrections with a clear theme, area, source, and affected feature or location.
- Ask the current data steward which batch format or channel is supported.
- Keep each proposed change identifiable so it can be reviewed separately.

## What This Does Not Mean

- A batch submission does not guarantee acceptance or publication of every correction.
- Batch submission does not bypass validation, review, attribution, or release controls.
- A batch does not automatically update OpenStreetMap, TDEI, or downstream products.

## How To Use This

Prepare a structured list of locations, proposed changes, evidence, and dataset version. Separate confirmed corrections from items needing verification, and use the ordinary issue workflow when a batch path is not documented.

## Example

An agency has ten verified curb-ramp corrections in one district. It groups the locations with field evidence and asks the steward whether they can be reviewed as one submission with individually traceable items.

## Assistant Guidance

Keep batch corrections distinct from priority-area requests. Do not invent an upload endpoint, file format, queue, or timeline; cite current guidance and abstain when the supported submission method is unknown.

## Related Concepts

- [Bulk correction submission](bulk-correction-submission.md)
- [Agency data integration](agency-data-integration.md)
- [Report an OS-CONNECT data error](../workflow/report-data-error.md)
