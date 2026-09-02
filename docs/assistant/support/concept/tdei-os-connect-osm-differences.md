---
uid: 38d55e6e-a248-4c4b-86bc-1b0dc6df5f5e
title: What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?
slug: tdei-os-connect-osm-differences
doc_type: concept
questions:
    - What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?
    - Is OS-CONNECT the same as OpenStreetMap data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - OS-CONNECT
    - AccessMap
    - Walksheds
    - TDEI
topics:
    - tdei-ecosystem
    - overview
    - os-connect
    - accessmap
    - walksheds
    - tdei
risk_level: medium
authority_level: explanatory
publication_status: draft
last_reviewed: 2026-07-31
retrieval_priority: high
assistant_behavior:
    allow_inference: false
    requires_citation: true
    abstain_if_missing_context: true
    do_not_claim:
        - TDEI, OS-CONNECT, and OpenStreetMap are interchangeable systems or automatically synchronized.
    related_pages:
        - assistant/tdei/concept/released-dataset.md
tags:
    - Assistant
---

<!-- @format -->

# What is the difference between TDEI, OS-CONNECT, OpenSidewalks, and OpenStreetMap?

## Short Answer

TDEI is role management and data exchange infrastructure, OpenSidewalks is a pedestrian-data schema and mapping effort, OpenStreetMap is a global collaborative geospatial database, and OS-CONNECT is a published connected pedestrian infrastructure dataset for Washington state.

## Significance

The distinction prevents users from confusing a source database, schema, publication system, and derived dataset.

## What This Means

OS-CONNECT may use OSM or other inputs, and its releases may be represented with OpenSidewalks structures, but its boundary, processing, attributes, version, and publication context must be checked separately.

## What This Does Not Mean

OS-CONNECT is not automatically the same as the live OSM database or an official accessibility or ADA certification.

## How To Use This

Ask which product, dataset ID, version, format, and intended use the partner means. Cite the relevant release or schema documentation.

## Example

An agency compares a versioned OS-CONNECT release with current OSM data and finds differences because the datasets have different processing and update contexts.

## Assistant Guidance

Use exact product names and avoid saying that one system automatically updates another unless a documented workflow confirms it.

## Related Concepts

- [Released dataset](../../tdei/concept/released-dataset.md)
