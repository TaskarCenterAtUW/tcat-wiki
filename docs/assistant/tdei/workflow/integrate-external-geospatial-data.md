---
title: "How do I integrate external geospatial data with TDEI?"
slug: integrate-external-geospatial-data
doc_type: workflow
questions:
    - How do I integrate external geospatial data with TDEI?
    - How can I combine partner data with an OpenSidewalks dataset?
    - How do I prepare external data for a TDEI job?
audiences:
    - developer
    - jurisdiction
    - planner
products:
    - TDEI
    - OpenSidewalks
    - Workspaces
topics:
    - tdei
    - opensidewalks
    - workspaces
    - interoperability
    - formats
    - dataset-lineage
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-16
retrieval_priority: high
assistant_behavior:
    allow_inference: true
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - Any external geospatial file will pass TDEI validation without conversion or cleanup.
        - A TDEI union or join job is a substitute for reviewing the output dataset.
related_pages:
    - assistant/opensidewalks/concept/external-attributes.md
    - assistant/tdei/concept/source-and-derivative-datasets.md
    - assistant/tdei/concept/osw-edges-and-nodes.md
    - assistant/tdei/concept/test-dataset-in-portal.md
    - assistant/workspaces/workflow/create-a-workspace-from-tdei.md
tags:
    - Assistant
---

<!-- @format -->

# How do I integrate external geospatial data with TDEI?

## Short Answer

A typical integration workflow is to prepare the partner data in a supported geospatial format, identify the OpenSidewalks edges and nodes when applicable, validate and upload the result to TDEI, run the required TDEI processing job, and inspect the output before using or releasing it.

The exact job names, fields, permissions, and interface may change. Use the current TDEI manual and dataset requirements for operational instructions.

## Significance

This workflow gives a jurisdiction a controlled path from an existing geodatabase or other source format to a versioned TDEI dataset that can be processed, reviewed, and optionally opened in Workspaces.

## What This Means

1. Prepare or convert the source data into the format required by the target workflow, commonly GeoJSON for OpenSidewalks data.
2. Clearly distinguish edge and node files or layers when the OpenSidewalks workflow requires both.
3. Preserve partner-specific fields with the `ext:` convention where appropriate, then validate the complete dataset.
4. Upload the prepared dataset to TDEI with the required account and project-group permissions.
5. Create the applicable TDEI job, such as a union or join, using the relevant dataset identifiers.
6. Review, download, and inspect the job output in suitable GIS tooling before further processing.
7. Re-upload a reviewed output or open it in Workspaces when collaborative editing is needed.
8. Treat publication as a separate review and release decision.

## What This Does Not Mean

A successful upload or processing job does not prove that the data is complete, correctly attributed, routable for every use case, or ready for public release.

## How To Use This

Start with a copy of the source data and retain the original. Record the source and output dataset identifiers, validation results, processing parameters, and fields intentionally removed or retained. Use the TDEI user manual for current screens and permission requirements, and use Workspaces only after the dataset is suitable for that workflow.

## Example

A partner supplies a geodatabase containing pedestrian lines, points, and local attributes. The steward converts it to the required GeoJSON edge and node datasets, preserves selected partner fields with `ext:`, uploads it to TDEI, runs a union job against another dataset, downloads and reviews the output, and then opens the reviewed version in Workspaces for collaborative edits.

## Assistant Guidance

Ask which source format, target schema, TDEI project group, and intended output are involved before giving detailed instructions. Do not promise that a particular job will preserve topology or every attribute. Cite the current TDEI and OpenSidewalks documentation for exact validation and job behavior.

## Related Concepts

- [OpenSidewalks external attributes](../../opensidewalks/concept/external-attributes.md)
- [Source and derivative datasets](../concept/source-and-derivative-datasets.md)
- [OpenSidewalks edges and nodes](../concept/osw-edges-and-nodes.md)
- [Test a dataset in the portal](../concept/test-dataset-in-portal.md)
