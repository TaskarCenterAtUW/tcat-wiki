---
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
last_reviewed: 2026-06-27
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A County dataset is assembled from the City, UGA, UI, and CDP datasets within the county.
        - A new City dataset automatically creates or updates a new County dataset.
        - A new County dataset automatically creates or updates the City, UGA, UI, or CDP datasets within the county.
        - The version of an overlapping lower-scope dataset can be inferred from the version of a higher-scope dataset.
related_pages:
    - assistant/os-connect/concept/geographic-coverage.md
    - assistant/os-connect/workflow/search-for-jurisdiction.md
tags:
    - Assistant
---

<!-- @format -->

# How do OS-CONNECT dataset scopes relate?

## Short Answer

OS-CONNECT dataset name suffixes describe the geographic area covered by a dataset. `County` is the broadest scope in this group. A county dataset covers the entire county, including its cities, urban growth areas (UGAs), unincorporated (UI) areas, and census-designated places (CDPs) geographically represented within the county.

`City` datasets are separate datasets for individual cities and towns. `UI` means unincorporated area. UGAs and CDPs are different types of unincorporated areas, and they are both included in the UI geographic scope. These relationships describe geographic coverage, not how datasets are created or updated.

## Significance

Overlapping coverage does not mean that datasets share a version history. A user comparing a city dataset with a county dataset should treat them as independent OS-CONNECT datasets. The county dataset is not created by combining the City, UGA, UI, and CDP downloads inside it.

This distinction matters when datasets appear to contain similar features but have different upload dates, versions, or data details. A new release of one scope does not by itself create a new release of another scope.

## What This Means

The suffixes describe these geographic scopes:

| Suffix   | Geographic scope                 | Relationship to other scopes                                                                                         |
| :------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| `County` | An entire county                 | The broadest scope in this group; its area includes the county's cities, UGAs, UI areas, and CDPs.                   |
| `City`   | One city or town                 | Published as an individual dataset for that city or town. It is not a combined dataset for all cities in the county. |
| `UI`     | Unincorporated areas in a county | Includes the county's unincorporated areas, including areas identified as UGAs and CDPs.                             |
| `UGA`    | An urban growth area             | A type of unincorporated area; its coverage is part of the UI geographic scope.                                      |
| `CDP`    | A census-designated place        | A type of unincorporated area; its coverage is part of the UI geographic scope.                                      |

The scopes can overlap geographically. For example, a `Seattle_City` dataset and a `King_County` dataset can both cover locations in Seattle. That overlap does not establish that one dataset was generated from the other.

Each dataset is uploaded separately. Therefore:

- A new version of `Seattle_City` does not automatically update or create a new version of `King_County`.
- A new version of `King_County` does not automatically update or create new versions of the city, UGA, UI, or CDP datasets within the county.
- County and city datasets can be uploaded in the same batch, but simultaneous upload does not establish a dependency between them.
- The datasets should generally align geographically, but release timing can create temporary differences between overlapping datasets.

The `dataset_area` and boundary information can help identify whether datasets overlap. Use the dataset's metadata, including its boundary, identifier, upload date, and version, when comparing releases. This identifies the datasets being compared; it does not establish that one was used to produce another.

## What This Does Not Mean

A county dataset is not a package assembled from every city, UGA, UI, and CDP dataset in the county. It is produced and uploaded independently.

A `UI` dataset does not mean that UGA and CDP are interchangeable legal or statistical designations. UGA and CDP have different purposes, but both are treated as unincorporated areas for this geographic relationship.

A city release does not trigger a county release, and a county release does not trigger releases for the smaller scopes. Do not infer the source version of an overlapping dataset from another dataset's version number or upload date.

## How To Use This

When selecting a dataset, choose the scope that matches the geographic question:

- Use a `City` dataset for a specific city or town.
- Use a `County` dataset when the analysis needs county-wide coverage.
- Use a `UI`, `UGA`, or `CDP` dataset when the analysis is limited to that unincorporated area or area type.

When comparing overlapping downloads, compare their dataset boundaries and metadata as separate records. If the comparison depends on release timing or exact feature differences, record the TDEI dataset IDs, versions, and upload dates for both datasets rather than treating one as the other's source.

## Example

Suppose an analyst compares `Seattle_City` with `King_County`. Both datasets can contain coverage for Seattle because the city lies within King County. If `Seattle_City` receives version 2, that release does not automatically produce version 2 of `King_County`. The county dataset remains the independently uploaded version identified in its own metadata.

The same principle applies to a UGA or CDP that falls within a county: geographic inclusion does not create an update dependency.

## Assistant Guidance

Answer scope questions by separating two ideas:

1. **Geographic coverage:** a county contains the smaller geographic areas represented by city, UI, UGA, and CDP scopes.
2. **Dataset lineage and updates:** each scope is created and uploaded independently; overlap does not indicate that one dataset was built from another or that releases propagate between them.

Use `dataset_area` and dataset boundary metadata to discuss possible overlap. Do not claim that a particular lower-scope version is included in a higher-scope dataset unless a separate source explicitly documents that lineage. If a user asks which exact versions were used to create another dataset, explain that the datasets are independently created and request authoritative release-specific information if needed.

## Related Concepts

- [Geographic coverage](geographic-coverage.md)
- [Search for a jurisdiction](../workflow/search-for-jurisdiction.md)
