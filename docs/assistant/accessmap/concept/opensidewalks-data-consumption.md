---
title: How does AccessMap consume OpenSidewalks or OS-CONNECT data?
slug: opensidewalks-data-consumption
doc_type: concept
questions:
    - How does AccessMap consume OpenSidewalks or OS-CONNECT data?
audiences:
    - planner
    - jurisdiction
    - advocate
    - public
products:
    - AccessMap
topics:
    - accessmap
    - os-connect
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
        - AccessMap consumes every OpenSidewalks attribute in every release.
        - A route based on OpenSidewalks data is physically verified.
related_pages:
    - assistant/accessmap/concept/accessmap.md
    - assistant/os-connect/concept/os-connect.md
    - assistant/cross-platform/concept/data-viewer-portal-workspaces-relationship.md
tags:
    - Assistant
---

<!-- @format -->

# How does AccessMap consume OpenSidewalks or OS-CONNECT data?

## Short Answer

AccessMap can consume a compatible pedestrian-network dataset such as an OpenSidewalks or OS-CONNECT release when that data is configured and supported by the current system. OS-CONNECT releases and AccessMap deployments are separate, so a release is not automatically available in every AccessMap deployment. The resulting routes depend on the dataset, profile, attributes, and routing implementation.

## Significance

The data handoff connects mapped pedestrian features with accessibility-aware routing. Understanding the boundary helps users distinguish source data from the routing product and its assumptions.

## What This Means

- Identify the source dataset, release, and geographic coverage.
- Confirm that the current AccessMap deployment and workflow support the specific release, format, and attributes; do not infer integration from the existence of an OS-CONNECT release.
- Check the selected mobility profile and explain how missing or uncertain attributes affect results.

## What This Does Not Mean

Consuming a dataset does not mean AccessMap reproduces every source field or that the route is a guarantee of accessibility. An OS-CONNECT release does not automatically imply deployment in AccessMap. OpenSidewalks, OS-CONNECT, and AccessMap remain distinct products and datasets.

## How To Use This

When explaining a route, cite the dataset and AccessMap guidance, identify the profile used, and distinguish modeled output from field conditions. Verify current integration behavior before giving technical instructions.

## Example

An analyst selects a released pedestrian dataset in the AccessMap workflow, chooses a mobility profile, and compares the resulting route with field knowledge before sharing it with a community group.

## Assistant Guidance

Do not claim that every OpenSidewalks attribute is consumed or that a route is physically verified. Ask for the AccessMap deployment, dataset release, and profile, cite current documentation, and abstain when integration details are missing.

## Related Concepts

- [What is AccessMap?](accessmap.md)
- [What is OS-CONNECT?](../../os-connect/concept/os-connect.md)
- [Data viewer, portal, and Workspaces relationship](../../cross-platform/concept/data-viewer-portal-workspaces-relationship.md)
