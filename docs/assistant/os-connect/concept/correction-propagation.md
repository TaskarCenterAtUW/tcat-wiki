---
title: Does a correction update OS-CONNECT or OpenStreetMap?
slug: correction-propagation
doc_type: concept
questions:
    - Does a correction update OS-CONNECT, OpenStreetMap, TDEI, or all of them?
    - Does a correction update OS-CONNECT or OpenStreetMap?
    - Does a correction update OS-CONNECT or OSM?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
topics:
    - os-connect
    - openstreetmap
    - feedback
    - stewardship
    - osm-interoperability
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-08-28
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - A correction automatically propagates to every related dataset or product.
    related_pages:
        - assistant/os-connect/concept/correction-release-lag.md
        - assistant/os-connect/concept/issue-report-follow-up.md
        - assistant/tdei/concept/released-dataset.md
tags:
    - Assistant
---

<!-- @format -->

# Does a correction update OS-CONNECT or OpenStreetMap?

## Short Answer

An update to an OS-CONNECT dataset does not directly update OpenStreetMap (OSM), TDEI, or every downstream product. A correction report, source-data edit, TDEI dataset update, released version, and downstream display are separate stages that require the applicable workflow and verification.

## Significance

Clear lineage and propagation understanding prevents users from treating a report in one viewer as a requested synchronized edit everywhere.

## What This Means

OS-CONNECT and OpenStreetMap are separate datasets. TDEI manages datasets and releases, while OS-CONNECT can present a released dataset; a correction must be reviewed and incorporated through the relevant source and release process.

## What This Does Not Mean

- A correction made in OS-CONNECT does not directly edit OpenStreetMap.
- A report or source edit does not automatically update TDEI or a released dataset.
- A release update does not prove that every downstream product has refreshed.

## How To Use This

Identify which system contains the reported problem, which dataset version is involved, and which release or downstream product the user means. Verify each stage separately instead of assuming synchronization.

## Example

An agency staffer verifies that a correction is present in a later OS-CONNECT release, then separately checks whether the source data, TDEI record, and downstream application have corresponding updates.

## Assistant Guidance

Do not infer synchronization across platforms without an explicit documented workflow and release evidence. Cite this page when explaining the distinction, and ask which system and version the user is referring to.

## Related Concepts

- [Correction release lag](correction-release-lag.md)
