---
uid: 84cafed7-b46f-4a51-8579-343d18ace865
title: What does the TDEI OSW Convert job do?
slug: job-osw-convert
doc_type: concept
questions:
    - What does the TDEI OSW Convert job do?
products:
    - TDEI
    - OpenSidewalks
audiences:
    - developer
    - jurisdiction
topics:
    - tdei
    - opensidewalks
    - interoperability
    - formats
risk_level: medium
authority_level: provisional
publication_status: draft
last_reviewed: 2026-08-19
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - The OSW Convert job in TDEI will process invalid OSW datasets without failing.
related_pages:
    - job-processing.md
    - ../concept/osw-vs-osm-format.md
    - ../../../tdei/portal/user-manual/jobs/osw-convert.md
tags:
    - Assistant
---

<!-- @format -->

# What does the TDEI OSW Convert job do?

## Short Answer

The OSW Convert job converts an OSW dataset to OSM format, or an OSM dataset to OSW format.

## Significance

The job supports exchange between OSW and OSM workflows. For OSW input, it also enforces the required file-name patterns inside the dataset archive. This check applies to conversion jobs and to workspace creation from a TDEI dataset or an uploaded local OSW file.

## What This Means

Choose `OSW` or `OSM` as the source and target formats. OSM input can use `.pbf`, `.osm`, or `.xml`. OSW input is a `.zip` archive.

### OSW File Format

An OSW dataset is a `.zip` archive. The `.geojson` files inside the archive must use one of these file name patterns:

- `*.nodes.geojson`
- `*.edges.geojson`
- `*.zones.geojson`
- `*.points.geojson`
- `*.lines.geojson`
- `*.polygons.geojson`

The **OSW - Convert** job checks the names of the files inside the archive. The job fails if an inner `.geojson` file does not match one of these patterns. This requirement also applies when the job is used during workspace creation from a TDEI dataset or an uploaded local OSW file.

The `points`, `lines`, and `polygons` files are optional. An archive containing valid `nodes`, `edges`, and `zones` files passes this file-name validation check when those optional files are not included.

For example, an archive containing files named `example-dataset-points.geojson`, `example-dataset-lines.geojson`, or `example-dataset-polygons.geojson` fails because the file names do not exactly match the required patterns. The corresponding valid names would use the required suffixes, such as `example-dataset.points.geojson`, `example-dataset.lines.geojson`, and `example-dataset.polygons.geojson`.

## What This Does Not Mean

Passing the file-name validation check does not guarantee that all fields, topology, or semantics are valid if other OSW data or schema requirements are not met.

## How To Use This

1. Confirm whether the source and target formats are `OSW` and `OSM`.
2. If the source is OSW, provide a `.zip` archive.
3. Check that every `.geojson` file inside the archive uses one of the required filename patterns.
4. Include valid `nodes`, `edges`, and `zones` files. Add `points`, `lines`, or `polygons` files only when needed.
5. Submit the job, record the job ID, and inspect the output.
6. Validate the converted result and compare important attributes and connectivity before using it in another workflow.

## Example

A valid OSW archive can contain `example-dataset.nodes.geojson`, `example-dataset.edges.geojson`, and `example-dataset.zones.geojson`. It can also contain optional files such as `example-dataset.points.geojson`. An archive containing `example-dataset-points.geojson` fails the file-name validation because it does not use the required `.points.geojson` suffix.

## Assistant Guidance

When explaining an OSW Convert failure, ask whether the input is a `.zip` archive and request the names of the `.geojson` files inside it. Check those names against the six permitted patterns. Do not claim that passing the filename checks guarantees complete schema validity or successful downstream use.

## Related Concepts

- [What does the OSW Validate job do?](job-osw-validate.md)
- [Which formats can a TDEI dataset download use?](dataset-download-formats.md)
