---
title: Are Sound Transit or other agencies publishing GTFS Pathways data?
slug: gtfs-pathways-agency-adoption
doc_type: concept
questions:
    - Are Sound Transit or other agencies publishing GTFS Pathways data?
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
    - gtfs
    - publishers
    - os-connect
    - accessmap
    - walksheds
    - tdei
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
        - An agency that publishes GTFS necessarily publishes GTFS Pathways.
        - A station map proves that an agency's current feed contains pathways.txt.
related_pages:
    - assistant/accessmap/concept/gtfs-pathways.md
    - assistant/support/workflow/check-gtfs-feed-pathways.md
    - assistant/cross-platform/concept/os-connect-vs-gtfs-pathways.md
tags:
    - Assistant
---

<!-- @format -->

# Are Sound Transit or other agencies publishing GTFS Pathways data?

## Short Answer

Whether Sound Transit or another agency publishes GTFS Pathways must be checked in that agency's current official feed and documentation. Do not infer publication from a station map or from the existence of pedestrian data.

## Significance

Agency adoption changes over time and affects whether station-internal pathway data can be used in a current analysis. Verification prevents outdated or assumed feed coverage from being presented as fact.

## What This Means

- Check the agency's current official GTFS feed and feed documentation.
- Confirm that `pathways.txt` is present and populated when relevant.
- Record the feed version or date used for the analysis.

## What This Does Not Mean

- An agency's publication of GTFS does not prove that it publishes GTFS Pathways.
- OS-CONNECT does not establish an agency's current station-pathway publication status.

## How To Use This

Identify the agency and feed version, then inspect the official feed contents. If the current feed cannot be verified, report the uncertainty and use available station or pedestrian sources only with their stated limitations.

## Example

A planner asks whether a transit agency publishes station pathways. The analyst downloads the current official feed, checks for `pathways.txt`, and records the result rather than relying on an older reference.

## Assistant Guidance

Do not claim that Sound Transit or another agency publishes pathways without current feed evidence. Cite the feed or official documentation when available and abstain if the agency or version is missing.

## Related Concepts

- [What is GTFS Pathways?](../../accessmap/concept/gtfs-pathways.md)
- [Check a GTFS feed for pathways](../workflow/check-gtfs-feed-pathways.md)
- [OS-CONNECT versus GTFS Pathways](../../cross-platform/concept/os-connect-vs-gtfs-pathways.md)
