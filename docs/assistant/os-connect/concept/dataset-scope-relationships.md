---
uid: 9ff9a145-1ee4-467f-8bcf-748eec5aa2d1
title: How do OS-CONNECT dataset scopes relate?
slug: dataset-scope-relationships
doc_type: concept
questions:
    - How do OS-CONNECT dataset scopes relate?
    - What is the difference between City, UGA, UI, County, and CDP OS-CONNECT datasets?
    - What does a County OS-CONNECT dataset include?
    - Does a new City OS-CONNECT dataset update the County dataset?
audiences:
    - planner
    - developers
    - jurisdiction
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - dataset-lineage
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
        - Overlapping dataset boundaries by themselves prove source lineage or version relationships.
related_pages:
    - assistant/os-connect/concept/geographic-coverage.md
    - assistant/os-connect/workflow/search-for-jurisdiction.md
tags:
    - Assistant
---

<!-- @format -->

# How do OS-CONNECT dataset scopes relate?

## Short Answer

OS-CONNECT dataset name suffixes indicate geographic scope. The overview documents `City`, `UGA`, `UI`, `County`, and `CDP` as area types; it describes `County` as broad and says UGA and CDP areas are included within the UI scope. The available overview and Viewer manual do not explain how overlapping datasets are assembled or whether their versions are related.

## Significance

Overlapping coverage alone does not establish whether datasets share source data, lineage, or version history. The reviewed overview and viewer manuals describe scope names and show dataset IDs and versions, but do not explain how overlapping datasets are assembled or whether releases depend on each other. Compare each dataset's displayed metadata without inferring a relationship that the sources do not document.

## What This Means

The suffixes describe these geographic scopes:

| Suffix   | Geographic scope          | Relationship to other scopes                                                    |
| :------- | :------------------------ | :------------------------------------------------------------------------------ |
| `County` | An entire county          | The overview identifies this as the broadest named scope.                       |
| `City`   | One city or town          | A geographic scope identified by the `City` suffix.                             |
| `UI`     | Unincorporated areas      | The overview says UGA and CDP scopes are included within the UI scope.          |
| `UGA`    | An urban growth area      | A type of unincorporated area; its coverage is part of the UI geographic scope. |
| `CDP`    | A census-designated place | A type of unincorporated area; its coverage is part of the UI geographic scope. |

The [OS-CONNECT overview](../../../os-connect/index.md) describes the suffixes as coverage types but does not document a dataset-generation lineage. Dataset boundaries can be inspected in the viewer; geographic overlap alone does not establish that one dataset was generated from another.

The reviewed OS-CONNECT overview and Viewer manual do not describe whether or how overlapping scopes are assembled or released. Do not infer upload dependency or synchronization from names or boundaries. For example, the names `Seattle_City` and `King_County` indicate different geographic scopes; their names alone do not establish a source or update relationship.

Use each dataset's displayed boundary, identifier, upload date, and version when comparing coverage or releases. This identifies the datasets being compared but does not establish that one was used to produce another.

## What This Does Not Mean

A county dataset's broad geographic scope does not show that it is assembled from city, UGA, UI, and CDP datasets.

UGA and CDP are not interchangeable legal or statistical designations. The OS-CONNECT overview identifies them as different area types that are included within the UI geographic scope.

A displayed version number for one dataset does not establish the source version or release dependency of an overlapping dataset.

## How To Use This

When selecting a dataset, use the displayed boundary and dataset name to identify the geographic area that matches your question. The overview identifies the suffixes `City`, `County`, `UI`, `UGA`, and `CDP`; verify the selected boundary before analysis.

When comparing overlapping downloads, compare their dataset boundaries and metadata as separate records. If the comparison depends on release timing or exact feature differences, record the TDEI dataset IDs, versions, and upload dates for both datasets rather than treating one as the other's source.

## Example

An analyst comparing `Seattle_City` with `King_County` can inspect the boundaries and displayed dataset versions. Because the reviewed references do not describe release dependencies, the analyst should not infer from the names or overlapping geography that a version change in one caused a version change in the other.

## Assistant Guidance

Answer scope questions by separating two ideas:

1. **Geographic coverage:** a county contains the smaller geographic areas represented by city, UI, UGA, and CDP scopes.
2. **Dataset lineage and updates:** the available sources do not document lineage or release dependencies between overlapping scopes; do not infer them from geographic overlap.

Use displayed dataset boundaries and metadata to discuss possible geographic overlap. Do not claim a source or version relationship unless a source explicitly documents it. If the user asks how one dataset was produced or released, explain that the reviewed references do not establish that relationship and direct them to the dataset steward for authoritative details.

## Related Concepts

- [Geographic coverage](geographic-coverage.md)
- [Search for a jurisdiction](../workflow/search-for-jurisdiction.md)
